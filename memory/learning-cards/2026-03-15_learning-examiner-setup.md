# 学习卡片：考官搭建

**日期：** 2026-03-15  
**主题：** 搭建学习考官 Agent（每周测试）  
**耗时：** 约 20 分钟

---

## 遇到的问题

用户记忆力差，学了容易忘。需要定期测试来：
1. 检验学习效果（吸收率）
2. 对抗遗忘（复习旧知识）
3. 找出薄弱点（错题分析）

---

## 解决方案

### 第一步：创建考官技能

位置：`skills/learning-examiner/`

包含文件：
- `SKILL.md` - 考官的核心逻辑
- `references/question-template.md` - 出题模板
- `references/report-template.md` - 吸收率报告模板

### 第二步：创建数据存储文件夹

```bash
mkdir -p memory/exam-wrong-answers/   # 错题本
mkdir -p memory/exam-reports/         # 吸收率报告
```

### 第三步：配置定时任务

在 `HEARTBEAT.md` 中添加：

**周五 17:30：**
- 秘书发送本周学习总结
- 考官出 20 道题（70% 本周 + 30% 遗忘点）
- 题型：10 选择 + 5 填空 + 5 实操

**周二 14:00：**
- 检查是否已答题
- 未答 → 发送超时提醒

**下周二 24:00：**
- 答题截止

### 第四步：答题流程

1. 用户收到题目（飞书）
2. 用户回复答案（如：1.A 2.B 3.C...）
3. 考官自动批改
4. 记录错题到 `memory/exam-wrong-answers/`
5. 生成吸收率报告到 `memory/exam-reports/`

---

## 关键命令/代码

```bash
# 错题本位置
memory/exam-wrong-answers/YYYY-Www-wrong.md

# 吸收率报告位置
memory/exam-reports/YYYY-Www-report.md
```

---

## 踩过的坑

- 一开始想每天出题，但用户负担太重
- 调整为每周 20 题，周末完成，节奏更合理
- 考题要基于实际学习卡片，不能超纲

---

## 下次遇到同样问题，第一步做什么

先确定测试频率和题量，再设计题型分布和出题逻辑。

---

## 关联知识点

- 与秘书 Agent 共享周五 17:30 的触发时间
- 与导师 Agent 共享 `memory/learning-cards/` 数据源
- 错题本用于后续复习和出题

---

## 复盘标记

- [ ] 已加入周复盘
- [ ] 已加入月复盘
