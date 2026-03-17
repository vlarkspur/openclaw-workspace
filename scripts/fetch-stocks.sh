#!/bin/bash
# 股票数据抓取脚本 - 使用腾讯财经接口

# 股票代码列表（格式：市场代码 + 股票代码）
# A 股：sz+ 代码，sh+ 代码
# 港股：hk+ 代码

stocks=(
    "sz002594"    # 比亚迪
    "hk01060"     # 大麦娱乐
    "sh601360"    # 三六零
    "sz000623"    # 吉林敖东
    "sh601390"    # 中国中铁
    "hk02015"     # 理想汽车
    "hk01810"     # 小米集团
    "hk09660"     # 地平线机器人
    "sz159529"    # 标普消费 ETF
)

echo "=== 股票数据抓取 ==="
echo "日期：$(date +%Y-%m-%d)"
echo ""

for stock in "${stocks[@]}"; do
    result=$(curl -s "http://qt.gtimg.cn/q=$stock")
    if [ -n "$result" ]; then
        # 提取股票名称和价格
        name=$(echo "$result" | sed 's/.*~\([^~]*\)~.*/\1/' | head -1)
        price=$(echo "$result" | sed 's/.*~[^~]*~[^~]*~\([^~]*\)~.*/\1/')
        open=$(echo "$result" | sed 's/.*~[^~]*~[^~]*~[^~]*~\([^~]*\)~.*/\1/')
        close_yest=$(echo "$result" | sed 's/.*~[^~]*~[^~]*~[^~]*~[^~]*~\([^~]*\)~.*/\1/')
        
        echo "$stock: $name | 现价：$price | 开盘：$open | 昨收：$close_yest"
    else
        echo "$stock: 数据获取失败"
    fi
done
