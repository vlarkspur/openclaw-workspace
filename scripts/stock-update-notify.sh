#!/bin/bash
# 股价更新 + 飞书通知执行脚本
# 由 HEARTBEAT.md 调用

# 运行 Python 脚本，获取 JSON 输出
OUTPUT=$(python3 /home/admin/.openclaw/workspace/scripts/update-holdings.py --json 2>&1)

# 提取 JSON 数据
JSON_DATA=$(echo "$OUTPUT" | sed -n '/JSON_START/,/JSON_END/p' | grep -v 'JSON_')

if [ -z "$JSON_DATA" ]; then
    echo "❌ 获取股价数据失败"
    exit 1
fi

# 解析 JSON 并生成消息
DATE=$(echo "$JSON_DATA" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['date'])")
PRICES=$(echo "$JSON_DATA" | python3 -c "import sys,json; d=json.load(sys.stdin); print(json.dumps(d['prices'], ensure_ascii=False))")

# 生成涨幅榜和跌幅榜
MESSAGE=$(python3 << EOF
import json

prices = json.loads('''$PRICES''')

# 按涨跌排序
up_stocks = [p for p in prices if p['change_pct'] > 0]
down_stocks = [p for p in prices if p['change_pct'] <= 0]

message = f"📊 股价更新 · $DATE\n\n"

# 涨幅榜
if up_stocks:
    message += "📈 涨幅榜：\n"
    for p in sorted(up_stocks, key=lambda x: x['change_pct'], reverse=True)[:3]:
        emoji = "🔥" if p['change_pct'] > 3 else "📈"
        message += f"{emoji} {p['name']}: {p['current']:.2f} ({p['change_pct']:+.2f}%)\n"

# 跌幅榜
if down_stocks:
    message += "\n📉 跌幅榜：\n"
    for p in sorted(down_stocks, key=lambda x: x['change_pct'])[:3]:
        emoji = "💀" if p['change_pct'] < -3 else "📉"
        message += f"{emoji} {p['name']}: {p['current']:.2f} ({p['change_pct']:+.2f}%)\n"

message += "\n---\n💃 金银 Planet · 资产增值部"
print(message)
EOF
)

# 输出消息（供 OpenClaw 读取并发送）
echo "MESSAGE_START"
echo "$MESSAGE"
echo "MESSAGE_END"

# 通过 OpenClaw message 工具发送飞书通知
openclaw message send --channel=feishu --target="ou_1a1f31c9c706ce055aa792b5870a00c5" --message="$MESSAGE"
