# 🔧 开发环境设置指南

## 🚀 快速开始

### 1. 创建dev分支（首次设置）

```bash
# 确保在main分支
git checkout main
git pull origin main

# 创建并切换到dev分支
git checkout -b dev

# 推送dev分支到远程
git push origin dev

# 设置上游分支
git branch --set-upstream-to=origin/dev dev
```

### 2. 日常开发流程

```bash
# 1. 切换到dev分支并获取最新代码
git checkout dev
git pull origin dev

# 2. 创建功能分支
git checkout -b feature/your-feature-name

# 3. 进行开发
# ... 编写代码 ...

# 4. 提交更改
git add .
git commit -m "feat: 添加新功能描述"

# 5. 推送功能分支
git push origin feature/your-feature-name

# 6. 在GitHub上创建Pull Request: feature/your-feature-name -> dev
```

### 3. 合并到主分支（发布）

```bash
# 1. 确保dev分支是最新的
git checkout dev
git pull origin dev

# 2. 在GitHub上创建Pull Request: dev -> main
# 3. 合并后在main分支创建版本标签
git checkout main
git pull origin main
git tag -a v2.1.0 -m "Release version 2.1.0"
git push origin v2.1.0
```

## 🛠️ 开发环境配置

### Python应用开发

```bash
# 1. 创建虚拟环境
python -m venv venv

# 2. 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. 安装依赖
cd app
pip install -r requirements.txt

# 4. 运行应用（需要管理员权限）
python main.py
```

### Vue.js网站开发

```bash
# 1. 安装Node.js依赖
cd web
npm install

# 2. 启动开发服务器
npm run dev

# 3. 构建生产版本
npm run build

# 4. 预览构建结果
npm run preview
```

## 🔄 自动化工作流

### dev分支触发的Actions

#### ✅ 推送到dev分支时
- 运行完整测试套件
- 构建网站和应用
- 部署到开发环境（如果配置）
- 生成开发版本构建产物

#### ✅ 创建PR到dev分支时
- 运行测试和代码检查
- 构建验证
- 代码质量分析

#### ✅ 合并到main分支时
- 运行生产构建
- 部署到生产环境
- 创建Release（如果推送标签）

### 查看构建状态

```bash
# 查看所有工作流状态
https://github.com/YOUR_USERNAME/HostsfileEdit/actions

# 查看特定分支的状态
https://github.com/YOUR_USERNAME/HostsfileEdit/actions?query=branch%3Adev
```

## 📋 开发任务清单

### 新功能开发
- [ ] 从dev分支创建feature分支
- [ ] 实现功能代码
- [ ] 编写或更新测试
- [ ] 更新文档
- [ ] 本地测试通过
- [ ] 创建PR到dev分支
- [ ] 代码审查通过
- [ ] 合并到dev分支

### Bug修复
- [ ] 在dev分支或创建hotfix分支
- [ ] 重现并修复问题
- [ ] 添加回归测试
- [ ] 验证修复效果
- [ ] 更新相关文档
- [ ] 合并到相应分支

### 发布准备
- [ ] 确保dev分支稳定
- [ ] 更新CHANGELOG.md
- [ ] 更新版本号
- [ ] 运行完整测试
- [ ] 创建PR: dev -> main
- [ ] 合并并创建版本标签

## 🧪 测试策略

### 本地测试

```bash
# Python应用测试
cd app
python -m pytest  # 如果有测试文件

# 手动功能测试
python main.py

# Vue.js网站测试
cd web
npm run build  # 构建测试
npm run dev     # 开发服务器测试
```

### 自动化测试
- **单元测试**: 每次提交自动运行
- **集成测试**: PR时运行
- **构建测试**: 每次推送验证
- **部署测试**: 部署后验证

## 🔍 代码质量

### 代码规范
- **Python**: 遵循PEP 8规范
- **JavaScript**: 使用ESLint检查
- **提交信息**: 遵循约定式提交规范
- **文档**: 保持README和注释更新

### 质量检查工具
- **GitHub Actions**: 自动化检查
- **本地检查**: 提交前验证
- **代码审查**: PR必须通过审查

## 🚨 故障排除

### 常见问题

#### 分支同步问题
```bash
# 解决分支落后问题
git checkout dev
git fetch origin
git rebase origin/dev

# 或者使用merge
git merge origin/dev
```

#### 构建失败
```bash
# 清理并重新安装依赖
cd web
rm -rf node_modules
npm install

# Python依赖问题
cd app
pip install --upgrade -r requirements.txt
```

#### 合并冲突
```bash
# 解决冲突后
git add .
git commit -m "resolve: 解决合并冲突"
```

### 获取帮助
- 📚 查看项目文档
- 🐛 在Issues中搜索类似问题
- 💬 在Discussions中提问
- 📧 联系维护者

## 📊 开发状态监控

### 分支状态
- **main**: 生产稳定版本
- **dev**: 最新开发代码
- **feature/***: 功能开发分支
- **hotfix/***: 紧急修复分支

### 监控工具
- **GitHub Insights**: 查看提交和PR统计
- **Actions**: 监控构建和部署状态
- **Issues**: 跟踪问题和功能请求
- **Projects**: 管理开发任务

---

**开发愉快！** 🎉

如果有任何问题，请查看 [BRANCHING_STRATEGY.md](BRANCHING_STRATEGY.md) 了解详细的分支策略。
