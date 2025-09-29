#!/bin/bash

# ========================================
# 官网分支设置脚本 - Linux/Mac版本
# ========================================

echo "正在设置官网分支..."
echo

# 检查是否在Git仓库中
if ! git status >/dev/null 2>&1; then
    echo "错误：当前目录不是Git仓库！"
    exit 1
fi

echo "[1/5] 切换到官网分支..."
if ! git checkout gh-pages; then
    echo "错误：官网分支不存在，请先运行 setup-branches.sh"
    exit 1
fi

echo
echo "[2/5] 清理官网分支（保留web目录）..."
# 删除除了web目录和.git之外的所有文件和目录
find . -maxdepth 1 -not -name '.' -not -name '..' -not -name '.git' -not -name 'web' -exec rm -rf {} + 2>/dev/null || true

echo
echo "[3/5] 将web目录内容移到根目录..."
if [ -d "web" ]; then
    cp -r web/* . 2>/dev/null || true
    cp -r web/.* . 2>/dev/null || true  # 复制隐藏文件
    rm -rf web
    echo "web目录内容已移动到根目录"
else
    echo "警告：web目录不存在！"
fi

echo
echo "[4/5] 创建官网分支专用文件..."

# 创建GitHub Pages配置
touch .nojekyll

# 创建官网分支README
cat > README.md << 'EOF'
# Hosts文件编辑工具 - 官方网站

这是Hosts文件编辑工具的官方网站分支，专门用于GitHub Pages部署。

## 自动部署

本分支通过GitHub Actions自动部署到GitHub Pages。

## 开发流程

1. 在主分支的web目录中进行开发
2. 通过GitHub Actions自动构建并部署到此分支
3. 网站自动更新

## 访问地址

https://YOUR_USERNAME.github.io/HostsfileEdit/
EOF

echo "已创建官网分支专用文件"

echo
echo "[5/5] 提交官网分支更改..."
git add .
git commit -m "feat: 设置官网分支，准备GitHub Pages部署"

echo
echo "========================================"
echo "官网分支设置完成！"
echo "========================================"
echo
echo "当前分支：gh-pages"
echo "用途：GitHub Pages网站部署"
echo
echo "建议操作："
echo "1. 推送到远程仓库：git push origin gh-pages"
echo "2. 在GitHub仓库设置中启用GitHub Pages"
echo "3. 设置部署源为gh-pages分支"
echo
