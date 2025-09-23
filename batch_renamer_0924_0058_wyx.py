# 代码生成时间: 2025-09-24 00:58:23
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

"""
批量文件重命名工具
使用TKINTER框架创建的图形界面，允许用户选择一个文件夹并批量重命名文件。
"""

class BatchRenamer:
    """批量文件重命名类"""
    def __init__(self, root):
        """初始化界面"""
        self.root = root
        self.root.title("批量文件重命名工具")
        self.root.geometry("400x200")

        # 创建文件夹选择按钮
        self.select_folder_btn = tk.Button(self.root, text="选择文件夹", command=self.select_folder)
        self.select_folder_btn.pack(pady=20)

        # 创建重命名按钮
        self.rename_btn = tk.Button(self.root, text="重命名文件", command=self.rename_files)
        self.rename_btn.pack(pady=10)

        self.folder_path = ""
        self.current_folder = ""

    def select_folder(self):
        "