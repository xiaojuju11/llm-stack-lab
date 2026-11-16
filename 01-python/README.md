# 01 - 为 LLM 应用服务的 Python

不是「Python 从入门到精通」，只学 LLM 应用真正会用到的部分：**把模型返回的不可靠文本，变成结构化的、可测试的数据**。

## 目标

跑完这个专题，我应该能：

- 用 pydantic 定义请求/响应/模型输出的结构，并让非法数据在边界处被拦住
- 用 asyncio 并发调用多个模型接口，而不是 for 循环串行等
- 写出带类型标注、能被 mypy 检查通过的业务代码
- 用 pytest 给工具函数和 API 端点写测试

## 前置

- 会用 Python 写函数、类、`pip install`
- 知道 HTTP 请求、JSON 是什么

## 章节

- [ ] 1.1 环境与包管理：venv / uv / pyproject.toml，锁定版本
- [ ] 1.2 类型标注：`Optional`、`Literal`、`TypedDict`、泛型；为什么 LLM 应用离不开类型
- [ ] 1.3 pydantic v2 基础：BaseModel、Field 校验、嵌套模型、`model_validate`
- [ ] 1.4 **模型输出结构化**：`response_format`、JSON mode、校验失败后的重试策略
- [ ] 1.5 asyncio 基础：`async/await`、`asyncio.gather`、`Semaphore` 限流、超时控制
- [ ] 1.6 装饰器与上下文管理器：写一个计时/重试装饰器
- [ ] 1.7 错误处理与日志：自定义异常体系、结构化日志（不打印密钥和完整 prompt）
- [ ] 1.8 测试：pytest、`monkeypatch` 打桩模型调用、fixture 复用
- [ ] 1.9 项目结构：src layout、配置从环境变量读取并集中校验

## 验收标准

1. 写一个 CLI 工具：接收一段自然语言，调用模型返回**严格符合 pydantic 模型**的结构化结果，失败自动重试 2 次。
2. 并发调用 10 个接口，带并发上限和超时，总耗时接近单次耗时而非 10 倍。
3. 给上面的工具函数写测试，`pytest` 全绿，且测试过程中**不发起真实网络请求**。

## code/ 目录约定

| 文件 | 内容 |
|---|---|
| `01-env-check.py` | 打印解释器版本、已装包版本、能否读到 .env |
| `02-typed-basics.py` | 类型标注对照示例 |
| `03-pydantic-model.py` | 校验成功 / 失败的对照 |
| `04-structured-output.py` | 让模型输出 JSON 并校验 |
| `05-async-gather.py` | 并发 vs 串行耗时对比 |
| `06-retry-decorator.py` | 手写重试装饰器 |
| `07-pytest-demo/` | 一个可 `pytest` 的最小项目 |

## 复盘（当天填）

- 卡住的地方：
- 报错原文与根因：
- 哪块是 AI 写的、我照抄的（下周重写）：

## AI 协作记录

（按 `docs/vibe-coding.md` 的模板记）
