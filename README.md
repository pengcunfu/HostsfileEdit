# HostsfileEdit - Windows Hosts文件编辑工具

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows/)
[![GUI Framework](https://img.shields.io/badge/GUI-PySide6-green.svg)](https://www.qt.io/qt-for-python)
[![Version](https://img.shields.io/badge/version-v2.0.0-brightgreen.svg)](https://github.com/YOUR_USERNAME/HostsfileEdit/releases)

> **一句话介绍**：专业的Windows系统hosts文件可视化编辑工具，基于PySide6开发，提供直观的图形界面和强大的编辑功能。

## 项目简介

HostsfileEdit 是一个现代化的Windows hosts文件管理工具，旨在为用户提供简单、安全、高效的hosts文件编辑体验。无论您是开发者、系统管理员还是普通用户，都能通过直观的图形界面轻松管理域名映射。

### 核心特色

- **现代化界面** - 基于PySide6的精美GUI设计
- **双重编辑模式** - 文本编辑与按条编辑自由切换
- **智能安全保护** - 权限检测、数据验证、自动备份
- **便民工具集** - 文件定位、记事本集成、环境变量快捷访问
- **完整生态** - 桌面应用 + 官方网站 + 详细文档

## 快速开始

### 系统要求

| 项目 | 要求 |
|------|------|
| 操作系统 | Windows 7 SP1 / 8 / 10 / 11 |
| Python版本 | Python 3.7+ （源码运行） |
| 内存 | 最少 512 MB RAM |
| 磁盘空间 | 50 MB 可用空间 |
| 权限 | **管理员权限（必需）** |

### 安装运行

#### 方式一：下载可执行文件（推荐）
1. 访问 [Releases页面](../../releases) 下载最新版本
2. 右键可执行文件，选择"**以管理员身份运行**"
3. 享受便捷的hosts文件编辑体验！

#### 方式二：从源码运行
```bash
# 克隆项目
git clone https://github.com/YOUR_USERNAME/HostsfileEdit.git
cd HostsfileEdit

# 安装依赖
pip install -r requirements.txt

# 以管理员身份运行
python main.py
```

## 功能特性

### 主界面功能

#### 双重编辑模式
- **文本编辑模式**
  - 完整的hosts文件内容展示
  - 支持直接编辑、保留注释和空行
  - 语法高亮，便于阅读和编辑
  - 一键重新加载和保存功能

- **按条编辑模式**
  - 列表形式显示所有有效hosts条目
  - 支持添加、修改、删除单个条目
  - IP地址格式自动验证
  - 操作简单，适合精确管理

#### 便民工具栏
- **定位到文件** - 在Windows资源管理器中快速定位hosts文件
- **在记事本中打开** - 使用系统记事本进行外部编辑
- **环境变量** - 快速访问Windows系统环境变量设置

### 安全特性

#### 智能权限管理
- 启动时自动检测管理员权限
- 友好的权限提示和错误处理
- 安全的文件读写操作

#### 数据保护机制
- 操作前自动备份原始文件
- IP地址格式严格验证
- 异常情况自动恢复
- 保留文件注释和格式

### 用户体验

#### 现代化界面设计
- 基于PySide6的原生Windows界面
- 响应式布局，适配不同屏幕尺寸
- 直观的操作流程和反馈机制
- 支持标签页切换，提高工作效率

#### 智能数据同步
- 两种编辑模式间数据实时同步
- 自动解析和更新hosts条目
- 保持文件完整性和一致性

## 使用指南

### 基本操作流程

1. **启动应用程序**
   ```
   重要：必须以管理员身份运行
   ```

2. **查看当前hosts配置**
   - 程序启动后自动加载系统hosts文件
   - 在"按条编辑"标签页查看所有有效条目
   - 在"文本编辑"标签页查看完整文件内容

3. **添加新的hosts条目**
   - 切换到"按条编辑"模式
   - 点击"添加"按钮
   - 输入IP地址和域名
   - 点击"确定"自动保存

4. **修改现有条目**
   - 在列表中选择要修改的条目
   - 点击"修改"按钮
   - 编辑IP地址或域名
   - 确认保存更改

5. **删除不需要的条目**
   - 选择要删除的条目
   - 点击"删除"按钮
   - 确认删除操作

### 实用场景示例

#### 本地开发环境
```hosts
# 开发环境域名映射
127.0.0.1    dev.myproject.com
127.0.0.1    api.myproject.local
127.0.0.1    admin.dashboard.local
```

#### 企业内网配置
```hosts
# 内网服务器访问
192.168.1.100    fileserver
192.168.1.200    database
192.168.1.50     printer.office
```

#### 广告屏蔽
```hosts
# 屏蔽广告域名
0.0.0.0    ads.example.com
0.0.0.0    tracker.analytics.com
0.0.0.0    popup.unwanted.com
```

#### 系统维护
```hosts
# 临时重定向
127.0.0.1    maintenance.site.com
192.168.1.10    backup.internal.com
```

## 项目架构

### 目录结构
```
HostsfileEdit/
├── main.py                 # 主程序文件（447行代码）
├── requirements.txt        # Python依赖（仅需PySide6）
├── README.md              # 项目文档
├── docs/                  # 完整项目文档
│   ├── PROJECT_OVERVIEW.md    # 项目概览
│   ├── CHANGELOG.md          # 版本更新日志
│   ├── CONTRIBUTING.md       # 贡献指南
│   ├── DEPLOYMENT.md         # 部署说明
│   ├── DEV_SETUP.md         # 开发环境搭建
│   ├── RELEASE_CHECKLIST.md # 发布检查清单
│   ├── QUICK_RELEASE.md     # 快速发布指南
│   ├── BRANCHING_STRATEGY.md # 分支策略
│   └── VERSION              # 当前版本号
├── scripts/               # 自动化脚本
│   ├── deploy.bat/.sh        # 部署脚本
│   ├── release.bat/.sh       # 发布脚本
│   └── create-dev-branch.*   # 开发分支创建
└── web/                   # 官方网站（Vue.js 3）
    ├── src/components/        # Vue组件
    │   ├── Home.vue              # 首页
    │   ├── Features.vue          # 功能介绍
    │   └── Download.vue          # 下载页面
    ├── public/               # 静态资源
    ├── package.json          # 前端依赖
    └── vite.config.js        # 构建配置
```

### 技术栈

#### 桌面应用程序
- **GUI框架**: PySide6 (Qt6 for Python)
- **编程语言**: Python 3.7+
- **架构模式**: MVC模式，单文件集成设计
- **核心类结构**:
  - `HandleMain` - 主窗口控制器（UI + 业务逻辑）
  - `HandleNewValue` - 条目编辑对话框
  - `WindowHandle` - 应用程序入口和窗口管理

#### 官方网站
- **前端框架**: Vue.js 3 + Composition API
- **构建工具**: Vite 4.4.5（快速构建和热重载）
- **路由管理**: Vue Router 4.2.4
- **样式方案**: 原生CSS + 响应式设计

#### 开发工具
- **版本控制**: Git
- **CI/CD**: GitHub Actions
- **文档格式**: Markdown
- **打包工具**: PyInstaller（计划中）

### 核心功能实现

#### 文件操作模块
- UTF-8编码支持，兼容中文和特殊字符
- 正则表达式解析hosts条目
- 保留原始文件格式和注释
- 异常安全的文件读写操作

#### UI交互模块
- Qt信号槽机制实现事件处理
- 标签页切换和数据同步
- 实时数据验证和用户反馈
- 现代化的对话框和提示系统

#### 系统集成模块
- Windows API调用（subprocess）
- 管理员权限检测和提升
- 系统工具集成（资源管理器、记事本、环境变量）

## 安全与稳定性

### 权限管理
- 启动时检测管理员权限状态
- 友好的权限不足提示信息
- 安全的系统调用和异常处理

### 数据安全
- 操作前自动创建备份文件
- 严格的IP地址格式验证
- 文件完整性保护机制
- 异常情况下的数据恢复

### 系统安全
- 仅操作hosts文件，不涉及其他系统文件
- 无网络通信，纯本地化处理
- 不收集用户数据，保护隐私

## 故障排除

### 常见问题

#### 权限相关问题
**问题**: "没有权限读取/写入hosts文件"
**解决方案**: 
1. 右键程序图标，选择"以管理员身份运行"
2. 确保当前用户账户具有管理员权限
3. 检查杀毒软件是否阻止了文件访问

#### 文件访问问题
**问题**: "找不到hosts文件"
**解决方案**:
1. 检查文件路径：`C:\Windows\System32\drivers\etc\hosts`
2. 确保Windows系统完整安装
3. 某些安全软件可能隐藏或保护该文件

#### 修改不生效
**问题**: "修改hosts文件后域名解析不生效"
**解决方案**:
```bash
# 以管理员身份运行命令提示符，执行以下命令：
ipconfig /flushdns

# 然后重启浏览器或相关应用程序
```

#### 程序启动问题
**问题**: "程序无法启动或出现错误"
**解决方案**:
1. 确保安装了Python 3.7+（源码运行）
2. 检查PySide6是否正确安装：`pip install PySide6`
3. 查看是否有杀毒软件误报并阻止运行
4. 尝试在命令行中运行查看详细错误信息

### 获取帮助

如果遇到其他问题，可以通过以下方式获取帮助：
- [提交Issue](../../issues) - 报告Bug或功能请求
- [讨论区](../../discussions) - 使用问题和经验分享
- 联系开发者：your.email@example.com

## 官方网站

我们为HostsfileEdit构建了完整的官方网站，提供：

- **响应式设计** - 完美适配桌面、平板和手机
- **详细文档** - 功能介绍、使用指南、最佳实践
- **便捷下载** - 多种下载方式和版本选择
- **使用案例** - 丰富的实际应用场景
- **FAQ支持** - 常见问题和解决方案

访问地址：[https://YOUR_USERNAME.github.io/HostsfileEdit/](https://YOUR_USERNAME.github.io/HostsfileEdit/)

## 参与贡献

我们欢迎所有形式的贡献！无论是代码、文档、测试还是反馈建议。

### 贡献方式

1. **报告问题**
   - 使用详细的Issue模板
   - 提供系统信息和复现步骤
   - 附上错误截图或日志

2. **功能建议**
   - 在Discussions中提出想法
   - 详细描述功能需求和使用场景
   - 参与功能设计讨论

3. **代码贡献**
   ```bash
   # 1. Fork项目到你的GitHub账户
   # 2. 克隆你的Fork
   git clone https://github.com/YOUR_USERNAME/HostsfileEdit.git
   
   # 3. 创建功能分支
   git checkout -b feature/your-feature-name
   
   # 4. 提交更改
   git commit -m "Add: 你的功能描述"
   
   # 5. 推送并创建Pull Request
   git push origin feature/your-feature-name
   ```

4. **文档改进**
   - 修正文档错误或不准确信息
   - 添加使用示例和最佳实践
   - 翻译文档到其他语言

### 开发指南

详细的开发环境搭建和代码规范请参考：
- [开发环境搭建](docs/DEV_SETUP.md)
- [贡献指南](docs/CONTRIBUTING.md)
- [分支策略](docs/BRANCHING_STRATEGY.md)

## 版本历史

### v2.0.0 (2025-01-25) - 首次发布

#### 新功能
- 基于PySide6的现代化GUI界面
- 双重编辑模式（文本编辑 + 按条编辑）
- 智能权限检测和安全保护
- 便民工具集成（文件定位、记事本、环境变量）
- 完整的官方网站和文档体系

#### 技术特性
- 单文件架构，部署简单
- 完善的异常处理和用户反馈
- 跨Windows版本兼容性
- 现代化的代码结构和设计模式

#### 发布内容
- Windows可执行文件（约25MB）
- 完整源代码
- 官方网站
- 详细文档和使用指南

### 未来规划

#### v2.1.0 (计划中)
- [ ] 添加语法高亮和代码折叠
- [ ] 支持批量导入/导出功能
- [ ] 添加hosts条目分类管理
- [ ] 优化大文件处理性能

#### v2.2.0 (计划中)
- [ ] 支持主题切换（浅色/深色）
- [ ] 添加快捷键支持
- [ ] 集成DNS查询工具
- [ ] 添加操作历史记录

## 相关链接

### 项目资源
- [官方网站](https://YOUR_USERNAME.github.io/HostsfileEdit/)
- [下载地址](../../releases)
- [项目文档](../../wiki)
- [问题反馈](../../issues)
- [讨论社区](../../discussions)

### 开发资源
- [GitHub Actions](../../actions)
- [项目统计](../../pulse)
- [贡献者](../../graphs/contributors)
- [项目看板](../../projects)

## 开源许可

本项目采用 [MIT License](LICENSE) 开源许可证。

```
MIT License

Copyright (c) 2025 HostsfileEdit

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

## 致谢

感谢以下开源项目和技术：
- [PySide6](https://www.qt.io/qt-for-python) - 优秀的Python GUI框架
- [Vue.js](https://vuejs.org/) - 渐进式JavaScript框架
- [Vite](https://vitejs.dev/) - 快速的前端构建工具
- [GitHub Pages](https://pages.github.com/) - 免费的静态网站托管

特别感谢所有测试用户、贡献者和支持者！

## 联系我们

- **邮箱**: your.email@example.com
- **Twitter**: [@your_username](https://twitter.com/your_username)
- **QQ群**: 123456789（HostsfileEdit用户群）
- **个人主页**: [https://github.com/YOUR_USERNAME](https://github.com/YOUR_USERNAME)

---

<div align="center">

### 如果这个项目对您有帮助，请给个Star支持一下！

**让hosts文件管理变得简单高效**

Made with ❤️ by [Your Name](https://github.com/YOUR_USERNAME)

</div>