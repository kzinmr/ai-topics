---
source_url: https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce
fetched: 2026-10-29 11:02 UTC
extraction: article-tag-extraction, gist
---

Instantly share code, notes, and snippets.

# 
 flamerix-ai / README.md 

 Last active
 October 29, 2026 10:44 

 Show Gist options 

- 

 Download ZIP

- 

 Star 
 
 51 
 ( 51 ) 

 You must be signed in to star a gist 

- 

 Fork 
 
 0 
 ( 0 ) 

 You must be signed in to fork a gist 

- 

 Embed 

# 
 Select an option

- 

- 

 Embed
 Embed this gist in your website. 

- 

 Share
 Copy sharable link for this gist. 

- 

 Clone via HTTPS
 Clone using the web URL. 

## No results found

 Learn more about clone URLs 

 Clone this repository at &lt;script src=&quot;https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce.js&quot;&gt;&lt;/script&gt;

- 
 
 Save flamerix-ai/c3905705cc4205e5de3011fa2e74efce to your computer and use it in GitHub Desktop. 

 Embed 

# 
 Select an option

- 

- 

 Embed
 Embed this gist in your website. 

- 

 Share
 Copy sharable link for this gist. 

- 

 Clone via HTTPS
 Clone using the web URL. 

## No results found

 Learn more about clone URLs 

 Clone this repository at &lt;script src=&quot;https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce.js&quot;&gt;&lt;/script&gt;

 Save flamerix-ai/c3905705cc4205e5de3011fa2e74efce to your computer and use it in GitHub Desktop. 

 Download ZIP 

 Claude Code burns ~15-20% of your tokens on a 3-word status line: a Bun preload that turns agent_summary off · by Flamerix AI, flamerix.ai · MIT

 Raw 

 README.md

# Claude Code burns ~15–20% of your tokens on a 3-word status line. Here's how to turn it off

 by Flamerix AI · MIT License

 Tested on Linux, Claude Code 2.1.257–2.1.312 (see Tested versions). The binary is not modified ( BUN_OPTIONS=--preload ). An update can silently undo it, so see Verify.

## TL;DR

 curl -fsSL https://gist.githubusercontent.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce/raw/no-agent-summary.js -o ~ /.local/share/no-agent-summary.js
claude daemon stop --any
BUN_OPTIONS= " ${BUN_OPTIONS : + $BUN_OPTIONS } --preload $HOME /.local/share/no-agent-summary.js " claude

 To make it permanent for every Claude Code process, see Install .

## The problem

 Every ~30 seconds, for every background agent, Claude Code sends that agent's entire
transcript to the agent's own model (usually Opus) and asks it to "describe your most recent
action in 3-5 words". The answer only updates the agent's status line in the agents panel; it
never reaches the model or your conversation. There is no setting that turns it off, and since
2.1.232 (August 2026) it has been on by default.

 The anomaly was detected by DRIM in Claude Code's OpenTelemetry export:
grouping claude_code.api_request events by query_source showed agent_summary costing more than the main conversation itself .

 query_source = agent_summary 
 week before the hook 
 2 days after 

 share of all Claude Code spend 
 16.4 % (main conversation: 15.7 %) 
 0 % 

 share of all API requests 
 19.7 % , about 1 in 5 
 0 % 

 part of that spend on Opus 
 96 % 
 — 

 input tokens per output token 
 ≈ 9,000 : 1 
 — 

 Spend here means Claude Code's own per-request estimate ( cost_usd ), not an invoice: on a
subscription, what you lose is rate-limit headroom. We are not the only ones who measured it:
 #86879 collects four independent
measurements of 18–26 %.

## The fix (how it works)

 no-agent-summary.js is a Bun preload (~80 lines of code). It wraps setTimeout / setInterval ;
when a callback's source text contains a summarizer anchor (e.g. the [AgentSummary] Timer fired 
log line), it returns an inert handle instead of arming the timer. Every other timer passes
through untouched. In the OpenTelemetry export the suppressed requests are
 claude_code.api_request events with query_source = agent_summary .

 Why a timer hook rather than something simpler: the module ships as precompiled Bun bytecode, so
