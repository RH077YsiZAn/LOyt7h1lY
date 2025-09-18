# 代码生成时间: 2025-09-18 13:12:41
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt

"""
统计数据分析器GUI程序
提供数据文件加载、分析和可视化功能
"""

class DataAnalyzer:
    def __init__(self, root):
        """初始化GUI界面"""
        self.root = root
        self.root.title("统计数据分析器")
        self.root.geometry("800x600")

        # 菜单栏
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # 文件菜单
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="打开", command=self.open_file)
        file_menu.add_command(label="退出", command=self.root.quit)
        menubar.add_cascade(label="文件", menu=file_menu)

        # 分析菜单
        analyze_menu = tk.Menu(menubar, tearoff=0)
        analyze_menu.add_command(label="分析数据", command=self.analyze_data)
        menubar.add_cascade(label="分析", menu=analyze_menu)

        # 可视化菜单
        visualize_menu = tk.Menu(menubar, tearoff=0)
        visualize_menu.add_command(label="绘制直方图", command=self.plot_histogram)
        menubar.add_cascade(label="可视化", menu=visualize_menu)

        # 数据分析结果显示区域
        self.result_area = tk.Text(self.root, height=20, width=80)
        self.result_area.pack()

    def open_file(self):
        """打开数据文件"""
        filename = filedialog.askopenfilename(title="选择数据文件", filetypes=[("CSV文件", "*.csv"), ("Excel文件", "*.xlsx")])
        if not filename:
            return
        try:
            self.data = pd.read_csv(filename)
            messagebox.showinfo("成功", "数据文件加载成功")
        except Exception as e:
            messagebox.showerror("错误", "加载文件失败: " + str(e))
        self.update_result_area("数据文件已加载")

    def analyze_data(self):
        "