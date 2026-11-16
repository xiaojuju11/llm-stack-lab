# 07 - MCP：把工具做成标准件

前面所有专题里，工具都是写在应用内部的函数。MCP 解决的是另一件事：**让工具脱离具体应用，成为任何客户端都能插拔的标准件**。写完这个专题，你的工具可以同时被 IDE、桌面客户端、自己的 Agent 使用。

## 目标

- 说清 MCP 的三个角色（Host / Client / Server）和它们之间谁跟谁说话
- 理解它为什么基于 JSON-RPC，传输层有哪几种（stdio / HTTP）
- 掌握三个原语：Tools（可执行）、Resources（可读取）、Prompts（可复用模板），以及各自适用场景
- 能用 SDK 写出一个可用的 Server，并被真实客户端加载
- 能写一个 Client，把 MCP 工具接进自己的 Agent 循环（对接 03 专题）
- 知道生产环境的坑：鉴权、超时、错误返回格式、工具描述对模型选择的影响

## 前置

- 03 专题完成（工具 schema、调用闭环）
- 有过「为什么每次接新工具都要改代码」的痛感

## 章节

- [ ] 7.1 MCP 是什么、不是什么：和 OpenAPI / function calling 的区别
- [ ] 7.2 架构与协议：Host/Client/Server、JSON-RPC 消息格式、初始化握手
- [ ] 7.3 传输层：stdio 与 HTTP，各自适合什么场景
- [ ] 7.4 三原语：Tools / Resources / Prompts 的边界，别把 Resource 当 Tool 用
- [ ] 7.5 写第一个 Server：`@tool` 装饰器、参数 schema、返回格式
- [ ] 7.6 资源与提示词：把文件、数据库暴露成 Resource
- [ ] 7.7 写 Client：连接、列工具、调用、把结果回灌给模型
- [ ] 7.8 接入真实客户端：在编辑器/桌面端配置并实际触发一次调用
- [ ] 7.9 把已有 HTTP API 包成 MCP Server
- [ ] 7.10 生产要点：鉴权、超时、错误语义、工具描述优化、调试手段

## 验收标准

1. 自己的 Server 能被真实客户端加载，**在对话里触发一次工具调用并拿到正确结果**（截图或日志留档）。
2. 同一个 Server 同时被你自己的 Agent（03 专题的循环）调用，代码几乎不用改——这就是标准件的意义。
3. 能解释：为什么工具的 `description` 写不好，模型就不会选它；举一个你优化前后的对比。
4. 工具内部报错时，返回给模型的是结构化错误信息，不是让整个连接断掉。

## code/ 目录约定

| 文件 | 内容 |
|---|---|
| `01-protocol-basics.py` | JSON-RPC 消息手写一遍，理解协议 |
| `02-first-server.py` | 最小 Server（一个 tool） |
| `03-tools-resources.py` | 三原语完整示例 |
| `04-client.py` | 自己写 Client 连接并调用 |
| `05-agent-integration.py` | 把 MCP 工具接进 Agent 循环 |
| `06-wrap-rest-api/` | 把 REST API 包成 Server |
| `07-production/` | 鉴权、超时、错误处理版本 |
| `config-example.json` | 客户端配置样例（不含密钥） |

## 复盘（当天填）

- 卡住的地方：
- 协议层最反直觉的一点：
- 工具描述改写前后的模型选择差异：

## AI 协作记录

（按 `docs/vibe-coding.md` 的模板记）
