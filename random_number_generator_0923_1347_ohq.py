# 代码生成时间: 2025-09-23 13:47:23
import tkinter as tk
from tkinter import messagebox
import random

"""随机数生成器程序，使用Tkinter框架。"""

class RandomNumberGenerator:
    """随机数生成器的主类。"""
    def __init__(self, master):
        self.master = master
        self.master.title('随机数生成器')

        # 设置布局
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        # 输入设置
        self.label = tk.Label(self.frame, text='输入最小和最大值：')
        self.label.pack()

        self.min_entry = tk.Entry(self.frame, width=10)
        self.min_entry.pack(side=tk.LEFT, padx=5)

        self.max_entry = tk.Entry(self.frame, width=10)
        self.max_entry.pack(side=tk.LEFT, padx=5)

        # 按钮设置
        self.generate_button = tk.Button(self.frame, text='生成随机数', command=self.generate_random)
        self.generate_button.pack(side=tk.LEFT, padx=5)

        # 显示设置
        self.result_label = tk.Label(self.master, text='', font=('Helvetica', 16))
        self.result_label.pack(pady=10)

    def generate_random(self):
        """生成随机数并显示结果。"""
        try:
            min_value = int(self.min_entry.get())
            max_value = int(self.max_entry.get())
            if min_value > max_value:
                messagebox.showerror('错误', '最小值不能大于最大值！')
                return
            random_number = random.randint(min_value, max_value)
            self.result_label.config(text=str(random_number))
        except ValueError:
            messagebox.showerror('错误', '请输入有效的整数！')

def main():
    "