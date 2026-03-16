# Git 备份自动化配置

## 日期
2026-03-16

## 问题
- 每天手动备份太麻烦，容易忘记
- 学习记录应该 AI 团队自动完成，不是用户手动写

## 解决方案

### 1. Git 自动备份（cron 定时任务）

**添加 cron 任务：**
```bash
crontab -e
# 添加这一行：
0 17 * * * cd /home/admin/.openclaw/workspace && git add . && git commit -m "自动备份 - 金银" && git push --quiet
```

**效果：** 每天 17:00 自动备份到 GitHub

### 2. 学习卡片自动生成

**修改 HEARTBEAT.md：**
- 任务 1 从"检查用户写卡片"改为"AI 自动扫描对话生成卡片"
- 每天 17:30 执行

**修改 learning-secretary SKILL.md：**
- 增加每日自动记录功能
- 每周汇总功能保持不变

### 3. SSH 密钥配置（前置步骤）

```bash
# 生成 SSH 密钥
ssh-keygen -t ed25519 -C "邮箱"

# 查看公钥
cat ~/.ssh/id_ed25519.pub

# 添加到 GitHub: https://github.com/settings/keys

# 测试连接
ssh -T git@github.com

# 关联远程仓库
git remote add origin git@github.com:用户名/仓库.git

# 首次推送
git add . && git commit -m "首次备份" && git push -u origin master
```

## 关键命令

| 命令 | 用途 |
|------|------|
| `crontab -e` | 编辑定时任务 |
| `crontab -l` | 查看定时任务 |
| `ssh-keygen -t ed25519` | 生成 SSH 密钥 |
| `git remote add origin` | 关联远程仓库 |
| `git push -u origin master` | 首次推送 |
| `git add . && git commit -m "备份" && git push` | 日常备份 |

## 踩坑记录

1. **SSH 密钥不存在** → 需要先生成 `ssh-keygen`
2. **Git 不知道你是谁** → 配置 `git config user.name/email`
3. **GitHub 指纹确认** → 第一次 push 输入 `yes`
4. **Permission denied** → SSH 公钥没添加到 GitHub
5. **在错误的地方执行命令** → workspace 在远程服务器，不在本地 Windows

## 自动化状态

| 任务 | 频率 | 状态 |
|------|------|------|
| Git 备份 | 每天 17:00 | ✅ 全自动 |
| 学习卡片生成 | 每天 17:30 | ✅ 全自动 |
| 学习周报汇总 | 每周五 17:30 | ✅ 全自动 |
| Elon 周报 | 每周日 20:00 | ✅ 全自动 |

## 下次直接用

**查看 cron 任务：**
```bash
crontab -l
```

**手动触发备份（如果需要）：**
```bash
cd /home/admin/.openclaw/workspace && git add . && git commit -m "备份" && git push
```

**验证 GitHub 仓库：**
```
https://github.com/vlarkspur/openclaw-workspace
```

---
💃 金银 Studio - 学习秘书自动生成
