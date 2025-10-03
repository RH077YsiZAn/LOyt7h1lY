# 代码生成时间: 2025-10-03 20:37:41
import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
import psycopg2
import psycopg2.extras

"""
SQL Query Optimizer using Python and Tkinter framework.
This program allows users to input SQL queries and optimizes them
by suggesting index creation based on the query's SELECT, WHERE, and JOIN clauses.
"""

class SQLQueryOptimizer:
    def __init__(self, master):
        """Initialize the main window and components."""
        self.master = master
        self.master.title("SQL Query Optimizer")
        self.master.geometry("600x400")

        # Input area for SQL query
        self.query_label = tk.Label(master, text="Enter SQL Query: ")
        self.query_label.pack()
        self.query_text = scrolledtext.ScrolledText(master, height=10, width=60)
        self.query_text.pack()

        # Button to optimize query
        self.optimize_button = tk.Button(master, text="Optimize Query", command=self.optimize_query)
        self.optimize_button.pack()

        # Output area for optimized query
        self.output_label = tk.Label(master, text="Optimized Query: ")
        self.output_label.pack()
        self.output_text = scrolledtext.ScrolledText(master, height=10, width=60)
        self.output_text.pack()

    def optimize_query(self):
        """Optimize the input SQL query by suggesting index creation."""
        query = self.query_text.get("1.0", "end-1c")
        try:
            # Parse the query to extract table names, columns for SELECT, WHERE, and JOIN clauses
            tables = self.parse_tables(query)
            columns_select = self.parse_select_columns(query)
            columns_where = self.parse_where_columns(query)
            join_columns = self.parse_join_columns(query)

            # Suggest index creation based on the extracted information
            optimized_query = self.suggest_index_creation(tables, columns_select, columns_where, join_columns)

            # Display the optimized query
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", optimized_query)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def parse_tables(self, query):
        """Extract table names from the SQL query."""
        # Regular expression to match table names
        table_pattern = r"FROM\s+([\w\s,]+)"
        tables = re.findall(table_pattern, query, re.IGNORECASE)
        return [table.strip() for table in tables[0].split(",")] if tables else []

    def parse_select_columns(self, query):
        "