editing its JS text inside the binary changes nothing, and the API client does not go through a
wrapped globalThis.fetch . But Function.prototype.toString still returns a callback's source
even when it runs from bytecode, so the timer can be recognised by a string inside it. The inert
timer uses exactly 2³¹−1 ms: Node and Bun treat a larger delay as 1 ms, so an "infinite" delay
would fire at once.

## Install

- 
 Put no-agent-summary.js somewhere stable; note its absolute path.

- 
 Set BUN_OPTIONS globally so every Claude Code process gets it. One of:

 # ~/.profile, ~/.bashrc, ~/.zshrc 
 export BUN_OPTIONS= " ${BUN_OPTIONS : + $BUN_OPTIONS } --preload /abs/path/no-agent-summary.js " 

 # ~/.config/fish/config.fish 
 set -gx BUN_OPTIONS " --preload /abs/path/no-agent-summary.js " 

 # ~/.config/environment.d/50-no-agent-summary.conf (systemd user env; also reaches 
 # user services and timers; applies when the user manager next starts, usually next login) 
 BUN_OPTIONS =--preload /abs/path/no-agent-summary.js

 Or a wrapper named claude earlier on PATH (the case keeps it idempotent when one Claude
Code process starts another):

 #! /bin/sh 
HOOK=/abs/path/no-agent-summary.js
 case " ${BUN_OPTIONS-} " in 
 * " --preload $HOOK " * ) ;;
 * ) export BUN_OPTIONS= " ${BUN_OPTIONS : + $BUN_OPTIONS } --preload $HOOK " ;;
 esac 
 : " ${CC_AGENT_SUMMARY_LOG := ${XDG_RUNTIME_DIR :-/ tmp} / no-agent-summary.log} " 
 export CC_AGENT_SUMMARY_LOG
 exec /path/to/the/real/claude " $@ " 

- 
 Restart the daemon and every already-running session, then start Claude Code from an
environment that has BUN_OPTIONS :

 claude daemon stop --any

### Env

 variable 
 values 
 effect 

 CC_AGENT_SUMMARY_MODE 
 off (default), pass 
 off suppresses the summary timer. pass is the A/B control: loads and logs, arms every timer untouched. Any other value warns on stderr and acts as off . 

 CC_AGENT_SUMMARY_LOG 
 file path, optional 
 Appends preload active mode=… bun=… hooked=… on load, one line per matched timer (first 20), and an exit count. 

 CC_AGENT_SUMMARY_MARKER 
 file path, optional 
 Overwritten on load with the preload active … line. 

## Nuances

- Restart the daemon after install. The daemon, pty host and pre-warmed bg-spare sessions
inherit the environment of the client that started the daemon, so a daemon started before
 BUN_OPTIONS was set keeps spawning unhooked sessions. Hence claude daemon stop --any .

- Headless runs need it too: claude -p , cron, CI, editor integrations.

- Platform: Linux tested, macOS and Windows untested. On Windows the /$bunfs/ gate most
likely never installs the hook.

- A/B: CC_AGENT_SUMMARY_MODE=pass loads the hook but arms every timer; the summaries come back, which shows the off result is the hook's doing.

- Background processes: daemon, pty host and bg-spare must carry --preload in their environment ( /proc/<pid>/environ on Linux); if not, restart the daemon.

## Verify (after every update)

- 
 Preload loads: 

 BUN_OPTIONS= " --preload $HOME /.local/share/no-agent-summary.js " CC_AGENT_SUMMARY_LOG=/tmp/nas.log claude --version && cat /tmp/nas.log

 Expect preload active mode=off … . No line: BUN_OPTIONS did not reach the process, or the
path is not absolute.

- 
 Timer suppressed: with the same BUN_OPTIONS and CC_AGENT_SUMMARY_LOG=/tmp/nas.log , run
a background subagent for a minute or two. The log shows
 summary timer #1 suppressed (setTimeout, delay=30000) and the agent's panel status stops
updating. If you export OpenTelemetry, query_source = agent_summary should stay at zero; this
is the only check that catches every failure mode.

