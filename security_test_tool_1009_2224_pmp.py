# 代码生成时间: 2025-10-09 22:24:53
import tkinter as tk
from tkinter import messagebox
import os

"""安全测试工具GUI界面"""

class SecurityTestTool:
    def __init__(self, master=None):
        self.master = master
        self.master.title("安全测试工具")
        self.create_widgets()

    def create_widgets(self):
        # 文件选择按钮
        self.button_select_file = tk.Button(self.master, text="选择文件", command=self.select_file)
        self.button_select_file.pack()

        # 文本框显示文件内容
        self.text_box = tk.Text(self.master, height=15, width=60)
        self.text_box.pack()

        # 安全测试按钮
        self.button_test = tk.Button(self.master, text="进行安全测试", command=self.test_security)
        self.button_test.pack()

        # 结果显示标签
        self.label_result = tk.Label(self.master, text="")
        self.label_result.pack()

    def select_file(self):
        "