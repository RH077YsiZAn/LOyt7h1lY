# 代码生成时间: 2025-10-07 19:14:43
import tkinter as tk
from tkinter import ttk
import time
import threading


"""
A tkinter application that demonstrates a progress bar and a loading animation.
"""

class ProgressBarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Progress Bar and Loading Animation")
        self.geometry("400x200")

        # Initialize the progress bar
        self.progress = 0
        self.max_progress = 100
        self.status_label = ttk.Label(self, text="Loading...")
        self.status_label.pack(pady=20)

        # Create the progress bar widget
        self.progress_bar = ttk.Progressbar(self,
                                          orient=tk.HORIZONTAL,
                                          length=200,
                                          mode='determinate')
        self.progress_bar.pack(pady=10)

        # Start the loading animation in a separate thread
        self.start_loading_thread()

    def update_progress(self):
        try:
            for i in range(self.max_progress + 1):
                self.update_idletasks()  # Update the GUI
                time.sleep(0.1)  # Simulate work being done
                self.progress_bar['value'] = i
                self.status_label['text'] = f"Loading... {i}%"
        except Exception as e:
            self.status_label['text'] = "Error: " + str(e)

    def start_loading_thread(self):
        # Create a thread for the loading animation
        loading_thread = threading.Thread(target=self.update_progress)
        loading_thread.daemon = True  # Allow the program to exit even if the thread is still running
        loading_thread.start()

    def on_closing(self):
        # Clean up on window close
        self.destroy()

if __name__ == "__main__":
    app = ProgressBarApp()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)  # Catch window close event
    app.mainloop()