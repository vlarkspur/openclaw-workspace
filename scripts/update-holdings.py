#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
股票数据自动更新脚本
- 抓取 9 只持仓股票的最新股价
- 更新 holdings.md 文件
- 输出 JSON 数据（供 HEARTBEAT 调用）

用法：
    python3 update-holdings.py --json
"""

import urllib.request
import re
import sys
import json
from datetime import datetime, timedelta

# 股票代码列表（腾讯财经格式）
STOCKS = [
    ("sz002594", "比亚迪", "002594.SZ"),
    ("hk01060", "大麦娱乐", "01060.HK"),
    ("sh601360", "三六零", "601360.SH"),
    ("sz000623", "吉林敖东", "000623.SZ"),
    ("sh601390", "中国中铁", "601390.SH"),
    ("hk02015", "理想汽车-W", "02015.HK"),
    ("hk01810", "小米集团-W", "01810.HK"),
    ("hk09660", "地平线机器人-W", "09660.HK"),
    ("sz159529", "标普消费 ETF", "159529.SZ"),
]

HOLDINGS_FILE = "/home/admin/.openclaw/workspace/memory/investment/holdings.md"

def fetch_stock_price(code):
    """抓取单只股票价格"""
    try:
        url = f"http://qt.gtimg.cn/q={code}"
        req = urllib.request.urlopen(url, timeout=5)
        data = req.read().decode('gbk')
        
        parts = data.split('~')
        if len(parts) >= 33:
            return {
                'name': parts[1],
                'current': float(parts[3]),
                'open': float(parts[4]),
                'close_yest': float(parts[5]),
                'change': float(parts[31]) if parts[31] else 0,
                'change_pct': float(parts[32]) if parts[32] else 0,
            }
    except Exception as e:
        print(f"抓取 {code} 失败：{e}")
    return None

def fetch_all_stocks():
    """抓取所有股票价格"""
    results = []
    for code, name, display_code in STOCKS:
        data = fetch_stock_price(code)
        if data:
            data['code'] = display_code
            results.append(data)
            print(f"✅ {display_code} {data['name']}: {data['current']} ({data['change']:+.2f}, {data['change_pct']:+.2f}%)")
        else:
            print(f"❌ {display_code} {name}: 抓取失败")
    return results

def update_holdings_file(prices):
    """更新 holdings.md 文件"""
    today = datetime.now().strftime("%Y-%m-%d")
    weekday = datetime.now().strftime("%A")
    
    # 读取现有文件
    try:
        with open(HOLDINGS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"文件不存在：{HOLDINGS_FILE}")
        return False
    
    # 生成今日股价表格
    today_table = f"""
### {today}（{weekday}）

| 代码 | 名称 | 收盘价 | 涨跌 | 涨跌幅 | 数据来源 |
|------|------|--------|------|--------|----------|
"""
    for p in prices:
        today_table += f"| {p['code']} | {p['name']} | {p['current']:.2f} | {p['change']:+.2f} | {p['change_pct']:+.2f}% | 腾讯财经 |\n"
    
    today_table += "\n**备注：** 港股价格为港币，盈亏计算需转换为人民币\n"
    
    # 检查是否已有今日数据
    if f"### {today}" in content:
        print(f"⚠️  {today} 的数据已存在，跳过更新")
        return True
    
    # 在"## 每日股价更新"后面插入今日数据
    marker = "## 每日股价更新"
    if marker in content:
        # 找到 marker 位置，插入到其后
        idx = content.find(marker) + len(marker)
        content = content[:idx] + "\n" + today_table + content[idx:]
    else:
        # 如果没有这个章节，添加到备注之前
        marker = "## 备注"
        if marker in content:
            idx = content.find(marker)
            content = content[:idx] + "## 每日股价更新\n" + today_table + "\n" + content[idx:]
    
    # 更新更新日志
    log_entry = f"| {today} | 自动更新 | Python 脚本抓取股价数据 |\n"
    if "| 日期 | 操作 | 备注 |" in content:
        idx = content.find("| 日期 | 操作 | 备注 |")
        idx = content.find("\n", idx) + 1
        content = content[:idx] + log_entry + content[idx:]
    
    # 更新最后更新时间
    content = re.sub(
        r'\*最后更新：[^*]+\*',
        f'*最后更新：{today} {datetime.now().strftime("%H:%M")}*',
        content
    )
    
    # 写回文件
    with open(HOLDINGS_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 文件已更新：{HOLDINGS_FILE}")
    return True

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', action='store_true', help='输出 JSON 格式')
    args = parser.parse_args()
    
    print(f"=== 股票数据自动更新 ===")
    print(f"时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("")
    
    # 抓取数据
    prices = fetch_all_stocks()
    if not prices:
        print("❌ 所有股票抓取失败，退出")
        sys.exit(1)
    
    print("")
    
    # 更新文件
    if update_holdings_file(prices):
        print("✅ 更新完成")
        
        # 如果指定 --json，输出 JSON 数据供 HEARTBEAT 调用
        if args.json:
            output = {
                'date': datetime.now().strftime("%Y-%m-%d"),
                'prices': prices
            }
            print("JSON_START")
            print(json.dumps(output, ensure_ascii=False))
            print("JSON_END")
        
        sys.exit(0)
    else:
        print("❌ 更新失败")
        sys.exit(1)

if __name__ == "__main__":
    main()
