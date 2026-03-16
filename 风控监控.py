#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小溪持仓风控监控脚本
功能：获取实时股价，计算盈亏，检查止损线

依赖：pip3 install akshare pandas

使用方法：
    python3 风控监控.py

数据源：AKShare (免费开源金融数据)
"""

import sys
import json
from datetime import datetime

# 检查依赖
try:
    import akshare as ak
    import pandas as pd
except ImportError as e:
    print(f"❌ 缺少依赖：{e}")
    print("请运行：pip3 install akshare pandas")
    sys.exit(1)

# 小溪的持仓配置 (需要填写)
PORTFOLIO = {
    "比亚迪": {"code": "sz002594", "shares": 0, "cost": 0.0, "stop_loss": 0.10},
    "大麦娱乐": {"code": "hk01060", "shares": 0, "cost": 0.0, "stop_loss": 0.15},
    "三六零": {"code": "sh601360", "shares": 0, "cost": 0.0, "stop_loss": 0.12},
    "吉林敖东": {"code": "sz000623", "shares": 0, "cost": 0.0, "stop_loss": 0.10},
    "中国中铁": {"code": "sh601390", "shares": 0, "cost": 0.0, "stop_loss": 0.08},
    "理想汽车": {"code": "hk02015", "shares": 0, "cost": 0.0, "stop_loss": 0.15},
    "小米集团": {"code": "hk01810", "shares": 0, "cost": 0.0, "stop_loss": 0.12},
    "地平线机器人": {"code": "hk09660", "shares": 0, "cost": 0.0, "stop_loss": 0.20},
}

# 风控阈值
TOTAL_ASSETS = 0  # 总资产 (元)
POSITION_LIMIT = 0.20  # 单只股票上限 20%
STOP_LOSS_DEFAULT = 0.10  # 默认止损线 10%

def get_stock_price(code):
    """获取股票实时价格"""
    try:
        if code.startswith("sz") or code.startswith("sh"):
            # A 股
            df = ak.stock_zh_a_spot_em()
            stock = df[df['代码'] == code[2:]]
            if not stock.empty:
                return float(stock.iloc[0]['最新价'])
        elif code.startswith("hk"):
            # 港股
            df = ak.stock_hk_spot()
            stock = df[df['代码'] == code[2:]]
            if not stock.empty:
                return float(stock.iloc[0]['最新价'])
    except Exception as e:
        print(f"⚠️ 获取 {code} 价格失败：{e}")
    return None

def check_risk(position, current_price):
    """检查风控状态"""
    cost = position["cost"]
    shares = position["shares"]
    stop_loss = position["stop_loss"]
    
    if cost == 0 or shares == 0:
        return {"status": "⚠️ 未设置", "pnl": 0, "pnl_pct": 0}
    
    market_value = shares * current_price
    cost_value = shares * cost
    pnl = market_value - cost_value
    pnl_pct = pnl / cost_value
    
    # 检查止损线
    if pnl_pct <= -stop_loss:
        return {
            "status": "🔴 触及止损",
            "pnl": pnl,
            "pnl_pct": pnl_pct,
            "alert": True
        }
    elif pnl_pct <= -(stop_loss - 0.05):
        return {
            "status": "🟡 接近止损",
            "pnl": pnl,
            "pnl_pct": pnl_pct,
            "alert": False
        }
    else:
        return {
            "status": "🟢 正常",
            "pnl": pnl,
            "pnl_pct": pnl_pct,
            "alert": False
        }

def main():
    print("=" * 60)
    print("🦞 小溪持仓风控监控")
    print(f"📅 时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    alerts = []
    
    for name, pos in PORTFOLIO.items():
        if pos["shares"] == 0:
            print(f"\n⚠️ {name} ({pos['code']}): 未设置持仓数量")
            continue
        
        price = get_stock_price(pos["code"])
        if not price:
            print(f"\n❌ {name} ({pos['code']}): 获取价格失败")
            continue
        
        risk = check_risk(pos, price)
        market_value = pos["shares"] * price
        
        # 检查是否关键数据
        is_key_data = market_value > 10000  # 金额>1 万
        
        print(f"\n📊 {name} ({pos['code']})")
        print(f"   当前价：{price:.2f} 元")
        print(f"   成本价：{pos['cost']:.2f} 元")
        print(f"   持仓：{pos['shares']} 股")
        print(f"   市值：{market_value:,.2f} 元" + (" ⭐关键数据" if is_key_data else ""))
        print(f"   盈亏：{risk['pnl']:,.2f} 元 ({risk['pnl_pct']*100:.2f}%)")
        print(f"   状态：{risk['status']}")
        
        if risk.get("alert"):
            alerts.append(f"🔴 {name} 触及止损线！当前亏损 {risk['pnl_pct']*100:.2f}%")
    
    print("\n" + "=" * 60)
    if alerts:
        print("🚨 风控警报:")
        for alert in alerts:
            print(f"   {alert}")
    else:
        print("✅ 无风控警报")
    print("=" * 60)
    
    return len(alerts)

if __name__ == "__main__":
    sys.exit(main())
