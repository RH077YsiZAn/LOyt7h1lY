# 代码生成时间: 2025-09-20 20:58:22
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

"""
Folder Structure Organizer

This Python program uses the Tkinter framework to create a graphical user interface
for organizing folder structures. The program allows users to select a folder and
then organizes its contents into subfolders based on file extensions.
"""

class FolderStructureOrganizer:
    def __init__(self, root):
        """Initialize the GUI with a Tkinter window."""
        self.root = root
        self.root.title("Folder Structure Organizer")
        self.root.geometry("400x200")

        # Create a label and button to select a folder
        label = tk.Label(root, text="Select a folder to organize:")
        label.pack(pady=10)

        button = tk.Button(root, text="Select Folder", command=self.select_folder)
        button.pack(pady=5)

        # Create a button to start the organization process
        self.organize_button = tk.Button(root, text="Organize Folder", command=self.organize_folder)
        self.organize_button.pack(pady=5)
        self.organize_button.config(state="disabled")  # Disable initially

        # Create a label to display the status message
        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=10)

    def select_folder(self):
        "