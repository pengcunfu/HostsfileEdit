#!/bin/bash

# ========================================
# 分支管理设置脚本 - Linux/Mac版本
# ========================================

echo "正在设置项目分支管理策略..."
echo

# 检查是否在Git仓库中
if ! git status >/dev/null 2>&1; then
    echo "错误：当前目录不是Git仓库！"
    echo "请先初始化Git仓库：git init"
    exit 1
fi

echo "[1/6] 创建开发分支..."
git checkout -b dev 2>/dev/null || git checkout dev
echo "开发分支创建/切换完成"

echo
echo "[2/6] 创建官网分支..."
git checkout -b gh-pages 2>/dev/null || git checkout gh-pages
echo "官网分支创建/切换完成"

echo
echo "[3/6] 回到主分支..."
git checkout main 2>/dev/null || git checkout master

echo
echo "[4/6] 从主分支移除web目录..."
if [ -d "web" ]; then
    git rm -r web --cached 2>/dev/null || true
    echo "web目录已从主分支移除"
else
    echo "web目录不存在，跳过移除步骤"
fi

echo
echo "[5/6] 更新主分支.gitignore..."
if ! grep -q "web/" .gitignore 2>/dev/null; then
    echo "web/" >> .gitignore
    echo "node_modules/" >> .gitignore
    echo "dist/" >> .gitignore
    echo "已更新.gitignore文件"
else
    echo ".gitignore已包含web目录忽略规则"
fi

echo
echo "[6/6] 提交更改..."
git add .gitignore
git commit -m "chore: 移除web目录，更新分支管理策略" 2>/dev/null || true

echo
echo "========================================"
echo "分支设置完成！"
echo "========================================"
echo
echo "分支说明："
echo "  main     - 主分支（桌面应用程序）"
echo "  dev      - 开发分支（日常开发工作）"
echo "  gh-pages - 官网分支（Vue.js网站）"
echo
echo "下一步操作："
echo "1. 运行 setup-web-branch.sh 设置官网分支"
echo "2. 推送所有分支到远程仓库"
echo
