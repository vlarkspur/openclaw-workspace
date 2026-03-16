# 用 GitHub 备份阿里云服务器上的 OpenClaw 文件

## 日期
2026-03-16

## 我今天想解决什么
- 备份阿里云服务器上 OpenClaw workspace 的文件
- 不想手动拷贝，想要自动化

## 我学会了什么

### 1. Git 是啥（大白话理解）
- **普通备份**：像 U 盘拷贝，不知道改了啥
- **Git 备份**：带时间轴的超级备份，每次都有备注

### 2. SSH 密钥配置（连到 GitHub）

**生成密钥：**
```bash
ssh-keygen -t ed25519 -C "邮箱"
```
→ 全程回车就行

**查看公钥：**
```bash
cat ~/.ssh/id_ed25519.pub
```
→ 复制整行输出

**添加到 GitHub：**
1. 打开 https://github.com/settings/keys
2. 点 "New SSH key"
3. 粘贴公钥

**测试连接：**
```bash
ssh -T git@github.com
```
→ 看到 `Hi vlarkspur!` 就成功了

### 3. Git 仓库配置

**关联远程仓库：**
```bash
cd /home/admin/.openclaw/workspace
git remote add origin git@github.com:vlarkspur/openclaw-workspace.git
```

**首次推送：**
```bash
git config --global user.name "vlarkspur"
git config --global user.email "6355134@qq.com"
git add .
git commit -m "首次备份"
git push -u origin master
```

### 4. 自动化备份（cron 定时任务）

**添加每天自动备份：**
```bash
crontab -e
# 添加这一行：
0 17 * * * cd /home/admin/.openclaw/workspace && git add . && git commit -m "自动备份" && git push --quiet
```

**效果：** 每天下午 5 点自动备份，不用我管

## 我今天踩的坑

| 坑 | 原因 | 解决办法 |
|----|------|----------|
| 在 Windows 上执行 Linux 命令 | workspace 在阿里云服务器，不在我本地 | 回到飞书聊天或 SSH 连服务器执行 |
| Permission denied | SSH 密钥没添加到 GitHub | 重新生成密钥并添加 |
| Git 不知道我是谁 | 没配置 user.name/email | `git config --global user.email "6355134@qq.com"` |
| 第一次 push 卡住 | GitHub 问信不信它的指纹 | 输入 `yes` 回车 |

## 关键命令（下次直接复制）

**手动备份：**
```bash
cd /home/admin/.openclaw/workspace && git add . && git commit -m "备份" && git push
```

**查看备份任务：**
```bash
crontab -l
```

**我的 GitHub 仓库：**
```
https://github.com/vlarkspur/openclaw-workspace
```

## 耗时
约 2 小时（09:34 - 11:50）

## 下一步
- 每天下午 5 点自动备份，我不用管了
- 每周日收学习周报

---
📝 小溪的学习卡片 - 金银自动生成
