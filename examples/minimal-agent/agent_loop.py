from __future__ import annotations

import ast
import operator
import sys
from dataclasses import dataclass
from typing import Any


ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


@dataclass
class ToolCall:
    name: str
    arguments: dict[str, Any]


@dataclass
class Decision:
    kind: str
    content: str | None = None
    tool_call: ToolCall | None = None


def calculate(expression: str) -> str:
    """Safely evaluate a small arithmetic expression."""
    tree = ast.parse(expression, mode="eval")
    result = _eval_node(tree.body)
    return str(result)


def _eval_node(node: ast.AST) -> float:
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in ALLOWED_OPERATORS:
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        return ALLOWED_OPERATORS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in ALLOWED_OPERATORS:
        operand = _eval_node(node.operand)
        return ALLOWED_OPERATORS[type(node.op)](operand)
    raise ValueError("only arithmetic expressions are supported")


TOOLS = {
    "calculate": calculate,
}


def fake_model_decide(state: dict[str, Any]) -> Decision:
    """Simulate an LLM deciding whether to call a tool or finish."""
    if not state["observations"]:
        return Decision(
            kind="tool_call",
            tool_call=ToolCall(
                name="calculate",
                arguments={"expression": state["goal"]},
            ),
        )

    latest = state["observations"][-1]
    return Decision(kind="final", content=f"The answer is {latest['result']}.")


def run_agent(goal: str, max_turns: int = 4) -> str:
    state: dict[str, Any] = {
        "goal": goal,
        "observations": [],
    }

    for _ in range(max_turns):
        decision = fake_model_decide(state)

        if decision.kind == "final":
            assert decision.content is not None
            return decision.content

        if decision.kind == "tool_call":
            assert decision.tool_call is not None
            tool_call = decision.tool_call
            print(f"Agent -> call {tool_call.name}({tool_call.arguments})")

            if tool_call.name not in TOOLS:
                state["observations"].append(
                    {"tool": tool_call.name, "error": "unknown tool"}
                )
                continue

            try:
                result = TOOLS[tool_call.name](**tool_call.arguments)
                print(f"Tool  -> {result}")
                state["observations"].append(
                    {"tool": tool_call.name, "result": result}
                )
            except Exception as exc:
                state["observations"].append(
                    {"tool": tool_call.name, "error": str(exc)}
                )
                return f"Cannot complete task: {exc}"

    return "Cannot complete task: reached max turns."


def main() -> None:
    goal = " ".join(sys.argv[1:]).strip()
    if not goal:
        goal = "12 * (3 + 4)"
    print(run_agent(goal))


if __name__ == "__main__":
    main()
