# 🤝 贡献指南

感谢您对 HostsfileEdit 项目的关注！我们欢迎各种形式的贡献。

## 📋 贡献方式

### 🐛 报告Bug
- 使用 [Bug报告模板](https://github.com/yourusername/HostsfileEdit/issues/new?template=bug_report.md)
- 提供详细的重现步骤
- 包含系统环境信息
- 附上相关截图或错误日志

### 💡 功能建议
- 使用 [功能建议模板](https://github.com/yourusername/HostsfileEdit/issues/new?template=feature_request.md)
- 详细描述功能需求
- 说明使用场景
- 考虑实现的可行性

### 🔧 代码贡献

#### 开发环境设置
1. **Fork 项目**
   ```bash
   git clone https://github.com/yourusername/HostsfileEdit.git
   cd HostsfileEdit
   ```

2. **设置Python环境**
   ```bash
   # 推荐使用虚拟环境
   python -m venv venv
   venv\Scripts\activate  # Windows
   pip install -r app/requirements.txt
   ```

3. **设置前端环境**
   ```bash
   cd web
   npm install
   ```

#### 开发流程
1. **创建功能分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **进行开发**
   - 遵循现有代码风格
   - 添加必要的注释
   - 确保功能完整

3. **测试代码**
   ```bash
   # 测试Python应用
   cd app
   python main.py
   
   # 测试前端网站
   cd web
   npm run dev
   ```

4. **提交更改**
   ```bash
   git add .
   git commit -m "feat: 添加新功能描述"
   git push origin feature/your-feature-name
   ```

5. **创建Pull Request**
   - 使用 [PR模板](https://github.com/yourusername/HostsfileEdit/compare)
   - 详细描述更改内容
   - 关联相关Issue

## 📏 代码规范

### Python代码
- 遵循 PEP 8 规范
- 使用有意义的变量名
- 添加必要的文档字符串
- 处理异常情况

```python
def example_function(param: str) -> bool:
    """
    示例函数说明
    
    Args:
        param: 参数说明
        
    Returns:
        bool: 返回值说明
    """
    try:
        # 实现逻辑
        return True
    except Exception as e:
        # 错误处理
        return False
```

### Vue.js代码
- 使用组合式API
- 组件名使用PascalCase
- 添加适当的注释
- 保持响应式设计

```vue
<template>
  <div class="component-name">
    <!-- 模板内容 -->
  </div>
</template>

<script>
export default {
  name: 'ComponentName',
  // 组件逻辑
}
</script>

<style scoped>
/* 组件样式 */
</style>
```

## 🧪 测试指南

### 应用程序测试
- 确保程序能正常启动
- 测试管理员权限检测
- 验证hosts文件读写功能
- 测试UI交互功能

### 网站测试
- 检查所有页面正常显示
- 验证响应式设计
- 测试导航功能
- 确保构建成功

## 📝 提交消息规范

使用语义化提交消息：

- `feat:` 新功能
- `fix:` Bug修复
- `docs:` 文档更新
- `style:` 代码格式化
- `refactor:` 重构
- `test:` 测试相关
- `chore:` 构建过程或辅助工具的变动

示例：
```
feat: 添加hosts文件备份功能
fix: 修复管理员权限检测问题
docs: 更新安装说明文档
```

## 🏷️ 版本发布

### 版本号规则
遵循语义化版本控制 (SemVer)：
- `MAJOR.MINOR.PATCH`
- 主版本号：不兼容的API修改
- 次版本号：向下兼容的功能性新增
- 修订号：向下兼容的问题修正

### 发布流程
1. 更新版本号
2. 更新CHANGELOG
3. 创建Git标签
4. GitHub Actions自动构建和发布

## 🆘 获取帮助

- 📖 查看 [项目文档](https://yourusername.github.io/HostsfileEdit/)
- 💬 在 [Discussions](https://github.com/yourusername/HostsfileEdit/discussions) 中讨论
- 📧 发送邮件到 your.email@example.com

## 📜 行为准则

请遵守我们的行为准则：
- 尊重所有参与者
- 使用友好和包容的语言
- 接受建设性的批评
- 关注社区的最佳利益

感谢您的贡献！🎉
