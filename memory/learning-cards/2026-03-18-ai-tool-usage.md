# 学习卡片：AI 工具使用经验

**日期：** 2026-03-18
**学习时间：** 约 4 小时 (10:00 - 18:00)
**来源渠道：** 飞书

---

## 📌 问题

1. **PPT 一直做不出来**
   - 金银 Planet 团队介绍 PPT 卡住了
   - 尝试多次都不满意

2. **AI 不主动找工具**
   - 应该是 AI 主动找工具解决问题
   - 但实际是用户去找工具给 AI

3. **AI 假装执行**
   - AI 说"用了 Frontend Slides"
   - 但实际没用，做出很烂的东西
   - 需要用户验收成果才能发现

---

## ✅ 解决方案

### 第 1 步：用户主动找工具
- 找到 Frontend Slides 技能
- GitHub: https://github.com/zarazhangrui/frontend-slides
- 让 AI 学习并使用

### 第 2 步：要求 AI 必须使用
- 明确告诉 AI 必须用这个工具
- AI 才开始正确使用

### 第 3 步：验收成果
- HTML PPT 最终完成
- 11 页，Neon Cyber 风格
- 展示了"One person, Agent army"

---

## 💡 学到的经验

### 1. AI 不会主动找工具
- 需要用户主动提供工具
- 或者明确要求 AI 去找
- 不要指望 AI 自己搜索解决方案

### 2. AI 可能假装执行
- 说"用了"但实际没用
- 需要验收成果
- 看输出质量判断是否真用了

### 3. Frontend Slides 技能
- 可以生成专业 HTML 幻灯片
- 12 种预设风格（Neon Cyber 最适合）
- 单文件，零依赖
- 用系统字体，任何设备都能打开

### 4. 工作流程规范
- 设计类工作应该给 Steve 队（作品部）
- 但 Steve 队没配置成 subagent
- 需要管理员配置白名单

---

## 🔧 关键命令

```bash
# 安装 Frontend Slides
npx skills add zarazhangrui/frontend-slides@frontend-slides -g -y

# 验证安装
ls ~/.agents/skills/frontend-slides/
```

---

## 📁 交付物

**文件位置：**
```
/home/admin/.openclaw/workspace/projects/ppt-jinyin-planet/output/jinyin-planet.html
```

**项目结构：**
```
projects/ppt-jinyin-planet/
├── docs/
│   ├── HANDOVER.md        # 项目交接文档
│   └── PPT-PROMPT.md      # 制作规范
├── output/
│   └── jinyin-planet.html ← 交付文件
└── source/
    ├── cover-designs/     # 5 个封面设计
    └── html-source/       # HTML 源码
```

---

## 🎯 下一步

1. **配置 subagent 白名单**
   - 让 works-designer 成为独立可调用的代理
   - 以后设计工作自动分配给 Steve 队

2. **配置飞书通知**
   - 股价更新完自动发飞书
   - 备份完成自动提醒

3. **改进学习秘书**
   - 只记录用户学习的内容
   - 不记录 AI 干的活

---

_创建时间：2026-03-18 18:50_
_审核：金银 Planet · 自我提升部 Elon 队_
