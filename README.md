# llm-stack-lab

把「LLM 应用」这一整栈从上到下跑通的实验仓：**Python 与 Go 打底 → Tool Calling 建立最小能力单元 → RAG 接入私有知识 → LangChain / LangGraph 做编排 → MCP 把能力标准化 → 成品沉淀**。

> 这里放的每一段代码都自己跑过；跑不通的地方连报错一起留下来。学习仓库和笔记仓库的区别就在这里：交付物是「能跑的东西 + 踩过的坑」，不是知识点的复述。

## 这个仓库是什么 / 不是什么

**是**：一份按依赖顺序推进的学习轨迹，每个专题有明确验收标准，代码可独立运行。

**不是**：教程搬运、链接收藏夹、单文件示例堆。凡是这里出现的技术点，都要求能说清「它解决什么问题、什么时候不该用」。

## 专题与进度

| 目录 | 覆盖内容 | 状态 | 开始 | 完成 |
|---|---|---|---|---|
| `01-python/` | 为 LLM 应用服务的 Python：类型标注、pydantic、asyncio、测试 | 未开始 | | |
| `02-go/` | Go 语法速通 → 并发 → HTTP 服务 → LLM 网关客户端 | 未开始 | | |
| `03-tool-calling/` | Function Calling 原理、schema 设计、调用闭环、并行与错误回灌 | 未开始 | | |
| `04-rag/` | 切分、向量化、检索、重排、混合召回、评估 | 未开始 | | |
| `05-langchain/` | LCEL、Runnable、Retriever 集成、流式回调、接 FastAPI | 未开始 | | |
| `06-langgraph/` | 状态图、条件边、持久化、人工介入、多 Agent 编排 | 未开始 | | |
| `07-mcp/` | 协议原理、三原语、写 Server、写 Client、接入编辑器 | 未开始 | | |
| `99-projects/` | 成品：每个子目录都是能独立启动的服务 | — | | |

配套文档：

- [`docs/roadmap.md`](docs/roadmap.md) — 16 周排期、里程碑、验收口径
- [`docs/vibe-coding.md`](docs/vibe-coding.md) — 用 AI 辅助写的规约：怎么用才不废掉基本功

## 为什么是这个顺序

**先语言，再能力，再框架。** LangChain 和 LangGraph 本质上只是把三件小事（调模型、查资料、跑循环）包装了起来。没手写过 `messages` 数组、没自己拼过工具 schema、没写过 while 循环版的 Agent，直接上框架会变成「会调 API 但不知道为什么这么调」——报错时完全无从下手。

**Tool Calling 放在 RAG 前面。** RAG 在系统里的角色就是「一个检索工具」，先理解工具怎么被模型选中和调用，再看检索，会顺很多；反过来先学 RAG，容易只学到「调库拼流程」。

**Go 排在 Python 之后。** Go 在本仓库的定位不是主力语言，而是「把能力包成高并发服务」的那一层，所以放在 Python 打好底之后，用 6 周内可完成的强度来学。

## 每个专题的组织约定

```
0X-topic/
├── README.md        # 目标 / 前置 / 章节清单(勾选) / 验收标准 / 复盘区
└── code/
    ├── 01-xxx.py    # 按章节编号，每个文件独立可运行
    └── 02-xxx.py
```

三条硬约束：

1. **每个 code 文件必须能独立跑**（`python code/01-xxx.py` 或 `go run code/01-xxx.go`），不依赖前一个文件的运行结果。
2. **章节清单用 `- [ ]` 勾选**，勾上前必须通过该章验收标准。
3. **复盘必须在当天填**，过期不补——事后回忆的「坑」都是编的。

## 环境准备

**Python（3.11+，推荐 3.12）**

```bash
python -m venv .venv
source .venv/Scripts/activate      # Windows Git Bash
pip install -U pip
pip install openai python-dotenv pydantic
```

**Go（1.22+，Day 里用到 1.22 增强版 ServeMux 路由）**

```bash
go version
go env -w GOPROXY=https://goproxy.cn,direct
```

**密钥一律走环境变量**，不写进代码、不提交仓库：

```bash
cp .env.example .env
# 填入真实值，.env 已在 .gitignore 里
```

## 运行约定

示例里的文件名以各专题 README 的「code/ 目录约定」表为准。

```bash
# Python 单文件
python 03-tool-calling/code/02-single-tool.py

# Go 单文件
go run 02-go/code/01-hello.go

# 成品服务（在各自目录内）
cd 99-projects/<name> && go run .      # 或 uvicorn main:app --reload
```

## 提交信息规范

```
feat(03): 单工具调用闭环
fix(04): 切片重叠导致召回重复
docs(06): 补充 checkpointer 踩坑
```

`type` 用 `feat` / `fix` / `docs` / `refactor` / `chore`，scope 是专题编号。半年后回看，这份历史本身就是能力证明。
