@echo off
echo 🚀 HostsfileEdit 部署脚本
echo ========================

echo 📋 检查Git状态...
git status

echo.
echo 📦 添加所有文件到Git...
git add .

echo.
set /p commit_message="💬 请输入提交信息: "
if "%commit_message%"=="" set commit_message=Update project files

echo.
echo 📝 提交更改...
git commit -m "%commit_message%"

echo.
echo 🌐 推送到GitHub...
git push origin main

echo.
echo ✅ 部署完成！
echo.
echo 📊 您可以在以下位置查看部署状态:
echo - GitHub Actions: https://github.com/YOUR_USERNAME/HostsfileEdit/actions
echo - 网站地址: https://YOUR_USERNAME.github.io/HostsfileEdit/
echo.
echo 🏷️ 如需发布新版本，请运行:
echo git tag -a v2.0.0 -m "Release version 2.0.0"
echo git push origin v2.0.0
echo.
pause
