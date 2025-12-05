"""
使用 Nuitka 编译 HostsFileEdit 项目
配置：非独立模式、并行编译、加速编译
"""
import subprocess
import sys
import os
from pathlib import Path

def build_with_nuitka():
    """使用 Nuitka 编译项目"""
    
    # 获取当前脚本所在目录
    current_dir = Path(__file__).parent.absolute()
    
    # 主文件路径
    main_file = current_dir / "main.py"
    
    # 图标路径
    icon_file = current_dir / "icon.png"
    
    # 输出目录 - dist 文件夹
    output_dir = current_dir / "dist"
    
    # 创建 dist 目录（如果不存在）
    output_dir.mkdir(exist_ok=True)
    
    # 检查文件是否存在
    if not main_file.exists():
        print(f"错误: 找不到主文件 {main_file}")
        sys.exit(1)
    
    if not icon_file.exists():
        print(f"警告: 找不到图标文件 {icon_file}")
    
    print("=" * 60)
    print("开始使用 Nuitka 编译项目")
    print("=" * 60)
    print(f"主文件: {main_file}")
    print(f"图标文件: {icon_file}")
    print(f"输出目录: {output_dir}")
    print("=" * 60)
    
    # Nuitka 编译命令参数
    nuitka_args = [
        sys.executable,
        "-m", "nuitka",
        
        # 基本设置
        str(main_file),
        
        # 输出设置 - standalone 模式（打包所有依赖到文件夹）
        "--standalone",  # 打包 Python 运行时和所有依赖到文件夹
        # 不使用 --onefile，这样会生成文件夹而不是单个文件，编译更快
        f"--output-dir={output_dir}",
        "--output-filename=HostsFileEditor-Windows.exe",  # 自定义可执行文件名
        
        # 图标设置
        f"--windows-icon-from-ico={icon_file}",
        
        # Windows 特定设置
        "--windows-console-mode=disable",  # 禁用控制台窗口
        "--enable-plugin=pyside6",  # 启用 PySide6 插件
        
        # 编译优化 - 加快编译速度
        "--jobs=32",  # 并行编译，使用 32 个进程
        "--assume-yes-for-downloads",  # 自动下载依赖
        
        # 性能优化
        "--lto=no",  # 禁用链接时优化（LTO），加快编译速度
        
        # 移除调试信息以减小体积
        "--remove-output",  # 编译成功后删除构建目录
        
        # 显示进度
        "--show-progress",
        "--show-memory",
    ]
    
    print("\n执行命令:")
    print(" ".join(nuitka_args))
    print("\n" + "=" * 60)
    
    try:
        # 执行编译
        result = subprocess.run(
            nuitka_args,
            cwd=current_dir,
            check=True,
            text=True
        )
        
        print("\n" + "=" * 60)
        print("编译成功！")
        print(f"程序文件夹: {output_dir / 'main.dist'}")
        print(f"可执行文件: {output_dir / 'main.dist' / 'HostsFileEditor-Windows.exe'}")
        print("\n说明: 已打包所有依赖，可将 main.dist 文件夹复制到其他电脑运行")
        print("=" * 60)
        
        return 0
        
    except subprocess.CalledProcessError as e:
        print("\n" + "=" * 60)
        print(f"编译失败，错误码: {e.returncode}")
        print("=" * 60)
        return e.returncode
    
    except Exception as e:
        print("\n" + "=" * 60)
        print(f"发生错误: {str(e)}")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    # 检查是否安装了 Nuitka
    try:
        subprocess.run(
            [sys.executable, "-m", "nuitka", "--version"],
            check=True,
            capture_output=True
        )
    except subprocess.CalledProcessError:
        print("错误: 未安装 Nuitka")
        print("请运行: pip install nuitka")
        sys.exit(1)
    
    # 执行编译
    exit_code = build_with_nuitka()
    sys.exit(exit_code)
