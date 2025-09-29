@echo off
chcp 65001 >nul
echo.
echo 🌳 创建开发分支脚本
echo ===================
echo.

:: 检查Git状态
echo 📋 检查Git仓库状态...
git status --porcelain > temp_status.txt
set /p git_status=<temp_status.txt
del temp_status.txt

if not "%git_status%"=="" (
    echo ⚠️  警告：存在未提交的更改！
    echo 请先提交所有更改后再创建分支。
    echo.
    git status
    echo.
    pause
    exit /b 1
)

echo ✅ Git仓库状态干净
echo.

:: 确保在main分支
echo 🔄 切换到main分支...
git checkout main
if errorlevel 1 (
    echo ❌ 切换到main分支失败！
    pause
    exit /b 1
)

:: 拉取最新代码
echo 📥 拉取最新代码...
git pull origin main
if errorlevel 1 (
    echo ❌ 拉取最新代码失败！
    pause
    exit /b 1
)

:: 检查是否已存在dev分支
git show-ref --verify --quiet refs/heads/dev
if not errorlevel 1 (
    echo ✅ dev分支已存在，切换到dev分支...
    git checkout dev
    git pull origin dev
    echo.
    echo 🎉 已切换到dev分支并更新到最新代码！
    goto :end
)

:: 创建dev分支
echo 🆕 创建dev分支...
git checkout -b dev
if errorlevel 1 (
    echo ❌ 创建dev分支失败！
    pause
    exit /b 1
)

echo ✅ dev分支创建成功
echo.

:: 推送dev分支到远程
echo 🌐 推送dev分支到远程仓库...
git push origin dev
if errorlevel 1 (
    echo ❌ 推送dev分支失败！
    pause
    exit /b 1
)

:: 设置上游分支
echo 🔗 设置上游分支...
git branch --set-upstream-to=origin/dev dev
if errorlevel 1 (
    echo ⚠️  设置上游分支失败，但这不影响使用
)

echo.
echo 🎉 开发环境设置完成！
echo =====================
echo.
echo 📋 接下来您可以:
echo 1. 开始在dev分支上进行开发
echo 2. 创建功能分支: git checkout -b feature/your-feature
echo 3. 查看开发指南: 阅读 DEV_SETUP.md
echo 4. 查看分支策略: 阅读 BRANCHING_STRATEGY.md
echo.
echo 🔗 有用的命令:
echo git branch -a           # 查看所有分支
echo git checkout dev        # 切换到dev分支
echo git pull origin dev     # 拉取dev分支最新代码
echo.

:end
echo 当前分支: 
git branch --show-current
echo.
pause
