# 金银 Planet PPT 项目 - Handover 文档

**创建时间：** 2026-03-18 10:22  
**负责人：** 小溪  
**对接人：** 金银（Steve 队协调）  
**状态：** 🟡 进行中 - 等待用户修改

---

## 📋 项目概述

**目标：** 金银 Planet 团队介绍 PPT（HTML 幻灯片格式）

**风格：** Neon Cyber（赛博朋克）
- 深海军蓝背景
- 青色 + 品红霓虹强调
- 网格背景 + 浮动粒子动画
- Clash Display + Satoshi 字体

**页数：** 12 页

---

## ✅ 已完成

| 任务 | 状态 | 备注 |
|------|------|------|
| Frontend Slides 技能安装 | ✅ | 2026-03-18 09:09 安装 |
| 12 页内容框架 | ✅ | 按 3 月 17 日记录框架 |
| HTML 幻灯片生成 | ✅ | Neon Cyber 风格 |
| 文件交付 | ✅ | 飞书已发送 |

---

## 📁 文件位置（已整理）

| 文件 | 路径 | 大小 |
|------|------|------|
| 主文件（交付） | `output/jinyin-planet.html` | 33KB |
| 主文件（源码） | `source/html-source/jinyin-planet-neon-cyber.html` | 33KB |
| 封面设计（5 个方案） | `source/cover-designs/cover-*.png` | 1.5-2.5MB |
| 成品 PPT 封面 | `source/01-封面 - 最终版.pptx` | 4.3MB |
| 设计文档 | `docs/DESIGN_SUMMARY.md` | 设计说明 |
| Handover | `docs/HANDOVER.md` | 项目交接 |

**完整路径：**
```
/home/admin/.openclaw/workspace/projects/ppt-jinyin-planet/
├── source/
│   ├── cover-designs/
│   │   ├── cover-01-stellar.png
│   │   ├── cover-02-metallic.png
│   │   ├── cover-03-spotlight.png
│   │   ├── cover-wong-01-chongqing.png
│   │   └── cover-wong-02-inthemood.png
│   ├── html-source/
│   │   └── jinyin-planet-neon-cyber.html
│   ├── 01-封面 - 最终版.pptx
│   └── 01-cover-preview.png
├── output/
│   └── jinyin-planet.html          ← 交付文件（用这个）
└── docs/
    ├── DESIGN_SUMMARY.md
    └── HANDOVER.md
```

---

## ⏳ 待办事项（用户修改）

### P0 - 必须改

| 页码 | 内容 | 修改建议 | 优先级 |
|------|------|----------|--------|
| 全部 | 文字内容 | 检查措辞、语气是否符合要求 | 🔥 |
| 5 | 团队架构 | 确认 4 位经理描述准确 | 🔥 |
| 6-9 | 各部门介绍 | 补充/删减具体职能 | 🔥 |

### P1 - 建议改

| 页码 | 内容 | 修改建议 | 优先级 |
|------|------|----------|--------|
| 1 | 封面 | 加 Logo 或人物图片 | ⚡ |
| 2 | 起源故事 | 补充细节或图片 | ⚡ |
| 10 | 自动化系统 | 确认 cron 时间准确 | ⚡ |
| 全部 | 颜色主题 | 不喜欢霓虹色可换 | ⚡ |

### P2 - 可选改

| 页码 | 内容 | 修改建议 | 优先级 |
|------|------|----------|--------|
| 全部 | 背景效果 | 关掉粒子/网格/光晕 | 💡 |
| 全部 | 动画速度 | 调快或调慢 | 💡 |
| 全部 | 字体 | 换其他 Google Fonts | 💡 |
| +? | 加页 | 需要补充内容随时加 | 💡 |

---

## 🎨 可修改内容清单

### 简单修改（⭐）

- ✅ 文字内容 - 直接改 HTML 里的文字
- ✅ 颜色主题 - 改 `:root` 里的 CSS 变量
- ✅ 动画速度 - 改 `transition` 的秒数

### 中等修改（⭐⭐）

- ✅ 加图片 - 插入 `<img>` 标签
- ✅ 关效果 - 删除/注释背景 div
- ✅ 换字体 - 改 Fontshare/Google Fonts 链接

