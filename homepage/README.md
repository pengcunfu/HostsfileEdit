# Hosts文件编辑工具 - 官方网站

<div align="center">

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-deployed-success)](https://pengcunfu.github.io/HostsfileEditWeb/)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?logo=vue.js)](https://vuejs.org/)
[![Vite](https://img.shields.io/badge/Vite-5.x-646CFF?logo=vite)](https://vitejs.dev/)

[在线访问](https://pengcunfu.github.io/HostsfileEditWeb/) | [主项目仓库](https://github.com/pengcunfu/HostsfileEdit)

</div>

---

## 📖 项目简介

这是 **Hosts文件编辑工具** 的官方网站项目，使用 Vue 3 + Vite 构建的现代化单页应用。网站提供工具介绍、功能展示、下载链接等内容，并通过 GitHub Pages 自动部署。

## ✨ 特性

- 🎨 现代化的响应式设计
- ⚡ 基于 Vite 的快速构建
- 🖼️ 精美的UI界面和动画效果
- 📱 完美支持移动端访问
- 🚀 自动化部署到 GitHub Pages

## 🛠️ 技术栈

- **框架**: Vue 3 (Composition API)
- **构建工具**: Vite 5.x
- **样式**: CSS3 + 渐变动画
- **部署**: GitHub Actions + GitHub Pages

## 🚀 快速开始

### 环境要求

- Node.js >= 16.x
- npm >= 8.x

### 安装依赖

```bash
npm install
```

### 开发模式

```bash
npm run dev
```

访问 `http://localhost:5173` 查看开发服务器。

### 构建生产版本

```bash
npm run build
```

构建产物将输出到 `dist` 目录。

### 预览生产构建

```bash
npm run preview
```

## 📦 项目结构

```
HostsfileEditWeb/
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions 自动部署配置
├── public/                 # 静态资源
│   ├── favicon.ico
│   └── favicon.svg
├── src/
│   ├── components/         # Vue 组件
│   │   ├── Home.vue       # 首页组件
│   │   ├── Features.vue   # 功能介绍组件
│   │   └── Download.vue   # 下载页面组件
│   ├── App.vue            # 根组件
│   ├── main.js            # 入口文件
│   └── style.css          # 全局样式
├── index.html             # HTML 模板
├── vite.config.js         # Vite 配置
├── package.json           # 项目配置
└── README.md             # 项目文档
```

## 🔄 自动部署

本项目通过 GitHub Actions 实现自动部署：

1. 推送代码到 `master` 分支
2. GitHub Actions 自动触发构建流程
3. 构建完成后自动部署到 GitHub Pages
4. 网站自动更新

查看 [.github/workflows/deploy.yml](.github/workflows/deploy.yml) 了解部署配置详情。

## 🌐 访问地址

**官方网站**: https://pengcunfu.github.io/HostsfileEditWeb/

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

## 📄 开源协议

本项目采用 [Apache License 2.0](LICENSE) 开源协议。

```
Copyright 2025 pengcunfu

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## 👤 作者

**pengcunfu**

- GitHub: [@pengcunfu](https://github.com/pengcunfu)
- 项目主页: [HostsfileEditWeb](https://github.com/pengcunfu/HostsfileEditWeb)

## 🔗 相关链接

- [主项目仓库](https://github.com/pengcunfu/HostsfileEdit) - Hosts文件编辑工具桌面应用
- [在线文档](https://pengcunfu.github.io/HostsfileEditWeb/) - 官方网站

---

<div align="center">

**如果这个项目对你有帮助，请给它一个 ⭐️ Star！**

</div>
