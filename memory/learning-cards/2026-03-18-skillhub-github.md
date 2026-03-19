# 学习卡片：Skillhub 安装与 GitHub 技能

**日期：** 2026-03-18
**来源渠道：** 飞书 WebUI
**学习时间：** 约 30 分钟

---

## 📌 问题

用户要求安装 Skillhub 商店（只安装 CLI），然后安装 GitHub 技能。

---

## ✅ 解决方案

### 第 1 步：安装 Skillhub CLI

```bash
curl -fsSL https://skillhub-1388575217.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash -s -- --cli-only
```

**安装位置：** `/home/admin/.local/bin/skillhub`

---

### 第 2 步：修复 Python 3.6 兼容性问题

**问题：** Python 3.6 不支持 `argparse.add_subparsers(required=True)`

**错误信息：**
```
TypeError: __init__() got an unexpected keyword argument 'required'
```

**解决：** 编辑 `/home/admin/.skillhub/skills_store_cli.py`，第 1433 行

```python
# 修改前
subparsers = parser.add_subparsers(dest="command", required=True)

# 修改后
subparsers = parser.add_subparsers(dest="command")
```

---

### 第 3 步：搜索并安装 GitHub 技能

```bash
# 搜索
skillhub search github

# 安装
skillhub install github
```

**安装位置：** `/home/admin/.openclaw/workspace/skills/github/`

---

## 🔧 常用命令

| 命令 | 功能 |
|------|------|
| `skillhub search [关键词]` | 搜索技能 |
| `skillhub install [技能名]` | 安装技能 |
| `skillhub list` | 列出已安装技能 |
| `skillhub upgrade` | 升级已安装技能 |
| `skillhub self-upgrade` | 升级 CLI 自身 |

---

## 📦 GitHub 技能功能

使用 `gh` CLI 与 GitHub 交互：

```bash
# 检查 PR 的 CI 状态
gh pr checks 55 --repo owner/repo

# 查看工作流运行
gh run list --repo owner/repo --limit 10

# 查看失败日志
gh run view <run-id> --repo owner/repo --log-failed

# API 高级查询
gh api repos/owner/repo/pulls/55 --jq '.title, .state, .user.login'

# JSON 输出
gh issue list --repo owner/repo --json number,title --jq '.[] | "\(.number): \(.title)"'
```

---

## 💡 踩坑记录

1. **Python 版本兼容性**
   - 系统 Python 3.6.8 太老
   - `required=True` 参数在 Python 3.7+ 才支持
   - 解决：去掉该参数

2. **技能安装位置**
   - Skillhub CLI 安装在 `~/.local/bin/`
   - 技能安装在当前 workspace 的 `skills/` 目录

---

## 🔗 相关资源

- Skillhub 安装文档：https://skillhub-1388575217.cos.ap-guangzhou.myqcloud.com/install/skillhub.md
- GitHub CLI 文档：https://cli.github.com/

---

_创建时间：2026-03-18 17:33_
