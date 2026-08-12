# 面试回答框架

Agent 面试最怕两个极端：只背概念，或者一上来就堆框架名。好的回答通常是“定义清楚、边界明确、机制具体、风险可控、指标可评估”。

## 概念题回答框架

适合回答“什么是 Agent”“什么是 MCP”“什么是 RAG 评测”这类题。

```text
1. 一句话定义
2. 它解决的问题
3. 核心组成或机制
4. 和相近概念的区别
5. 常见失败模式
6. 工程上如何落地
7. 用什么指标评估
```

示例：

```text
Agent 是一个围绕 LLM 构建的可行动系统，它不只是生成文本，而是能在目标、状态、工具和反馈循环中多步完成任务。和普通 chatbot 相比，Agent 更强调工具调用、状态更新和终止条件；和 workflow 相比，Agent 的路径更动态。生产中要关注工具权限、循环失控、上下文污染和 eval/trace。
```

## 对比题回答框架

适合回答“Agent vs workflow”“MCP vs function calling”“RAG vs memory”。

```text
1. 先分别定义两个概念
2. 对比输入、输出、控制流、适用场景、风险
3. 给一个适合 A 的例子
4. 给一个适合 B 的例子
5. 说明工程中常常如何组合使用
```

## 系统设计题回答框架

适合回答智能客服 Agent、代码 Agent、数据分析 Agent。

```text
1. 澄清需求和约束
2. 定义成功指标和风险动作
3. 画主链路
4. 拆模块：router、planner、tools、RAG、memory、policy、eval、trace
5. 说明关键数据结构和工具 schema
6. 说明失败恢复和人工介入
7. 说明性能、成本、扩展性和灰度发布
8. 总结权衡
```

## 失败排查题回答框架

适合回答“Agent 为什么跑偏”“RAG 为什么幻觉”“工具为什么调用错”。

```text
1. 复现：拿到输入、trace、模型版本、prompt 版本、工具版本
2. 分层定位：输入、prompt、模型、检索、工具、状态、权限、外部系统
3. 判断影响范围：偶发、特定用户、特定任务、全局回归
4. 临时止血：降级、禁用工具、提高审批、回滚版本
5. 根因修复：schema、prompt、retrieval、policy、eval case
6. 回归验证：离线 eval、线上小流量、监控指标
```

## 项目题 STAR+

传统 STAR 可以用，但 Agent 项目最好多补一层指标和失败复盘。

```text
S: 场景和业务问题
T: 目标和约束
A: 架构、工具、RAG、记忆、eval、trace、安全
R: 结果指标
+: 失败案例、权衡、下一步优化
```

## 高频对比答案

### Agent vs Workflow

- Workflow：流程由代码预先定义，适合稳定、可审计、低风险任务。
- Agent：下一步由模型根据状态和工具反馈动态决定，适合开放、多步、信息不完整任务。
- 生产中常组合：外层 workflow 控制阶段和权限，内部某些节点使用 Agent。

### Agent vs Chatbot

- Chatbot 关注对话体验。
- Agent 关注任务完成和行动能力。
- 一个客服 chatbot 可以没有工具；客服 Agent 通常要查订单、查政策、申请退款和转人工。

### RAG vs Memory

- RAG 面向外部知识检索，通常来自文档、网页、数据库。
- Memory 面向会话和用户历史，包括短期任务状态和长期偏好。
- RAG 需要引用和权限过滤；memory 需要写入策略、隐私和遗忘机制。

### Function Calling vs MCP

- Function calling 是模型选择函数和参数的调用模式。
- MCP 是标准化连接外部工具、资源和 prompt 的协议。
- 可以把 MCP server 暴露的工具交给模型通过 function calling 使用。

### Tool vs Skill

- Tool 是可执行动作，例如查询订单、运行 SQL、搜索网页。
- Skill 是可复用的任务知识包，例如什么时候触发、怎么分步骤、有什么限制。
- Skill 可以指导 Agent 如何使用多个工具完成一类任务。

### ReAct vs Plan-and-Execute

- ReAct 边推理边行动，适合环境反馈强、不确定性高的任务。
- Plan-and-Execute 先拆计划再执行，适合长任务和需要用户确认的任务。
- 长任务里常用先规划，再在执行中局部 ReAct。

### Reflection vs Eval

- Reflection 是 Agent 自己复盘，可能用于下一步修正。
- Eval 是外部评测体系，用于判断行为是否达标。
- Reflection 不能替代 eval，因为它可能自我合理化。

### Single-Agent vs Multi-Agent

- Single-agent 简单、低成本、容易调试。
- Multi-agent 适合角色分工、并行、互审和权限隔离。
- Multi-agent 的问题是协调成本、冲突、重复工作和 trace 复杂度。

### Harness vs Framework

- Framework 提供组件，例如模型、工具、图、状态、回调。
- Harness 是更完整的运行时脚手架，负责 loop、工具执行、上下文、审批、观测和进度管理。
- 面试中可以把 harness 理解为“让模型持续、可控地完成任务的发动机”。

### Offline Eval vs Online Eval

- Offline eval 用人工整理的测试集做开发和回归。
- Online eval 监控真实流量中的质量、安全和漂移。
- 成熟系统会把线上失败样例回流到离线测试集。

### Guardrail vs Human-in-the-Loop

- Guardrail 是自动规则、模型或策略检查。
- Human-in-the-loop 是把高风险或不确定动作交给人确认。
- 高风险写操作通常两者都要有。

### Prompt Optimization vs System Optimization

- Prompt optimization 改指令、格式、例子和工具描述。
- System optimization 改工具 schema、检索、状态、模型路由、缓存、eval 和权限。
- 生产问题通常不能只靠改 prompt 解决。

