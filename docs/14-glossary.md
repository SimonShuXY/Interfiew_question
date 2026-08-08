# 14. 术语表

本章用于快速回查。术语不追求百科式完整，而是服务 Agent 工程判断。

## Agent

由 LLM 驱动，能围绕目标读取上下文、调用工具、观察结果并循环推进任务的系统。

## Agentic Workflow

包含 LLM、工具或模型判断的工作流。步骤通常由代码预定义，灵活性低于自主 Agent，但更可控。

## Agent Loop

Agent 的执行循环：观察状态、决定下一步、调用工具或输出、更新状态，直到停止。

## Tool Calling

模型根据工具定义生成工具名和参数，由 runtime 执行工具并把结果返回模型。

## Function Calling

工具调用的一种常见形式，把普通函数暴露给模型使用。

## RAG

Retrieval-Augmented Generation，检索增强生成。先检索外部资料，再让模型基于资料回答。

## Agentic RAG

由 Agent 动态决定是否检索、如何改写查询、是否拆子问题、是否继续检索的 RAG。

## Memory

Agent 保存和使用跨轮次、跨任务信息的机制，包括工作记忆、情景记忆、语义记忆、程序记忆等。

## Context Engineering

设计和管理模型可见上下文的工程方法，包括指令、资料、历史、状态、工具定义和输出格式。

## Guardrails

护栏。用于约束 Agent 输入、工具调用、输出和运行过程的规则、模型、代码或人工流程。

## Handoff

一个 Agent 把控制权交给另一个 Agent。常用于客服分流和专家升级。

## Manager Pattern

中心 Agent 作为 manager，通过工具调用协调多个专家 Agent，并负责对外汇总。

## MCP

Model Context Protocol。用于 AI 应用连接外部工具、资源和提示的开放协议。

## A2A

Agent2Agent Protocol。用于独立 Agent 系统之间发现能力、通信、管理任务和交换产物的开放协议。

## Trace

一次 Agent 运行的完整执行记录，通常由多个 span 组成，包括模型调用、工具调用、检索、handoff 和护栏事件。

## Span

Trace 中的一个子步骤，例如一次模型调用或一次工具调用。

## LLM-as-judge

用 LLM 按 rubric 对输出或轨迹评分的方法。适合扩展评测，但需要人工校准。

## Checkpoint

任务执行中的可恢复状态。用于长任务、失败恢复和人工介入。

## Idempotency

幂等性。同一个动作重复执行不会产生重复副作用。动作工具尤其需要幂等设计。

## Sandbox

受限执行环境，用于隔离代码执行、文件访问、浏览器操作等高风险能力。

## Human-in-the-loop

人在回路。系统在关键节点请求人类确认、补充信息、审核或接管。