### 较难修改（⭐⭐⭐）

- ✅ 改布局 - 调整 grid 列数、间距
- ✅ 加动画 - 写新的 CSS keyframes
- ✅ 加页数 - 复制 slide 块改内容

---

## 📖 修改指南

### 快速上手

**1. 用 VS Code 打开 HTML 文件**
```bash
code /home/admin/.openclaw/workspace/projects/ppt-jinyin-planet/output/jinyin-planet.html
```

**2. 搜索要改的内容**
- `Ctrl+F` 搜索文字
- 找到后直接改

**3. 保存预览**
- `Ctrl+S` 保存
- 浏览器刷新看效果

---

### 常用修改示例

**改颜色：**
```html
<!-- 找到第 15 行左右的 :root -->
:root {
    --accent-cyan: #00ffcc;  /* 改成你喜欢的颜色 */
    --accent-magenta: #ff00aa;
}
```

**加图片：**
```html
<!-- 在任意 slide-content 里加 -->
<img src="图片路径.png" alt="描述" style="max-height: 50vh; margin: 2rem auto;">
```

**调动画速度：**
```html
<!-- 找到第 150 行左右的 .reveal -->
.reveal {
    transition: opacity 0.6s, transform 0.6s;  /* 改成 0.3s 更快 */
}
```

---

## 🔧 技术细节

### 使用的技能
- **Frontend Slides** (`~/.agents/skills/frontend-slides/`)
- 风格 preset：Neon Cyber

### 字体来源
- Clash Display (Fontshare)
- Satoshi (Fontshare)

### 导航支持
- 键盘：箭头键 / 空格 / PageUp/Down
- 鼠标：滚轮 / 点击导航点
- 触摸：上下滑动

### 响应式断点
- 700px 高度以下
- 600px 高度以下
- 500px 高度以下
- 600px 宽度以下

---

## 📅 时间线

| 日期 | 事件 | 状态 |
|------|------|------|
| 2026-03-15 | PPT 项目启动，生成封面图片 | ✅ |
| 2026-03-17 | 记录 Frontend Slides 技能 | ✅ |
| 2026-03-18 09:09 | 安装 Frontend Slides 技能 | ✅ |
| 2026-03-18 09:54 | 开始生成 HTML 幻灯片 | ✅ |
| 2026-03-18 10:06 | 完成 12 页 HTML 文件 | ✅ |
| 2026-03-18 10:13 | 飞书发送文件给用户 | ✅ |
| 2026-03-18 10:22 | 创建 Handover 文档 | ✅ |
| 2026-03-18 ~ 2026-03-2X | 用户修改期 | ⏳ |
| TBD | 最终验收 | ⏳ |

---

## 📞 对接说明

### 用户修改期间

**金银待命：**
- 用户随时可以问"这行怎么改"
- 用户说"帮我改 XXX"，金银执行
- 用户验收后，项目关闭

### 验收标准

- [ ] 12 页内容都检查过
- [ ] 文字、颜色、图片满意
- [ ] 动画效果满意
- [ ] 可以在浏览器正常演示

---

## 📝 备注

1. **HTML vs PPTX：** 当前交付的是 HTML 格式（浏览器打开），不是 .pptx 格式。如需 .pptx，需另外转换。

2. **封面方案：** 之前做了 5 个封面设计（`ppt-design/`），用户如果要用到 HTML 里，可以转成 PNG 插入。

3. **技能位置：** Frontend Slides 技能在 `~/.agents/skills/frontend-slides/`，SKILL.md 有完整文档。

4. **备份：** 修改前建议复制一份原文件：
   ```bash
   cd /home/admin/.openclaw/workspace/projects/ppt-jinyin-planet/output/
   cp jinyin-planet.html jinyin-planet-backup.html
   ```

---

**下次更新：** 用户完成修改后通知金银验收

**Handover 状态：** 🟢 已完成 - 等待用户验收

**最新版本：** v1.1 (2026-03-18 12:36)
- 移除 Fontshare 字体依赖（用系统字体）
- 移除外部图片（用 emoji 图标）
- 确保手机/电脑都能正常显示

---

_创建人：金银（大管家）_  
_创建时间：2026-03-18 10:22_
