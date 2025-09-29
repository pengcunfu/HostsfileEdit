from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QMessageBox, QListView, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QLabel, QTabWidget,
    QTextEdit, QGridLayout, QPlainTextEdit
)
from PySide6.QtCore import QStringListModel, Qt
from PySide6.QtGui import QFont
import sys
import os
import re
import subprocess


class HandleMain(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
        self.hosts_entries = []
        self.window = None
        self.new_value_dialog = None
        self.setupUi()

    def setupUi(self):
        """创建主界面UI"""
        self.setWindowTitle("Host文件修改工具")
        self.resize(717, 564)
        
        # 创建主布局
        layout = QVBoxLayout(self)
        
        # 创建功能按钮区域
        function_layout = QHBoxLayout()
        
        self.locate_file_btn = QPushButton("定位到文件")
        self.open_notepad_btn = QPushButton("在记事本中打开")
        self.env_vars_btn = QPushButton("环境变量")
        
        function_layout.addWidget(self.locate_file_btn)
        function_layout.addWidget(self.open_notepad_btn)
        function_layout.addWidget(self.env_vars_btn)
        function_layout.addStretch()  # 添加弹性空间
        
        layout.addLayout(function_layout)
        
        # 创建标签页
        self.tabWidget = QTabWidget()
        
        # Tab 1 - 文本编辑（调整顺序，文本编辑放前面）
        self.text_tab = QWidget()
        text_layout = QVBoxLayout(self.text_tab)
        
        # 创建文本编辑器
        self.hostsTextEdit = QPlainTextEdit()
        self.hostsTextEdit.setMinimumSize(701, 450)
        text_layout.addWidget(self.hostsTextEdit)
        
        # 创建文本编辑按钮布局
        text_button_layout = QHBoxLayout()
        text_button_layout.addStretch()
        
        self.loadButton = QPushButton("重新加载")
        self.saveButton = QPushButton("保存")
        
        text_button_layout.addWidget(self.loadButton)
        text_button_layout.addWidget(self.saveButton)
        
        text_layout.addLayout(text_button_layout)
        
        self.tabWidget.addTab(self.text_tab, "文本编辑")
        
        # Tab 2 - 按条编辑（原列表管理）
        self.list_tab = QWidget()
        list_layout = QVBoxLayout(self.list_tab)
        
        # 创建列表视图
        self.listView = QListView()
        self.listView.setMinimumSize(701, 450)
        self.listView.setStyleSheet("QListView{border:1px solid #0078d7}")
        list_layout.addWidget(self.listView)
        
        # 创建按钮布局
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # 添加弹性空间
        
        # 创建按钮
        self.pushButton_2 = QPushButton("添加")
        self.pushButton_3 = QPushButton("删除")
        self.pushButton = QPushButton("修改")
        
        button_layout.addWidget(self.pushButton_2)
        button_layout.addWidget(self.pushButton_3)
        button_layout.addWidget(self.pushButton)
        
        list_layout.addLayout(button_layout)
        
        self.tabWidget.addTab(self.list_tab, "按条编辑")
        
        layout.addWidget(self.tabWidget)
        
        # 连接信号
        self.pushButton.clicked.connect(self.handle_modify)  # 修改
        self.pushButton_2.clicked.connect(self.handle_add)   # 添加
        self.pushButton_3.clicked.connect(self.handle_delete) # 删除
        self.loadButton.clicked.connect(self.load_hosts_text) # 重新加载
        self.saveButton.clicked.connect(self.save_hosts_text) # 保存文本
        self.tabWidget.currentChanged.connect(self.on_tab_changed) # 标签页切换
        
        # 连接新功能按钮信号
        self.locate_file_btn.clicked.connect(self.locate_hosts_file)
        self.open_notepad_btn.clicked.connect(self.open_in_notepad)
        self.env_vars_btn.clicked.connect(self.open_env_vars)

    def setEvent(self, win):
        self.window = win
        self.load_hosts_file()

    def load_hosts_file(self):
        """加载hosts文件内容"""
        try:
            if os.path.exists(self.hosts_path):
                with open(self.hosts_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.parse_hosts_content(content)
                self.update_list_view()
                self.load_hosts_text()  # 同时加载到文本编辑器
            else:
                QMessageBox.warning(self, "警告", "找不到hosts文件")
        except PermissionError:
            QMessageBox.critical(self, "错误", "没有权限读取hosts文件，请以管理员身份运行")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"读取hosts文件失败: {str(e)}")

    def parse_hosts_content(self, content):
        """解析hosts文件内容"""
        self.hosts_entries = []
        lines = content.split('\n')
        for line_num, line in enumerate(lines):
            line = line.strip()
            if line and not line.startswith('#'):
                # 匹配IP和域名的正则表达式
                match = re.match(r'^(\S+)\s+(\S+)', line)
                if match:
                    ip, domain = match.groups()
                    self.hosts_entries.append({
                        'ip': ip,
                        'domain': domain,
                        'line_num': line_num,
                        'original_line': line
                    })

    def update_list_view(self):
        """更新列表视图"""
        model = QStringListModel()
        entries = [f"{entry['ip']}\t{entry['domain']}" for entry in self.hosts_entries]
        model.setStringList(entries)
        self.listView.setModel(model)

    def save_hosts_file(self):
        """保存hosts文件"""
        try:
            # 读取原始文件保留注释
            with open(self.hosts_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # 清除旧的非注释条目
            new_lines = []
            for line in lines:
                if line.strip().startswith('#') or not line.strip():
                    new_lines.append(line)
            
            # 添加新的条目
            for entry in self.hosts_entries:
                new_lines.append(f"{entry['ip']}\t{entry['domain']}\n")
            
            # 写入文件
            with open(self.hosts_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            
            QMessageBox.information(self, "成功", "hosts文件已保存")
        except PermissionError:
            QMessageBox.critical(self, "错误", "没有权限写入hosts文件，请以管理员身份运行")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"保存hosts文件失败: {str(e)}")

    def load_hosts_text(self):
        """加载hosts文件内容到文本编辑器"""
        try:
            if os.path.exists(self.hosts_path):
                with open(self.hosts_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.hostsTextEdit.setPlainText(content)
            else:
                QMessageBox.warning(self, "警告", "找不到hosts文件")
        except PermissionError:
            QMessageBox.critical(self, "错误", "没有权限读取hosts文件，请以管理员身份运行")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"读取hosts文件失败: {str(e)}")

    def save_hosts_text(self):
        """保存文本编辑器内容到hosts文件"""
        try:
            content = self.hostsTextEdit.toPlainText()
            with open(self.hosts_path, 'w', encoding='utf-8') as f:
                f.write(content)
            QMessageBox.information(self, "成功", "hosts文件已保存")
            # 重新解析内容并更新列表视图
            self.parse_hosts_content(content)
            self.update_list_view()
        except PermissionError:
            QMessageBox.critical(self, "错误", "没有权限写入hosts文件，请以管理员身份运行")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"保存hosts文件失败: {str(e)}")

    def on_tab_changed(self, index):
        """处理标签页切换"""
        if index == 0:  # 切换到文本编辑标签页
            self.load_hosts_text()
        elif index == 1:  # 切换到按条编辑标签页
            # 可以在这里添加从文本编辑器同步到列表的逻辑
            pass
    
    def locate_hosts_file(self):
        """定位到hosts文件"""
        try:
            # 使用Windows资源管理器打开并选中hosts文件
            result = subprocess.run(['explorer', '/select,', self.hosts_path], capture_output=True)
            # 不检查返回码，因为explorer命令即使成功也可能返回非零值
            QMessageBox.information(self, "成功", "已在资源管理器中定位到hosts文件")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"无法定位到文件: {str(e)}")
    
    def open_in_notepad(self):
        """在记事本中打开hosts文件"""
        try:
            subprocess.run(['notepad', self.hosts_path], check=True)
        except Exception as e:
            QMessageBox.critical(self, "错误", f"无法在记事本中打开文件: {str(e)}")
    
    def open_env_vars(self):
        """打开Windows环境变量设置"""
        try:
            # 打开系统属性的环境变量页面
            subprocess.run(['rundll32', 'sysdm.cpl,EditEnvironmentVariables'], check=True)
        except Exception as e:
            QMessageBox.critical(self, "错误", f"无法打开环境变量设置: {str(e)}")

    def handle_modify(self):
        """修改选中的条目"""
        selection = self.listView.selectionModel().selectedIndexes()
        if not selection:
            QMessageBox.warning(self, "警告", "请先选择要修改的条目")
            return
        
        index = selection[0].row()
        if 0 <= index < len(self.hosts_entries):
            entry = self.hosts_entries[index]
            self.show_edit_dialog(entry, index)

    def handle_add(self):
        """添加新条目"""
        self.show_edit_dialog(None, -1)

    def handle_delete(self):
        """删除选中的条目"""
        selection = self.listView.selectionModel().selectedIndexes()
        if not selection:
            QMessageBox.warning(self, "警告", "请先选择要删除的条目")
            return
        
        reply = QMessageBox.question(self, "确认", "确定要删除选中的条目吗？",
                                   QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            index = selection[0].row()
            if 0 <= index < len(self.hosts_entries):
                del self.hosts_entries[index]
                self.update_list_view()
                self.save_hosts_file()

    def show_edit_dialog(self, entry, index):
        """显示编辑对话框"""
        if hasattr(self, 'new_value_dialog') and self.new_value_dialog:
            self.new_value_dialog.show_dialog(entry, index, self.on_dialog_result)

    def on_dialog_result(self, result, entry_data, index):
        """处理对话框结果"""
        if result:
            if index >= 0:  # 修改
                self.hosts_entries[index] = entry_data
            else:  # 添加
                self.hosts_entries.append(entry_data)
            self.update_list_view()
            self.save_hosts_file()


class HandleNewValue(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.callback = None
        self.current_entry = None
        self.current_index = -1
        self.setupUi()

    def setupUi(self):
        """创建对话框UI"""
        self.setWindowTitle("Dialog")
        self.resize(350, 180)
        
        # 创建主布局
        layout = QVBoxLayout(self)
        
        # 创建输入区域
        input_layout = QVBoxLayout()
        
        # IP地址输入
        ip_layout = QHBoxLayout()
        self.ip_label = QLabel("IP地址:")
        self.ip_label.setMinimumWidth(60)
        self.ip_input = QTextEdit()
        self.ip_input.setMaximumHeight(31)
        self.ip_input.setPlaceholderText("请输入IP地址，如: 127.0.0.1")
        ip_layout.addWidget(self.ip_label)
        ip_layout.addWidget(self.ip_input)
        
        # 域名输入
        domain_layout = QHBoxLayout()
        self.domain_label = QLabel("域名:")
        self.domain_label.setMinimumWidth(60)
        self.domain_input = QTextEdit()
        self.domain_input.setMaximumHeight(31)
        self.domain_input.setPlaceholderText("请输入域名，如: www.example.com")
        domain_layout.addWidget(self.domain_label)
        domain_layout.addWidget(self.domain_input)
        
        input_layout.addLayout(ip_layout)
        input_layout.addLayout(domain_layout)
        layout.addLayout(input_layout)
        
        # 创建按钮布局
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        self.confirm_button = QPushButton("确定")
        self.cancel_button = QPushButton("取消")
        button_layout.addWidget(self.confirm_button)
        button_layout.addWidget(self.cancel_button)
        
        layout.addLayout(button_layout)
        
        # 连接信号
        self.confirm_button.clicked.connect(self.handle_confirm)
        self.cancel_button.clicked.connect(self.handle_cancel)

    def setEvent(self, win):
        # 这个方法保留为了兼容性，但实际上不需要了
        pass

    def show_dialog(self, entry, index, callback):
        """显示对话框"""
        self.current_entry = entry
        self.current_index = index
        self.callback = callback
        
        if entry:  # 修改模式
            self.setWindowTitle("修改hosts条目")
            # 填充现有数据
            self.ip_input.setPlainText(entry['ip'])
            self.domain_input.setPlainText(entry['domain'])
        else:  # 添加模式
            self.setWindowTitle("添加hosts条目")
            # 清空输入框
            self.ip_input.clear()
            self.domain_input.clear()
        
        self.exec()

    def handle_confirm(self):
        """处理确认输入"""
        ip = self.ip_input.toPlainText().strip()
        domain = self.domain_input.toPlainText().strip()
        
        if not ip or not domain:
            QMessageBox.warning(self, "警告", "请输入IP地址和域名")
            return
        
        if not self.validate_ip(ip):
            QMessageBox.warning(self, "警告", "请输入有效的IP地址")
            return
        
        entry_data = {
            'ip': ip,
            'domain': domain,
            'line_num': 0,
            'original_line': f"{ip} {domain}"
        }
        
        if self.callback:
            self.callback(True, entry_data, self.current_index)
        
        self.accept()

    def handle_cancel(self):
        """处理取消"""
        if self.callback:
            self.callback(False, None, self.current_index)
        self.reject()

    def validate_ip(self, ip):
        """验证IP地址格式"""
        # 简单的IP地址验证
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        try:
            for part in parts:
                num = int(part)
                if num < 0 or num > 255:
                    return False
            return True
        except ValueError:
            return False


class WindowHandle():
    def __init__(self) -> None:
        self.main = None
        self.dlg = None

    def handle(self):
        # 创建主窗口
        self.ui1 = HandleMain()
        self.ui1.setEvent(None)  # 传入None，因为HandleMain现在是独立的widget
        
        # 创建对话框
        self.ui2 = HandleNewValue()
        
        # 连接主窗口和对话框
        self.ui1.new_value_dialog = self.ui2

        # 显示主窗口
        self.ui1.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowHandle()
    win.handle()
    sys.exit(app.exec())
