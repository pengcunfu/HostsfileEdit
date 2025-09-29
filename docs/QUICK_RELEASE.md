# 🚀 快速发布指南

## 📋 发布前准备

1. **替换用户名**
   - 将所有文件中的 `YOUR_USERNAME` 替换为您的GitHub用户名
   - 主要文件：README.md, DEPLOYMENT.md, release.bat, release.sh

2. **创建GitHub仓库**
   - 在GitHub上创建名为 `HostsfileEdit` 的新仓库
   - 选择Public（公开）
   - 不要初始化README、.gitignore或LICENSE（我们已经有了）

## 🎯 方式一：使用发布脚本（推荐）

### Windows用户
1. 双击运行 `release.bat`
2. 或在命令行中运行：
   ```cmd
   release.bat
   ```

### Linux/Mac用户
1. 给脚本添加执行权限：
   ```bash
   chmod +x release.sh
   ```
2. 运行脚本：
   ```bash
   ./release.sh
   ```

## 🔧 方式二：手动发布

### 1. 初始化Git仓库（如果还未初始化）
```bash
git init
git add .
git commit -m "Initial commit: HostsfileEdit v2.0.0"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/HostsfileEdit.git
git push -u origin main
```

### 2. 创建并推送版本标签
```bash
git tag -a v2.0.0 -m "Release version 2.0.0 - First stable release"
git push origin v2.0.0
```

## 📊 发布后检查

### 1. GitHub Actions状态
访问：`https://github.com/YOUR_USERNAME/HostsfileEdit/actions`
- 检查构建是否成功
- 等待可执行文件生成（约5-10分钟）

### 2. Release页面
访问：`https://github.com/YOUR_USERNAME/HostsfileEdit/releases`
- 确认Release已创建
- 检查可执行文件是否已上传

### 3. 网站部署
访问：`https://YOUR_USERNAME.github.io/HostsfileEdit/`
- 确认网站正常显示
- 检查所有页面功能

## 🎉 发布完成！

发布成功后，用户就可以：
- 🌐 访问官网了解产品
- 📥 下载最新版本的可执行文件
- 🐛 在Issues中反馈问题
- 💬 在Discussions中讨论

## 🔗 重要链接模板

发布后，这些链接将变为有效：
- **官网**: https://YOUR_USERNAME.github.io/HostsfileEdit/
- **下载**: https://github.com/YOUR_USERNAME/HostsfileEdit/releases/latest
- **源码**: https://github.com/YOUR_USERNAME/HostsfileEdit
- **问题**: https://github.com/YOUR_USERNAME/HostsfileEdit/issues
- **讨论**: https://github.com/YOUR_USERNAME/HostsfileEdit/discussions

## ⚠️ 常见问题

### Q: 构建失败怎么办？
A: 
1. 检查GitHub Actions日志
2. 确认Python依赖正确
3. 删除失败标签：`git tag -d v2.0.0`
4. 修复问题后重新发布

### Q: 网站部署失败？
A:
1. 检查GitHub Pages设置
2. 确认Actions权限正确
3. 手动触发部署工作流

### Q: 可执行文件被杀毒软件误报？
A:
1. 这是正常现象，PyInstaller打包的文件常被误报
2. 在Release说明中提醒用户添加信任
3. 考虑申请代码签名证书（长期方案）

---

**准备好了吗？开始发布您的第一个版本吧！** 🚀
