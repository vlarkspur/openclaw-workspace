#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
股票数据抓取脚本 - 腾讯财经接口
输出：代码 | 名称 | 现价 | 开盘 | 昨收 | 涨跌额 | 涨跌幅
"""

import urllib.request
import re

# 股票代码列表
stocks = [
    ("sz002594", "比亚迪"),
    ("hk01060", "大麦娱乐"),
    ("sh601360", "三六零"),
    ("sz000623", "吉林敖东"),
    ("sh601390", "中国中铁"),
    ("hk02015", "理想汽车"),
    ("hk01810", "小米集团"),
    ("hk09660", "地平线机器人"),
    ("sz159529", "标普消费 ETF"),
]

print("=== 股票数据抓取 ===")
print(f"日期：2026-03-17")
print("")
print(f"{'代码':<12} {'名称':<15} {'现价':>10} {'开盘':>10} {'昨收':>10} {'涨跌':>10} {'涨跌幅':>10}")
print("-" * 80)

for code, name in stocks:
    try:
        url = f"http://qt.gtimg.cn/q={code}"
        req = urllib.request.urlopen(url, timeout=5)
        data = req.read().decode('gbk')  # 腾讯接口返回 GBK 编码
        
        # 解析数据：v_sz002594="51~比亚迪~002594~102.87~104.62~104.63~...
        # 字段索引 (从 0 开始):
        # 0=市场，1=名称，2=代码，3=现价，4=开盘，5=昨收，...
        # 31=时间，32=涨跌额，33=涨跌幅%
        
        parts = data.split('~')
        if len(parts) >= 34:
            stock_name = parts[1]
            current = parts[3]
            open_price = parts[4]
            close_yest = parts[5]
            change = parts[31] if len(parts) > 31 else "0"    # 涨跌额
            change_pct = parts[32] if len(parts) > 32 else "0" # 涨跌幅%
            
            # 清理数据
            try:
                current_f = float(current)
                open_f = float(open_price)
                close_f = float(close_yest)
                change_f = float(change) if change else 0
                change_pct_f = float(change_pct) if change_pct else 0
                
                print(f"{code:<12} {stock_name:<15} {current_f:>10.2f} {open_f:>10.2f} {close_f:>10.2f} {change_f:>10.2f} {change_pct_f:>10.2f}%")
            except ValueError as e:
                print(f"{code:<12} {stock_name:<15} {'数据格式错误':>10}")
        else:
            print(f"{code:<12} {name:<15} {'字段不足':>10}")
    except Exception as e:
        print(f"{code:<12} {name:<15} {f'错误：{str(e)}':>10}")

print("")
print("数据来源：腾讯财经 (qt.gtimg.cn)")
print("注意：港股价格为港币")
