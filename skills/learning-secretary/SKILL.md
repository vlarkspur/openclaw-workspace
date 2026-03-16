---
name: learning-secretary
description: 学习秘书。每周日 20:00 自动汇总本周学习卡片，生成 Word 文档到 memory/learning-summaries/。支持手动触发汇总。
---

# 学习秘书 (Learning Secretary)

## 触发时机

**每周日 20:00 自动执行**（通过 HEARTBEAT.md 配置）

也支持手动触发：用户说"汇总本周学习"、"生成本周总结"等。

## 核心功能

### 第一步：扫描本周学习卡片

位置：`memory/learning-cards/`

筛选条件：
- 文件名格式：`YYYY-MM-DD-*.md`
- 日期范围：本周一到本周日
- 排除：TEMPLATE.md

### 第二步：提取卡片内容

从每张卡片中提取：
- 主题（文件名中的主题部分）
- 遇到的问题
- 解决方案
- 关键命令/代码
- 踩过的坑
- 耗时

### 第三步：生成汇总文档

输出位置：`memory/learning-summaries/YYYY-Www-summary.md`

例如：`memory/learning-summaries/2026-W12-summary.md`

文档结构：
1. 本周学习概览
2. 学习主题详情（每个主题一小节）
3. 踩坑汇总
4. 关键命令速查
5. 下周学习计划（可选）

### 第四步：转换为 Word（可选）

如果用户需要 Word 格式，调用 Python 脚本转换：
```bash
python3 scripts/convert-to-docx.py memory/learning-summaries/2026-W12-summary.md
```

输出：`memory/learning-summaries/2026-W12-summary.docx`

## 文档模板

见 `references/summary-template.md`

## 与导师 Agent 配合

- 导师负责日常创建学习卡片
- 秘书负责定期汇总成文档
- 两者共享 `memory/learning-cards/` 文件夹

## 手动触发

用户说以下任意一句时触发：
- "汇总本周学习"
- "生成本周总结"
- "把这周学的整理一下"
- "生成学习周报"

## 参考资源

- `references/summary-template.md`：汇总文档模板
- `scripts/convert-to-docx.py`：Markdown 转 Word 脚本
