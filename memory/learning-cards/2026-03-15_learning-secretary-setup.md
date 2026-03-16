# 学习卡片：学习秘书搭建

**日期：** 2026-03-15  
**主题：** 搭建学习秘书 Agent（每周汇总）  
**耗时：** 约 15 分钟

---

## 遇到的问题

学习系统已经有导师和监工，但缺少定期汇总机制。碎片化的学习卡片需要有人整理成完整的周报文档。

---

## 解决方案

### 第一步：创建秘书技能

位置：`skills/learning-secretary/`

包含文件：
- `SKILL.md` - 秘书的核心逻辑
- `references/summary-template.md` - 汇总文档模板
- `scripts/convert-to-docx.py` - Markdown 转 Word 脚本

### 第二步：创建汇总文件夹

```bash
mkdir -p memory/learning-summaries/
```

### 第三步：配置定时任务

在 `HEARTBEAT.md` 中添加：
- 每周日 20:00 触发
- 扫描本周学习卡片
- 生成汇总文档（Markdown + Word）
- 飞书通知用户

### 第四步：文档结构

汇总文档包含：
1. 本周学习概览（主题数、总耗时、卡片数）
2. 学习主题详情（每个主题的问题→解决方案→关键命令）
3. 踩坑汇总
4. 关键命令速查
5. 下周学习计划（可选）

---

## 关键命令/代码

```bash
# 汇总文档存放位置
memory/learning-summaries/YYYY-Www-summary.md
memory/learning-summaries/YYYY-Www-summary.docx

# 手动触发汇总（如果需要）
python3 skills/learning-secretary/scripts/convert-to-docx.py input.md output.docx
```

---

## 踩过的坑

- 一开始想用复杂的 Word 格式，但 python-docx 处理 Markdown 表格比较麻烦
- 解决方案：先输出 Markdown，再用脚本简单转换，表格可以手动调整

---

## 下次遇到同样问题，第一步做什么

先确定汇总频率（周/月）和输出格式（Markdown/Word），再创建技能和定时任务。

---

## 关联知识点

- 与导师 Agent 共享 `memory/learning-cards/` 文件夹
- 与监工 Agent 共享 `HEARTBEAT.md` 配置
- 使用 python-docx 库生成 Word 文档

---

## 复盘标记

- [ ] 已加入周复盘
- [ ] 已加入月复盘
