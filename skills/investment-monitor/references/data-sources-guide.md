# 股票数据抓取指南

**创建日期：** 2026-03-19  
**最后更新：** 2026-03-19  
**适用场景：** 港股、A 股股票数据抓取（用于调仓分析）

---

## 🎯 核心原则

1. **数据源优先级** —— 不要轻信聚合平台，以官方披露为准
2. **交叉验证** —— 关键数据必须 2 个以上来源
3. **标注来源** —— 每条数据都要说明从哪里来的
4. **单位确认** —— 港股/美股/财报单位可能不同，务必核对

---

## 📊 数据源优先级

### 港股 (01810.HK 类型)

| 优先级 | 数据源 | URL 模板 | 可信度 | 用途 |
|--------|--------|---------|--------|------|
| ⭐⭐⭐⭐⭐ | **同花顺 F10** | `https://basic.10jqka.com.cn/176/HK{code}/` | 官方 | 股本、股东数据 |
| ⭐⭐⭐⭐⭐ | **富途牛牛** | `https://www.futunn.com/stock/{code}-HK` | 官方 | 市值、PE、PB |
| ⭐⭐⭐⭐ | 东方财富 | `https://quote.eastmoney.com/hk/{code}.html` | 可靠 | 备选验证 |
| ⭐⭐⭐ | 同花顺 stockpage | `https://stockpage.10jqka.com.cn/HK{code}/` | 简版 | **仅概览，财务数据不全** |
| ⭐⭐⭐ | 腾讯财经 | `http://qt.gtimg.cn/q=hk{code}` | 一般 | 仅股价 |
| ❌ | 腾讯财经 | - | 不可靠 | **PE/PB 数据错误，弃用** |

### A 股 (601360.SH 类型)

| 优先级 | 数据源 | URL 模板 | 可信度 |
|--------|--------|---------|--------|
| ⭐⭐⭐⭐⭐ | 同花顺 stockpage | `https://stockpage.10jqka.com.cn/{code}/` | 官方 |
| ⭐⭐⭐⭐⭐ | 东方财富 | `https://quote.eastmoney.com/{code}.html` | 官方 |
| ⭐⭐⭐⭐ | 腾讯财经 | `http://qt.gtimg.cn/q={code}` | 股价可用 |

---

## ⚠️ 踩过的坑（血泪教训）

### 坑 1：腾讯财经 PE 数据错误

**问题：**
- 小米集团腾讯财经显示 PE=37.17
- 同花顺官方显示 PE=20.33
- **差异 83%**，严重误导分析

**原因：**
- 腾讯财经用的净利润口径可能不同
- 或者数据更新滞后

**解决：**
- **弃用腾讯财经的 PE/PB 数据**
- 以同花顺/东方财富官方数据为准

---

### 坑 2：每股净资产计算错误

**问题：**
- 我手动计算：每股净资产 = 股东权益 / 总股本
- 我用的是 929.28 亿元 / 261.46 亿股 = 3.55 元
- 同花顺官方：10.20 元
- **差异 187%**

**原因：**
- 股东权益单位可能不是"亿元"
- 或者财报口径不同（含少数股东权益 vs 不含）

**解决：**
- **不要手动计算财报指标**
- 直接从官方页面抓取披露值

---

### 坑 3：财报数据口径不一致

**问题：**
- 不同平台的营收/净利润数值不同
- 小米 2025-09-30 财报：
  - 我抓的：营收 3,728 亿，净利润 384 亿
  - 同花顺：营收 3,404 亿，净利润 351 亿

**原因：**
- 可能是单季度 vs 累计值
- 或者人民币 vs 港元
- 或者含/不含少数股东权益

**解决：**
- **明确标注报告期和口径**
- 统一用同花顺官方数据

---

### 坑 4：网络接口不稳定

**问题：**
- 新浪财经 404
- 理杏仁 429 限流
- 雪球需要登录

**解决：**
- **首选富途牛牛/同花顺 F10**（数据全）
- 备选东方财富
- 设置超时和重试

---

### 坑 5：同花顺 stockpage 是简版页面 ⚠️ 新发现

**问题：**
- 地平线机器人 (09660.HK) 用 stockpage 页面抓不到财务数据
- 页面只包含概览信息，没有详细的 PE、PB、每股收益等
- 小米集团 (01810.HK) 的 stockpage 却有完整数据

