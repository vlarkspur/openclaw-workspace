# 学习卡片 2026-03-20

**日期：** 2026-03-20  
**主题：** 股票分析框架打磨 + Skills 可用性测试  
**耗时：** 约 4 小时（14:00-18:00）

---

## 遇到的问题

### 问题 1：股票分析框架需要验证

理想汽车 2025 年年报已出，需要用 Charlie 团队的框架分析持仓是否合理，并将这个框架应用到其他已出年报的股票（如地平线机器人）。

### 问题 2：已安装的 Skills 并非都能用

发现有些 skills 安装后无法使用，比如搜索功能搜不出来。需要逐一测试哪些 skills 能用、哪些不能用、不能用的原因是什么（需要 API Key？配置后仍不能用？）。

---

## 解决方案

### 1️⃣ 股票分析框架打磨（理想汽车 → 地平线机器人）

**步骤：**

1. **数据收集**
   - 收集理想汽车 2025 年财报数据（营收/利润/研发投入等）
   - 收集地平线机器人 2025 年财报数据

2. **数据验证（交叉比对）**
   - 用 6 个独立来源交叉验证数据准确性
   - 来源：新浪财经/同花顺/观察者网/华夏时报/汽车之家/网易汽车
   - 验证项目：营收/净利润/研发投入/现金储备等

3. **深挖数据背后原因**
   - 不只看表面数据（如"净利润 -86%"）
   - 深挖原因：all in AI 战略投入 113 亿（50% 投向 AI/自研芯片）
   - 区分"一次性损失"（MEGA 召回 17 亿）和"持续性恶化"
   - 区分"战略投入"（研发 113 亿）和"经营不善"

4. **应用框架到地平线机器人**
   - 用同样的方法分析地平线机器人
   - 7 个小弟分析 + Charlie 综合审核
   - 输出完整分析报告

**关键发现：**
- 理想汽车：净利润 11 亿（-85.8%），但研发投入 113 亿创历史新高
- 地平线机器人：营收 37.58 亿（+57.67%），但亏损 104.7 亿
- 两者都是"战略投入期"，不是"经营恶化"

---

### 2️⃣ Skills 可用性测试

**测试方法：**
1. 列出所有已安装的 skills
2. 逐一测试功能是否正常
3. 记录不能用的原因和解决方案

**测试结果：**

| Skill | 状态 | 原因 | 解决方案 |
|-------|------|------|---------|
| **multi-search-engine** | ✅ 可用 | 无需 API Key | 直接用 |
| **tavily-search** | ✅ 可用 | 需 API Key | 已配置 |
| **openai-whisper** | ⚠️ 部分可用 | 技能文件已安装，CLI 未安装 | `brew install openai-whisper` |
| **agent-browser** | ⚠️ 部分可用 | 技能文件已安装，CLI 未安装 | `npm install -g agent-browser` |
| **skill-vetter** | ✅ 可用 | 无需额外配置 | 直接用 |
| **其他搜索 skills** | ❌ 不可用 | 配置问题/依赖缺失 | 用 multi-search-engine 替代 |

**关键发现：**
- 技能文件≠工具本身（如 Whisper/Agent Browser 需要额外安装 CLI）
- 有些 skills 需要 API Key（如 Tavily）
- 有些 skills 无需配置（如 multi-search-engine）
- 优先使用无需配置的 skills

---

### 3️⃣ 共享记忆文件创建

**目的：** 解决飞书会话和 Web UI 会话记忆不互通的问题

**文件位置：** `memory/SHARED_AGENT_RULES.md`

**内容：**
- 消息落款格式要求
- 部门列表
- 任务类型列表

---

## 关键命令/代码

### 数据验证
```bash
# 交叉验证数据来源
grep -r "理想汽车 2025 年财报" 多个新闻来源

# 检查 API Key 配置
cat ~/.openclaw/.env | grep -i tavily
echo $TAVILY_API_KEY
```

### Skills 测试
```bash
# 检查 whisper CLI 是否安装
which whisper

# 检查 agent-browser CLI 是否安装
which agent-browser

# 测试搜索功能
python3 skills/openclaw-tavily-search/scripts/tavily_search.py \
  --query "关键词" \
  --max-results 10 \
  --format md
```

### 技能安全审查
```bash
# 搜索危险关键词
grep -r "curl\|wget\|eval\|exec\|API_KEY" /opt/openclaw/skills/*/SKILL.md

# 搜索敏感路径
grep -r "~/.ssh\|~/.aws\|/etc/" /opt/openclaw/skills/*/SKILL.md
```

---

## 踩过的坑

- [ ] **技能文件≠工具本身** —— 以为安装了 skill 就能用，实际需要额外安装 CLI
- [ ] **数据表面 vs 深层原因** —— 看到"净利润 -86%"就下结论，没深挖是战略投入
- [ ] **会话记忆不互通** —— 飞书会话的配置，Web UI 会话不知道（需要共享文件）
- [ ] **搜索工具选择** —— 先用 Google/Bing 触发 reCAPTCHA，改用百度成功
- [ ] **Tavily 脚本路径** —— 在 `skills/openclaw-tavily-search/scripts/` 不是 `scripts/`

---

## 下次遇到同样问题，第一步做什么

**股票分析：**
1. 收集财报数据（至少 3 个独立来源）
2. 交叉验证数据准确性
3. 深挖数据背后原因（区分一次性/持续性/战略投入）
4. 用 Charlie 框架分析（7 个小弟 + Charlie 综合）

**Skills 测试：**
1. 检查技能文件是否存在
2. 检查 CLI 是否安装（`which 命令`）
3. 检查 API Key 是否配置
4. 优先使用无需配置的 skills

---

## 关联知识点

- [x] 与 2026-03-19 的 Charlie 团队分析框架有关联
- [x] 与 2026-03-18 的 AI 工具使用卡片有关联
- [ ] 后续需要深入理解 agent-browser 的高级用法
- [ ] 需要安装 Whisper CLI 和 agent-browser CLI

---

## 复盘标记

- [x] 已加入周复盘（2026-W12）
- [ ] 已加入月复盘

---

## 📋 待办事项

| 任务 | 优先级 | 状态 | 备注 |
|------|--------|------|------|
| 完成地平线机器人完整分析 | P0 | 🔄 进行中 | 应用理想汽车框架 |
| 安装 Whisper CLI | P1 | ⏳ 待执行 | `brew install openai-whisper` |
| 安装 agent-browser CLI | P2 | ⏳ 待执行 | `npm install -g agent-browser` |
| 检查 4 个中等风险技能权限 | P2 | ⏳ 待执行 | bear-notes/gh-issues/notion/himalaya |
| 继续测试其他 skills 可用性 | P2 | 🔄 进行中 | 逐步解决 |

---

## 💡 核心收获

1. **数据分析要深挖** —— 不只看表面数字，要理解背后的战略意图
2. **交叉验证很重要** —— 至少 3 个独立来源验证数据准确性
3. **技能安装≠技能可用** —— 有些需要额外安装 CLI 或配置 API Key
4. **优先使用简单工具** —— 无需配置的 skills 优先使用（如 multi-search-engine）

---

**记录人：** 金银 Planet · 后勤保障部（嘟嘟）  
**记录时间：** 2026-03-20 18:00
