@echo off
chcp 65001 >nul
echo.
echo 🚀 HostsfileEdit 版本发布脚本
echo ================================
echo.

:: 检查Git状态
echo 📋 检查Git仓库状态...
git status --porcelain > temp_status.txt
set /p git_status=<temp_status.txt
del temp_status.txt

if not "%git_status%"=="" (
    echo ⚠️  警告：存在未提交的更改！
    echo 请先提交所有更改后再发布版本。
    echo.
    git status
    echo.
    pause
    exit /b 1
)

echo ✅ Git仓库状态干净
echo.

:: 获取版本号
set /p version="🏷️  请输入版本号 (例如: v2.0.0): "
if "%version%"=="" (
    echo ❌ 版本号不能为空！
    pause
    exit /b 1
)

:: 验证版本号格式
echo %version% | findstr /r "^v[0-9]\+\.[0-9]\+\.[0-9]\+$" >nul
if errorlevel 1 (
    echo ❌ 版本号格式错误！请使用格式: v2.0.0
    pause
    exit /b 1
)

echo.
echo 📝 准备发布版本: %version%
echo.

:: 获取发布说明
set /p release_notes="📋 请输入发布说明 (可选): "
if "%release_notes%"=="" set release_notes=Release %version%

echo.
echo 🔍 发布信息确认:
echo ================
echo 版本号: %version%
echo 说明: %release_notes%
echo.
set /p confirm="确认发布吗？(y/N): "
if /i not "%confirm%"=="y" (
    echo ❌ 发布已取消
    pause
    exit /b 0
)

echo.
echo 🏷️  创建Git标签...
git tag -a %version% -m "%release_notes%"
if errorlevel 1 (
    echo ❌ 创建标签失败！
    pause
    exit /b 1
)

echo ✅ 标签创建成功
echo.

echo 🌐 推送标签到GitHub...
git push origin %version%
if errorlevel 1 (
    echo ❌ 推送标签失败！
    echo 正在删除本地标签...
    git tag -d %version%
    pause
    exit /b 1
)

echo ✅ 标签推送成功
echo.

echo 🎉 版本发布完成！
echo ==================
echo.
echo 📊 您可以在以下位置查看发布状态:
echo.
echo 🔗 GitHub Actions (构建状态):
echo    https://github.com/YOUR_USERNAME/HostsfileEdit/actions
echo.
echo 🔗 Releases页面 (发布页面):
echo    https://github.com/YOUR_USERNAME/HostsfileEdit/releases
echo.
echo 🔗 官方网站:
echo    https://YOUR_USERNAME.github.io/HostsfileEdit/
echo.
echo ⏱️  GitHub Actions 需要几分钟时间来构建可执行文件
echo 📦 构建完成后，用户就可以下载 %version% 版本了！
echo.
echo 📋 接下来您可以:
echo 1. 查看GitHub Actions构建日志
echo 2. 测试下载的可执行文件
echo 3. 更新发布说明（如需要）
echo 4. 在社交媒体宣传新版本
echo.
pause