**原因：**
- 同花顺 stockpage 对不同股票展示的数据不同
- 次新股/科创板股票可能数据不完整
- **stockpage 是简版，F10 才是完整版**

**解决：**
- **改用同花顺 F10**: `https://basic.10jqka.com.cn/176/HK{code}/`
- **或者用富途牛牛**: `https://www.futunn.com/stock/{code}-HK`
- 富途牛牛数据完整，无需登录，强烈推荐

**案例：**
```
地平线机器人 (09660.HK):
- stockpage: 无财务数据 ❌
- F10: 有股本数据 ✅
- 富途牛牛：市值 1081 亿，PE 44.46 ✅
```

---

### 坑 6：新浪财经解码失败

**问题：**
- 部分港股新浪财经页面返回 GBK 编码
- Python 用 UTF-8 解码会报错：`'utf-8' codec can't decode byte 0xb5`

**解决：**
- 尝试用 GBK 解码：`data.decode('gbk')`
- 或者直接用富途牛牛/东方财富（都是 UTF-8）

---

## 🛠️ 标准抓取流程

### 步骤 1：确定股票代码格式

```
港股：01810.HK → 同花顺用 HK1810，腾讯用 hk01810
A 股：601360.SH → 同花顺用 601360，腾讯用 sh601360
```

### 步骤 2：抓取核心数据

**首选：富途牛牛（数据最完整）**
```
https://www.futunn.com/stock/{code}-HK
```
**提取字段：**
- 总市值（亿港元）
- 市盈率 (TTM)
- 市净率
- 股价
- 涨跌幅

**备选：同花顺 F10（股本、股东数据）**
```
https://basic.10jqka.com.cn/176/HK{code}/
```
**提取字段：**
- 总股本（亿股）
- 流通股本（亿股）
- 股东户数
- 股本变动历史

**⚠️ 注意：** 同花顺 stockpage 是简版页面，财务数据可能不完整，不要作为首选。

### 步骤 3：抓取股价

**方案 A：富途牛牛（推荐，数据完整）**
```
https://www.futunn.com/stock/{code}-HK
```
直接提取页面显示的股价、涨跌幅、市值、PE、PB

**方案 B：腾讯财经（仅股价，快速）**
```
http://qt.gtimg.cn/q=hk01810
```

**解析响应（~分隔）：**
```
parts[3] = 股价
parts[31] = 涨跌
parts[32] = 涨跌幅%
parts[39] = PE（不可信，仅供参考）
parts[48] = 52 周高
parts[49] = 52 周低
```

### 步骤 4：交叉验证

| 数据项 | 主来源 | 验证源 | 允许差异 |
|--------|--------|--------|----------|
| 股价 | 腾讯财经 | 同花顺 | <1% |
| 总股本 | 同花顺 | 东方财富 | <1% |
| PE | 同花顺 | 东方财富 | <5% |
| PB | 同花顺 | 东方财富 | <5% |
| 净利润 | 同花顺 | - | 单一来源需标注 |

### 步骤 5：标注数据质量

```markdown
**数据项：** 市盈率
**数值：** 20.33
**来源：** 同花顺 stockpage
**时间：** 2026-03-19
**可信度：** ⭐⭐⭐⭐⭐（官方披露）
**交叉验证：** 东方财富（一致）
```

---

## 📁 标准输出模板

```markdown
## 📊 {股票名称} ({代码}) - 数据报告

**数据时间：** {日期}

### 核心数据

| 数据项 | 数值 | 来源 | 可信度 |
|--------|------|------|--------|
| 股价 | {价格} | 腾讯财经 | ⭐⭐⭐⭐⭐ |
| 总股本 | {股本} | 同花顺 | ⭐⭐⭐⭐⭐ |
| 市值 | {市值} | 计算 | ⭐⭐⭐⭐⭐ |
| PE-TTM | {pe} | 同花顺 | ⭐⭐⭐⭐⭐ |
| PB | {pb} | 同花顺 | ⭐⭐⭐⭐⭐ |

### 财务数据（{报告期}）

| 指标 | 数值 |
|------|------|
| 营收 | {营收} |
| 净利润 | {净利润} |
| 每股收益 | {eps} |
| 每股净资产 | {bvps} |
| ROE | {roe} |

### 数据质量说明

- ✅ 所有核心数据已交叉验证
- ⚠️ {说明}
```

