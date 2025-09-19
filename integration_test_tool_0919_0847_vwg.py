# 代码生成时间: 2025-09-19 08:47:29
import tkinter as tk
from tkinter import messagebox
import subprocess


class IntegrationTestTool:
    """
    A simple integration test tool using tkinter framework.
    This tool allows users to run integration tests and display results.
    """

    def __init__(self, master):
        """
        Initialize the main window of the integration test tool.
        """
        self.master = master
        self.master.title('Integration Test Tool')

        # Create input field for test command
        self.label = tk.Label(master, text='Test Command:')
        self.label.pack()
        self.entry = tk.Entry(master, width=50)
        self.entry.pack()

        # Create run button
        self.run_button = tk.Button(master, text='Run Test', command=self.run_test)
        self.run_button.pack()

        # Create output text area
        self.output_text = tk.Text(master, height=10, width=50)
        self.output_text.pack()

    def run_test(self):
        """
        Execute the test command entered by the user.
        """
        try:
            # Get the test command from the input field
            test_command = self.entry.get()
            
            # Check if the test command is not empty
            if not test_command:
                messagebox.showerror('Error', 'Please enter a test command')
                return
            
            # Run the test command using subprocess
            process = subprocess.Popen(test_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            
            # Display the test results
            if process.returncode == 0:
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, stdout.decode('utf-8'))
            else:
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, stderr.decode('utf-8'))
                messagebox.showerror('Error', 'Test failed with return code: {}'.format(process.returncode))
        except Exception as e:
            messagebox.showerror('Error', str(e))


if __name__ == '__main__':
    # Create the main window
    root = tk.Tk()
    
    # Create an instance of the IntegrationTestTool class
    app = IntegrationTestTool(root)
    
    # Start the main loop
    root.mainloop()