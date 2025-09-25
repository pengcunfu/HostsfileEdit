# 📋 变更日志

所有值得注意的项目更改都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
本项目遵循 [语义化版本控制](https://semver.org/lang/zh-CN/)。

## [v2.0.0] - 2025-01-25

### 🎉 首次发布
这是 HostsfileEdit 项目的首次正式发布，包含完整的桌面应用程序和官方网站。

### ✨ 新增功能

#### 桌面应用程序
- **可视化编辑界面** - 直观的GUI界面，告别命令行操作
- **双重编辑模式** - 支持文本编辑和按条编辑两种模式
- **智能权限检测** - 自动检测管理员权限并提供友好提示
- **数据验证机制** - IP地址格式验证，防止错误输入
- **便民工具集成**
  - 一键定位hosts文件位置
  - 快速在记事本中打开
  - 直接访问环境变量设置
- **安全保护机制**
  - 自动备份原始文件
  - 操作前确认提示
  - 异常恢复处理

#### 官方网站
- **现代化响应式设计** - 适配所有设备尺寸
- **完整的产品展示**
  - 功能特性详细介绍
  - 使用场景案例展示
  - 技术架构说明
- **用户友好的下载页面**
  - 多种下载选项
  - 详细安装指南
  - 系统要求说明
  - 常见问题解答
- **Vue.js 3 + Vite** - 现代前端技术栈

### 🛠️ 技术特性

#### 核心技术
- **PySide6** - 基于Qt6的现代GUI框架
- **Python 3.7+** - 支持多个Python版本
- **跨Windows版本** - 兼容Windows 7/8/10/11
- **PyInstaller打包** - 生成独立可执行文件

#### 开发工具链
- **GitHub Actions** - 完整的CI/CD流程
- **自动化构建** - 版本标签触发自动构建
- **自动化部署** - 网站自动部署到GitHub Pages
- **代码质量检查** - 多版本Python测试

### 📦 发布内容

#### 可执行文件
- `HostsFileEditor.exe` - Windows独立可执行文件
- 文件大小：约25MB
- 无需安装Python环境
- 支持Windows 7及以上版本

#### 源代码
- 完整的Python源码
- Vue.js网站源码
- 详细的文档和说明
- GitHub Actions配置

### 📚 文档

#### 用户文档
- **README.md** - 项目总体说明
- **DEPLOYMENT.md** - 部署指南
- **CONTRIBUTING.md** - 贡献指南
- **PROJECT_OVERVIEW.md** - 项目概览

#### 开发文档
- 应用程序开发说明
- 网站开发指南
- API参考文档
- 故障排除指南

### 🎯 使用场景

#### 开发者
```hosts
127.0.0.1 dev.myproject.com
127.0.0.1 api.local
127.0.0.1 admin.dashboard.local
```

#### 网络管理
```hosts
192.168.1.100 fileserver
192.168.1.200 database
192.168.1.50  printer
```

#### 广告屏蔽
```hosts
0.0.0.0 ads.example.com
0.0.0.0 tracker.analytics.com
0.0.0.0 popup.ads.com
```

### ⚠️ 重要说明

#### 系统要求
- **操作系统**: Windows 7 SP1 或更高版本
- **权限**: 必须以管理员身份运行
- **内存**: 至少512MB RAM
- **磁盘**: 50MB可用空间

#### 安全提醒
- 首次运行可能被杀毒软件误报，请添加信任
- 建议在使用前备份原始hosts文件
- 修改后需要刷新DNS缓存才能生效

#### 使用建议
- 定期备份hosts文件
- 谨慎添加不明来源的域名映射
- 及时清理不需要的条目

### 🔗 相关链接
- **官方网站**: https://YOUR_USERNAME.github.io/HostsfileEdit/
- **GitHub仓库**: https://github.com/YOUR_USERNAME/HostsfileEdit
- **下载地址**: https://github.com/YOUR_USERNAME/HostsfileEdit/releases/tag/v2.0.0
- **问题反馈**: https://github.com/YOUR_USERNAME/HostsfileEdit/issues
- **使用讨论**: https://github.com/YOUR_USERNAME/HostsfileEdit/discussions

### 🙏 致谢
感谢所有测试用户和贡献者的支持！

---

## [计划中的版本]

### v2.1.0 (计划中)
- [ ] 添加hosts文件语法高亮
- [ ] 支持批量导入/导出
- [ ] 添加条目分类功能
- [ ] 优化大文件处理性能

### v2.2.0 (计划中)
- [ ] 添加主题切换功能
- [ ] 支持自定义快捷键
- [ ] 添加操作历史记录
- [ ] 集成DNS查询工具

---

**说明**: 
- 🎉 表示主要版本发布
- ✨ 表示新增功能
- 🐛 表示Bug修复
- 🛠️ 表示技术改进
- 📚 表示文档更新
- ⚠️ 表示重要提醒
