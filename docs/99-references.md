# 参考资料

资料核验日期：2026-08-07。以下链接优先选择官方文档和论文。框架 API、模型名和协议版本会变化，实践时请再次核对。

## 官方指南与工程实践

- OpenAI, [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)：Agent 定义、适用场景、工具、指令、编排和护栏。
- Anthropic, [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)：工作流与 Agent 的区别，prompt chaining、routing、parallelization、orchestrator-workers、evaluator-optimizer 等模式。

## Agent SDK 与框架

- OpenAI, [Agents SDK documentation](https://openai.github.io/openai-agents-python/)：Agent、工具、handoff、guardrails、sessions、tracing。
- LangChain, [Agents documentation](https://docs.langchain.com/oss/python/langchain/agents)：`create_agent`、工具、上下文、流式和 LangGraph runtime。
- LangChain, [LangGraph v1 release notes](https://docs.langchain.com/oss/python/releases/langgraph-v1)：图执行、持久化、checkpoint、人机协作。
- LlamaIndex, [Agents use case documentation](https://developers.llamaindex.ai/python/framework/use_cases/agents/)：Agentic RAG、工具、工作流和数据增强 Agent。
- Microsoft, [Agent Framework overview](https://learn.microsoft.com/en-us/agent-framework/overview/)：Agents、Harness、Workflows、MCP、多 provider 和企业工程能力。
- Microsoft, [Agent Framework Workflows](https://learn.microsoft.com/en-us/agent-framework/workflows/)：函数式工作流、图工作流、checkpoint、人机协作和多 Agent 编排。

## 协议

- Model Context Protocol, [latest specification](https://modelcontextprotocol.io/specification/latest)：MCP 规范、tools、resources、prompts、安全原则。
- Model Context Protocol, [architecture overview](https://modelcontextprotocol.io/docs/learn/architecture)：Host、Client、Server、数据层和传输层。
- A2A Protocol, [latest specification](https://a2a-protocol.org/latest/specification/)：Agent Card、Message、Task、Artifact、版本协商和协议绑定。
- A2A Protocol, [Life of a Task](https://a2a-protocol.org/latest/topics/life-of-a-task/)：任务生命周期、上下文 ID、任务 ID、artifact 更新。

## 经典论文与思想来源

- Yao et al., [ReAct: Synergizing Reasoning and Acting in Language Models](https://react-lm.github.io/)：推理和行动交替的 Agent 思想。
- Schick et al., [Toolformer: Language Models Can Teach Themselves to Use Tools](https://doi.org/10.48550/arXiv.2302.04761)：模型学习工具使用的早期代表工作。
- Shinn et al., [Reflexion: Language Agents with Verbal Reinforcement Learning](https://doi.org/10.48550/arXiv.2303.11366)：通过语言反思和情景记忆改进 Agent 后续尝试。

## 评测与观测

- LangSmith, [Evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts)：离线评测、线上评测、runs、threads、human/code/LLM-as-judge/pairwise evaluator。
- OpenAI, [Evals](https://evals.openai.com/)：面向模型和 Agent 能力的评测研究与数据集。

## 维护建议

每次更新手册时，建议检查：

- MCP latest spec 是否仍指向当前版本。
- A2A latest spec 是否有破坏性变更。
- OpenAI Agents SDK、LangChain、LlamaIndex、Microsoft Agent Framework 的 API 是否更新。
- 示例代码是否仍能运行。
- 参考资料是否仍是官方页面或论文。
