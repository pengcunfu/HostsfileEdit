#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hosts文件编辑工具 - 版本发布脚本

使用方法:
1. 交互式发布: python scripts/release.py
2. 指定版本: python scripts/release.py 1.0.0
3. 列出版本: python scripts/release.py --list
4. 模拟运行: python scripts/release.py 1.0.0 --dry-run

支持的命令选项:
--help, -h      显示帮助信息
--no-update     不更新代码中的版本号
--message "..." 指定发布消息
--dry-run       模拟运行，不实际执行
--list, -l      列出所有发布版本

功能特性:
- 自动检测Git状态，确保干净的工作目录
- 从main.py读取当前版本号，支持语义化版本
- 自动更新代码中的版本号
- 创建Git标签并推送到远程
- 触发GitHub Actions自动构建多平台可执行文件
- 生成包含更新内容的发布说明
"""

import os
import sys
import subprocess
import re
import argparse
from datetime import datetime
from typing import Optional, List, Tuple

class ReleaseManager:
    """版本发布管理器"""

    def __init__(self):
        self.root_dir = self._get_project_root()
        os.chdir(self.root_dir)

    def _get_project_root(self) -> str:
        """获取项目根目录"""
        current = os.path.dirname(os.path.abspath(__file__))
        parent = os.path.dirname(current)
        if os.path.exists(os.path.join(parent, 'main.py')):
            return parent
        raise FileNotFoundError("无法找到项目根目录")

    def _run_command(self, cmd: List[str], check: bool = True) -> subprocess.CompletedProcess:
        """执行命令"""
        print(f"执行命令: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True, check=check)
        return result

    def _get_current_version(self) -> str:
        """从main.py获取当前版本"""
        try:
            with open('main.py', 'r', encoding='utf-8') as f:
                content = f.read()
                # 查找版本信息行，格式如: __version__ = "1.0.0"
                match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', content)
                if match:
                    return match.group(1)
                else:
                    # 如果没找到版本信息，提示用户
                    print("⚠️ 未在main.py中找到__version__定义")
                    return None
        except FileNotFoundError:
            print("❌ 找不到main.py文件")
            return None

    def _update_version(self, new_version: str) -> bool:
        """更新main.py中的版本号"""
        try:
            with open('main.py', 'r', encoding='utf-8') as f:
                content = f.read()

            # 更新版本号
            if '__version__' in content:
                content = re.sub(
                    r'__version__\s*=\s*["\'][^"\']+["\']',
                    f'__version__ = "{new_version}"',
                    content
                )
            else:
                # 如果没有版本信息，在文件开头添加
                version_line = f'__version__ = "{new_version}"\n'
                content = version_line + content

            with open('main.py', 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"✅ 版本号已更新为: {new_version}")
            return True
        except Exception as e:
            print(f"❌ 更新版本号失败: {e}")
            return False

    def _validate_version(self, version: str) -> bool:
        """验证版本号格式 (语义化版本)"""
        pattern = r'^v?\d+\.\d+\.\d+(?:-[a-zA-Z0-9]+)?$'
        return bool(re.match(pattern, version))

    def _get_git_status(self) -> Tuple[bool, str]:
        """检查Git状态"""
        try:
            result = self._run_command(['git', 'status', '--porcelain'])
            if result.stdout.strip():
                return False, "工作目录有未提交的更改"

            # 检查是否与远程同步
            result = self._run_command(['git', 'rev-parse', '@{u}'])
            remote_commit = result.stdout.strip()
            result = self._run_command(['git', 'rev-parse', 'HEAD'])
            local_commit = result.stdout.strip()

            if local_commit != remote_commit:
                return False, "本地分支与远程不同步"

            return True, "Git状态正常"
        except subprocess.CalledProcessError as e:
            return False, f"Git检查失败: {e}"

    def _create_tag(self, version: str, message: Optional[str] = None) -> bool:
        """创建Git标签"""
        tag_name = version if version.startswith('v') else f'v{version}'

        if message is None:
            message = f"发布版本 {tag_name}"

        try:
            # 创建标签
            self._run_command(['git', 'tag', '-a', tag_name, '-m', message])
            print(f"✅ 创建标签: {tag_name}")

            # 推送标签
            self._run_command(['git', 'push', 'origin', tag_name])
            print(f"✅ 推送标签到远程: {tag_name}")

            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ 创建或推送标签失败: {e}")
            return False

    def _get_changelog(self, version: str) -> str:
        """获取最近的更改内容"""
        try:
            # 获取上一个标签
            result = self._run_command(['git', 'describe', '--tags', '--abbrev=0', 'HEAD^'])
            if result.returncode == 0:
                prev_tag = result.stdout.strip()
                diff_result = self._run_command(['git', 'log', '--oneline',
                                                f'{prev_tag}..HEAD'])
                commits = diff_result.stdout.strip()
            else:
                # 如果没有上一个标签，获取最近10次提交
                diff_result = self._run_command(['git', 'log', '--oneline', '-10'])
                commits = diff_result.stdout.strip()

            if commits:
                changelog = "### 📝 更新内容\n\n"
                for line in commits.split('\n'):
                    if line.strip():
                        hash_part, *message_parts = line.split(' ', 1)
                        if message_parts:
                            changelog += f"- {message_parts[0]}\n"
                return changelog
            else:
                return "- 初始发布\n"
        except Exception as e:
            print(f"⚠️ 获取更改内容失败: {e}")
            return "- 各种改进和修复\n"

    def release_version(self, version: Optional[str] = None,
                       update_code: bool = True,
                       message: Optional[str] = None,
                       dry_run: bool = False) -> bool:
        """发布版本的主流程"""

        print("🚀 Hosts文件编辑工具 - 版本发布脚本")
        print("=" * 50)

        # 1. 检查Git状态
        print("\n📋 检查Git状态...")
        status_ok, status_msg = self._get_git_status()
        if not status_ok:
            print(f"❌ {status_msg}")
            print("请先提交所有更改并同步远程仓库")
            return False
        print(f"✅ {status_msg}")

        # 2. 处理版本号
        if version is None:
            current_version = self._get_current_version()
            if current_version:
                print(f"📦 当前版本: {current_version}")

                # 建议新版本号
                parts = current_version.split('.')
                if len(parts) >= 3:
                    patch = int(parts[2]) + 1
                    suggested_version = f"{parts[0]}.{parts[1]}.{patch}"
                else:
                    suggested_version = "1.0.1"

                version = input(f"请输入新版本号 (建议: {suggested_version}): ").strip()
                if not version:
                    version = suggested_version
            else:
                version = input("请输入版本号 (如: 1.0.0): ").strip()

        if not self._validate_version(version):
            print(f"❌ 版本号格式无效: {version}")
            print("请使用语义化版本号，如: 1.0.0, 2.1.3, 3.0.0-beta")
            return False

        # 3. 更新代码中的版本号
        if update_code:
            print(f"\n📝 更新版本号...")
            if not self._update_version(version):
                return False

        # 4. 提交版本更新
        if update_code:
            print(f"\n💾 提交版本更新...")
            try:
                self._run_command(['git', 'add', 'main.py'])
                commit_msg = f"更新版本号到 {version}"
                self._run_command(['git', 'commit', '-m', commit_msg])
                self._run_command(['git', 'push'])
                print(f"✅ 版本更新已提交")
            except subprocess.CalledProcessError as e:
                print(f"❌ 提交版本更新失败: {e}")
                return False

        # 5. 创建标签
        if not dry_run:
            print(f"\n🏷️ 创建发布标签...")
            if message is None:
                changelog = self._get_changelog(version)
                message = f"发布版本 {version}\n\n{changelog}"

            if not self._create_tag(version, message):
                return False

        # 6. 显示发布信息
        tag_name = version if version.startswith('v') else f'v{version}'
        print(f"\n🎉 版本发布完成!")
        print("=" * 50)
        print(f"📦 版本号: {version}")
        print(f"🏷️ 标签: {tag_name}")
        print(f"🌐 GitHub Actions将在几分钟后开始构建")
        print(f"📥 发布地址: https://github.com/yourusername/HostsFileEdit/releases/tag/{tag_name}")
        print("\n⏳ 等待GitHub Actions完成构建...")
        print("   你可以在GitHub Actions页面查看构建进度")

        return True

    def list_releases(self) -> None:
        """列出所有发布版本"""
        print("\n📋 已发布的版本:")
        print("-" * 30)

        try:
            result = self._run_command(['git', 'tag', '-l', 'v*'])
            tags = result.stdout.strip().split('\n') if result.stdout.strip() else []

            if tags:
                for tag in sorted(tags, reverse=True):
                    try:
                        date_result = self._run_command(['git', 'log', '-1', '--format=%ai', tag])
                        date = date_result.stdout.strip().split(' ')[0]
                        print(f"  {tag} ({date})")
                    except:
                        print(f"  {tag}")
            else:
                print("  暂无发布版本")
        except subprocess.CalledProcessError as e:
            print(f"  ❌ 获取版本列表失败: {e}")

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='Hosts文件编辑工具 - 版本发布脚本')
    parser.add_argument('version', nargs='?', help='版本号 (如: 1.0.0)')
    parser.add_argument('--no-update', action='store_true', help='不更新代码中的版本号')
    parser.add_argument('--message', '-m', help='发布消息')
    parser.add_argument('--dry-run', action='store_true', help='模拟运行，不实际执行')
    parser.add_argument('--list', '-l', action='store_true', help='列出所有发布版本')

    args = parser.parse_args()

    try:
        manager = ReleaseManager()

        if args.list:
            manager.list_releases()
            return

        success = manager.release_version(
            version=args.version,
            update_code=not args.no_update,
            message=args.message,
            dry_run=args.dry_run
        )

        if success:
            print("\n✅ 发布成功!")
            sys.exit(0)
        else:
            print("\n❌ 发布失败!")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n\n⚠️ 用户取消操作")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()