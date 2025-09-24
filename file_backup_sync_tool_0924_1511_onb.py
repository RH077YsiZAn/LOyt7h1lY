# 代码生成时间: 2025-09-24 15:11:00
import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

"""
文件备份和同步工具
使用Python和Tkinter框架创建
"""

class FileBackupSyncTool:
    def __init__(self, master):
        """初始化GUI界面"""
        self.master = master
        self.master.title('文件备份和同步工具')
        self.master.geometry('400x200')

        self.source_label = tk.Label(master, text='源文件夹：')
        self.source_label.grid(row=0, column=0)
        self.source_entry = tk.Entry(master, width=40)
        self.source_entry.grid(row=0, column=1)
        self.source_button = tk.Button(master, text='浏览', command=self.select_source_folder)
        self.source_button.grid(row=0, column=2)

        self.target_label = tk.Label(master, text='目标文件夹：')
        self.target_label.grid(row=1, column=0)
        self.target_entry = tk.Entry(master, width=40)
        self.target_entry.grid(row=1, column=1)
        self.target_button = tk.Button(master, text='浏览', command=self.select_target_folder)
        self.target_button.grid(row=1, column=2)

        self.backup_button = tk.Button(master, text='备份文件', command=self.backup_files)
        self.backup_button.grid(row=2, column=0, columnspan=3)

    def select_source_folder(self):
        "