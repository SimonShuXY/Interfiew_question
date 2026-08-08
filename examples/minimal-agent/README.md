# 最小 Agent loop 示例

这个示例不依赖外部模型 API，用一个确定性的 `fake_model_decide` 函数模拟模型决策。它的目标是帮助初学者看懂 Agent loop 的形状：

```text
用户目标 -> 模型决定工具调用 -> runtime 校验并执行工具 -> observation 回到模型 -> 最终回答
```

运行：

```bash
python3 agent_loop.py "12 * (3 + 4)"
```

示例输出会展示：

- Agent 想调用什么工具。
- 工具返回什么 observation。
- Agent 如何基于 observation 给出最终答案。

真实项目中，你需要把 `fake_model_decide` 替换成实际 LLM 调用，并增加 schema 校验、权限、日志、trace、最大预算和人工审批。
