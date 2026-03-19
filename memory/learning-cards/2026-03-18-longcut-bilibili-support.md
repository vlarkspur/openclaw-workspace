# LongCut 项目 - B 站 URL 解析支持

**日期：** 2026-03-18
**来源渠道：** 飞书
**耗时：** 约 7 小时 (8:28 - 15:38)

---

## 🎯 学习目标

完成 LongCut 项目第一步：支持 B 站视频 URL 解析

---

## 📝 遇到的问题

### 问题 1：服务器内存不足
- **现象：** Next.js 开发模式频繁崩溃
- **原因：** 服务器仅 1.8GB 内存，Node.js 默认内存限制过高
- **解决方案：**
  ```bash
  NODE_OPTIONS="--max-old-space-size=256" npx next dev
  ```

### 问题 2：阿里云公网访问 502
- **现象：** 安全组规则已配置，但公网 IP 无法访问服务
- **原因：** 阿里云 NAT 架构，服务器自己不能用公网 IP 访问自己
- **解决方案：** 使用 localhost 或 SSH 隧道访问

---

## ✅ 解决方案

### 1. 修改 `lib/utils.ts`
- 新增 B 站 URL 解析逻辑
- 支持 `bilibili.com/video/BVxxx` 格式
- 支持 `b23.tv/BVxxx` 短链接

### 2. 修改 `components/url-input.tsx`
- 输入框提示改为中文
- 提示文案："粘贴 B 站 或 YouTube 视频链接..."

### 3. 服务启动脚本
```bash
cd /home/admin/.openclaw/workspace/longcut
NODE_OPTIONS="--max-old-space-size=256" nohup npx next dev -H 0.0.0.0 -p 3000 > /tmp/next.log 2>&1 &
```

---

## 🔧 关键命令

```bash
# 查看 Next.js 日志
tail -f /tmp/next.log

# 本地测试服务
curl http://localhost:3000

# SSH 隧道（从本地访问服务器服务）
ssh -L 3000:localhost:3000 admin@47.253.202.134
```

---

## ⚠️ 踩过的坑

| 坑 | 避免方法 |
|---|---------|
| Next.js 开发模式内存溢出 | 启动时限制 NODE_OPTIONS 为 256MB |
| 阿里云公网 IP 自访问 502 | 用 localhost 测试，或用 SSH 隧道 |
| 安全组规则配置后仍无法访问 | 检查是否是 NAT 架构，服务器不能用公网 IP 访问自己 |

---

## 📊 服务器信息

- **公网 IP：** 47.253.202.134
- **实例 ID：** i-0xic0cvww4vpu7kgsq5z
- **内存：** 1.8GB
- **工作目录：** `/home/admin/.openclaw/workspace/longcut`

---

## 📅 下一步计划

**第二步：B 站播放器嵌入**
- 修改 `components/youtube-player.tsx` 为通用播放器
- 支持 B 站 iframe 嵌入

---

_创建时间：2026-03-18 17:30_
