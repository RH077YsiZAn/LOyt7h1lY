# 代码生成时间: 2025-09-21 20:10:54
import tkinter as tk
from tkinter import messagebox
import threading
import time
import requests

"""
性能测试脚本程序
本程序使用Python和Tkinter框架创建一个简单的图形界面，用于执行性能测试。
用户可以输入URL，并选择测试次数，程序会在后台线程中进行HTTP请求测试。
"""

class PerformanceTestApp:
    def __init__(self, master):
        """初始化界面"""
        self.master = master
        master.title("性能测试脚本")
        
        # URL输入框
        self.url_label = tk.Label(master, text="请输入测试URL：")
        self.url_label.grid(row=0, column=0)
        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.grid(row=0, column=1)
        
        # 测试次数输入框
        self.times_label = tk.Label(master, text="请输入测试次数：")
        self.times_label.grid(row=1, column=0)
        self.times_entry = tk.Entry(master, width=50)
        self.times_entry.grid(row=1, column=1)
        
        # 开始测试按钮
        self.start_button = tk.Button(master, text="开始测试", command=self.start_test)
        self.start_button.grid(row=2, column=0, columnspan=2)
        
        # 结果显示标签
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=3, column=0, columnspan=2)
        
    def start_test(self):
        """开始性能测试"""
        url = self.url_entry.get()
        times = self.times_entry.get()
        
        # 错误处理
        if not url or not times:
            messagebox.showerror("错误", "URL和测试次数不能为空！")
            return
        try:
            times = int(times)
        except ValueError:
            messagebox.showerror("错误", "测试次数必须是整数！")
            return
        
        self.result_label.config(text="测试中，请稍候...")
        self.master.update()
        
        # 后台线程执行测试
        threading.Thread(target=self.run_test, args=(url, times)).start()
        
    def run_test(self, url, times):
        """执行性能测试"""
        start_time = time.time()
        total_time = 0
        
        for _ in range(times):
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()  # 检查请求是否成功
                total_time += response.elapsed.total_seconds()
            except requests.RequestException as e:
                self.result_label.config(text=f"请求失败：{e}")
                return
        
        avg_time = total_time / times
        self.result_label.config(text=f"测试完成！平均响应时间：{avg_time:.2f}秒")

if __name__ == "__main__":
    root = tk.Tk()
    app = PerformanceTestApp(root)
    root.mainloop()