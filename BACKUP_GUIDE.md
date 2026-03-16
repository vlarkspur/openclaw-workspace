# 💃 金银 Studio 备份指南

**最后更新：** 2026-03-15  
**备份频率：** 每天 17:00

---

## 📁 需要备份的核心文件

### 1. 技能文件夹（最重要）

```
/home/admin/.openclaw/workspace/skills/
```

**包含：** 21 个 AI 小弟的技能文件（SKILL.md）

### 2. 数据文件夹

```
/home/admin/.openclaw/workspace/memory/
```

**包含：** 学习卡片、财务数据、健康数据、错题本

### 3. 配置文件

```
/home/admin/.openclaw/workspace/
├── SOUL.md              ← 金银人格
├── USER.md              ← 小溪档案
├── MEMORY.md            ← 长期记忆
├── HEARTBEAT.md         ← 定时任务
├── TEAM_CONFIG.md       ← 团队配置
├── BACKUP_GUIDE.md      ← 本文件
└── team_managers/       ← 经理档案
```

---

## 🔄 备份方法

### 方法 1：手动复制（最简单）

**每天 17:00 执行：**

```bash
# 1. 打开终端
# 2. 运行以下命令：
cp -r /home/admin/.openclaw/workspace /你的备份位置/workspace-backup-$(date +%Y%m%d)
```

**示例：**
```bash
cp -r /home/admin/.openclaw/workspace /home/admin/backup/workspace-backup-20260315
```

### 方法 2：Git 版本控制（推荐）

**首次设置：**

```bash
cd /home/admin/.openclaw/workspace
git init
git add .
git commit -m "Initial commit - 金银 Studio"
# 然后关联远程仓库（GitHub/Gitee）
git remote add origin <你的仓库地址>
git push -u origin main
```

**每天 17:00 执行：**

```bash
cd /home/admin/.openclaw/workspace
git add .
git commit -m "每日备份 $(date +%Y%m%d)"
git push
```

### 方法 3：云同步（最省心）

**使用阿里云盘/坚果云：**

1. 安装云同步客户端
2. 设置同步文件夹为 `/home/admin/.openclaw/workspace`
3. 开启自动同步

---

## ⏰ 17:00 备份提醒

**提醒方式：** 飞书消息

**提醒内容：**
```
🕔 金银 Studio 备份时间到！

请执行以下操作：

1. 打开终端
2. 运行：
   cd /home/admin/.openclaw/workspace
   git add . && git commit -m "备份" && git push

或手动复制：
   cp -r /home/admin/.openclaw/workspace /你的备份位置/

备份指南：BACKUP_GUIDE.md

---
💃 金银 Studio 后勤保障部
```

---

## 📊 备份检查清单

**每天 17:00 检查：**

- [ ] skills/ 文件夹已备份（21 个技能）
- [ ] memory/ 文件夹已备份（学习卡片、财务、健康）
- [ ] 配置文件已备份（SOUL.md、USER.md 等）
- [ ] 备份位置有足够空间
- [ ] 备份日期正确

---

## 🚨 恢复方法

**如果系统重置或文件丢失：**

```bash
# 从备份恢复
cp -r /你的备份位置/workspace-backup-YYYYMMDD /home/admin/.openclaw/workspace
```

**然后重启 OpenClaw：**
```bash
openclaw restart
```

---

## 💡 备份建议

| 备份方式 | 频率 | 优点 | 缺点 |
|---------|------|------|------|
| **Git** | 每天 | 有版本历史、可追溯 | 需要学习 Git |
| **云同步** | 实时 | 自动、省心 | 需要云空间 |
| **手动复制** | 每天 | 简单直接 | 容易忘记 |

**推荐：Git + 云同步 双重备份**

---

_备份是你的 AI 团队的"人寿保险"。_  
_每天 17:00，别忘了。_

💃 金银 Studio 后勤保障部 - 马未都
