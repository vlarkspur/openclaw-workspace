# 小溪持仓股票监控系统

## 📊 监控目标

监控小溪 8 只持仓股票的关键数据：
- 比亚迪 (002594.SZ)
- 大麦娱乐 (01060.HK)
- 三六零 (601360.SH)
- 吉林敖东 (000623.SZ)
- 中国中铁 (601390.SH)
- 理想汽车 (02015.HK)
- 小米集团 (01810.HK)
- 地平线机器人 (09660.HK)

## 📈 监控指标

| 指标 | 更新频率 | 数据来源 | 可信度 |
|------|----------|----------|--------|
| 股价 | 实时 | 东方财富/港交所 | 高 |
| 市盈率 (TTM) | 实时 | 东方财富 | 高 |
| 融资余额 | 每日 | 东方财富 | 高 |
| 股东户数 | 季度（财报） | 东方财富/公司公告 | 高 |

## 🔍 数据来源

### A 股 (东方财富网)
- 行情：`https://quote.eastmoney.com/{市场}{代码}.html`
- 股东户数：`https://data.eastmoney.com/gdhs/detail/{代码}.html`
- 融资融券：`https://data.eastmoney.com/rzrq/stock/{代码}.html`

### 港股
- 港交所：`https://www.hkex.com.hk/`
- 东方财富港股：`https://quote.eastmoney.com/hk/{代码}.html`

## ✅ 数据验证要求

**关键数据需 2 个以上独立来源交叉验证：**
1. 东方财富网 (主要来源)
2. 同花顺 iFinD (验证来源)
3. 雪球网 (验证来源)

**验证方法：**
- 比较同一指标在不同平台的数据差异
- 差异>1% 时需调查原因
- 记录验证状态在 CSV 文件中

## 🚨 异常波动告警

**告警阈值：>5% 变动**

监控以下指标的日环比/周环比变动：
- 股价涨跌幅
- 融资余额变动
- 股东户数变动（季度）

**告警流程：**
1. 检测异常波动
2. 记录异常数据
3. 分析原因（财报/公告/市场事件）
4. 向小溪报告

## 📁 文件结构

```
stock_monitoring/
├── README.md                    # 本文件
├── stock_data_YYYY-MM-DD.csv    # 每日数据快照
├── anomaly_reports/             # 异常波动报告
└── scripts/                     # 自动化脚本（待开发）
```

## 🤖 自动化建议

### Python 脚本示例框架

```python
import requests
import pandas as pd
from datetime import datetime

# 股票列表
STOCKS = [
    {'code': '002594', 'market': 'sz', 'name': '比亚迪'},
    {'code': '01060', 'market': 'hk', 'name': '大麦娱乐'},
    # ... 其他股票
]

def fetch_stock_data(code, market):
    """从东方财富获取股票数据"""
    # 实现数据抓取逻辑
    pass

def check_anomaly(current, previous, threshold=0.05):
    """检查是否异常波动"""
    change = abs(current - previous) / previous
    return change > threshold

def export_to_csv(data, date):
    """导出 Excel 友好型 CSV"""
    df = pd.DataFrame(data)
    df.to_csv(f'stock_data_{date}.csv', index=False, encoding='utf-8-sig')
```

### 定时任务设置

```bash
# 每日收盘后更新（工作日 15:30）
30 15 * * 1-5 cd /path/to/stock_monitoring && python fetch_data.py

# 季度财报后更新股东户数（财报披露后 1 天）
0 9 * 1,4,7,10 * cd /path/to/stock_monitoring && python update_shareholder.py
```

## 📊 数据质量说明

### 可信度评级
- **高**：官方交易所数据、上市公司公告
- **中**：主流财经平台（东方财富、同花顺）
- **低**：用户生成内容（股吧、论坛）

### 数据更新时间
- A 股：交易日 9:30-15:00 实时更新
- 港股：交易日 9:30-16:00 实时更新
- 股东户数：财报披露后更新（季报/年报）

## ⚠️ 注意事项

1. **货币单位**：A 股数据为人民币 (元)，港股数据为港元 (HKD)
2. **交易时间**：数据仅在交易时段更新
3. **财报延迟**：股东户数数据有财报披露延迟
4. **数据校验**：关键决策前需交叉验证

## 📞 联系与反馈

数据问题或监控需求变更，请联系小溪。

---

*最后更新：2026-03-14*
*监控专员：金银 (AI 管家)*
