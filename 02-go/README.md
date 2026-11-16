# 02 - Go：把 AI 能力包成服务的那一层

Go 在这个仓库里不是主力语言，定位很明确：**Python 负责和模型打交道，Go 负责把能力包成高并发、低内存、易部署的线上服务**。所以只学到这里够用：语法 + 并发 + HTTP 服务 + 一个 LLM 客户端。

## 目标

- 能从 Python/Java 的直觉切换到 Go 的值语义、显式错误、接口隐式实现
- 能用 goroutine + channel + context 写并发程序，并用 `-race` 验证无数据竞争
- 能用标准库 `net/http` 写出带中间件、能优雅关闭的 REST 服务
- 能写一个调用 LLM 接口的客户端，含超时、重试、错误映射

## 前置

- 至少熟练一门语言（Python 即可）
- 知道 HTTP 方法、状态码、JSON

## 章节

- [ ] 2.1 环境与工具链：`go run/build/test`、Go Modules、`go.mod`
- [ ] 2.2 语法速通（用 Python 视角对照）：变量、零值、`:=`、控制流
- [ ] 2.3 切片与 map：三要素（指针/长度/容量）、`append` 扩容陷阱、共享底层数组
- [ ] 2.4 指针与值语义：`new` vs `make`、什么时候该传指针
- [ ] 2.5 结构体、方法、接口：值接收者 vs 指针接收者、隐式实现、`nil` 接口陷阱
- [ ] 2.6 错误处理：`error`、`%w` 包装、`errors.Is/As`、`defer` 与 panic 边界
- [ ] 2.7 并发：goroutine、channel、`select`、`context` 取消、`sync` 原语、worker pool
- [ ] 2.8 标准库实战：`encoding/json`、`io.Reader/Writer`、`net/http` 客户端
- [ ] 2.9 HTTP 服务：Go 1.22 增强路由、中间件链、统一错误结构、优雅关闭
- [ ] 2.10 测试与部署：表驱动测试、`httptest`、`go vet`、多阶段构建

## 验收标准

1. 能解释清楚「切片 A 和 B 共享底层数组，修改 A 影响了 B」的成因，并写出复现代码。
2. 写一个 worker pool：10 个任务、3 个 worker、支持超时取消、`go run -race` 无告警。
3. 写出一个 `/v1/chat` 端点：接收消息数组，转发给 LLM 接口，返回统一结构；上游超时返回 504，上游 5xx 映射为 502；含 `/healthz`。

## code/ 目录约定

每个 `.go` 文件都是独立 `package main`，用 `go run 文件名.go` 单跑：

| 文件 | 内容 |
|---|---|
| `01-hello.go` | 环境验证 |
| `02-slice-trap.go` | 切片共享底层数组的复现 |
| `03-interface.go` | 值/指针接收者对接口实现的影响 |
| `04-error-wrap.go` | `%w` 包装与 `errors.Is` |
| `05-worker-pool.go` | 带 context 取消的 worker pool |
| `06-http-server.go` | 最小 REST 服务 + 中间件 |
| `07-llm-client.go` | 带超时重试的 LLM 客户端 |

## 复盘（当天填）

- 卡住的地方：
- 报错原文与根因：
- 从 Python 思维带过来的错误直觉：

## AI 协作记录

（按 `docs/vibe-coding.md` 的模板记）
