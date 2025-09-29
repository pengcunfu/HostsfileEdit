# 🌳 Git分支策略

## 📋 分支结构

### 主要分支

#### 🚀 main分支
- **用途**: 生产分支，只包含稳定的发布版本
- **保护**: 启用分支保护，禁止直接推送
- **触发**: 自动构建和发布
- **合并**: 只能从dev分支通过PR合并

#### 🔧 dev分支
- **用途**: 开发分支，日常开发和功能集成
- **特点**: 最新的开发代码
- **测试**: 自动运行测试，部署到测试环境
- **合并**: 接受来自feature分支的合并

### 辅助分支

#### ✨ feature分支
- **命名**: `feature/功能名称`
- **用途**: 开发具体功能
- **生命周期**: 功能开发完成后删除
- **合并**: 合并到dev分支

#### 🐛 hotfix分支
- **命名**: `hotfix/问题描述`
- **用途**: 紧急修复生产问题
- **生命周期**: 修复完成后删除
- **合并**: 同时合并到main和dev分支

## 🔄 工作流程

### 1. 日常开发流程

```bash
# 1. 从dev分支创建功能分支
git checkout dev
git pull origin dev
git checkout -b feature/new-feature

# 2. 开发功能
# ... 编写代码 ...
git add .
git commit -m "feat: 添加新功能"

# 3. 推送功能分支
git push origin feature/new-feature

# 4. 创建PR: feature/new-feature -> dev
# 5. 代码审查通过后合并到dev
# 6. 删除功能分支
git branch -d feature/new-feature
git push origin --delete feature/new-feature
```

### 2. 发布流程

```bash
# 1. 从dev分支创建发布PR到main
# 2. 测试通过后合并到main
# 3. 在main分支创建版本标签
git checkout main
git pull origin main
git tag -a v2.1.0 -m "Release version 2.1.0"
git push origin v2.1.0
```

### 3. 热修复流程

```bash
# 1. 从main分支创建hotfix分支
git checkout main
git pull origin main
git checkout -b hotfix/critical-bug

# 2. 修复问题
# ... 修复代码 ...
git add .
git commit -m "fix: 修复关键问题"

# 3. 推送hotfix分支
git push origin hotfix/critical-bug

# 4. 创建PR到main和dev分支
# 5. 合并后创建新的补丁版本
git tag -a v2.0.1 -m "Hotfix version 2.0.1"
git push origin v2.0.1
```

## ⚙️ GitHub Actions配置

### main分支触发
- ✅ 构建生产版本
- ✅ 部署到生产环境
- ✅ 创建Release（标签推送时）

### dev分支触发
- ✅ 运行测试
- ✅ 构建开发版本
- ✅ 部署到测试环境

### feature分支触发
- ✅ 运行测试
- ✅ 代码质量检查

## 🛡️ 分支保护规则

### main分支保护
- ❌ 禁止直接推送
- ✅ 要求PR审查
- ✅ 要求状态检查通过
- ✅ 要求分支为最新
- ✅ 限制管理员权限

### dev分支保护
- ❌ 禁止直接推送
- ✅ 要求PR审查（可选）
- ✅ 要求状态检查通过

## 📝 提交信息规范

### 提交类型
- `feat:` 新功能
- `fix:` Bug修复
- `docs:` 文档更新
- `style:` 代码格式化
- `refactor:` 重构
- `test:` 测试相关
- `chore:` 构建过程或辅助工具的变动

### 示例
```
feat: 添加hosts文件语法高亮功能
fix: 修复管理员权限检测问题
docs: 更新README安装说明
```

## 🚀 快速开始

### 1. 创建dev分支
```bash
# 从main分支创建dev分支
git checkout main
git checkout -b dev
git push origin dev
```

### 2. 设置分支保护
1. 进入GitHub仓库设置
2. 找到"Branches"部分
3. 添加分支保护规则

### 3. 开始开发
```bash
# 创建功能分支
git checkout dev
git checkout -b feature/your-feature
# 开发完成后推送并创建PR
```

## 🔧 分支管理命令

### 查看分支
```bash
# 查看所有分支
git branch -a

# 查看远程分支
git branch -r
```

### 切换分支
```bash
# 切换到dev分支
git checkout dev

# 创建并切换到新分支
git checkout -b feature/new-feature
```

### 合并分支
```bash
# 合并feature分支到dev
git checkout dev
git merge feature/new-feature

# 删除已合并的分支
git branch -d feature/new-feature
```

### 同步分支
```bash
# 同步远程分支
git fetch origin

# 拉取最新代码
git pull origin dev
```

## 📊 分支状态监控

### 推荐工具
- **GitHub网页界面** - 查看分支状态和PR
- **Git命令行** - 本地分支管理
- **IDE集成** - Visual Studio Code Git插件
- **GitHub Desktop** - 图形化Git客户端

### 监控指标
- 分支数量
- PR状态
- 构建状态
- 代码覆盖率
- 部署状态

## ⚠️ 注意事项

### 最佳实践
- 保持分支简洁，及时删除已合并的分支
- 定期同步dev分支到main分支
- 功能分支应该短小精悍，专注单一功能
- 提交信息要清晰明确

### 常见问题
- **分支冲突**: 定期从主分支拉取最新代码
- **分支过多**: 及时清理已合并的分支
- **提交混乱**: 使用规范的提交信息格式

---

**建议**: 对于个人项目或小团队，可以简化为 main + dev 两分支模型，大型项目再考虑更复杂的分支策略。
