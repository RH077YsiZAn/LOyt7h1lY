# 代码生成时间: 2025-10-10 20:41:47
import tkinter as tk
from tkinter import messagebox

"""
健康风险评估程序
"""

class HealthRiskAssessmentApp:
    def __init__(self, master):
        """
        初始化界面
        :param master: tkinter的主窗口
        """
        self.master = master
        self.master.title("健康风险评估")

        # 创建输入框和标签
        self.create_widgets()

    def create_widgets(self):
        """创建界面元素"""
        # 年龄输入框
        tk.Label(self.master, text="年龄").grid(row=0, column=0, padx=10, pady=10)
        self.age_entry = tk.Entry(self.master)
        self.age_entry.grid(row=0, column=1, padx=10, pady=10)

        # 体重输入框
        tk.Label(self.master, text="体重（kg）").grid(row=1, column=0, padx=10, pady=10)
        self.weight_entry = tk.Entry(self.master)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=10)

        # 开始评估按钮
        tk.Button(self.master, text="开始评估", command=self.assess_risk).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def assess_risk(self):
        """评估健康风险"""
        try:
            # 获取用户输入
            age = int(self.age_entry.get())
            weight = float(self.weight_entry.get())

            # 简单的风险评估逻辑（示例）
            if age < 18 or age > 100:
                messagebox.showerror("错误", "请输入一个有效的年龄。")
                return
            if weight < 30 or weight > 200:
                messagebox.showerror("错误", "请输入一个有效的体重。")
                return

            # 这里可以根据实际情况添加更复杂的评估逻辑
            risk_level = "低风险"
            if age > 50 and weight > 80:
                risk_level = "高风险"
            elif age > 40 and weight > 70:
                risk_level = "中等风险"

            # 显示评估结果
            messagebox.showinfo("评估结果", f"您的健康风险等级为：{risk_level}")
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字。")

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthRiskAssessmentApp(root)
    root.mainloop()