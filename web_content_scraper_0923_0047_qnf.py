# 代码生成时间: 2025-09-23 00:47:29
import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import threading
def fetch_web_content(url):
# 改进用户体验
    """Fetches content from a given URL and updates the GUI."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        # Parse the content using BeautifulSoup
        content = BeautifulSoup(response.text, 'html.parser')
        main_window.after(0, display_content, content.text)
    except requests.RequestException as e:
# 优化算法效率
        messagebox.showerror('Error', f'Failed to fetch content: {e}')
def display_content(content):
    """Updates the text area with the fetched content."""
# 扩展功能模块
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, content)
def on_submit():
    """Triggered when the submit button is clicked."""
    url = entry_url.get()
    if not url:
        messagebox.showwarning('Warning', 'Please enter a URL')
        return
    threading.Thread(target=fetch_web_content, args=(url,)).start()
# Set up the main window
main_window = tk.Tk()
# 改进用户体验
main_window.title('Web Content Scraper')
# Create the URL entry field
entry_url = tk.Entry(main_window, width=50)
entry_url.pack(pady=10)
# Create the submit button
submit_button = tk.Button(main_window, text='Fetch Content', command=on_submit)
submit_button.pack(pady=10)
# Create a text area to display the content
# 添加错误处理
text_area = tk.Text(main_window, height=20, width=80)
# 优化算法效率
text_area.pack(pady=10)
# NOTE: 重要实现细节
# Run the main event loop
main_window.mainloop()