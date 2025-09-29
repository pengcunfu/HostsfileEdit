# 分支管理策略

本文档描述了 HostsfileEdit 项目的分支管理策略和工作流程。

## 分支结构

### 主要分支

#### `main` 分支
- **用途**: 桌面应用程序的主分支
- **内容**: 
  - Python源代码 (`main.py`)
  - 项目依赖 (`requirements.txt`)
  - 项目文档 (`README.md`, `docs/`)
  - 构建脚本 (`scripts/`)
- **不包含**: `web/` 目录
- **保护**: 受保护分支，需要PR审查

#### `dev` 分支
- **用途**: 日常开发工作
- **内容**: 包含所有开发中的功能
- **基于**: `main` 分支
- **合并**: 定期合并到 `main` 分支

#### `gh-pages` 分支
- **用途**: GitHub Pages 网站部署
- **内容**: 构建后的静态网站文件
- **来源**: 从 `main` 分支的 `web/` 目录自动构建
- **部署**: 自动部署到 GitHub Pages

## 工作流程

### 开发流程

1. **功能开发**
   ```bash
   # 从main分支创建功能分支
   git checkout main
   git pull origin main
   git checkout -b feature/your-feature-name
   
   # 开发完成后提交
   git add .
   git commit -m "feat: 添加新功能"
   git push origin feature/your-feature-name
   
   # 创建PR合并到dev分支
   ```

2. **测试验证**
   ```bash
   # 在dev分支进行集成测试
   git checkout dev
   git merge feature/your-feature-name
   
   # 测试通过后合并到main分支
   git checkout main
   git merge dev
   git push origin main
   ```

3. **网站更新**
   ```bash
   # 修改web目录中的内容
   cd web/
   npm run dev  # 本地开发
   npm run build  # 构建测试
   
   # 提交到main分支会自动触发网站部署
   git add web/
   git commit -m "feat: 更新网站内容"
   git push origin main
   ```

### 发布流程

1. **准备发布**
   ```bash
   # 确保main分支是最新的
   git checkout main
   git pull origin main
   
   # 更新版本信息
   echo "2.1.0" > docs/VERSION
   
   # 更新CHANGELOG.md
   # 提交版本更新
   git add docs/VERSION docs/CHANGELOG.md
   git commit -m "chore: 准备发布 v2.1.0"
   git push origin main
   ```

2. **创建发布标签**
   ```bash
   # 创建并推送标签
   git tag -a v2.1.0 -m "Release version 2.1.0"
   git push origin v2.1.0
   
   # GitHub Actions 将自动构建并创建 Release
   ```

## 自动化部署

### GitHub Actions 工作流

#### 网站部署 (`.github/workflows/deploy-web.yml`)
- **触发条件**: 
  - `main` 分支的 `web/` 目录有变更
  - 手动触发
- **执行步骤**:
  1. 检出代码
  2. 设置Node.js环境
  3. 安装依赖并构建
  4. 部署到 `gh-pages` 分支
  5. 自动发布到 GitHub Pages

#### 应用构建 (`.github/workflows/build-app.yml`)
- **触发条件**: 创建版本标签 (v*)
- **执行步骤**:
  1. 构建Windows可执行文件
  2. 创建GitHub Release
  3. 上传构建产物

## 分支保护规则

### `main` 分支
- 禁止直接推送
- 需要PR审查
- 需要状态检查通过
- 需要分支保持最新

### `gh-pages` 分支
- 仅允许自动化部署
- 禁止手动修改

## 目录结构差异

### `main` 分支结构
```
HostsfileEdit/
├── main.py
├── requirements.txt
├── README.md
├── docs/
├── scripts/
├── .github/
└── .gitignore  # 包含 web/ 忽略规则
```

### `gh-pages` 分支结构
```
HostsfileEdit/
├── index.html
├── assets/
├── favicon.ico
├── .nojekyll
└── README.md  # 网站说明
```

### `dev` 分支结构
```
HostsfileEdit/
├── main.py
├── requirements.txt
├── README.md
├── docs/
├── scripts/
├── .github/
├── web/          # 包含web开发文件
└── .gitignore
```

## 设置脚本

### 初始化分支结构
```bash
# Windows
scripts/setup-branches.bat
scripts/setup-web-branch.bat

# Linux/Mac
chmod +x scripts/setup-branches.sh
chmod +x scripts/setup-web-branch.sh
./scripts/setup-branches.sh
./scripts/setup-web-branch.sh
```

### 推送所有分支
```bash
# 推送主分支
git push origin main

# 推送开发分支
git push origin dev

# 推送网站分支
git push origin gh-pages

# 推送所有标签
git push origin --tags
```

## 最佳实践

### 提交信息规范
- `feat:` 新功能
- `fix:` 错误修复
- `docs:` 文档更新
- `style:` 代码格式调整
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建过程或辅助工具的变动

### 分支命名规范
- `feature/功能名称` - 新功能分支
- `fix/问题描述` - 错误修复分支
- `docs/文档类型` - 文档更新分支
- `refactor/重构内容` - 重构分支

### 代码审查
- 所有PR需要至少一人审查
- 确保代码质量和一致性
- 检查功能完整性和测试覆盖

### 版本管理
- 遵循语义化版本控制 (SemVer)
- 主版本.次版本.修订版本
- 每个发布都要有对应的Git标签

## 故障排除

### 分支同步问题
```bash
# 重置本地分支到远程状态
git fetch origin
git reset --hard origin/main
```

### 网站部署失败
1. 检查 `web/` 目录的构建配置
2. 查看 GitHub Actions 日志
3. 确认 GitHub Pages 设置正确

### 合并冲突
```bash
# 解决冲突后
git add .
git commit -m "resolve: 解决合并冲突"
```

## 联系支持

如果在分支管理过程中遇到问题，请：
1. 查看本文档的故障排除部分
2. 提交 Issue 描述具体问题
3. 联系项目维护者

---

**注意**: 本分支策略旨在保持代码库的清洁和部署的自动化。请严格遵循流程以确保项目的稳定性。