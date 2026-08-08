# 0 到 1 学习路线

这条路线面向完全没有 Agent 背景的学习者。目标不是速成框架 API，而是在 4 周内建立正确的概念和最小实践能力。

## 第 1 周：理解 Agent 边界

阅读：

- `docs/00-how-to-use.md`
- `docs/01-what-is-agent.md`
- `docs/02-llm-foundations.md`

任务：

- 用自己的话解释 Agent、RAG、工作流的区别。
- 找 5 个产品案例，判断它们是不是 Agent。
- 写一页笔记：为什么 Agent 不能被当成普通函数。

验收：

- 能说清楚 Agent 的组成：模型、指令、状态、工具、循环、护栏。
- 能判断什么时候不该做 Agent。

## 第 2 周：提示词、上下文和工具

阅读：

- `docs/03-prompt-context.md`
- `docs/04-tools-function-calling.md`

任务：

- 为一个客服 Agent 写上下文契约。
- 设计 5 个工具，包括名称、参数、返回值、权限和失败策略。
- 跑通 `examples/minimal-agent`。

验收：

- 能解释模型负责“选择工具”，runtime 负责“执行工具”。
- 能识别高风险动作工具。

## 第 3 周：RAG、记忆和 Agent loop

阅读：

- `docs/05-rag-memory.md`
- `docs/06-agent-loop-planning.md`

任务：

- 为一个知识库问答系统设计 RAG 流程。
- 写出一个 Agent 状态结构。
- 为一个长任务定义停止条件。

验收：

- 能区分 RAG 和长期记忆。
- 能画出 Observe -> Decide -> Act -> Reflect 循环。

## 第 4 周：评测、安全和小项目

阅读：

- `docs/09-evaluation-observability.md`
- `docs/10-safety-security.md`
- `docs/13-capstone-projects.md`

任务：

- 做项目 1：结构化信息抽取器。
- 做项目 2：最小工具调用 Agent。
- 写 20 条评测样例。
- 写一份风险清单。

验收：

- 项目可运行。
- 有 README。
- 有评测样例。
- 能解释已知限制。

## 继续前进

完成 4 周后，进入 [工程师到专家路线](01-engineer-to-expert.md)。
