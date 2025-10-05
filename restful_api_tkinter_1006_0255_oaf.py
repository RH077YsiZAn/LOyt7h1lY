# 代码生成时间: 2025-10-06 02:55:30
import tkinter as tk
from tkinter import messagebox
import requests

# Define a function to send HTTP GET request to a RESTful API
def send_get_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.text
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to send GET request: {e}")
        return None

# Define a function to send HTTP POST request to a RESTful API
def send_post_request(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.text
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to send POST request: {e}")
        return None

# Define a function to send HTTP PUT request to a RESTful API
def send_put_request(url, data):
    try:
        response = requests.put(url, json=data)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.text
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to send PUT request: {e}")
        return None

# Define a function to send HTTP DELETE request to a RESTful API
def send_delete_request(url):
    try:
        response = requests.delete(url)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.text
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to send DELETE request: {e}")
        return None

# Create the main window
root = tk.Tk()
root.title("RESTful API Client")

# Create a label for the GET request URL
get_label = tk.Label(root, text="GET Request URL:")
get_label.pack(pady=5)

# Create an entry widget for the GET request URL
get_entry = tk.Entry(root, width=50)
get_entry.pack(pady=5)

# Create a button to send a GET request
get_button = tk.Button(root, text="Send GET Request", command=lambda: messagebox.showinfo("Response", send_get_request(get_entry.get())))
get_button.pack(pady=5)

# Create a label for the POST request URL
post_label = tk.Label(root, text="POST Request URL:")
post_label.pack(pady=5)

# Create an entry widget for the POST request URL
post_entry = tk.Entry(root, width=50)
post_entry.pack(pady=5)

# Create a label for the POST request data
post_data_label = tk.Label(root, text="POST Request Data (JSON):")
post_data_label.pack(pady=5)

# Create a text widget for the POST request data
post_data_text = tk.Text(root, height=5, width=50)
post_data_text.pack(pady=5)

# Create a button to send a POST request
post_button = tk.Button(root, text="Send POST Request", command=lambda: messagebox.showinfo("Response", send_post_request(post_entry.get(), json.loads(post_data_text.get("1.0", tk.END)))))
post_button.pack(pady=5)

# Create a label for the PUT request URL
put_label = tk.Label(root, text="PUT Request URL:")
put_label.pack(pady=5)

# Create an entry widget for the PUT request URL
put_entry = tk.Entry(root, width=50)
put_entry.pack(pady=5)

# Create a label for the PUT request data
put_data_label = tk.Label(root, text="PUT Request Data (JSON):")
put_data_label.pack(pady=5)

# Create a text widget for the PUT request data
put_data_text = tk.Text(root, height=5, width=50)
put_data_text.pack(pady=5)

# Create a button to send a PUT request
put_button = tk.Button(root, text="Send PUT Request", command=lambda: messagebox.showinfo("Response", send_put_request(put_entry.get(), json.loads(put_data_text.get("1.0", tk.END)))))
put_button.pack(pady=5)

# Create a label for the DELETE request URL
delete_label = tk.Label(root, text="DELETE Request URL:")
delete_label.pack(pady=5)

# Create an entry widget for the DELETE request URL
delete_entry = tk.Entry(root, width=50)
delete_entry.pack(pady=5)

# Create a button to send a DELETE request
delete_button = tk.Button(root, text="Send DELETE Request", command=lambda: messagebox.showinfo("Response", send_delete_request(delete_entry.get())))
delete_button.pack(pady=5)

# Start the main event loop
root.mainloop()