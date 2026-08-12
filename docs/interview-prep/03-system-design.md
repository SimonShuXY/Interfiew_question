# Agent 系统设计题

Agent 系统设计面试的核心不是“用了什么框架”，而是你能否把不确定的模型行为放进一个可控、可评估、可审计的工程系统。

## 通用回答框架

建议按 7 步回答：

1. 明确需求：用户是谁，任务是什么，成功标准是什么，哪些动作有风险。
2. 定义边界：Agent 能做什么，必须人工确认什么，不能访问什么。
3. 设计主流程：输入、理解、规划、工具调用、观察、输出、停止条件。
4. 设计数据和工具：知识库、数据库、API、文件、浏览器、代码执行、权限。
5. 设计状态和记忆：session state、短期记忆、长期记忆、上下文压缩。
6. 设计安全和评测：guardrail、human-in-the-loop、eval、trace、失败归因。
7. 设计生产能力：延迟、成本、限流、降级、监控、灰度、回滚。

## 题 1：智能客服 Agent

### 需求

用户可以咨询政策、查询订单、申请退款、修改地址。系统要能处理多轮对话，复杂问题转人工，高风险动作需要确认。

### 参考架构

```text
User
  -> API Gateway
  -> Conversation Orchestrator
  -> Intent Router
      -> FAQ/RAG Agent
      -> Order Tool Agent
      -> Refund Workflow
      -> Human Support Queue
  -> Policy Guardrail
  -> Trace and Eval Store
```

### 关键设计点

- 知识类问题走 RAG，必须给引用。
- 订单查询用只读工具。
- 退款、改地址等写操作必须先 dry-run，再让用户确认。
- 缺少订单号、身份验证不足时不能继续执行敏感工具。
- session state 记录订单号、意图、已确认信息、审批状态和转人工原因。

### 常见追问

- 如何防止用户绕过退款政策？
- 如果知识库和订单系统冲突，以哪个为准？
- 如何评估客服 Agent 的效果？
- 如何处理用户辱骂、威胁或要求违法操作？

### 指标

- 一次解决率。
- 转人工率。
- 错误退款率。
- 平均响应时延。
- 单会话成本。
- 引用准确率。
- 用户满意度。

## 题 2：代码修复 Agent

### 需求

输入 GitHub issue、失败测试或用户描述，Agent 读取仓库、定位问题、修改代码、运行测试，并生成 PR 摘要。

### 参考架构

```text
Issue/Test Failure
  -> Task Parser
  -> Repo Indexer
  -> Planning Agent
  -> Code Search Tool
  -> Patch Tool
  -> Test Runner Sandbox
  -> Review Agent
  -> PR Summary
  -> Eval Harness
```

### 关键设计点

- 代码读取和修改必须在隔离 workspace 中进行。
- patch 前要先定位相关文件和测试。
- 每次修改后运行最小相关测试，再逐步扩大。
- 防止 Agent 修改无关文件或绕过测试。
- trace 记录搜索、文件读取、patch、测试结果和失败原因。

### 常见追问

- 如何避免 Agent 破坏用户已有改动？
- 如何处理测试 flaky？
- 如果没有测试怎么办？
- 如何评估代码 Agent 的能力？

### 指标

- issue resolve rate。
- patch apply success。
- test pass rate。
- irrelevant diff ratio。
- 平均迭代次数。
- 人工 review 修改量。

## 题 3：企业知识库 Agent

### 需求

员工查询内部制度、产品文档、会议纪要和项目资料。系统要支持权限隔离、引用溯源、拒答和文档更新。

### 参考架构

```text
Documents
  -> Ingestion Pipeline
  -> Parser and Chunker
  -> Metadata and ACL
  -> Hybrid Index
  -> Reranker
  -> Answer Generator
  -> Citation Verifier
  -> Feedback and Eval Loop
```

### 关键设计点

- 摄取时保留来源、版本、时间、权限和文档结构。
- 查询时先做身份和权限过滤，再检索。
- 混合检索用于兼顾语义和关键词。
- 没有足够证据时拒答，而不是编造。
- 需要引用校验，答案中的关键事实必须能回到原文。

### 常见追问

- 如何处理权限变更？
- 如何处理过期文档？
- 如何支持表格、PDF 和图片？
- 如何发现知识库缺口？

### 指标

- recall@k。
- answer correctness。
- citation precision。
- no-answer accuracy。
- 权限泄露数。
- 文档更新延迟。

## 题 4：数据分析 Agent

### 需求

业务人员用自然语言询问数据问题，Agent 自动理解表结构、生成 SQL、执行只读查询、生成图表并解释结果。

