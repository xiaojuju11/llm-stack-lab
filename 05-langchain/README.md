# 05 - LangChain：把 01-04 专题手写的东西换成框架

学 LangChain 的正确姿势是**先手写再对照**：01-04 专题里你已经手写过调用、检索、循环，现在看框架怎么把它们抽象成 Runnable，重点回答一个问题——**它省了我什么，又藏了什么**。

## 目标

- 理解 LCEL 的本质：`Runnable` 组合、管道操作符、`invoke/stream/batch` 三种调用方式
- 能用 `PromptTemplate` + 输出解析器 + pydantic 组合出稳定流程
- 能把 04 专题的检索链路用框架重写，并对比两者的坑
- 能接 `ChatOpenAI` 之外的兼容接口（国内外各家 OpenAI 兼容 API）
- 能把链包成 FastAPI 服务，支持流式输出

## 前置

- 03、04 专题完成（手写过工具循环与检索链路）
- 否则这个专题会变成「抄 API 文档」

## 章节

- [ ] 5.1 LCEL 与 Runnable：`|` 到底做了什么，为什么能 `stream`
- [ ] 5.2 Prompt 模板与消息类型：`system/human/ai`、少样本示例的组织
- [ ] 5.3 输出解析：`JsonOutputParser` + pydantic，解析失败怎么兜底
- [ ] 5.4 模型接入：`ChatOpenAI` 的 base_url、超时、重试、流式
- [ ] 5.5 检索集成：`VectorStore`、`Retriever`、`Document`，与 04 的手写版本对照
- [ ] 5.6 记忆与会话：`MessagesPlaceholder`、多轮压缩策略
- [ ] 5.7 工具与 Agent：`bind_tools` 与 Agent 执行器的关系（明确它和 03 手写循环的对应）
- [ ] 5.8 流式与回调：token 流、事件回调、日志接入
- [ ] 5.9 包成服务：FastAPI + SSE，前端能收到逐字输出
- [ ] 5.10 什么时候不该用 LangChain：轻量场景直接调 SDK 更可控

## 验收标准

1. 用 LCEL 重写 04 专题的问答链路，代码量对比手写版，**说清少了哪些代码、多了哪些抽象**。
2. 输出解析失败时（模型返回了非 JSON），你的链能自动重试或降级，不会整条链崩掉。
3. 服务端 `/chat` 支持 SSE，`curl` 能看到逐 token 返回。
4. 能列出至少 3 个「LangChain 抽象让你更难调试」的具体场景。

## code/ 目录约定

| 文件 | 内容 |
|---|---|
| `01-lcel-basics.py` | Runnable 组合与三种调用方式 |
| `02-prompt-parse.py` | 模板 + JSON 解析 |
| `03-model-options.py` | base_url/超时/重试/流式配置 |
| `04-retriever.py` | 检索集成，对照 04 手写版 |
| `05-memory.py` | 多轮会话 |
| `06-bind-tools.py` | 工具绑定与 Agent 执行 |
| `07-streaming.py` | 流式输出 |
| `08-rag-service/` | FastAPI + SSE 成品 |

## 复盘（当天填）

- 卡住的地方：
- 框架藏起来的东西（调试时最想骂的地方）：
- 哪些手写代码被框架替代后我真的省事了：

## AI 协作记录

（按 `docs/vibe-coding.md` 的模板记）
