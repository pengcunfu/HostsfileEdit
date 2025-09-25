#!/bin/bash

echo ""
echo "🚀 HostsfileEdit 版本发布脚本"
echo "================================"
echo ""

# 检查Git状态
echo "📋 检查Git仓库状态..."
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  警告：存在未提交的更改！"
    echo "请先提交所有更改后再发布版本。"
    echo ""
    git status
    echo ""
    exit 1
fi

echo "✅ Git仓库状态干净"
echo ""

# 获取版本号
read -p "🏷️  请输入版本号 (例如: v2.0.0): " version
if [ -z "$version" ]; then
    echo "❌ 版本号不能为空！"
    exit 1
fi

# 验证版本号格式
if ! [[ $version =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "❌ 版本号格式错误！请使用格式: v2.0.0"
    exit 1
fi

echo ""
echo "📝 准备发布版本: $version"
echo ""

# 获取发布说明
read -p "📋 请输入发布说明 (可选): " release_notes
if [ -z "$release_notes" ]; then
    release_notes="Release $version"
fi

echo ""
echo "🔍 发布信息确认:"
echo "================"
echo "版本号: $version"
echo "说明: $release_notes"
echo ""
read -p "确认发布吗？(y/N): " confirm
if [[ ! $confirm =~ ^[Yy]$ ]]; then
    echo "❌ 发布已取消"
    exit 0
fi

echo ""
echo "🏷️  创建Git标签..."
if ! git tag -a "$version" -m "$release_notes"; then
    echo "❌ 创建标签失败！"
    exit 1
fi

echo "✅ 标签创建成功"
echo ""

echo "🌐 推送标签到GitHub..."
if ! git push origin "$version"; then
    echo "❌ 推送标签失败！"
    echo "正在删除本地标签..."
    git tag -d "$version"
    exit 1
fi

echo "✅ 标签推送成功"
echo ""

echo "🎉 版本发布完成！"
echo "=================="
echo ""
echo "📊 您可以在以下位置查看发布状态:"
echo ""
echo "🔗 GitHub Actions (构建状态):"
echo "   https://github.com/YOUR_USERNAME/HostsfileEdit/actions"
echo ""
echo "🔗 Releases页面 (发布页面):"
echo "   https://github.com/YOUR_USERNAME/HostsfileEdit/releases"
echo ""
echo "🔗 官方网站:"
echo "   https://YOUR_USERNAME.github.io/HostsfileEdit/"
echo ""
echo "⏱️  GitHub Actions 需要几分钟时间来构建可执行文件"
echo "📦 构建完成后，用户就可以下载 $version 版本了！"
echo ""
echo "📋 接下来您可以:"
echo "1. 查看GitHub Actions构建日志"
echo "2. 测试下载的可执行文件"
echo "3. 更新发布说明（如需要）"
echo "4. 在社交媒体宣传新版本"
echo ""
