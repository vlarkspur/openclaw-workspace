# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## 🔍 搜索工具优先级

**原则：** 优先使用不需要 API key 的工具

| 优先级 | 工具 | 原因 |
|--------|------|------|
| ⭐⭐⭐⭐⭐ | **Multi Search Engine** | 无需 API key，支持 17 个搜索引擎（百度/Bing/Google/DuckDuckGo 等） |
| ⭐⭐⭐⭐ | `browser` 工具 | 可抓取实时页面，但提取效率低 |
| ⭐⭐⭐ | `web_fetch` | 静态页面可用，动态页面失败 |
| ⭐⭐ | `web_search` | 需要 Brave API key（未配置） |
| ⭐ | `summarize` | 需要 Gemini API key（已配置，但用于总结而非搜索） |

**Multi Search Engine 用法：**
```javascript
// 百度
web_fetch({"url": "https://www.baidu.com/s?wd=关键词"})

// Bing 国际
web_fetch({"url": "https://cn.bing.com/search?q=关键词"})

// DuckDuckGo（英文搜索）
web_fetch({"url": "https://duckduckgo.com/html/?q=keyword"})

// Google
web_fetch({"url": "https://www.google.com/search?q=keyword"})
```

**数据验证原则：**
- 关键数据必须 2-3 个独立来源交叉验证
- 来源示例：国家统计局 + 媒体报道 + 国际机构（CNBC/高盛/UBS）

---

Add whatever helps you do your job. This is your cheat sheet.
