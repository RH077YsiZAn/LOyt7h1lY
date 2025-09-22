# 代码生成时间: 2025-09-22 15:25:16
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox

class HashCalculatorApp:
    """
    A simple GUI application to calculate hashes of files using Python and Tkinter.
    """

def create_hash(file_path, algorithm):
    """
    Calculate the hash of a file using the specified algorithm.
    """
    hash_obj = getattr(hashlib, algorithm)()
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(8192):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except Exception as e:
        return f"Error: {e}"

def choose_file():
    """
    Open a file dialog to select a file.
    """
    file_path = filedialog.askopenfilename()
    if file_path:
        update_hash_label(file_path)

def update_hash_label(file_path):
    """
    Update the hash label with the calculated hash value.
    """
    hash_algorithm = hash_algorithm_combobox.get()
    hash_value = create_hash(file_path, hash_algorithm)
    hash_label.config(text=hash_value)

def on_algorithm_change(event):
    """
    Call update_hash_label when algorithm is changed.
    """
    if file_path_var.get():
        update_hash_label(file_path_var.get())

def on_file_path_change(event):
    """
    Call update_hash_label when file path is changed.
    """
    if hash_algorithm_combobox.get():
        update_hash_label(file_path_var.get())

def main():
    """
    Initialize the GUI application.
    """
    root = tk.Tk()
    root.title("Hash Calculator")
    root.geometry("400x200")

    # Label for file path
    file_path_label = tk.Label(root, text="File Path:")
    file_path_label.grid(row=0, column=0, padx=10, pady=10)

    # Entry for file path
    file_path_var = tk.StringVar()
    file_path_entry = tk.Entry(root, textvariable=file_path_var, width=40)
    file_path_entry.grid(row=0, column=1, padx=10, pady=10)

    # Button to choose file
    choose_file_button = tk.Button(root, text="Choose File", command=choose_file)
    choose_file_button.grid(row=0, column=2, padx=10, pady=10)

    # Label for hash algorithm
    algorithm_label = tk.Label(root, text="Algorithm:")
    algorithm_label.grid(row=1, column=0, padx=10, pady=10)

    # Combobox for hash algorithm
    hash_algorithms = ["md5", "sha1", "sha256", "sha512"]
    hash_algorithm_combobox = tk.StringVar(value=hash_algorithms[0])
    algorithm_combobox = tk.OptionMenu(root, hash_algorithm_combobox, *hash_algorithms)
    algorithm_combobox.grid(row=1, column=1, padx=10, pady=10)
    algorithm_combobox.config(width=20)
    algorithm_combobox.bind("<Configure>", on_algorithm_change)

    # Label to display hash value
    hash_label = tk.Label(root, text="")
    hash_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    # Bind file_path_entry to on_file_path_change function
    file_path_entry.bind("<FocusOut>", on_file_path_change)

    # Start the GUI loop
    root.mainloop()

def __name__ == "__main__":
    main()
