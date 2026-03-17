# 学习卡片：Charlie 投资团队搭建

**日期：** 2026-03-15  
**主题：** 搭建 Charlie 投资团队（1 个经理 + 7 个小弟）  
**耗时：** 约 60 分钟

---

## 遇到的问题

需要有一个专业的投资团队来管理资产增值，基于 Charlie 的价值投资理念，监控持仓股票、风控、认知偏差、估值、基本面、宏观经济和舆情。

---

## 解决方案

### 第一步：创建 Charlie 经理技能

位置：`skills/investment-manager-charlie/`

**核心职责：**
- 审核数据质量（来源、可信度、交叉验证）
- 提供反面论证（"反过来想，什么会导致失败"）
- 量化不确定性（概率区间、置信度）
- 认知偏差监控（25 种人类误判）

### 第二步：创建 7 个下属角色

**1. 投资监控小弟（investment-monitor）**
- 抓取 8 只持仓股票数据
- 标注来源和可信度
- 交叉验证（2 个以上独立来源）

**2. 风控监控小弟（risk-control-monitor）**
- 监控止损线（单只 -15%/-20%，整体 -10%/-15%）
- 监控仓位风险（单只<20%，行业<40%）
- 识别情绪化交易（死扛、报复性交易）

**3. 行为心理学小弟（behavioral-psychology）**
- 监控 25 种认知偏差
- 提供决策检查清单
- 交易后复盘

**4. 估值分析小弟（valuation-analyst）**
- 计算内在价值（PE 法、DCF 法、PEG 法）
- 计算安全边际（>30% 才买入）
- 判断贵/便宜（历史分位）

**5. 公司基本面分析小弟（fundamentals-analyst）**
- 财报分析（利润表、资产负债表、现金流量表）
- 护城河评估（5 种类型、星级评分）
- 管理层质量分析（诚信、能力、股东利益）

**6. 宏观经济小弟（macro-economy）**
- 跟踪经济周期（美林时钟）
- 分析政策影响（货币、财政、产业）
- 行业景气度分析

**7. 新闻舆情小弟（news-sentiment）**
- 监控重大新闻（红色/黄色/绿色分级）
- 过滤噪音 vs 信号
- 舆情情感分析

---

## 关键命令/代码

```bash
# Charlie 团队技能位置
skills/investment-manager-charlie/
skills/investment-monitor/
skills/risk-control-monitor/
skills/behavioral-psychology/
skills/valuation-analyst/
skills/fundamentals-analyst/
skills/macro-economy/
skills/news-sentiment/
```

---

## 踩过的坑

- 一开始想让 Charlie 管所有事，但他应该专注数据质量和反面论证
- 风控规则需要明确阈值，不能模糊
- 认知偏差监控需要具体检查清单，不能只说"注意偏差"

---

## 下次遇到同样问题，第一步做什么

先定义经理的核心职责和思维模型，再设计下属角色分工，最后定义协作流程。

---

## 关联知识点

- 与自我提升部门协作（Elon 团队）
- 与作品团队协作（Jobs 团队）
- 使用 TEAM_CONFIG.md 作为配置蓝图
- 参考 Charlie_Munger_profile.md 人物档案

---

## 复盘标记

- [ ] 已加入周复盘
- [ ] 已加入月复盘