---

## 🔧 代码片段

### 抓取富途牛牛（推荐）

```python
import urllib.request
import re

def fetch_futu_data(code):
    """抓取富途牛牛数据（港股）"""
    url = f"https://www.futunn.com/stock/{code}-HK"
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    })
    resp = urllib.request.urlopen(req, timeout=15)
    html = resp.read().decode('utf-8')
    
    # 提取数据
    patterns = {
        'price': r'>([\d.]+)</div>.*?交易中',
        'market_cap': r'([\d.]+) 亿总市值',
        'pe_ttm': r'([\d.]+) 市盈率 TTM',
        'change_pct': r'[+-]([\d.]+)%',
    }
    
    result = {}
    for name, pattern in patterns.items():
        match = re.search(pattern, html)
        if match:
            result[name] = float(match.group(1))
    
    return result
```

### 抓取同花顺 F10（股本数据）

```python
import urllib.request
import re

def fetch_ths_data(code, market='HK'):
    """抓取同花顺 stockpage 数据"""
    if market == 'HK':
        url = f"https://stockpage.10jqka.com.cn/{market}{code}/"
    else:
        url = f"https://stockpage.10jqka.com.cn/{code}/"
    
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    })
    resp = urllib.request.urlopen(req, timeout=15)
    html = resp.read().decode('utf-8')
    
    # 提取数据
    patterns = {
        '总股本': r'总股本 [^<]*<[^>]*>([\d.]+)',
        '每股收益': r'每股收益 [^<]*<[^>]*>([\d.]+)',
        '每股净资产': r'每股净资产 [^<]*<[^>]*>([\d.]+)',
        '净利润': r'净利润 [^<]*<[^>]*>([\d.]+)',
        '营业收入': r'营业收入 [^<]*<[^>]*>([\d.]+)',
        'ROE': r'净资产收益率 [^<]*<[^>]*>([\d.]+)',
    }
    
    result = {}
    for name, pattern in patterns.items():
        match = re.search(pattern, html)
        if match:
            result[name] = float(match.group(1))
    
    return result
```

### 抓取腾讯财经股价

```python
def fetch_tencent_price(code, market='hk'):
    """抓取腾讯财经股价（仅股价）"""
    if market == 'hk':
        url = f"http://qt.gtimg.cn/q={market}{code}"
    else:
        url = f"http://qt.gtimg.cn/q={code}"
    
    resp = urllib.request.urlopen(url, timeout=5)
    data = resp.read().decode('gbk')
    parts = data.split('~')
    
    if len(parts) >= 50:
        return {
            'price': float(parts[3]),
            'change': float(parts[31]) if parts[31] else 0,
            'change_pct': float(parts[32]) if parts[32] else 0,
            'high52': float(parts[48]) if len(parts) > 48 else 0,
            'low52': float(parts[49]) if len(parts) > 49 else 0,
        }
    return None
```

---

## 📚 参考链接

### 成功案例

| 股票 | 代码 | 数据源 | 状态 |
|------|------|--------|------|
| 小米集团 | 01810.HK | 同花顺 + 新浪 | ✅ 完整 |
| 地平线机器人 | 09660.HK | 富途牛牛 + 东方财富 | ✅ 完整 |

### 数据源链接

- 同花顺 F10: https://basic.10jqka.com.cn/176/HK{code}/
- 富途牛牛：https://www.futunn.com/stock/{code}-HK
- 东方财富：https://quote.eastmoney.com/hk/{code}.html
- 腾讯财经：http://qt.gtimg.cn/q=hk{code}

---

## 🔄 更新记录

| 日期 | 更新内容 | 备注 |
|------|----------|------|
| 2026-03-19 | 初始版本 | 基于小米集团数据抓取经验 |
| 2026-03-19 | 添加富途牛牛数据源 | 地平线机器人抓取经验 |
| 2026-03-19 | 添加坑 5、坑 6 | stockpage 简版问题、编码问题 |
| 2026-03-19 | 更新数据源优先级 | 富途牛牛升为⭐⭐⭐⭐⭐ |

---

_**重要：** 每次抓取新股票前，先读这个文档，避免重复踩坑。_

---

_**重要：** 每次抓取新股票前，先读这个文档，避免重复踩坑。_
