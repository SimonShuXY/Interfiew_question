# Agent 从入门到精通手册

这是一套面向 0 基础学习者的 Agent 技术手册。它从“什么是 Agent”讲起，逐步过渡到工具调用、RAG、记忆、规划、工作流、多 Agent、协议、评测、观测、安全和生产化工程，目标是帮助读者从能理解概念，走到能设计、实现、评测并上线 Agent 系统。

资料核验日期：2026-08-07。Agent 生态变化很快，涉及框架 API、模型能力和协议版本时，请以官方文档为准。

## 适合谁

- 完全没有 Agent 背景，但想系统入门的人。
- 已会一点提示词或 RAG，想补齐工程知识的人。
- 准备做 Agent 项目、课程、分享、团队培训或 GitHub 开源手册的人。
- 想从“会调 API”提升到“能设计生产级 Agent 系统”的工程师。

## 学习目标

读完并完成配套练习后，你应该能够：

- 区分 LLM 应用、RAG、工作流、Agent、多 Agent。
- 解释 Agent 的核心循环：目标、状态、模型、工具、观察、停止条件。
- 为 Agent 设计清晰、可测试、低风险的工具接口。
- 判断什么时候该用单 Agent、工作流、多 Agent、MCP 或 A2A。
- 搭建基础 Agent 原型，并设计评测集、日志、追踪和回归门禁。
- 理解生产环境中的权限、安全、成本、延迟、可靠性和人工介入问题。

## 章节路径

| 阶段 | 章节 | 你会建立的能力 |
| --- | --- | --- |
| 入门 | 00-03 | 认识 Agent，理解 LLM、提示词、上下文 |
| 核心 | 04-06 | 掌握工具调用、RAG、记忆、Agent 循环和规划 |
| 架构 | 07-08 | 设计工作流、多 Agent 协作和协议边界 |
| 工程 | 09-11 | 做评测、观测、安全和生产化落地 |
| 精通 | 12-13 | 选型框架，完成可展示的综合项目 |
| 附录 | 14, 99 | 查询术语和参考资料 |

## 快速开始

直接按顺序阅读：

1. [如何使用本手册](docs/00-how-to-use.md)
2. [Agent 是什么](docs/01-what-is-agent.md)
3. [LLM 基础](docs/02-llm-foundations.md)

运行最小示例：

```bash
python3 examples/minimal-agent/agent_loop.py "12 * (3 + 4)"
```

本地预览文档站点：

```bash
python3 -m pip install -r requirements-docs.txt
mkdocs serve
```

## 项目结构

```text
.
├── README.md
├── SUMMARY.md
├── mkdocs.yml
├── docs/
│   ├── 00-how-to-use.md
│   ├── 01-what-is-agent.md
│   └── ...
├── roadmaps/
│   ├── 00-zero-to-one.md
│   ├── 01-engineer-to-expert.md
│   └── checklists.md
├── examples/
│   └── minimal-agent/
└── .github/
    ├── ISSUE_TEMPLATE/
    └── workflows/
```

## 推荐学习方式

每章按“先概念、再判断标准、再练习”的顺序读。不要只背术语，Agent 的关键能力来自能把问题拆成工程边界：模型负责什么，代码负责什么，工具允许做什么，失败时如何停下来。

## 贡献

欢迎补充案例、修正框架 API、添加练习答案或翻译术语。提交前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。
