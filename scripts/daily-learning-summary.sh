#!/bin/bash
# 每天 17:30 执行，生成并发送学习日报

WORKSPACE="/home/admin/.openclaw/workspace"
CARDS_DIR="$WORKSPACE/memory/learning-cards"
TODAY=$(date +%Y-%m-%d)

# 查找今天的学习卡片
CARDS=$(ls -1 "$CARDS_DIR" 2>/dev/null | grep "^$TODAY" | grep -v TEMPLATE)

if [ -z "$CARDS" ]; then
    MESSAGE="💡 今日学习检查完成，今天没有新学习内容。继续保持！

---
💃 金银 Studio 学习秘书"
else
    # 统计卡片数量
    COUNT=$(echo "$CARDS" | wc -l)
    
    # 提取卡片主题
    TOPICS=""
    for card in $CARDS; do
        # 从文件名提取主题（去掉日期前缀）
        topic=$(echo "$card" | sed "s/^$TODAY-//" | sed 's/\.md$//')
        TOPICS="$TOPICS- $topic\n"
    done
    
    MESSAGE="📝 今日学习已自动记录：

$TOPICS
共 $COUNT 个学习主题。

卡片位置：\`memory/learning-cards/\`

---
💃 金银 Studio 学习秘书"
fi

# 发送飞书消息
openclaw message send --channel "feishu" --message "$MESSAGE"
