# 代码生成时间: 2025-09-18 00:03:37
import tkinter as tk
from tkinter import filedialog, messagebox
import logging
from logging.handlers import TimedRotatingFileHandler
import os

# 配置日志
def setup_logging(log_filename, log_level=logging.INFO):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    handler = TimedRotatingFileHandler(f'logs/{log_filename}', when='midnight', backupCount=7)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.setLevel(log_level)
    logger.addHandler(handler)
    return logger

# GUI界面
class SecurityAuditLogApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Security Audit Log')
        self.root.geometry('400x200')
        
        self.logger = setup_logging('audit.log')
        
        self.create_widgets()

    def create_widgets(self):
        # 按钮：导出日志
        btn_export = tk.Button(self.root, text='Export Log', command=self.export_log)
        btn_export.pack(pady=20)
        
    def export_log(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')], title='Save Log File')
            if file_path:
                with open('logs/audit.log', 'r') as file:
                    with open(file_path, 'w') as new_file:
                        new_file.write(file.read())
                messagebox.showinfo('Success', 'Log file exported successfully.')
        except Exception as e:
            self.logger.error(f'Error exporting log: {e}')
            messagebox.showerror('Error', f'An error occurred: {e}')

# 主函数
def main():
    root = tk.Tk()
    app = SecurityAuditLogApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()