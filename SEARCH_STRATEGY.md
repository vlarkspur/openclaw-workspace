# 🔍 搜索工具使用策略

**创建日期：** 2026-03-20  
**设计者：** 小溪  
**适用范围：** 所有搜索任务

---

## 📊 可用搜索工具

| 工具 | 状态 | API Key | 引擎数量 | 推荐度 |
|------|------|---------|---------|--------|
| **multi-search-engine** | ✅ 可用 | ❌ 不需要 | 17 个 | ⭐⭐⭐⭐⭐ |
| **tavily-search** | ✅ 可用 | ✅ 已配置 | Tavily | ⭐⭐⭐⭐ |

---

## 🎯 优先级规则

### 第一优先级：multi-search-engine

**使用场景：**
- ✅ 日常搜索
- ✅ 新闻搜索
- ✅ 信息检索
- ✅ 普通查询

**优点：**
- 无需 API Key
- 支持 17 个搜索引擎（百度/Google/Bing/DuckDuckGo 等）
- 灵活选择搜索引擎

**使用方法：**
```javascript
// 百度搜索
web_fetch({"url": "https://www.baidu.com/s?wd=关键词"})

// Google 搜索
web_fetch({"url": "https://www.google.com/search?q=keyword"})

// DuckDuckGo（隐私搜索）
web_fetch({"url": "https://duckduckgo.com/html/?q=keyword"})

// 站内搜索
web_fetch({"url": "https://www.google.com/search?q=site:github.com+react"})

// 文件类型搜索
web_fetch({"url": "https://www.google.com/search?q=machine+learning+filetype:pdf"})
```

---

### 第二优先级：tavily-search

**使用场景：**
- ✅ multi-search-engine 失败时
- ✅ 需要结构化结果时
- ✅ 需要简短答案时

**优点：**
- 返回结构化数据（标题/URL/摘要）
- 可以包含简短答案
- AI 优化搜索结果

**使用方法：**
```bash
cd /home/admin/.openclaw/workspace
python3 skills/openclaw-tavily-search/scripts/tavily_search.py \
  --query "关键词" \
  --max-results 5 \
  --format md
```

**高级用法：**
```bash
# 带答案
python3 skills/openclaw-tavily-search/scripts/tavily_search.py \
  --query "关键词" --include-answer

# 指定结果数量
python3 skills/openclaw-tavily-search/scripts/tavily_search.py \
  --query "关键词" --max-results 10
```

---

### 第三优先级：同时使用（交叉验证）

**使用场景：**
- ✅ 重要数据需要交叉验证
- ✅ 关键信息需要多源确认
- ✅ 股票数据/财务数据/医疗数据等

**使用方法：**
```bash
# 1. 先用 multi-search-engine 搜索
web_fetch({"url": "https://www.baidu.com/s?wd=关键词"})

# 2. 再用 tavily-search 搜索
python3 skills/openclaw-tavily-search/scripts/tavily_search.py \
  --query "关键词" --format md

# 3. 对比两个结果，交叉验证
```

**示例：股票数据验证**
```
数据来源 1：同花顺
数据来源 2：东方财富
数据来源 3：富途牛牛
→ 其中两个来源数据一致 → ✅ 可信
→ 数据不一致 → ⚠️ 需要进一步核实
```

---

## 📋 决策流程图

```
开始搜索任务
    ↓
是否需要交叉验证？
    ↓
是 → 同时使用 multi + tavily → 对比结果 → 输出
    ↓
否
    ↓
使用 multi-search-engine
    ↓
成功？
    ↓
是 → 输出结果
    ↓
否
    ↓
使用 tavily-search
    ↓
输出结果
```

---

## 🎯 具体场景应用

### 场景 1：日常新闻搜索

**工具：** multi-search-engine（优先）

```javascript
// 百度搜索新闻
web_fetch({"url": "https://www.baidu.com/s?wd=新闻关键词&rtt=1&bsst=1"})
```

---

### 场景 2：股票数据查询

**工具：** 同时使用（交叉验证）

```bash
# 1. multi-search-engine 搜索同花顺
web_fetch({"url": "https://stock.10jqka.com.cn/stock/代码.html"})

# 2. tavily-search 搜索多个来源
python3 skills/openclaw-tavily-search/scripts/tavily_search.py \
  --query "股票代码 最新股价 财报" --max-results 10

# 3. 对比验证
```

---

### 场景 3：技术问题搜索

**工具：** multi-search-engine（优先）

```javascript
// Google 搜索技术文档
web_fetch({"url": "https://www.google.com/search?q=site:github.com+技术问题"})
```

---

### 场景 4：学术论文搜索

**工具：** multi-search-engine（优先）

```javascript
// Google Scholar 或 filetype:pdf
web_fetch({"url": "https://www.google.com/search?q=关键词+filetype:pdf"})
```

---

## ⚠️ 注意事项

### 1. multi-search-engine 的限制

- ❌ 某些搜索引擎可能触发验证码
- ❌ 动态网页可能无法完整抓取
- ✅ 解决方法：换用其他搜索引擎

### 2. tavily-search 的限制

- ⚠️ 需要 API Key（已配置）
- ⚠️ 有调用频率限制
- ✅ 适合结构化搜索

### 3. 交叉验证的原则

- ✅ 至少 2 个独立来源
- ✅ 优先选择权威来源（官方/财报/主流财经媒体）
- ❌ 避免单一来源（尤其是自媒体）

---

## 📍 脚本路径

**tavily-search 脚本位置：**
```
/home/admin/.openclaw/workspace/skills/openclaw-tavily-search/scripts/tavily_search.py
```

**使用时必须用完整路径！**

---

## 📊 工具对比总结

| 维度 | multi-search-engine | tavily-search |
|------|---------------------|---------------|
| API Key | ❌ 不需要 | ✅ 需要 |
| 引擎数量 | 17 个 | 1 个（Tavily） |
| 结果格式 | HTML | 结构化（JSON/MD） |
| 适用场景 | 日常搜索 | 结构化搜索 |
| 推荐度 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

---

**最后更新：** 2026-03-20 20:50  
**下次审查：** 发现新搜索工具时更新
