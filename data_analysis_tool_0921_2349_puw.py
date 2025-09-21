# 代码生成时间: 2025-09-21 23:49:25
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from pandas.plotting import parallel_coordinates
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

"""
数据统计分析器，使用TKINTER框架创建GUI。
支持用户上传数据文件，进行数据预览、统计分析和结果展示。
"""

class DataAnalysisTool:
    def __init__(self, root):
        """初始化GUI界面"""
        self.root = root
        self.root.title("数据统计分析器")
        self.root.geometry("800x600")
        
        # 添加文件选择按钮
        self.btn_load = tk.Button(root, text="加载数据文件", command=self.load_data)
        self.btn_load.pack()
        
        # 添加数据预览区域
        self.text_preview = tk.Text(root, height=10, width=50)
        self.text_preview.pack()
        
        # 添加统计分析按钮
        self.btn_analyze = tk.Button(root, text="统计分析", command=self.analyze_data)
        self.btn_analyze.pack()
        
        # 添加结果显示区域
        self.text_result = tk.Text(root, height=10, width=50)
        self.text_result.pack()
        
    def load_data(self):
        "