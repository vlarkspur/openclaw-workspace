#!/bin/bash
# rebuild_team.sh - 一键重建 Charlie 的投资团队
# 用法：bash rebuild_team.sh

echo "💃 金银：开始重建 Charlie 的投资团队..."
echo "============================================"

# 检查 OpenClaw 是否运行
if ! pgrep -f "openclaw" > /dev/null; then
    echo "❌ OpenClaw 未运行，请先启动 OpenClaw"
    exit 1
fi

echo "✅ OpenClaw 运行中"
echo ""

# 创建工作目录
WORKSPACE="/home/admin/.openclaw/workspace"
mkdir -p "$WORKSPACE/templates"
mkdir -p "$WORKSPACE/stock_monitoring"
mkdir -p "$WORKSPACE/health"
mkdir -p "$WORKSPACE/.learnings"

echo "📁 工作目录已准备"
echo ""

# 检查核心文件是否存在
echo "🔍 检查核心文件..."

if [ ! -f "$WORKSPACE/SOUL.md" ]; then
    echo "⚠️  SOUL.md 缺失 - 需要手动重建"
fi

if [ ! -f "$WORKSPACE/USER.md" ]; then
    echo "⚠️  USER.md 缺失 - 需要手动重建"
fi

if [ ! -f "$WORKSPACE/MEMORY.md" ]; then
    echo "⚠️  MEMORY.md 缺失 - 需要手动重建"
fi

echo ""
echo "============================================"
echo "📋 团队重建说明"
echo "============================================"
echo ""
echo "由于子代理（subagent）是运行时创建的，无法通过脚本自动重建。"
echo ""
echo "请按以下步骤手动重建团队："
echo ""
echo "1️⃣  在 OpenClaw 中发送以下消息："
echo ""
echo "   '重建 Charlie 团队'"
echo ""
echo "2️⃣  金银会自动执行以下 spawn 命令："
echo ""
echo "   - Charlie (投资风控经理)"
echo "   - 投资监控小弟"
echo "   - 风控监控小弟"
echo "   - 行为心理学小弟"
echo "   - 估值分析小弟"
echo "   - 公司基本面分析小弟"
echo "   - 宏观经济小弟"
echo "   - 新闻舆情小弟"
echo ""
echo "3️⃣  等待所有小弟交活（约 5-10 分钟）"
echo ""
echo "============================================"
echo "📞 如需帮助，联系金银（大管家）"
echo "============================================"
echo ""
echo "💃 金银：重建脚本执行完毕！"