### Fail-open

 Matching is by source text : an anchor must sit inside the callback passed to the timer. If an
update breaks that, the hook matches nothing and summaries silently come back. Ways it can happen:

- the log line or query-source id is renamed;

- the callback is passed via fn.bind(...) (no source in toString ) or another wrapper;

- the strings move to a shared constant outside the callback;

- the timer moves to an unwrapped API ( timers/promises , a scheduler loop).

 So re-run Verify after every update.

## Effect

- We run it under every Claude Code process on our machine (2.1.301). Since then there have been
zero agent_summary requests, and no other side query grew to take its place.

- Subagents, background agents, forked skills and background sessions run normally; only the
summary fork is skipped.

- Visible change: the per-agent panel status stops updating; SDK task_progress has no summary .

- Overhead: one Function.prototype.toString per distinct timer callback, cached in a WeakMap .
 claude --version : ~10 ms → ~17 ms (one measurement).

## Tested versions

 Linux x64 binary from npm @anthropic-ai/claude-code-linux-x64 (its sha256 equals the native
installer's manifest.json checksum). Static: the extracted bundle's summary timer callback
carries a hook anchor. Live: claude -p --model haiku with
 CLAUDE_CODE_AGENT_PROGRESS_SUMMARIES=1 , one subagent doing 8 steps of ~20 s, counting
 [AgentSummary] Forking in --debug-file .

 version 
 published 
 sha256 
 static 
 summary forks in a ~2.5-min agent run: no hook / hook pass / hook off 
 notes 

 2.1.312 
 2026-10-27 
 4f4178ce41d8 
 OK 
 5 / 5 / 0 
 latest on 2026-10-28; interactive: 6 no hook, 0 off 

 2.1.310 
 2026-10-23 
 b73676430af1 
 OK 
 5 / 5 / 0 

 2.1.308 
 2026-10-22 
 356733f185fa 
 OK 
 5 / 6 / 0 
 stable on 2026-10-28; the pass run's agent took 9 steps instead of 8 

 2.1.301 
 2026-10-15 
 bc1aad9982c7 
 OK 
 5 / 5 / 0 
 same with earlier hook builds; interactive off also 0; in daily use since 2026-10-26, 0 agent_summary requests in telemetry 

 2.1.280 
 2026-09-22 
 1e08503dbdf3 
 OK 
 1 / 1 / 0 (timer fired 11 / 11 / 0) 
 interactive: -p cannot enable summaries on this version. The agent sat at a permission prompt, so later timers skipped the unchanged transcript 

 2.1.257 
 2026-09-01 
 9a64bda9d872 
 OK 
 1 / 1 / 0 (timer fired 11 / 11 / 0) 
 same as 2.1.280 

 5 / 5 / 0 = the fork happens on this version, merely loading the hook changes nothing, and off 
removes it.

## Why there is no setting for this

- The documented switch only turns it on. The SDK option agentProgressSummaries defaults to
 false , but in the bundle it is one term of an OR, and every code path that writes it sets
 true . So false changes nothing, and the undocumented CLAUDE_CODE_AGENT_PROGRESS_SUMMARIES 
can only enable summaries too.

- The interval belongs to the server. It comes from a per-model-family server flag and is
clamped to 30–240 s. The default is already the minimum, and no value disables the timer.

- The obvious env vars miss. DISABLE_NON_ESSENTIAL_MODEL_CALLS , which some packagers set,
does not occur in the binary at all. CLAUDE_CODE_FORK_SUBAGENT=0 and
 CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1 do stop it, but only by taking fork subagents or
background agents with it.

- The prompt cache makes it cheaper, not cheap. About 98 % of these calls re-read the
transcript from cache; the ~2 % that hit a cold cache carry over a third of its cost.

- Cost tools that read transcripts don't see it. These requests are not written to the
session logs on disk ( #104358 ); only
the OpenTelemetry export shows them. The docs section on background token usage doesn't list it
either, while Agent View's row summaries are documented as a Haiku-class model refreshing every
few minutes.

- A cheaper variant already exists, switched off. 2.1.310 ships a short mode: about 2k
tokens of notes instead of the full transcript, optionally written by a smaller model. The
default is still the full transcript, and only server flags can change it.

### Timeline (2026)

 version (published) 
 what changed 

 2.1.32 (Feb 5) 
 the code first appears; dead in public builds 

 2.1.72 (Mar 9) 
 reachable as an SDK opt-in 

 2.1.117 (Apr 21) 
 reachable in the interactive CLI behind the fork gate or a server rollout 

 ≤ 2.1.220 (Jul 24) 
 forked skills are always summarized 

 2.1.232 (Aug 13) 
 on by default for interactive background agents 

 2.1.300 (Oct 14) 
 interval becomes server-tunable, 30–240 s 

 2.1.310 (Oct 23) 
 the cheaper short mode lands, switched off 

 In our telemetry its weekly share of spend went from 3.5–7 % in July (the fork gate was already
open for us) to 7.3 % and then 11.8 % in the week we picked up 2.1.233, and to about 16 % by
mid-October.

## License and disclaimer

 MIT © 2026 Flamerix AI . Provided as is , without warranty of any kind;
you use it at your own risk. Flamerix AI is not liable for any damage, data loss or account
action arising from its use. Changing a client's runtime behaviour may conflict with the terms of
the service you use it with; checking that is on you.

 "Claude" and "Claude Code" are trademarks of Anthropic, PBC. This project is independent and is
not affiliated with, sponsored or endorsed by Anthropic.

 Raw 

 no-agent-summary.js

 This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
 Learn more about bidirectional Unicode characters 

 Show hidden characters

 // no-agent-summary.js v2: Bun --preload hook that switches off Claude Code's `agent_summary` 

 // side-query. Unofficial, not affiliated with Anthropic. Tested on Linux, Claude Code 2.1.301. 

 // Install, env vars, verification and fail-open caveats: README.md. 

 // 

 // SPDX-License-Identifier: MIT 

 // Copyright (c) 2026 Flamerix AI (https://flamerix.ai). Provided "as is", without warranty; 

 // full license text: README.md. 

 // 

 // Anchors: the summarizer's debug-log line and its query-source id, both inside the timer 

 // callback on 2.1.301. 

 const IN_COMPILED_BUN = 

 typeof Bun !== "undefined" && typeof Bun . main === "string" && Bun . main . startsWith ( "/$bunfs/" ) ; 

 function install ( ) { 

 const fs = require ( "fs" ) ; 

 const ANCHORS = [ "[AgentSummary] Timer fired" , "agent_summary" ] ; 

 const RAW_MODE = process . env . CC_AGENT_SUMMARY_MODE || "off" ; 

 const MODE = RAW_MODE === "pass" ? "pass" : "off" ; 

 if ( RAW_MODE !== MODE ) process . stderr . write ( `[no-agent-summary] unknown mode ${ RAW_MODE } , forcing off\n` ) ; 

 const LOG = process . env . CC_AGENT_SUMMARY_LOG ; 

 const log = ( s ) => { if ( LOG ) { try { fs . appendFileSync ( LOG , ` ${ new Date ( ) . toISOString ( ) } pid= ${ process . pid } ${ s } \n` ) ; } catch { } } } ; 

 const verdict = new WeakMap ( ) ; // fn -> bool (is the summary timer callback) 

 function isSummaryTimer ( fn ) { 

 if ( typeof fn !== "function" ) return false ; 

 let v = verdict . get ( fn ) ; 

 if ( v === undefined ) { 

 try { 

 const src = Function . prototype . toString . call ( fn ) ; 

 v = ANCHORS . some ( ( a ) => src . includes ( a ) ) ; 

 } catch { v = false ; } 

 verdict . set ( fn , v ) ; 

 } 

 return v ; 

 } 

 let matched = 0 ; 

 let suppressed = 0 ; 

 const PROMISIFY = Symbol . for ( "nodejs.util.promisify.custom" ) ; 

 const wrappers = new Map ( ) ; // original timer fn -> its wrapper: one wrapper per original 

 const hookedFns = new WeakSet ( ) ; 

 function wrap ( orig , name ) { 

 if ( typeof orig !== "function" ) return orig ; 

 if ( wrappers . has ( orig ) ) return wrappers . get ( orig ) ; 

 const hooked = function ( fn , delay , ... args ) { 

 if ( isSummaryTimer ( fn ) ) { 

 matched ++ ; 

 if ( MODE === "off" ) { 

 suppressed ++ ; 

 if ( matched <= 20 ) log ( `summary timer # ${ matched } suppressed ( ${ name } , delay= ${ delay } )` ) ; 

 const t = orig ( ( ) => { } , 2 ** 31 - 1 ) ; // clear*-compatible handle of the same kind, never fires 

 if ( t && typeof t . unref === "function" ) t . unref ( ) ; 

 return t ; 

 } 

 if ( matched <= 20 ) log ( `summary timer # ${ matched } passed (control, ${ name } , delay= ${ delay } )` ) ; 

 } 

 return orig ( fn , delay , ... args ) ; 

 } ; 

 Object . defineProperty ( hooked , "name" , { value : name } ) ; 

 // util.promisify(setTimeout) reads these; without the custom one it calls the wrapper 

 // callback-last and node throws ERR_INVALID_ARG_TYPE. 

 if ( orig . __promisify__ ) hooked . __promisify__ = orig . __promisify__ ; 

 if ( orig [ PROMISIFY ] ) hooked [ PROMISIFY ] = orig [ PROMISIFY ] ; 

 wrappers . set ( orig , hooked ) ; 

 hookedFns . add ( hooked ) ; 

 return hooked ; 

 } 

 // require("timers/promises").setTimeout(delay, value) takes no callback, so there is no source 

 // to match an anchor in; it stays unwrapped. 

 const timers = ( ( ) => { try { return require ( "timers" ) ; } catch { return null ; } } ) ( ) ; 

 const hookedApis = [ ] ; 

 for ( const name of [ "setTimeout" , "setInterval" ] ) { 

 globalThis [ name ] = wrap ( globalThis [ name ] , name ) ; 

 if ( hookedFns . has ( globalThis [ name ] ) ) hookedApis . push ( `global. ${ name } ` ) ; 

 if ( timers ) { 

 try { timers [ name ] = wrap ( timers [ name ] , name ) ; } catch { } 

 if ( hookedFns . has ( timers [ name ] ) ) hookedApis . push ( `timers. ${ name } ` ) ; 

 } 

 } 

 const active = `preload active mode= ${ MODE } bun= ${ Bun . version } hooked= ${ hookedApis . join ( "," ) } ` ; 

 log ( active ) ; 

 if ( LOG ) process . on ( "exit" , ( ) => log ( `exit: ${ suppressed } summary timer(s) suppressed, ${ matched } matched` ) ) ; 

 const MARKER = process . env . CC_AGENT_SUMMARY_MARKER ; 

 if ( MARKER ) { 

 try { fs . writeFileSync ( MARKER , ` ${ active } pid= ${ process . pid } \n` ) ; } 

 catch ( e ) { process . stderr . write ( `[no-agent-summary] cannot write marker ${ MARKER } : ${ e . message } \n` ) ; } 

 } 

 } 

 if ( IN_COMPILED_BUN ) install ( ) ; 

### 

 Bedz01 

 commented 

 Oct 29, 2026 

 Copy link

 Copy Markdown

 Heads up on the global BUN_OPTIONS install. With a space, --preload /path , every bun subcommand breaks: on bun 1.4.3 bun install, add, test, build and x all fail with Script not found "install" and so on. It's bun's parser, any value flag before the subcommand does it, e.g. bun --define x:1 install . --preload=/path works for both bun and Claude Code.

 I also gated install() on Bun.main === "/$bunfs/root/cli" plus execPath being a Claude Code install, so other compiled Bun binaries don't get their timers wrapped. Got the same 5/5/0 on 2.1.308 your way.

 --> 

 Sign up for free 
 to join this conversation on GitHub .
 Already have an account?
 Sign in to comment