---
title: "From Zero to Production Agent with Codex — Development & Deployment Workflow"
author: "逸尘 (Yichen / @gengdaJ)"
source: https://x.com/gengdaJ/status/2069345006859805168
date: 2026-06-23
type: x-tweet
format: note_tweet
language: zh
getxapi: false
---

# From Zero to Production Agent with Codex — Development & Deployment Workflow

Author: 逸尘 (Yichen), X handle [@gengdaJ](https://x.com/gengdaJ). AI entrepreneur, founder, YouTube creator (100K+ subscribers in one month). Multiple AI products generating 5-figure revenue.

---

实战教程！给大家带来一期《从0到1开发并部署上线第一款生产级Agent》小白友好视频。

我之前分享过很多关于Codex和Claude Code的教程，用它们做出了很多酷炫的东西，也实际提高了生产力。

但是知其然，而不知其所以然，所以最近潜心学习了很多Agent相关的概念：链路追踪、记忆系统、模型网关、沙箱工具......

也在开发"书镜"Agent的过程中沉淀了一套自己的开发思路：

先用问答的方式和Codex对齐产品，写PRD文档；
再把PRD拆分成多个Plan.md；
用乔木老师开源的Skill撰写 /goal 提示词；
把Codex调整成"目标"模式，发送提示词；
开发一轮后，把所有plan.md整合成一个consolidation.md，然后重复上述过程进行下一轮开发。

用Codex本地Agent开发好后，才算完成了第一步，下一步是部署上线，要保证能在生产环境中能够正常使用。

我选择了腾讯云 EdgeOne Makers 边缘Web与AI Agent托管平台进行部署，因为确实比较方便简单，适合上手：

1.有内置的内容创作助手模板。记忆系统、沙箱工具、调用链路追踪、模型网关都是开箱即用，我直接把代码拿过来用Codex略改一下就能快速上线。

2.前后端（Web与Agent）共用同一个项目。传统的前端和后端是分隔开的，经常有跨域请求的麻烦，统一之后技术框架更为优雅，也能更好地统一管理账号、部署、监控和域名。

3.不限制部署项目的框架、语言和模型。Claude / OpenAI / LangGraph / CrewAI的框架都适配，没有自己的SDK；不限制开发语言（JS / Python）；有统一的AI Gateway，但是也可以接第三方API。
