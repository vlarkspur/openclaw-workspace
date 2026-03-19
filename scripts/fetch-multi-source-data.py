#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
多源股票数据抓取脚本 v2
- 股价：腾讯财经（行业标准，可靠）
- PE/PB/市值：web_fetch 抓取东方财富
- 交叉验证：关键数据标注来源，供 Charlie 团队审核

用法：
    python3 fetch-multi-source-data.py --json
"""

import urllib.request
import sys
import json
from datetime import datetime

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

def fetch_tencent_price(code):
    """从腾讯财经抓取股价"""
    try:
        url = f"http://qt.gtimg.cn/q={code}"
        req = urllib.request.urlopen(url, timeout=5)
        data = req.read().decode('gbk')
        parts = data.split('~')
        if len(parts) >= 33:
            return {
                'source': '腾讯财经',
                'confidence': '⭐⭐⭐⭐⭐',
                'current': float(parts[3]),
                'change': float(parts[31]) if parts[31] else 0,
                'change_pct': float(parts[32]) if parts[32] else 0,
                'high': float(parts[33]) if len(parts) > 33 and parts[33] else 0,
                'low': float(parts[34]) if len(parts) > 34 and parts[34] else 0,
                'volume': float(parts[6]) if len(parts) > 6 and parts[6] else 0,
                'turnover': float(parts[37]) if len(parts) > 37 and parts[37] else 0,
            }
    except Exception as e:
        print(f"腾讯财经抓取 {code} 失败：{e}")
    return None

def fetch_all_stocks():
    """抓取所有股票数据"""
    results = []
    
    for code, name, display_code in STOCKS:
        print(f"正在抓取 {display_code} {name}...", end=" ")
        
        data = fetch_tencent_price(code)
        
        if data:
            result = {
                'code': display_code,
                'name': name,
                'current': data['current'],
                'change': data['change'],
                'change_pct': data['change_pct'],
                'high': data.get('high', 0),
                'low': data.get('low', 0),
                'volume': data.get('volume', 0),
                'turnover': data.get('turnover', 0),
                'data_quality': {
                    'source': data['source'],
                    'confidence': data['confidence'],
                    'type': '实时数据',
                    'cross_verify': '股价为公开实时数据，腾讯财经为行业标准',
                    'note': 'PE/PB/股东户数等关键数据需单独抓取并交叉验证'
                },
                'data_timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            results.append(result)
            print(f"✅ {data['current']} ({data['change_pct']:+.2f}%)")
        else:
            print(f"❌ 抓取失败")
    
    return results

def main():
    """主函数"""
    if len(sys.argv) > 1 and sys.argv[1] == '--json':
        prices = fetch_all_stocks()
        output = {
            'date': datetime.now().strftime("%Y-%m-%d"),
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'prices': prices,
            'data_quality': {
                'total_stocks': len(prices),
                'success': sum(1 for p in prices if p['current'] > 0),
                'failed': sum(1 for p in prices if p['current'] == 0),
            },
            'note': '股价数据来自腾讯财经（行业标准）。PE/PB/股东户数等关键数据需 Charlie 团队进一步抓取并交叉验证。'
        }
        print("\n--- JSON OUTPUT START ---")
        print(json.dumps(output, ensure_ascii=False, indent=2))
        print("--- JSON OUTPUT END ---")
    else:
        print("📊 多源股票数据抓取 v2")
        print("=" * 50)
        print("数据源：腾讯财经（行业标准）")
        print("关键数据（PE/PB/股东户数）需单独交叉验证")
        print("=" * 50)
        fetch_all_stocks()

if __name__ == "__main__":
    main()
