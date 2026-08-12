# 40 天学习计划

这份计划按“概念理解 -> 工程机制 -> 系统设计 -> 模拟面试”的节奏安排。每天建议投入 1.5 到 3 小时：

- 40 分钟阅读和整理笔记。
- 40 分钟口述 3 到 5 道题。
- 40 到 80 分钟做小实验、画架构图或补项目材料。

## 第 1 阶段：Agent 基础和 LLM 基础

| 天数 | 主题 | 当天产出 |
| --- | --- | --- |
| Day 1 | Agent 定义与边界 | 写一页笔记：Agent、LLM app、chatbot、workflow 的区别 |
| Day 2 | Agent 核心组成 | 画出目标、状态、模型、工具、观察、终止条件的闭环图 |
| Day 3 | Agent 适用场景 | 整理 10 个适合 Agent 和 10 个不适合 Agent 的场景 |
| Day 4 | Token 与上下文窗口 | 解释 token、上下文窗口、上下文溢出、输出截断 |
| Day 5 | 采样参数 | 对比 temperature、top_p、max tokens、seed 对行为的影响 |
| Day 6 | Prompt 层级和 Few-shot | 写 3 个 system/developer/user 层级冲突案例 |
| Day 7 | 结构化输出和缓存 | 设计一个 JSON schema 输出，并解释 prompt cache 的收益和限制 |

## 第 2 阶段：规划、执行和工具

| 天数 | 主题 | 当天产出 |
| --- | --- | --- |
| Day 8 | Agent Loop | 写出 observe-think-act-observe 的伪代码 |
| Day 9 | ReAct | 用 ReAct 解释一个“查资料后写摘要”的任务轨迹 |
| Day 10 | Plan-and-Execute | 比较一次性规划和边执行边修正的优缺点 |
| Day 11 | Reflection | 说明 reflection 什么时候有用，什么时候会浪费成本 |
| Day 12 | 状态机和终止条件 | 设计最大步数、无进展检测、目标完成检测 |
| Day 13 | Function Calling | 设计 3 个工具 schema，并写出错误参数处理方式 |
| Day 14 | 工具权限和读写隔离 | 给一个退款工具设计 dry-run、approval、audit log |

## 第 3 阶段：MCP、Skills、RAG 和记忆

| 天数 | 主题 | 当天产出 |
| --- | --- | --- |
| Day 15 | MCP 基础 | 画出 Host、Client、Server、Tools、Resources、Prompts 的关系 |
| Day 16 | Skills | 写一个 Skill 说明：触发条件、能力边界、输入输出、风险 |
| Day 17 | Embedding 和向量检索 | 解释 embedding、相似度、召回率和语义漂移 |
| Day 18 | Chunk 策略 | 对比固定长度、语义切分、标题层级切分和表格切分 |
| Day 19 | 混合检索和 Rerank | 设计 BM25 + vector + reranker 的检索链路 |
| Day 20 | Query Rewrite | 设计多轮追问、歧义查询和过滤条件的 query rewrite |
| Day 21 | RAG 评测 | 写 20 条 RAG eval case，覆盖找不到、权限不足、过期资料 |
| Day 22 | 短期记忆和 Session State | 设计一个客服 Agent 的 session state 字段 |
| Day 23 | 长期记忆 | 说明用户偏好、事实记忆、任务记忆如何分开存储 |
| Day 24 | 上下文压缩和污染 | 写出 5 种上下文污染来源和对应防护 |

## 第 4 阶段：多 Agent、Harness、评测和安全

| 天数 | 主题 | 当天产出 |
| --- | --- | --- |
| Day 25 | Multi-Agent 编排 | 对比 supervisor、router、peer collaboration、blackboard |
| Day 26 | Agent 通信和共享状态 | 设计共享状态 schema 和冲突解决策略 |
| Day 27 | Harness | 解释 harness 和 agent framework、workflow runtime 的区别 |
| Day 28 | Eval 分层 | 设计 final response、single-step、trajectory、system eval |
| Day 29 | Trace 和失败归因 | 画出 trace span：LLM、tool、retrieval、guardrail、handoff |
| Day 30 | Prompt Injection | 写出 5 个攻击样例和 5 个防护策略 |
| Day 31 | Human-in-the-Loop | 给高风险动作设计审批、回滚和审计 |
| Day 32 | 生产可靠性 | 设计重试、超时、限流、降级、灰度发布 |

## 第 5 阶段：生产架构、系统设计和面试冲刺

| 天数 | 主题 | 当天产出 |
| --- | --- | --- |
| Day 33 | 性能和成本 | 估算一次 Agent 任务的 token、工具调用、缓存和并发成本 |
| Day 34 | 模型路由 | 设计小模型分类、大模型规划、专用模型检索判断的路由 |
| Day 35 | 智能客服 Agent 系统设计 | 完整讲一遍需求、架构、工具、评测、安全、成本 |
| Day 36 | 代码 Agent 系统设计 | 完整讲一遍 repo 理解、补丁生成、测试、sandbox、PR |
| Day 37 | 数据分析 Agent 系统设计 | 完整讲一遍 Text-to-SQL、权限、校验、图表、解释 |
| Day 38 | 知识库 Agent 系统设计 | 完整讲一遍文档摄取、检索、引用、权限、更新 |
| Day 39 | 项目和简历表达 | 写好 GitHub README、架构图说明、3 条简历 bullet |
| Day 40 | 模拟面试 | 做一轮 60 分钟模拟面试，复盘回答卡点和项目短板 |

## 每日复盘模板

```markdown
## Day X

### 今天掌握的概念

- 

### 今天能口述的问题

- 

### 还不稳的问题

- 

### 一个可讲的工程例子

- 场景：
- 设计：
- 风险：
- 指标：

### 明天要补

- 
```

## 每周检查点

第 1 周结束：

- 能在 3 分钟内解释 Agent 和 workflow 的区别。
- 能说明模型参数和 prompt 层级如何影响输出稳定性。

第 2 周结束：

- 能画出 Agent loop。
- 能为工具设计 schema、权限和错误处理。

第 3 周结束：

- 能讲清 RAG、MCP、Skills 和记忆的边界。
- 能设计一套 RAG 评测集。

第 4 周结束：

- 能讲清 harness、multi-agent、eval、trace 和安全。
- 能从失败日志中做归因。

第 5 到 6 周结束：

- 能完整回答 2 到 3 个 Agent 系统设计题。
- 能把自己的项目讲成工程成果，而不是 demo。

