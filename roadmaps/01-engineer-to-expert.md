# 工程师到专家路线

这条路线面向已经能写 API、做 Web 服务或 ML 应用的工程师。目标是在 12 到 16 周内掌握 Agent 系统设计、生产化和技术选型。

## 阶段 1：重建基础判断

时间：1-2 周。

学习：

- Agent 与 workflow 的边界。
- LLM 的不确定性。
- 上下文工程。
- 工具调用和权限。

产出：

- `ADR-001-agent-or-workflow.md`
- 一个最小工具调用 Agent。
- 20 条核心评测样例。

## 阶段 2：RAG 与知识系统

时间：2-3 周。

学习：

- 文档加载和切分。
- metadata 和权限过滤。
- 关键词、向量、混合检索。
- rerank 和引用。
- Agentic RAG。

产出：

- 一个带引用的内部知识库 Agent。
- RAG 评测集。
- 提示注入防护策略。

## 阶段 3：编排和多 Agent

时间：2-3 周。

学习：

- prompt chaining。
- routing。
- parallelization。
- orchestrator-workers。
- evaluator-optimizer。
- handoff。
- 多 Agent 通信 schema。
- MCP 与 A2A 的边界。

产出：

- 一个研究报告多 Agent demo。
- 每个 Agent 的职责和工具边界。
- 端到端 trace。

## 阶段 4：评测、观测和安全

时间：2-3 周。

学习：

- offline eval。
- trajectory eval。
- LLM-as-judge。
- trace/span。
- 成本、延迟和失败率指标。
- 权限、审批、沙箱、审计。

产出：

- 至少 50 条评测样例。
- CI 回归门禁。
- threat model。
- production readiness checklist。

## 阶段 5：生产化架构

时间：3-5 周。

学习：

- session 和 checkpoint。
- 长任务异步执行。
- tool gateway。
- 状态机。
- 版本管理。
- 部署和监控。
- 人工介入。

产出：

- 一个接近生产形态的 Agent 项目。
- 架构文档。
- runbook。
- dashboard 指标草案。
- 回滚和降级方案。

## 专家能力标准

你可以认为自己进入“Agent 技术精通”的门槛，是能独立完成这些判断：

- 明确说明为什么某需求需要或不需要 Agent。
- 设计工具 schema、权限和审批机制。
- 解释每个上下文来源的信任级别。
- 用评测数据证明 prompt、模型或框架改动是否提升。
- 读 trace 定位失败来自模型、检索、工具、状态还是权限。
- 给出成本、延迟和可靠性优化方案。
- 在框架抽象失效时，能回到基础 Agent loop 排查问题。
