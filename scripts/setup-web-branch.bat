@echo off
REM ========================================
REM 官网分支设置脚本 - Windows版本
REM ========================================

echo 正在设置官网分支...
echo.

REM 检查是否在Git仓库中
git status >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误：当前目录不是Git仓库！
    pause
    exit /b 1
)

echo [1/5] 切换到官网分支...
git checkout gh-pages
if %errorlevel% neq 0 (
    echo 错误：官网分支不存在，请先运行 setup-branches.bat
    pause
    exit /b 1
)

echo.
echo [2/5] 清理官网分支（保留web目录）...
REM 删除除了web目录之外的所有文件
for %%f in (*) do (
    if /I not "%%f"=="web" (
        if exist "%%f" (
            if exist "%%f\*" (
                rmdir /s /q "%%f" 2>nul
            ) else (
                del /q "%%f" 2>nul
            )
        )
    )
)

echo.
echo [3/5] 将web目录内容移到根目录...
if exist web (
    xcopy web\* . /E /Y /Q >nul 2>&1
    rmdir /s /q web >nul 2>&1
    echo web目录内容已移动到根目录
) else (
    echo 警告：web目录不存在！
)

echo.
echo [4/5] 创建官网分支专用文件...

REM 创建GitHub Pages配置
echo. > .nojekyll

REM 创建官网分支README
(
echo # Hosts文件编辑工具 - 官方网站
echo.
echo 这是Hosts文件编辑工具的官方网站分支，专门用于GitHub Pages部署。
echo.
echo ## 自动部署
echo.
echo 本分支通过GitHub Actions自动部署到GitHub Pages。
echo.
echo ## 开发流程
echo.
echo 1. 在主分支的web目录中进行开发
echo 2. 通过GitHub Actions自动构建并部署到此分支
echo 3. 网站自动更新
echo.
echo ## 访问地址
echo.
echo https://YOUR_USERNAME.github.io/HostsfileEdit/
) > README.md

echo 已创建官网分支专用文件

echo.
echo [5/5] 提交官网分支更改...
git add .
git commit -m "feat: 设置官网分支，准备GitHub Pages部署"

echo.
echo ========================================
echo 官网分支设置完成！
echo ========================================
echo.
echo 当前分支：gh-pages
echo 用途：GitHub Pages网站部署
echo.
echo 建议操作：
echo 1. 推送到远程仓库：git push origin gh-pages
echo 2. 在GitHub仓库设置中启用GitHub Pages
echo 3. 设置部署源为gh-pages分支
echo.
pause
