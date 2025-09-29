# 🖥️ Hosts文件编辑工具 (HostsfileEdit)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows/)
[![GUI Framework](https://img.shields.io/badge/GUI-PySide6-green.svg)](https://www.qt.io/qt-for-python)

一个基于PySide6的Windows系统hosts文件可视化编辑工具，提供友好的图形界面来管理系统hosts文件。告别复杂的命令行操作，让域名映射管理变得简单高效！

## 📸 界面预览

```
┌─────────────────────────────────────────────────────────────┐
│ Host文件修改工具                                    ─ □ ✕    │
├─────────────────────────────────────────────────────────────┤
│ [定位到文件] [在记事本中打开] [环境变量]                      │
├─────────────────────────────────────────────────────────────┤
│ 文本编辑 │ 按条编辑                                           │
├─────────────────────────────────────────────────────────────┤
│ # This is a sample hosts file                               │
│ 127.0.0.1    localhost                                     │
│ 127.0.0.1    dev.mysite.com                               │
│ 192.168.1.100 fileserver                                  │
│                                                             │
│                                            [重新加载] [保存] │
└─────────────────────────────────────────────────────────────┘
```

## ✨ 功能特性

### 🎯 核心功能
- **📋 可视化列表显示** - 以表格形式显示当前hosts文件中的所有条目
- **➕ 添加新条目** - 支持添加新的IP地址和域名映射
- **✏️ 修改现有条目** - 可以编辑已存在的hosts条目
- **🗑️ 删除条目** - 安全删除不需要的hosts条目
- **💾 自动保存** - 修改后自动保存到系统hosts文件

### 🛠️ 高级功能
- **🔄 双编辑模式** - 支持文本编辑和按条编辑两种方式
- **🔒 权限检测** - 自动检测管理员权限并提示
- **📁 快速定位** - 一键定位到hosts文件所在目录
- **📝 记事本集成** - 快速在记事本中打开hosts文件
- **⚙️ 环境变量** - 快速访问Windows环境变量设置
- **✅ 数据验证** - IP地址格式验证，防止错误输入

### 🔧 便民工具
- **📍 文件定位** - 在资源管理器中直接定位hosts文件
- **📄 外部编辑** - 支持在记事本中快速打开编辑
- **🌐 环境变量** - 快速访问系统环境变量设置
- **🔄 实时同步** - 两种编辑模式间数据实时同步

## 🚀 快速开始

### 📋 系统要求

| 项目 | 要求 |
|------|------|
| **操作系统** | Windows 7 SP1 / 8 / 10 / 11 |
| **Python版本** | Python 3.7+ |
| **内存** | 至少 512 MB RAM |
| **磁盘空间** | 50 MB 可用空间 |
| **权限** | 管理员权限（必须） |

### 🔧 安装方式

#### 方式一：可执行文件（推荐）
1. 从 [Releases](../../releases) 下载最新版本
2. 右键选择"以管理员身份运行"
3. 开始使用！

#### 方式二：从源码运行
```bash
# 1. 克隆项目
git clone https://github.com/YOUR_USERNAME/HostsfileEdit.git
cd HostsfileEdit

# 2. 安装依赖
pip install -r app/requirements.txt

# 3. 运行程序（需要管理员权限）
cd app
python main.py
```

### 🎮 使用方法

#### 启动程序
⚠️ **重要：必须以管理员身份运行**

```bash
# 方法1：右键点击可执行文件，选择"以管理员身份运行"
# 方法2：以管理员身份打开命令提示符
python main.py
```

#### 基本操作

1. **查看hosts条目**
   - 程序启动后自动加载当前hosts文件
   - 在列表中查看所有有效条目

2. **添加新条目**
   - 点击"添加"按钮
   - 输入IP地址和域名
   - 点击"确定"保存

3. **修改条目**
   - 在列表中选择要修改的条目
   - 点击"修改"按钮
   - 编辑信息后保存

4. **删除条目**
   - 选择要删除的条目
   - 点击"删除"按钮
   - 确认删除操作

## 📚 使用场景

### 💻 本地开发
```bash
# 为开发环境设置本地域名
127.0.0.1 dev.myproject.com
127.0.0.1 api.myproject.local
127.0.0.1 admin.myproject.local
```

### 🚫 广告屏蔽
```bash
# 屏蔽广告和跟踪域名
0.0.0.0 ads.example.com
0.0.0.0 tracker.example.com
0.0.0.0 analytics.unwanted.com
```

### 🏢 企业内网
```bash
# 配置内网服务器访问
192.168.1.100 fileserver
192.168.1.200 database
192.168.1.50  printer
```

### 🔧 系统维护
```bash
# 临时重定向进行维护
127.0.0.1 maintenance.site.com
192.168.1.10 backup.internal.com
```

## 🏗️ 项目结构

```
HostsfileEdit/
├── app/                    # 应用程序目录
│   ├── main.py            # 主程序文件
│   ├── requirements.txt   # Python依赖
│   ├── run.bat           # 快速启动脚本
│   └── README.md         # 应用说明文档
├── web/                   # 官方网站
│   ├── src/              # Vue.js源码
│   ├── public/           # 静态资源
│   ├── package.json      # 前端依赖
│   └── README.md         # 网站说明文档
└── README.md             # 项目总体说明
```

## 🛠️ 技术架构

### 核心技术栈
- **GUI框架**: PySide6 (Qt6 for Python)
- **编程语言**: Python 3.7+
- **文件处理**: Python标准库
- **正则表达式**: 用于hosts文件解析
- **权限管理**: Windows API调用

### 架构特点
- **单文件架构**: 所有功能集成在main.py中
- **事件驱动**: 基于Qt的信号槽机制
- **内存安全**: 严格的异常处理和资源管理
- **跨版本兼容**: 支持Windows 7-11

## 🔒 安全特性

### 权限管理
- ✅ 自动检测管理员权限
- ✅ 安全的文件读写操作
- ✅ 操作前确认提示

### 数据保护
- ✅ 自动备份原始文件
- ✅ IP地址格式验证
- ✅ 异常恢复机制

### 系统安全
- ✅ 只修改hosts文件
- ✅ 不涉及网络通信
- ✅ 本地化处理

## 🐛 故障排除

### 常见问题及解决方案

#### ❌ "没有权限读取/写入hosts文件"
**解决方案**: 
- 右键选择"以管理员身份运行"程序
- 确保当前用户具有管理员权限

#### ❌ "找不到hosts文件"
**解决方案**:
- 检查文件路径: `C:\Windows\System32\drivers\etc\hosts`
- 确保Windows系统完整安装
- 某些安全软件可能隐藏此文件

#### ❌ "修改后不生效"
**解决方案**:
```bash
# 以管理员身份运行命令提示符，执行：
ipconfig /flushdns
# 然后重启浏览器或相关应用
```

#### ❌ "程序无法启动"
**解决方案**:
- 确保安装了Python 3.7+
- 检查PySide6是否正确安装: `pip install PySide6`
- 查看是否有杀毒软件阻止运行

#### ❌ "界面显示异常"
**解决方案**:
- 更新显卡驱动
- 确保系统DPI设置正常
- 重启程序

## 🤝 贡献指南

我们欢迎各种形式的贡献！

### 🔧 开发贡献
1. Fork 本项目
2. 创建功能分支: `git checkout -b feature/AmazingFeature`
3. 提交更改: `git commit -m 'Add some AmazingFeature'`
4. 推送分支: `git push origin feature/AmazingFeature`
5. 创建 Pull Request

### 🐛 问题报告
使用 [Issues](https://github.com/yourusername/HostsfileEdit/issues) 报告问题时，请包含：
- 操作系统版本
- Python版本
- 详细的错误描述
- 复现步骤

### 💡 功能建议
我们欢迎新功能建议！请在 Issues 中详细描述您的想法。

## 📈 版本历史

### v2.0.0 (2025-01-XX)
- ✨ 迁移到PySide6框架
- 🎨 全新的UI设计
- 🔄 双编辑模式支持
- 🛠️ 便民工具集成
- 📱 响应式界面优化
- 🐛 修复已知问题

### v1.0.0 (2024-XX-XX)
- 🎉 初始版本发布
- 📋 基本hosts文件编辑功能
- 🖥️ 图形化用户界面
- ➕ 支持添加、修改、删除操作

## 🔗 相关链接

- 📖 [详细文档](../../wiki)
- 🌐 [官方网站](https://YOUR_USERNAME.github.io/HostsfileEdit/)
- 🐛 [问题反馈](../../issues)
- 💬 [讨论区](../../discussions)

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- 感谢 [Qt](https://www.qt.io/) 团队提供优秀的GUI框架
- 感谢 [PySide6](https://www.qt.io/qt-for-python) 项目
- 感谢所有贡献者和用户的支持

## 📞 联系方式

- 📧 邮箱: your.email@example.com
- 🐦 Twitter: [@yourusername](https://twitter.com/yourusername)
- 💬 QQ群: 123456789

---

<div align="center">

**⭐ 如果这个项目对您有帮助，请给个Star支持一下！ ⭐**

Made with ❤️ by [Your Name](https://github.com/YOUR_USERNAME)

</div>
# Windows Hosts文件编辑工具

一个基于PySide6的Windows系统hosts文件可视化编辑工具，提供友好的图形界面来管理系统hosts文件。

## 功能特性

- 📋 **可视化列表显示** - 以表格形式显示当前hosts文件中的所有条目
- ➕ **添加新条目** - 支持添加新的IP地址和域名映射
- ✏️ **修改现有条目** - 可以编辑已存在的hosts条目
- 🗑️ **删除条目** - 安全删除不需要的hosts条目
- 💾 **自动保存** - 修改后自动保存到系统hosts文件
- 🔒 **权限检测** - 自动检测管理员权限并提示
- 📝 **双输入模式** - 支持单行输入和分别输入两种方式

## 系统要求

- Windows 7/8/10/11
- Python 3.7+
- PySide6

## 安装依赖

```bash
pip install PySide6
```

或者使用requirements.txt安装：

```bash
pip install -r requirements.txt
```

## 使用方法

### 1. 启动程序

**重要：必须以管理员身份运行**

```bash
# 右键点击命令提示符，选择"以管理员身份运行"
python main.py
```

或者：
- 右键点击 `main.py` 文件
- 选择"以管理员身份运行"

### 2. 主界面操作

- **查看条目**：程序启动后会自动加载并显示当前hosts文件中的所有条目
- **选择条目**：点击列表中的任意条目进行选择
- **添加条目**：点击"添加"按钮
- **修改条目**：选中条目后点击"修改"按钮
- **删除条目**：选中条目后点击"删除"按钮

### 3. 添加/修改条目

程序提供两种输入方式：

#### 单行输入模式
- 在文本框中输入：`IP地址 域名`
- 例如：`127.0.0.1 localhost`
- 例如：`192.168.1.100 myserver.local`

#### 分别输入模式
- IP地址和域名分别在不同的文本框中输入
- 更适合精确输入

### 4. 常用hosts条目示例

```
# 本地开发
127.0.0.1 localhost
127.0.0.1 dev.mysite.com

# 屏蔽广告
0.0.0.0 ads.example.com
0.0.0.0 tracker.example.com

# 内网服务器
192.168.1.100 fileserver
192.168.1.200 database
```

## 文件结构

```
PyHostFileEdit/
├── main.py          # 主程序文件（包含UI和逻辑）
├── requirements.txt # 依赖包列表
├── README.md        # 说明文档
└── __pycache__/     # Python缓存目录
```

## 技术实现

- **GUI框架**：PySide6
- **文件操作**：Python标准库
- **正则表达式**：用于解析hosts文件格式
- **权限管理**：检测和处理Windows文件权限
- **架构设计**：UI和逻辑代码完全集成在main.py中

## 注意事项

### ⚠️ 重要提醒

1. **管理员权限**：修改hosts文件需要管理员权限，请务必以管理员身份运行程序
2. **备份建议**：建议在使用前备份原始hosts文件（位于 `C:\Windows\System32\drivers\etc\hosts`）
3. **防病毒软件**：某些防病毒软件可能会阻止hosts文件修改，请临时关闭或添加例外
4. **DNS缓存**：修改hosts文件后，可能需要刷新DNS缓存才能生效

### 刷新DNS缓存

修改hosts文件后，建议执行以下命令刷新DNS缓存：

```bash
# 以管理员身份运行命令提示符，然后执行：
ipconfig /flushdns
```

## 故障排除

### 常见问题

1. **"没有权限读取/写入hosts文件"**
   - 解决方案：以管理员身份运行程序

2. **"找不到hosts文件"**
   - 检查路径：`C:\Windows\System32\drivers\etc\hosts`
   - 确保文件存在且未被移动

3. **修改后不生效**
   - 刷新DNS缓存：`ipconfig /flushdns`
   - 重启浏览器或应用程序

4. **程序无法启动**
   - 检查Python和PySide6是否正确安装
   - 确保所有依赖文件完整

## 开发信息

- **开发语言**：Python 3
- **GUI框架**：PySide6
- **兼容系统**：Windows 7/8/10/11
- **许可证**：MIT License

## 更新日志

### v2.0.0
- 迁移到PySide6框架
- UI代码完全集成到main.py中
- 移除独立的ui.py文件
- 优化代码结构和性能

### v1.0.0
- 初始版本发布
- 基本的hosts文件编辑功能
- 图形化用户界面
- 支持添加、修改、删除操作
- 双输入模式支持

---

**免责声明**：本工具仅用于合法的系统管理目的。用户应当遵守相关法律法规，不得将本工具用于任何非法用途。使用本工具所产生的任何后果由用户自行承担。