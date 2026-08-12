# 项目与简历表达

Agent 面试中，项目的价值不在于“我调用了某个模型”，而在于你证明自己能把不确定的模型行为工程化。

## GitHub 项目最低配置

一个能放进简历的 Agent 项目，建议至少包含：

- 清晰 README：问题背景、目标用户、核心能力、技术栈、运行方式。
- 架构图：模型、工具、RAG、记忆、eval、trace、安全和部署关系。
- 可运行 demo：命令行、Web UI 或 API 都可以。
- 工具调用：至少 3 类工具，例如搜索、数据库、文件、代码执行、浏览器、业务 API。
- 状态管理：session state、任务进度、短期记忆或长期记忆。
- 评测集：至少 30 到 100 条任务，包含正常、边界、攻击和失败场景。
- 评测报告：成功率、轨迹正确率、成本、延迟、失败归因。
- 安全边界：权限、审批、沙箱、敏感信息处理。
- 部署说明：Docker、本地启动、环境变量、可选云部署。

## 推荐项目 1：代码修复 Agent

### 项目目标

输入 issue 或失败测试，Agent 自动读取仓库、定位问题、生成补丁、运行测试并输出 PR 摘要。

### 技术栈

- Python 或 TypeScript。
- LangGraph / OpenAI Agents SDK / 自研 loop。
- 文件系统工具、搜索工具、patch 工具、测试执行工具。
- SQLite/Postgres 存 trace 和 eval 结果。
- Docker sandbox。

### 亮点

- 支持最小相关测试和全量测试两级验证。
- 记录每次文件读取、修改、测试失败和重试。
- 评测 50 个开源 repo issue 或自制 bug task。
- 指标包括修复成功率、测试通过率、无关 diff 比例和平均迭代次数。

### 简历 bullet 示例

```text
Built a coding agent that reads GitHub issues, edits repository files, runs tests in a sandbox, and generates PR summaries; evaluated on 50 bug-fix tasks with trace-level failure analysis.
```

```text
Implemented tool-level permissions, patch validation, retry logic, and regression evals, reducing irrelevant file modifications and improving test-pass rate across iterative runs.
```

## 推荐项目 2：企业知识库 Agent

### 项目目标

让用户查询内部文档、PDF、网页和表格，Agent 能检索、引用、拒答、处理多轮追问并遵守权限。

### 技术栈

- FastAPI + Postgres/pgvector 或 Chroma。
- 文档解析、chunk、embedding、BM25、rerank。
- RAG eval、citation verifier、trace。
- 简单 Web UI 或 CLI。

### 亮点

- 支持 metadata 和 ACL 过滤。
- 支持 hybrid search 和 rerank。
- 对“不知道”场景做拒答评测。
- 引用必须能回到原文片段。

### 简历 bullet 示例

```text
Developed an enterprise knowledge-base agent with hybrid retrieval, reranking, ACL filtering, citation verification, and no-answer handling for grounded responses.
```

```text
Built a RAG evaluation suite covering retrieval recall, citation precision, hallucination, permission leakage, and stale-document scenarios.
```

## 推荐项目 3：Agent Eval Harness

### 项目目标

为不同 Agent 提供统一任务集、runner、trace collector、评分器和回归报告。

### 技术栈

- Python runner。
- YAML/JSON task dataset。
- deterministic evaluator + LLM-as-judge。
- HTML/Markdown 报告。
- GitHub Actions 可选。

### 亮点

- 支持 final response、single-step、trajectory、safety、cost/latency 评测。
- 支持 replay 和失败归因标签。
- 支持把线上失败样例加入离线数据集。

### 简历 bullet 示例

```text
Built an agent evaluation harness with task datasets, trace capture, trajectory scoring, safety checks, and CI regression gates for comparing agent versions.
```

```text
Designed rubric-based evaluators and failure taxonomy to diagnose prompt, retrieval, tool schema, policy, and model-capability errors.
```

## 项目 README 推荐结构

```markdown
# Project Name

## What it does

## Why Agent

## Architecture

## Key Features

## Evaluation

## Safety

## Cost and Latency

## Demo

## Run Locally

## Limitations

## Roadmap
```

## 面试中讲项目的顺序

1. 一句话说明项目解决的问题。
2. 说明为什么需要 Agent，而不是普通脚本或 workflow。
3. 画出核心链路。
4. 讲一个最难的技术点。
5. 讲评测方法和结果。
6. 讲一个失败案例和你如何改。
7. 讲生产化还缺什么。

## 项目评分 Rubric

| 维度 | 1 分 | 2 分 | 3 分 |
| --- | --- | --- | --- |
| 任务真实性 | toy demo | 有真实场景 | 可复现真实任务集 |
| 工具调用 | 1 个工具 | 多个工具 | 工具权限、审批、错误恢复完整 |
| 状态管理 | 无状态 | 有 session | 有短期/长期记忆和压缩 |
| 评测 | 手工试用 | 有少量 case | 有分层 eval 和报告 |
| 可观测性 | 只打日志 | 有 trace | 可回放、可归因、可对比 |
| 安全 | 口头说明 | 有规则 | 最小权限、沙箱、审批、审计 |
| 生产化 | 本地脚本 | API 或 UI | Docker、部署、监控、降级 |

目标是让主项目至少达到 15 分以上，最好达到 18 分以上。

