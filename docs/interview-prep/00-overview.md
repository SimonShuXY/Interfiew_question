# Agent 面试准备总览

本目录是一套面向 Agent 方向岗位的面试准备项目。目标不是背完术语，而是让你能在面试中讲清楚：

- Agent 的能力边界是什么。
- 一个 Agent 系统如何从原型走到生产。
- RAG、工具调用、记忆、规划、多 Agent、评测、安全和成本分别解决什么问题。
- 当面试官给出一个真实业务场景时，如何设计可落地、可评估、可维护的 Agent 架构。

资料核验日期：2026-08-12。Agent 生态变化很快，涉及具体框架 API、模型能力、协议版本和价格时，请以官方文档为准。

## 使用方式

建议按下面顺序准备：

1. 用 [40 天学习计划](01-40-day-plan.md) 安排节奏。
2. 每天从 [92 道面试题](02-question-bank-92.md) 中抽题口述。
3. 用 [系统设计题](03-system-design.md) 练习完整架构表达。
4. 用 [回答框架](04-answer-frameworks.md) 把答案组织得更像工程师，而不是像背书。
5. 用 [项目与简历表达](05-project-and-resume.md) 把学习结果沉淀成 GitHub 项目和简历 bullet。
6. 用 [模拟面试](06-mock-interview.md) 做最后冲刺。

## 面试知识地图

| 学习阶段 | 核心内容 | 重点解决的问题 |
| --- | --- | --- |
| Agent 基础 | Agent 定义、核心组成、Agent 与 LLM、聊天机器人、Workflow 的区别 | 建立清晰的 Agent 能力边界 |
| LLM 与 Prompt 基础 | Token、采样参数、提示层级、Few-shot、结构化输出、Prompt Cache | 讲清模型调用中最常见的基础问题 |
| 规划与执行 | Agent Loop、ReAct、Plan-and-Execute、Reflection、状态机、终止条件 | 理解 Agent 如何多步完成任务，以及如何避免跑偏和死循环 |
| 工具、MCP 与 Skills | Function Calling、工具设计、参数 Schema、读写隔离、MCP、Skill | 回答 Agent 如何连接外部世界并安全执行动作 |
| RAG 与知识库 | Embedding、向量数据库、Chunk、混合检索、Rerank、Query Rewrite、RAG 评测 | 掌握知识检索链路与幻觉治理 |
| 记忆与上下文工程 | 短期记忆、长期记忆、Session State、Context Window、上下文压缩与污染 | 理解上下文如何组织，而不是一味把 Prompt 写长 |
| Multi-Agent 与 Harness | 多 Agent 编排、通信、共享状态、冲突治理、Harness | 理解从单 Agent 到复杂系统的演进方式 |
| 安全、评测与可观测 | Prompt Injection、最小权限、Human-in-the-Loop、Eval、Trace、失败归因 | 回答系统如何从“能运行”走向“可信赖” |
| 生产架构、性能与成本 | 模型路由、时延、Token 成本、缓存、限流、降级、灰度与回滚 | 建立生产级 Agent 的完整工程视角 |
| 综合系统设计 | 智能客服 Agent、代码 Agent、数据分析 Agent、知识库 Agent | 把前面的知识串成可落地的系统设计回答 |

## 准备到什么程度算合格

最低合格线：

- 能清楚区分 Agent、workflow、RAG、chatbot 和 multi-agent。
- 能独立画出一个带工具、记忆、评测、trace 和人工审批的 Agent 架构。
- 能解释至少 5 类失败模式：工具参数错、检索错、上下文污染、循环失控、权限越界。
- 能针对一个业务场景设计 20 到 50 条 eval case。
- 能讲清一个自己的 Agent 项目，包括数据流、工具接口、评测结果和生产风险。

较强水平：

- 能把模型能力、确定性代码、工具权限和人工审批分层设计。
- 能说明离线评测、线上评测和 trace 如何形成闭环。
- 能对比 LangGraph、OpenAI Agents SDK、LlamaIndex、Microsoft Agent Framework、MCP 的适用边界。
- 能给出成本和延迟优化方案，而不只说“换更便宜的模型”。

优秀水平：

- 能用指标描述系统质量，例如任务成功率、轨迹正确率、人工介入率、P95 延迟、单任务成本、幻觉率。
- 能解释为什么某些任务应该用 workflow，而不是强行上 autonomous agent。
- 能把安全和权限放进主架构，而不是最后补一句“加 guardrail”。
- 能从失败 trace 中定位问题属于 prompt、tool schema、retrieval、policy、model capability 还是业务流程。

## GitHub 项目建议

这个仓库适合被包装成：

- Agent 面试准备手册。
- Agent 工程学习路线。
- Agent 系统设计题库。
- 个人 Agent 项目准备记录。

建议在 GitHub README 中突出三点：

- 覆盖 10 个 Agent 面试核心模块。
- 包含 92 道题和 40 天准备节奏。
- 强调工程落地：eval、trace、安全、成本、生产化。

