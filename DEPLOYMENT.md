# 🚀 部署指南

本文档说明如何部署 HostsfileEdit 项目到 GitHub，包括自动化构建和网站部署。

## 📋 前置要求

- GitHub 账户
- Git 已安装
- Node.js 18+ (用于网站构建)
- Python 3.7+ (用于应用程序构建)

## 🔧 GitHub 仓库设置

### 1. 创建仓库
```bash
# 在GitHub上创建新仓库 "HostsfileEdit"
# 然后克隆到本地
git clone https://github.com/yourusername/HostsfileEdit.git
cd HostsfileEdit
```

### 2. 推送代码
```bash
# 添加所有文件
git add .
git commit -m "Initial commit: HostsfileEdit project"
git push origin main
```

## 🌐 GitHub Pages 设置

### 1. 启用 GitHub Pages
1. 进入仓库设置页面
2. 找到 "Pages" 部分
3. Source 选择 "GitHub Actions"
4. 保存设置

### 2. 配置自定义域名（可选）
1. 在 `web/public/` 目录下创建 `CNAME` 文件
2. 写入您的域名，如：`hostsfileeditor.com`
3. 在域名DNS设置中添加CNAME记录指向 `yourusername.github.io`

## ⚙️ GitHub Actions 工作流

项目包含三个主要工作流：

### 1. 应用程序构建 (build-app.yml)
- **触发条件**: 推送标签 (v*) 或手动触发
- **功能**: 构建Windows可执行文件并创建Release
- **输出**: `HostsFileEditor.exe`

### 2. 网站部署 (deploy-web.yml)
- **触发条件**: 推送到main分支且web目录有更改
- **功能**: 构建Vue.js网站并部署到GitHub Pages
- **输出**: 静态网站文件

### 3. 测试 (test.yml)
- **触发条件**: 推送或PR到main分支
- **功能**: 运行代码测试和构建验证
- **输出**: 测试结果

## 📦 发布新版本

### 1. 准备发布
```bash
# 确保所有更改已提交
git add .
git commit -m "Prepare for release v2.0.0"
git push origin main
```

### 2. 创建标签
```bash
# 创建版本标签
git tag -a v2.0.0 -m "Release version 2.0.0"
git push origin v2.0.0
```

### 3. 自动构建
- GitHub Actions 会自动构建应用程序
- 创建 GitHub Release
- 上传可执行文件

### 4. 手动发布（可选）
如果需要手动触发构建：
1. 进入 Actions 页面
2. 选择 "Build Application" 工作流
3. 点击 "Run workflow"

## 🔍 监控部署状态

### 检查构建状态
1. 进入仓库的 "Actions" 页面
2. 查看各个工作流的运行状态
3. 点击具体运行查看详细日志

### 常见问题排查
- **构建失败**: 检查依赖是否正确安装
- **部署失败**: 确认GitHub Pages权限设置
- **网站404**: 检查路由配置和base路径

## 📊 网站统计（可选）

### 添加 Google Analytics
1. 在 `web/index.html` 中添加GA代码
2. 重新部署网站

### 添加访问统计
可以使用以下服务：
- Google Analytics
- GitHub Pages自带的访问统计
- 第三方统计服务

## 🔒 安全设置

### 1. 保护主分支
1. 进入仓库设置
2. 找到 "Branches" 部分
3. 添加分支保护规则：
   - 要求PR审查
   - 要求状态检查通过
   - 限制推送权限

### 2. 管理访问权限
- 设置协作者权限
- 配置团队访问级别
- 启用两因素认证

## 🔄 持续集成最佳实践

### 1. 代码质量
- 启用代码检查
- 设置测试覆盖率要求
- 使用预提交钩子

### 2. 自动化测试
- 单元测试
- 集成测试
- UI测试

### 3. 部署策略
- 分阶段部署
- 回滚机制
- 监控和告警

## 📈 性能优化

### 1. 构建优化
- 缓存依赖
- 并行构建
- 增量构建

### 2. 网站优化
- 资源压缩
- CDN加速
- 图片优化

## 🆘 故障排除

### 常见错误及解决方案

#### 构建失败
```bash
# 检查Python版本
python --version

# 重新安装依赖
pip install -r app/requirements.txt
```

#### 部署失败
```bash
# 检查Node.js版本
node --version

# 清理并重新安装
cd web
rm -rf node_modules
npm install
```

#### 权限问题
- 确保GitHub Actions有足够权限
- 检查Token配置
- 验证分支保护设置

## 📞 获取支持

如果遇到部署问题：
1. 查看GitHub Actions日志
2. 检查相关文档
3. 在Issues中寻求帮助
4. 联系维护者

---

**部署完成后，您的项目将在以下地址可用：**
- 🌐 **网站**: https://yourusername.github.io/HostsfileEdit/
- 📥 **下载**: https://github.com/yourusername/HostsfileEdit/releases/
