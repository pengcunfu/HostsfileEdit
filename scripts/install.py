"""
安装脚本：将编译后的程序复制到指定目录并创建快捷方式
"""
import shutil
import os
import sys
from pathlib import Path
import win32com.client


# ==================== 配置区域 ====================
# 源目录配置（编译后的程序所在目录，None 表示使用脚本所在目录）
SOURCE_BASE_DIR = None  # 例如: r"D:\Tools\.PyTools\PyHostsFileEdit\src\HostsfileEdit"
SOURCE_DIST_FOLDER = "dist/main.dist"  # 相对于 SOURCE_BASE_DIR 的路径

# 安装目标目录（程序将被复制到此目录下的 dist 文件夹）
INSTALL_BASE_DIR = r"D:\Tools\.PyTools\PyHostsFileEdit"

# 可执行文件名
EXE_NAME = "HostsFileEditor-Windows.exe"

# 快捷方式名称（不含 .lnk 后缀）
SHORTCUT_NAME = "HostsFileEditor-Windows"

# 快捷方式描述
SHORTCUT_DESCRIPTION = "Hosts 文件编辑工具"
# =================================================


def create_shortcut(target_path, shortcut_path, description=""):
    """创建 Windows 快捷方式"""
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(str(shortcut_path))
    shortcut.TargetPath = str(target_path)
    shortcut.WorkingDirectory = str(target_path.parent)
    shortcut.Description = description
    shortcut.IconLocation = str(target_path)
    shortcut.save()


def install_program():
    """安装程序到指定目录"""
    
    # 确定源基础目录
    if SOURCE_BASE_DIR is None:
        # 使用脚本所在目录
        source_base = Path(__file__).parent.absolute()
    else:
        # 使用配置的目录
        source_base = Path(SOURCE_BASE_DIR)
    
    # 源目录：编译后的程序文件夹
    source_dir = source_base / SOURCE_DIST_FOLDER
    
    # 使用配置的目标目录
    target_base = Path(INSTALL_BASE_DIR)
    target_dir = target_base / "dist"
    
    # 快捷方式目录
    shortcut_dir = target_base
    
    # 使用配置的可执行文件名
    exe_name = EXE_NAME
    
    print("=" * 60)
    print(f"开始安装 {EXE_NAME}")
    print("=" * 60)
    
    # 检查源目录是否存在
    if not source_dir.exists():
        print(f"错误: 找不到编译后的程序目录")
        print(f"请先运行 build.py 进行编译")
        print(f"期望目录: {source_dir}")
        sys.exit(1)
    
    # 检查可执行文件是否存在
    source_exe = source_dir / exe_name
    if not source_exe.exists():
        print(f"错误: 找不到可执行文件 {exe_name}")
        print(f"期望路径: {source_exe}")
        sys.exit(1)
    
    print(f"源目录: {source_dir}")
    print(f"目标目录: {target_dir}")
    print(f"快捷方式目录: {shortcut_dir}")
    print("=" * 60)
    
    try:
        # 创建目标目录（如果不存在）
        target_dir.mkdir(parents=True, exist_ok=True)
        print(f"\n✓ 创建目标目录: {target_dir}")
        
        # 如果目标目录已存在内容，先清空（保留目录本身）
        if target_dir.exists():
            print(f"✓ 清空目标目录...")
            for item in target_dir.iterdir():
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()
        
        # 复制 main.dist 内的所有文件到目标 dist 目录
        print(f"✓ 复制程序文件...")
        for item in source_dir.iterdir():
            if item.is_dir():
                shutil.copytree(item, target_dir / item.name)
            else:
                shutil.copy2(item, target_dir / item.name)
        print(f"  已复制到: {target_dir}")
        
        # 目标可执行文件路径
        target_exe = target_dir / exe_name
        
        # 创建快捷方式（使用配置的名称和描述）
        shortcut_path = shortcut_dir / f"{SHORTCUT_NAME}.lnk"
        print(f"\n✓ 创建快捷方式...")
        create_shortcut(
            target_exe,
            shortcut_path,
            description=SHORTCUT_DESCRIPTION
        )
        print(f"  快捷方式: {shortcut_path}")
        
        print("\n" + "=" * 60)
        print("安装成功！")
        print("=" * 60)
        print(f"程序目录: {target_dir}")
        print(f"可执行文件: {target_exe}")
        print(f"快捷方式: {shortcut_path}")
        print("\n可以通过以下方式启动程序:")
        print(f"1. 双击快捷方式: {shortcut_path}")
        print(f"2. 直接运行: {target_exe}")
        print("=" * 60)
        
        return 0
        
    except PermissionError as e:
        print("\n" + "=" * 60)
        print(f"错误: 权限不足")
        print(f"详情: {str(e)}")
        print("请以管理员身份运行此脚本")
        print("=" * 60)
        return 1
        
    except Exception as e:
        print("\n" + "=" * 60)
        print(f"安装失败: {str(e)}")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    # 检查是否安装了 pywin32
    try:
        import win32com.client
    except ImportError:
        print("错误: 未安装 pywin32")
        print("请运行: pip install pywin32")
        sys.exit(1)
    
    # 执行安装
    exit_code = install_program()
    sys.exit(exit_code)
