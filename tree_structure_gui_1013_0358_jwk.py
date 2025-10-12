# 代码生成时间: 2025-10-13 03:58:22
import tkinter as tk
from tkinter import ttk

"""
A simple GUI application that demonstrates the use of the Treeview widget
to create a tree structure.
"""

class TreeStructureGUI:
    def __init__(self, root):
        """
        Initialize the GUI with the tree structure.
        :param root: The root window of the application.
        """
        self.root = root
        self.root.title('Tree Structure GUI')

        # Create a Treeview widget
        self.tree = ttk.Treeview(root)
        self.tree['columns'] = ('one', 'two')
        self.tree['show'] = 'headings'
        self.tree.column('#0', width=200, minwidth=100, stretch=tk.NO)
        self.tree.heading('#0', text='Item')
        self.tree.column('one', width=100, minwidth=50, stretch=tk.NO)
        self.tree.heading('one', text='Description')
        self.tree.column('two', width=100, minwidth=50, stretch=tk.NO)
        self.tree.heading('two', text='Value')

        # Define the structure of the tree
        self.tree.insert('', 'end', text='Node 1', values=('Description 1', 'Value 1'))
        self.tree.insert('', 'end', text='Node 2', values=('Description 2', 'Value 2'))

        # Insert a child node under Node 1
        self.tree.insert('Node 1', 'end', text='Child Node 1', values=('Description 3', 'Value 3'))

        # Pack the Treeview widget
        self.tree.pack(expand=True, fill=tk.BOTH)

    def run(self):
        """
        Start the GUI event loop.
        """
        self.root.mainloop()

# Create the main window
root = tk.Tk()

# Create an instance of the TreeStructureGUI class
gui = TreeStructureGUI(root)

# Run the GUI
gui.run()