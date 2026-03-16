# 错误记录 (Errors)

记录投资团队和系统运行中的错误、失败、异常。

---

## [ERR-20260316-001] cron 自动备份未执行

**Logged**: 2026-03-16T19:00:00+08:00
**Priority**: high
**Status**: resolved
**Area**: 系统配置

### Summary
每天 17:00 的 Git 自动备份任务没有执行

### Error
```
crontab 配置了但 17:00 没有执行备份
Git 最后提交时间是 11:57（手动提交）
不是 17:00 的自动提交
```

### Context
- crontab 配置：`0 17 * * * cd /home/admin/.openclaw/workspace && git add . && git commit -m "自动备份 - 金银" && git push --quiet`
- cron 进程在运行（/usr/sbin/crond）
- 但配置缺少 PATH 环境变量

### Suggested Fix
在 crontab 中添加 PATH 环境变量

### Resolution
- **Resolved**: 2026-03-16T19:30:00+08:00
- **修复**: 添加 PATH 到 crontab
- **补备份**: 手动执行了 git push

### Metadata
- Reproducible: yes
- 相关团队：金银（管家）
- 相关任务：Git 自动备份

---

## 条目格式模板

```markdown
## [ERR-YYYYMMDD-XXX] 错误主题

**Logged**: ISO-8601 时间戳
**Priority**: high | medium | low
**Status**: pending | resolved | wont_fix
**Area**: 投资分析 | 风控 | 学习系统 | 系统配置 | 数据抓取

### Summary
简要描述什么出错了

### Error
```
实际错误信息或输出
```

### Context
- 尝试的操作
- 使用的输入/参数
- 相关环境信息

### Suggested Fix
如果可以识别，什么可能解决这个问题

### Resolution
- **Resolved**: 解决时间
- **Commit/PR**: 相关提交
- **Notes**: 解决说明

### Metadata
- Reproducible: yes | no | unknown
- 相关团队：团队名称
- 相关任务：任务描述
```

---
