# 08. 多 Agent 与协议

上一章解释了工作流和编排。本章讨论更复杂的场景：多个 Agent 如何协作，以及 MCP、A2A 这类协议分别解决什么问题。

本章目标：理解多 Agent 的真实价值、常见模式和协议边界。
下一章：无论单 Agent 还是多 Agent，都必须用评测和观测证明它可靠。

## 多 Agent 解决什么

多 Agent 的价值不是“人多力量大”，而是隔离复杂性：

- 隔离职责：研究、写作、审查、执行分开。
- 隔离工具：退款 Agent 有退款工具，FAQ Agent 没有。
- 隔离上下文：财务资料不进入客服 Agent。
- 隔离模型：简单任务用快模型，复杂任务用强模型。
- 隔离失败：某个专家失败，不一定拖垮整个系统。

如果没有这些隔离需求，多 Agent 往往只是增加成本和调试难度。

## 常见多 Agent 模式

| 模式 | 说明 | 适合场景 |
| --- | --- | --- |
| Manager | 一个中心 Agent 调用多个专家 Agent | 需要统一对外体验和汇总 |
| Handoff | 一个 Agent 把控制权交给另一个 Agent | 客服分流、专业升级 |
| Pipeline | Agent 按固定顺序处理 | 研究 -> 写作 -> 审稿 |
| Blackboard | 多 Agent 读写共享任务板 | 复杂协作、长期任务 |
| Debate / Review | 多 Agent 独立判断再比较 | 风险审查、方案评估 |

Manager 更可控，handoff 更自然，pipeline 更稳定，blackboard 更灵活但更难治理。

## Agent 通信要传什么

不要默认共享完整对话历史。通信内容应尽量结构化：

```json
{
  "task": "审查合同付款条款",
  "context_refs": ["doc://contract#section-4"],
  "constraints": ["只评估法律风险", "不修改原文"],
  "expected_output": "risk_items[]",
  "deadline": "10m",
  "permissions": ["read_contract"]
}
```

优秀的 Agent 通信像 API 契约，而不是把所有上下文扔给下游。

## MCP 与 A2A 的区别

| 协议 | 解决的问题 | 典型关系 |
| --- | --- | --- |
| MCP | Agent 或 AI 应用如何接入工具、资源、提示 | Agent -> Tool/Context Server |
| A2A | 独立 Agent 系统之间如何发现、通信、协作 | Agent Client -> Remote Agent |

简单说：

- MCP 让 Agent 使用工具和上下文。
- A2A 让 Agent 与另一个远程 Agent 协作。

两者可以互补：一个远程 Agent 通过 A2A 对外提供能力，而它内部可能通过 MCP 使用数据库、文件系统或业务 API。

## A2A 的核心概念

A2A，Agent2Agent，是用于独立 Agent 系统互操作的开放协议。它强调：

- Agent Discovery：通过 Agent Card 描述身份、能力、技能、端点和认证要求。
- Message：客户端和远程 Agent 的通信回合。
- Task：有状态的工作单元，可经历生命周期。
- Artifact：任务产物，例如报告、文件、图片、结构化数据。
- Streaming / Async：支持长任务的流式更新和异步通知。
- Versioning：客户端和服务端需要协商协议版本。

A2A 适合远程、异构、可能互相不透明的 Agent 系统。它不适合替代进程内函数调用。

## 多 Agent 的失败模式

| 失败模式 | 说明 | 缓解 |
| --- | --- | --- |
| 职责重叠 | 多个 Agent 都觉得自己该处理 | 明确路由规则和 handoff 条件 |
| 上下文丢失 | 交接时漏掉关键事实 | 结构化交接摘要 |
| 循环交接 | A 交给 B，B 又交回 A | 记录交接历史和最大次数 |
| 成本膨胀 | 多 Agent 并行和重复推理 | 预算、缓存、裁剪工具 |
| 权限扩散 | 每个 Agent 都拿到过多工具 | 最小权限和工具隔离 |
| 难以评测 | 只看最终答案，不知道中间错哪 | 轨迹评测和 trace |

## 什么时候不要用多 Agent

- 单 Agent 加清晰工具已经能稳定完成。
- 任务步骤固定，可以用工作流。
- 你还没有基础评测集。
- 没有明确的职责边界。
- 没有可观测性，无法调试消息传递和工具调用。

多 Agent 应该是复杂性隔离手段，不是默认架构。

## 本章练习

设计一个“研究报告系统”：

- Research Agent：搜索和筛选资料。
- Analyst Agent：抽取观点和证据。
- Writer Agent：写报告。
- Reviewer Agent：审查引用和逻辑。

为每个 Agent 写出职责、可用工具、输入输出 schema、不能访问的数据，以及失败时如何交接。

下一章会讲如何证明这些设计真的有效：评测与可观测性。
