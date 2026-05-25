---
title: "从 github cli 学习如何设计 agent friendly cli"
author: "@yan5xu"
date: 2026-05-23
url: https://x.com/yan5xu/status/2058151727333880265
type: x_article
source: x
---

GitHub の gh 應該是 vibe coding 裡非常高頻的命令了，而且它 CLI 本身也設計得很 agent-friendly，很適合拿來學習研究。

我覺得 gh 最值得學的，不是某幾個具體 command，而是它處理了兩個很關鍵的問題：一個是 GitHub 能力面太大，CLI command 很容易爆炸。另一個是 agent 的 context 很貴，命令輸出不能把無關信息全塞進來。

先看 command 爆炸的問題。

GitHub 的能力面非常大。如果每個能力都做成一個 command，很快會變成：

gh issue list
gh issue create
gh issue comment delete
gh repo deploy-key add
gh project item archive
...

command 越來越多，整個 --help 也會變得難以維護。agent 也永遠要猜：這個操作到底有沒有對應的 command？

gh api 用很取巧的方式解決了這個問題（當然這也建立在 GitHub 本身非常完善的 RESTful API 基礎上）：

gh api repos/cli/cli/pulls/13492 --jq '{number: .number, title: .title, state: .state}'

它不是簡單地「可以直接調 API」，而是把 RESTful API 裡的 resource model 自然遷移到了 CLI 裡：路徑定位資源，HTTP method 表達動作，認證和輸出格式由 gh 統一處理。

所以文檔裡看到：

DELETE /repos/{owner}/{repo}/issues/comments/{comment_id}

幾乎不用翻譯，就能寫成：

gh api repos/epiral/bb-viewer/issues/comments/4517246421 -X DELETE

這對 agent 特別重要。API 文檔本身就可以變成 CLI 使用說明。agent 不需要學一套和 API 文檔完全不同的 DSL，也不需要等 CLI 作者給每個長尾能力都包一層 command。

比如用 REST 路徑直接查一個 PR：

gh pr list -R cli/cli --limit 1 --json number,title,author,labels,state,reviewDecision,updatedAt

輸出：

{
  "number": 13492,
  "state": "open",
  "title": "Replace SITE_DEPLOY_PAT with gh-cli-site-deployer App"
}

路徑就是資源定位，--jq 做字段裁剪，整個過程不需要記任何專用 command。

這背後其實是一層 resource interface。resource 層解決的是覆蓋面問題：能力很多，但語法可以統一。

但 resource 不是萬能的。RESTful 一直以來的問題就是，有些用戶意圖很難自然 resource 化。

比如 login。它不是對某個資源做 CRUD。
比如 clone。它既涉及遠程 repo，也涉及本地文件系統和 git 狀態。
比如 checkout。它不是更新一個遠程資源，而是在本地切換工作區狀態。
比如 merge。它經常包含多個底層動作，但用戶表達的不是「修改這個字段，再刪除那個分支」，而是「把這個改動合進去」。

所以 CLI 裡還需要 command 層。command 不是「多步驟編排」的同義詞。多步驟編排只是 command 的常見來源之一。command 的本質是承接那些無法自然 resource 化的用戶意圖。

如果從 gh 再抽像一步，可以把 resource 和 command 在語法上顯式分開。一個可能的方案是用 / 前綴表示 resource：

# command，沒有 / 前綴，表達動作
cli login
cli clone epiral/bb-viewer
cli checkout 353
cli merge 353 --squash
cli status

# resource，用 / 前綴，表達對像路徑
cli /issues list
cli /issues/42 get
cli /issues/42 update state=closed
cli /issues/42 delete
cli /issues/42/comments create body="LGTM"
cli /projects/4/items list

/ 的好處是它不佔用任何單詞。如果用 api，會讓人以為這是傳統 API wrapper；如果用 resource，太囉嗦；如果直接寫 issues list，又會有歧義：issues 到底是 command 還是 resource？/issues 就很清楚：這是一個資源路徑。

resource 層的動詞可以收斂到一個很小的集合：

list
get
create
update
delete

這樣 agent 學會一個資源，就基本學會了所有資源。

參數也可以分清楚：key=value 是資源參數，--flag 是 CLI 行為控制。

cli /issues/42 get --json --jq '.title'

resource 層負責覆蓋長尾能力，command 層負責表達高層意圖。兩者不是替代關係，而是互補關係。

再看第二個問題：輸出污染。

在 agent workflow 裡，命令輸出不是越多越好。無關字段進入 context，不僅浪費 token，還會污染語義空間，干擾後續推理。

gh 的 --json / --jq 很值得學。

比如不做裁剪，agent 拿到的可能是這種輸出：

title:    Replace SITE_DEPLOY_PAT with gh-cli-site-deployer App
state:    OPEN
author:   williammartin
reviewers: copilot-pull-request-reviewer (Commented), BagToad (Requested)
number:   13492
url:      https://github.com/cli/cli/pull/13492
additions: 26
deletions: 2
--
## Summary

Replaces the personally-held SITE_DEPLOY_PAT used by the release workflow...

但如果下一步只是要知道 PR 標題，真正需要進入 context 的只有一行：

gh pr list -R cli/cli --limit 1 --json title --jq '.[0].title'

--jq 的價值不是「省一個管道」，而是把信息裁剪發生在進入 LLM context 之前。先減少 token 浪費，再減少無關字段對後續推理的干擾。

還有一種情況：默認輸出本身就是語義化的。

cli /issues/42 get

輸出：

Issue #42: Fix login bug
State:   open
Author:  epiral
Labels:  bug, auth
Updated: 2h ago

Login fails when session expires.

這類輸出比一整坨 JSON 更適合 LLM 直接理解。

所以 JSON 的定位應該是串聯和精確抽取，不是默認認知界面。默認輸出應該盡量語義化。自然語言是模型更擅長的表徵。

如果設計自己的 resource 風格 CLI，也可以沿用這個思路：

默認輸出：
cli /issues/42 get

Issue #42: Fix login bug
State:   open
Author:  epiral
Labels:  bug, auth
Updated: 2h ago

Login fails when session expires.

需要串聯時：
cli /issues list state=open --json --jq '.[].title'

默認語義化，需要時結構化。

最後還有一些執行層面的設計也值得學。

gh 的 flags 很一致：--repo、--assignee、--label、--json、--jq、--web 在不同 command 裡復用。對人是降低學習成本，對 agent 是提高泛化能力。

--web 是一個自然的 fallback：

gh pr view --web

CLI 不需要假裝覆蓋所有交互。有些事情就是 Web 更合適。

還有非交互模式：

GH_PROMPT_DISABLED=1 gh pr create --title "fix bug" --body "..."

--yes 跳確認，--dry-run 做預覽，token 走環境變量。這些都是 agent 能穩定使用 CLI 的基礎設施。

所以 agent-friendly CLI 不只是 machine-readable CLI。machine-readable 解決的是程序串聯；agent-friendly 還要解決語義理解。

結構上要穩定可組合：resource path、統一動詞、--json、--jq。
語義上要適合 LLM：默認自然語言輸出、清晰錯誤信息、少 token 噪音。

從 gh 裡可以學到的核心就是這個方向：用 resource 層避免 command 爆炸，用 command 層承接無法 resource 化的動作，再用輸出裁剪避免污染 agent 的 context。
