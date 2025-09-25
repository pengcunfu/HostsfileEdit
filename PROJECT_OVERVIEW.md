# 📋 HostsfileEdit 项目概览

## 🎯 项目简介
HostsfileEdit 是一个专业的 Windows 系统 hosts 文件可视化编辑工具，包含桌面应用程序和配套官方网站。

## 📁 项目结构
```
HostsfileEdit/
├── .github/                    # GitHub配置
│   ├── workflows/             # 自动化工作流
│   │   ├── build-app.yml      # 应用程序构建
│   │   ├── deploy-web.yml     # 网站部署
│   │   └── test.yml           # 自动化测试
│   ├── ISSUE_TEMPLATE/        # Issue模板
│   └── PULL_REQUEST_TEMPLATE.md # PR模板
├── app/                       # 桌面应用程序
│   ├── main.py               # 主程序文件
│   ├── requirements.txt      # Python依赖
│   ├── run.bat              # 快速启动脚本
│   └── README.md            # 应用说明
├── web/                      # 官方网站
│   ├── src/                 # Vue.js源码
│   │   ├── components/      # Vue组件
│   │   ├── App.vue         # 主应用组件
│   │   ├── main.js         # 入口文件
│   │   └── style.css       # 全局样式
│   ├── public/             # 静态资源
│   ├── package.json        # 前端依赖
│   ├── vite.config.js      # Vite配置
│   └── README.md           # 网站说明
├── README.md               # 项目主文档
├── LICENSE                 # MIT许可证
├── CONTRIBUTING.md         # 贡献指南
├── DEPLOYMENT.md           # 部署指南
├── .gitignore             # Git忽略文件
├── deploy.bat             # Windows部署脚本
└── deploy.sh              # Linux/Mac部署脚本
```

## 🛠️ 技术栈

### 桌面应用程序
- **语言**: Python 3.7+
- **GUI框架**: PySide6 (Qt6)
- **打包工具**: PyInstaller
- **目标平台**: Windows 7/8/10/11

### 官方网站
- **框架**: Vue.js 3
- **构建工具**: Vite
- **路由**: Vue Router 4
- **部署**: GitHub Pages

### 开发工具
- **版本控制**: Git
- **CI/CD**: GitHub Actions
- **代码托管**: GitHub
- **文档**: Markdown

## 🚀 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/YOUR_USERNAME/HostsfileEdit.git
cd HostsfileEdit
```

### 2. 开发应用程序
```bash
cd app
pip install -r requirements.txt
python main.py  # 需要管理员权限
```

### 3. 开发网站
```bash
cd web
npm install
npm run dev
```

### 4. 部署到GitHub
```bash
# Windows
deploy.bat

# Linux/Mac
chmod +x deploy.sh
./deploy.sh
```

## 🔄 自动化流程

### 应用程序构建
- **触发**: 推送版本标签 (v*)
- **过程**: 
  1. 设置Python环境
  2. 安装依赖
  3. 使用PyInstaller打包
  4. 创建GitHub Release
  5. 上传可执行文件

### 网站部署
- **触发**: 推送到main分支
- **过程**:
  1. 设置Node.js环境
  2. 安装依赖
  3. 构建静态文件
  4. 部署到GitHub Pages

### 自动化测试
- **触发**: 推送或PR
- **过程**:
  1. 多版本Python测试
  2. 代码语法检查
  3. 网站构建测试

## 📦 发布流程

### 1. 开发完成
- 完成功能开发
- 通过所有测试
- 更新文档

### 2. 准备发布
```bash
# 更新版本信息
# 提交所有更改
git add .
git commit -m "Prepare for release v2.0.0"
git push origin main
```

### 3. 创建发布
```bash
# 创建版本标签
git tag -a v2.0.0 -m "Release version 2.0.0"
git push origin v2.0.0
```

### 4. 自动构建
- GitHub Actions自动构建
- 创建Release页面
- 上传可执行文件
- 更新网站

## 🔗 重要链接

### 开发相关
- **仓库**: https://github.com/YOUR_USERNAME/HostsfileEdit
- **Actions**: https://github.com/YOUR_USERNAME/HostsfileEdit/actions
- **Issues**: https://github.com/YOUR_USERNAME/HostsfileEdit/issues
- **Releases**: https://github.com/YOUR_USERNAME/HostsfileEdit/releases

### 用户相关
- **官网**: https://YOUR_USERNAME.github.io/HostsfileEdit/
- **下载**: https://github.com/YOUR_USERNAME/HostsfileEdit/releases/latest
- **文档**: https://github.com/YOUR_USERNAME/HostsfileEdit/wiki
- **支持**: https://github.com/YOUR_USERNAME/HostsfileEdit/discussions

## 🎯 项目目标

### 短期目标
- [x] 完成基础功能开发
- [x] 创建官方网站
- [x] 设置自动化部署
- [ ] 发布第一个正式版本
- [ ] 收集用户反馈

### 长期目标
- [ ] 支持更多操作系统
- [ ] 添加高级功能
- [ ] 构建用户社区
- [ ] 持续优化体验

## 📊 项目统计

### 代码统计
- **Python代码**: ~450行
- **Vue.js代码**: ~1800行
- **文档**: ~2000行
- **配置文件**: ~200行

### 功能统计
- **核心功能**: 6个
- **页面数量**: 3个
- **自动化工作流**: 3个
- **支持平台**: Windows全系列

## 🤝 贡献方式

1. **报告问题**: 使用Issue模板
2. **功能建议**: 提交Feature Request
3. **代码贡献**: 提交Pull Request
4. **文档改进**: 更新文档内容
5. **测试反馈**: 提供使用体验

## 📞 联系方式

- **开发者**: [Your Name]
- **邮箱**: your.email@example.com
- **GitHub**: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)

---

**最后更新**: 2025年1月
**项目状态**: 开发中
**许可证**: MIT License
