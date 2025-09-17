# 代码生成时间: 2025-09-18 06:42:03
import tkinter as tk
from tkinter import ttk
import psutil
import subprocess
# 扩展功能模块

"""
进程管理器程序，使用Python和Tkinter框架。
允许用户查看系统进程，并进行终止操作。
"""
# 改进用户体验

class ProcessManager:
    def __init__(self, root):
# 优化算法效率
        """初始化进程管理器界面。"""
        self.root = root
        self.root.title('进程管理器')
        self.root.geometry('600x400')

        # 创建TreeView组件显示进程信息
        self.tree = ttk.Treeview(self.root, columns=('PID', '进程名', '内存使用'),
# NOTE: 重要实现细节
                               show='headings')
        self.tree.heading('PID', text='PID')
        self.tree.heading('进程名', text='进程名')
        self.tree.heading('内存使用', text='内存使用 (MB)')
        self.tree.pack(pady=20)

        # 填充进程信息到TreeView
        self.update_processes()

        # 创建按钮，用于终止选中的进程
        self.terminate_btn = ttk.Button(self.root, text='终止进程', command=self.terminate_process)
        self.terminate_btn.pack(pady=10)

    def update_processes(self):
        """更新TreeView中的进程信息。"""
        self.tree.delete(*self.tree.get_children())  # 清除旧的进程信息
# 添加错误处理
        for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
# 优化算法效率
            try:
                pid = proc.info['pid']
                name = proc.info['name']
                memory_usage = proc.info['memory_info'].rss / (1024 * 1024)  # 转换为MB
                self.tree.insert('', 'end', values=(pid, name, memory_usage))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
# 改进用户体验
                pass

    def terminate_process(self):
        """终止选中的进程。"""
        selected = self.tree.selection()
        if not selected:
            return

        pid = self.tree.item(selected[0], 'values')[0]
        try:
            process = psutil.Process(int(pid))
            process.terminate()
# 优化算法效率
            self.update_processes()  # 更新进程列表
        except psutil.NoSuchProcess:
# TODO: 优化性能
            tk.messagebox.showerror('错误', '进程不存在。')
        except psutil.AccessDenied:
# 扩展功能模块
            tk.messagebox.showerror('错误', '没有权限终止该进程。')
        except Exception as e:
# 添加错误处理
            tk.messagebox.showerror('错误', str(e))

def main():
    """程序入口点。"""
    root = tk.Tk()
# 添加错误处理
    app = ProcessManager(root)
    root.mainloop()

if __name__ == '__main__':
    main()