# 06. Agent 循环与规划

前面几章分别讲了模型、上下文、工具、RAG 和记忆。本章把它们串成一个完整执行系统：Agent 如何一步步推进任务。

本章目标：理解 Agent loop、规划模式、停止条件和错误恢复。
下一章：比较更可控的工作流与更灵活的 Agent 编排。

## Agent loop

最小 Agent loop 包含四个动作：

```text
Observe -> Decide -> Act -> Reflect
```

| 动作 | 说明 | 例子 |
| --- | --- | --- |
| Observe | 读取目标、状态、上下文、工具结果 | “订单状态是已发货” |
| Decide | 判断下一步 | “需要检查退款政策” |
| Act | 调用工具或生成输出 | `check_refund_policy(order_id)` |
| Reflect | 根据结果更新状态 | “政策允许退货，但需用户补充照片” |

不是所有系统都需要显式“反思”，但任何 Agent 都需要根据 observation 更新状态。

## ReAct 思想

ReAct 指 reasoning and acting，即把推理和行动交替进行。现代 Agent 不一定暴露完整推理过程，但工程上仍保留这个结构：

```text
当前问题
  -> 判断需要什么信息
  -> 调用工具
  -> 观察结果
  -> 更新任务状态
  -> 决定继续或结束
```

ReAct 的价值在于让模型不要一次性猜答案，而是通过外部环境获得 ground truth。

## 规划模式

常见规划模式有三类：

| 模式 | 做法 | 适合场景 | 风险 |
| --- | --- | --- | --- |
| 即时决策 | 每一步只决定下一步 | 简单任务、工具少 | 容易局部最优 |
| 先计划后执行 | 先生成计划，再逐步执行 | 任务较长、步骤清晰 | 计划可能过时 |
| 动态重规划 | 执行中根据结果修正计划 | 搜索、代码、研究任务 | 成本和复杂度高 |

工程上常用混合方式：先生成粗计划，再允许每步根据工具结果调整。

## 停止条件

Agent 必须知道何时停止。常见停止条件：

- 模型返回最终答案。
- 达到结构化输出要求。
- 达到最大轮数。
- 达到成本或时间预算。
- 工具连续失败。
- 需要用户补充信息。
- 触发安全规则。
- 动作需要人工审批。

没有停止条件的 Agent 不可上线。

## 状态设计

Agent 状态至少包括：

```text
goal: 用户目标
facts: 已确认事实
plan: 当前计划
steps_done: 已完成步骤
pending_questions: 待确认问题
tool_history: 工具调用摘要
budget: 剩余轮数、时间、成本
final_criteria: 完成标准
```

状态要服务决策，不是记录一切。工具返回的大对象应保存到外部存储，只把摘要和引用放进模型上下文。

## 错误恢复

Agent 常见错误恢复策略：

| 情况 | 策略 |
| --- | --- |
| 参数错误 | 根据 schema 重新生成参数 |
| 工具超时 | 重试、换工具、降级、告知用户 |
| 信息不足 | 向用户提问，不要猜 |
| 结果矛盾 | 标记冲突，二次检索或请求人工 |
| 权限不足 | 请求审批或停止 |
| 多次失败 | 总结已尝试步骤，交给人工 |

错误恢复不是让模型无限重试，而是让系统可控地前进或停止。

## 最小伪代码

```python
state = init_state(user_goal)

for turn in range(max_turns):
    decision = model.decide(state, tools)

    if decision.type == "final":
        return validate_output(decision.output)

    if decision.type == "tool_call":
        checked_args = validate_args(decision.tool, decision.args)
        if requires_approval(decision.tool, checked_args):
            return request_human_approval(decision)
        observation = execute_tool(decision.tool, checked_args)
        state = update_state(state, decision, observation)
        continue

    if decision.type == "ask_user":
        return ask_user(decision.question)

return fail_with_summary(state)
```

## 本章练习

为“代码修复 Agent”写出状态字段和停止条件。至少考虑：

- 如何知道修复完成？
- 测试失败时如何重试？
- 文件编辑权限如何控制？
- 连续失败几次后交给人工？
- 如何记录每次工具调用？

下一章会比较两条路线：用固定工作流提高可控性，还是用更自主的 Agent loop 提高灵活性。
