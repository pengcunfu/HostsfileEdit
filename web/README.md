# Hosts文件编辑工具 - 官方网站

这是Hosts文件编辑工具的官方网站，基于Vue.js 3和Vite构建。

## 功能特性

- 🎨 现代化的响应式设计
- ⚡ 基于Vite的快速开发体验
- 📱 移动端友好的界面
- 🎯 专业的产品展示页面
- 📥 详细的下载和安装指南
- ❓ 常见问题解答

## 页面结构

- **首页** - 产品介绍和主要功能展示
- **功能特性** - 详细的功能说明和技术特性
- **下载页面** - 下载链接、安装指南和系统要求

## 开发环境

### 环境要求

- Node.js 16.0 或更高版本
- npm 或 yarn

### 安装依赖

```bash
npm install
```

### 开发服务器

```bash
npm run dev
```

开发服务器将在 `http://localhost:5173` 启动

### 构建生产版本

```bash
npm run build
```

构建后的文件将输出到 `dist/` 目录

### 预览生产版本

```bash
npm run preview
```

## 项目结构

```
web/
├── public/                 # 静态资源
│   └── favicon.svg        # 网站图标
├── src/
│   ├── components/        # Vue组件
│   │   ├── Home.vue      # 首页
│   │   ├── Features.vue  # 功能特性页
│   │   └── Download.vue  # 下载页
│   ├── App.vue           # 主应用组件
│   ├── main.js          # 应用入口
│   └── style.css        # 全局样式
├── index.html           # HTML模板
├── vite.config.js       # Vite配置
├── package.json         # 项目配置
└── README.md           # 项目说明
```

## 技术栈

- **Vue.js 3** - 渐进式JavaScript框架
- **Vue Router 4** - 官方路由管理器
- **Vite** - 下一代前端构建工具
- **CSS3** - 现代CSS特性和响应式设计

## 设计特色

### 视觉设计
- 渐变色背景和现代化配色方案
- 卡片式布局和阴影效果
- 平滑的动画过渡
- 响应式网格系统

### 用户体验
- 直观的导航结构
- 清晰的信息层次
- 移动端优化
- 快速加载性能

### 内容组织
- 产品价值突出展示
- 功能特性详细说明
- 简化的下载流程
- 完善的帮助文档

## 自定义配置

### 修改品牌信息
在 `src/App.vue` 中修改导航栏和页脚的品牌信息。

### 更新产品信息
- 首页内容：`src/components/Home.vue`
- 功能特性：`src/components/Features.vue`
- 下载信息：`src/components/Download.vue`

### 样式定制
全局样式定义在 `src/style.css` 中，包括：
- 颜色变量
- 通用组件样式
- 响应式断点

## 部署指南

### 静态网站部署
1. 运行 `npm run build` 构建项目
2. 将 `dist/` 目录中的文件上传到Web服务器
3. 配置服务器支持单页应用路由

### GitHub Pages
1. 在 `vite.config.js` 中设置正确的 `base` 路径
2. 使用GitHub Actions自动部署

### 其他平台
项目支持部署到任何静态网站托管平台，如Netlify、Vercel等。

## 浏览器支持

- Chrome 85+
- Firefox 78+
- Safari 14+
- Edge 85+

## 贡献指南

欢迎提交问题和功能建议！请遵循以下步骤：

1. Fork本项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建Pull Request

## 许可证

MIT License - 详见LICENSE文件
