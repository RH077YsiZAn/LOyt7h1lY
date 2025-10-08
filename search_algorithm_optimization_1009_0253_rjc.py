# 代码生成时间: 2025-10-09 02:53:29
import tkinter as tk
from tkinter import messagebox

"""
    A simple Python and Tkinter application demonstrating a search algorithm optimization.
    This application allows users to input a list of data and perform a search.
    The search algorithm can be optimized by choosing different algorithms.
"""

class SearchAlgorithmOptimizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Search Algorithm Optimization')

        # Label for the data input field
        self.data_label = tk.Label(root, text='Enter data separated by commas:')
        self.data_label.grid(row=0, column=0)

        # Text field for user to input data
        self.data_entry = tk.Text(root, height=4)
        self.data_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Label for the algorithm selection
        self.algorithm_label = tk.Label(root, text='Select search algorithm:')
        self.algorithm_label.grid(row=2, column=0)

        # Dropdown menu for selecting search algorithm
        self.algorithms = ['Linear Search', 'Binary Search']
        self.algorithm_var = tk.StringVar(root)
        self.algorithm_var.set(self.algorithms[0])  # Set default value
        self.algorithm_menu = tk.OptionMenu(root, self.algorithm_var, *self.algorithms)
        self.algorithm_menu.grid(row=2, column=1, padx=5)

        # Button to perform search
        self.search_button = tk.Button(root, text='Search', command=self.search)
        self.search_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Label for search results
        self.search_results_label = tk.Label(root, text='')
        self.search_results_label.grid(row=4, column=0, columnspan=2)

    def search(self):
        # Get the data from the text field
        data = self.data_entry.get(1.0, 'end-1').split(',')

        # Convert data to a list of integers
        try:
            data = [int(item) for item in data]
        except ValueError:
            messagebox.showerror('Error', 'Invalid input. Please enter integers separated by commas.')
            return

        # Get the search term from the user
        search_term = simpledialog.askstring('Search', 'Enter the number you want to search for:')
        if search_term is None:
            return

        try:
            search_term = int(search_term)
        except ValueError:
            messagebox.showerror('Error', 'Invalid search term. Please enter an integer.')
            return

        # Perform the search based on the selected algorithm
        if self.algorithm_var.get() == 'Linear Search':
            result = self.linear_search(data, search_term)
        elif self.algorithm_var.get() == 'Binary Search':
            result = self.binary_search(data, search_term)

        # Display the search results
        self.search_results_label.config(text=f'Result: {result}')

    def linear_search(self, data, search_term):
        """
        Perform a linear search on the data.
        :param data: List of integers
        :param search_term: The integer to search for
        :return: The index of the search term if found, otherwise -1
        """
        for index, item in enumerate(data):
            if item == search_term:
                return f'Found at index {index}'
        return 'Not found'

    def binary_search(self, data, search_term):
        """
        Perform a binary search on the data.
        :param data: List of integers
        :param search_term: The integer to search for
        :return: The index of the search term if found, otherwise 'Not found'
        """
        left, right = 0, len(data) - 1
        while left <= right:
            mid = (left + right) // 2
            if data[mid] == search_term:
                return f'Found at index {mid}'
            elif data[mid] < search_term:
                left = mid + 1
            else:
                right = mid - 1
        return 'Not found'

# Main function to run the application
if __name__ == '__main__':
    root = tk.Tk()
    app = SearchAlgorithmOptimizationApp(root)
    root.mainloop()