### 参考架构

```text
User Question
  -> Intent and Metric Parser
  -> Schema Retriever
  -> SQL Generator
  -> SQL Guardrail
  -> Read-only Query Executor
  -> Result Verifier
  -> Chart and Narrative Generator
```

### 关键设计点

- 只允许读权限，禁止 DDL、DML 和高成本查询。
- schema retrieval 只给相关表和字段，避免上下文过大。
- SQL 生成后先 explain 或 dry-run。
- 对结果做 sanity check，例如空值、异常大数、时间范围。
- 对业务指标要维护 metric dictionary，避免口径不一致。

### 常见追问

- 如何防止 SQL 注入或越权查询？
- 如何处理用户问题含糊？
- 如果 SQL 正确但业务口径错怎么办？
- 如何评测 Text-to-SQL Agent？

### 指标

- SQL execution accuracy。
- business metric accuracy。
- unsafe query block rate。
- query latency。
- chart correctness。
- clarification rate。

## 题 5：多 Agent 研究写作系统

### 需求

输入一个研究主题，系统自动搜索资料、筛选来源、提取观点、生成大纲、写作、事实核查并输出带引用的报告。

### 参考架构

```text
User Topic
  -> Supervisor
      -> Research Agent
      -> Source Ranking Agent
      -> Outline Agent
      -> Writer Agent
      -> Fact Checker Agent
      -> Editor Agent
  -> Citation Auditor
  -> Final Report
```

### 关键设计点

- supervisor 负责拆任务、分配角色和合并结果。
- 每个子 Agent 输出结构化 artifact，而不是自由聊天。
- fact checker 必须基于来源做逐条核验。
- 冲突观点要保留，不应强行合并成单一结论。
- 成本控制上，搜索和初筛可用较便宜模型，最终写作和核查用更强模型。

### 常见追问

- 为什么不用单 Agent？
- 多 Agent 之间意见冲突怎么办？
- 如何防止引用看起来存在但实际不支持结论？
- 如何评测报告质量？

### 指标

- source precision。
- citation support rate。
- fact error rate。
- coverage。
- redundancy。
- cost per report。

## 题 6：Agent Eval Harness

### 需求

为任意 Agent 提供测试任务、运行环境、轨迹记录、评分器和回归报告，让团队知道 Agent 改动是否变好。

### 参考架构

```text
Task Dataset
  -> Runner
  -> Environment Adapter
  -> Agent Under Test
  -> Trace Collector
  -> Evaluators
      -> Final Answer Eval
      -> Tool Call Eval
      -> Trajectory Eval
      -> Safety Eval
      -> Cost/Latency Eval
  -> Report and CI Gate
```

### 关键设计点

- 每条任务要有输入、初始环境、期望行为、禁止行为、评分 rubric。
- 支持 deterministic evaluator 和 LLM-as-judge。
- 轨迹中要记录工具调用顺序、参数摘要、观察结果和错误。
- CI 中设置阈值，例如成功率下降超过 3% 阻断。
- 支持 replay，便于定位某次失败。

### 常见追问

- 如何处理多条正确路径？
- 如何避免 judge 偏差？
- 如何把线上失败加入离线测试集？
- 如何评估工具调用轨迹？

### 指标

- task success rate。
- trajectory match score。
- safety violation rate。
- cost per task。
- P95 latency。
- regression count。

## 题 7：浏览器或视觉 Computer-Use Agent

### 需求

Agent 根据用户目标操作网页或桌面应用，例如填写表单、查询信息、下载文件、提交申请。

### 参考架构

```text
User Goal
  -> Task Planner
  -> Page Observer
      -> DOM Parser
      -> Screenshot/Vision Parser
  -> Action Selector
  -> Browser Executor
  -> State Verifier
  -> Safety Approval
  -> Trace Replay
```

### 关键设计点

- 能用 DOM 和 API 时优先用结构化信息，视觉用于补充布局、图像和不可访问元素。
- 每次动作后要观察状态变化，不能盲目连点。
- 外部提交、购买、发送消息等动作前需要人工确认。
- 网页内容可能包含 prompt injection，需要把页面内容视为不可信数据。
- 坐标点击要有 fallback，例如元素定位失败时重新观察或请求用户介入。

### 常见追问

- 视觉 grounding 失败怎么办？
- 如何评测浏览器 Agent？
- 如何防止网页诱导 Agent 泄露信息？
- DOM-only 和 screenshot-only 各有什么问题？

### 指标

- task completion rate。
- action accuracy。
- recovery rate。
- unsafe action block rate。
- average steps。
- replayability。

