# 功能请求 (Feature Requests)

记录用户希望投资团队增加的新功能、改进建议。

---

## [FEAT-20260316-001] 投资团队自我进化系统

**Logged**: 2026-03-16T20:45:00+08:00
**Priority**: high
**Status**: in_progress
**Area**: 投资系统

### Requested Capability
用户希望投资团队跟她一起学习成长：
- Charlie 犯的错误要记录
- 监控小弟的误判要追踪
- 估值分析的错误要改进
- 用户的纠正反馈要升级给整个团队

### User Context
用户 46 岁，文科背景，长线筹码集中度策略
希望 AI 团队主动学习，不是被动等待指令

### Complexity Estimate
medium

### Suggested Implementation
1. 为每个投资团队成员创建学习记录
2. 错误/纠正 → .learnings/
3. 重要经验 → 升级到各团队 SKILL.md
4. 每周 Elon 周报包含团队成长总结

### Metadata
- Frequency: recurring
- 相关功能：learning-secretary, self-improvement
- 相关团队：investment-manager-charlie, investment-monitor, valuation-analyst, risk-control-monitor

---

## [FEAT-20260316-002] 估值分析需要敏感性分析

**Logged**: 2026-03-16T22:03:00+08:00
**Priority**: high
**Status**: pending
**Area**: 投资分析

### Requested Capability
估值分析输出需要包含敏感性分析表格：
- 增长率变化 ±2% 对估值的影响
- 折现率变化 ±1% 对估值的影响
- 用表格展示 9 种情景组合

### User Context
用户是文科背景，需要直观理解估值的不确定性
单一数字容易误导，需要看到区间和情景

### Complexity Estimate
medium

### Suggested Implementation
1. 修改 valuation-analyst SKILL.md
2. 添加敏感性分析计算逻辑
3. 输出格式：Markdown 表格
4. 默认展示 3x3 情景矩阵

### Metadata
- Frequency: recurring
- 相关功能：valuation-analyst
- 相关团队：valuation-analyst, investment-manager-charlie

---

## 条目格式模板

```markdown
## [FEAT-YYYYMMDD-XXX] 功能名称

**Logged**: ISO-8601 时间戳
**Priority**: low | medium | high | critical
**Status**: pending | in_progress | completed | wont_fix
**Area**: 投资分析 | 风控 | 学习系统 | 数据展示

### Requested Capability
用户想要什么功能

### User Context
为什么需要这个功能，解决什么问题

### Complexity Estimate
simple | medium | complex

### Suggested Implementation
如何实现，可能扩展哪些现有功能

### Metadata
- Frequency: first_time | recurring
- 相关功能：现有功能名称
- 相关团队：团队名称
```

---
