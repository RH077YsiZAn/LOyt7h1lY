# 代码生成时间: 2025-10-11 19:02:36
import tkinter as tk
from tkinter import ttk
import random
import threading
import time

"""
Sensor Data Collection Program using Python and Tkinter framework.
This program simulates sensor data collection with a simple GUI.
"""

class SensorApp:
    def __init__(self, root):
        """
        Initialize the SensorApp class.
        """
        self.root = root
        self.root.title("Sensor Data Collection")

        # Create a frame for the GUI layout
        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Create a label for the sensor data
        self.data_label = ttk.Label(self.frame, text="Sensor Data: ")
        self.data_label.grid(row=0, column=0, padx=5, pady=5)

        # Create a label to display the current sensor data value
        self.value_label = ttk.Label(self.frame, text="N/A")
        self.value_label.grid(row=0, column=1, padx=5, pady=5)

        # Create a button to start collecting sensor data
        self.start_button = ttk.Button(self.frame, text="Start Collecting", command=self.start_collecting)
        self.start_button.grid(row=1, column=0, padx=5, pady=5)

        # Create a button to stop collecting sensor data
        self.stop_button = ttk.Button(self.frame, text="Stop Collecting", command=self.stop_collecting)
        self.stop_button.grid(row=1, column=1, padx=5, pady=5)

        # Initialize the sensor data collection flag
        self.collecting = False

    def start_collecting(self):
        """
        Start collecting sensor data.
        """
        self.collecting = True
        self.update_sensor_data()

    def stop_collecting(self):
        """
        Stop collecting sensor data.
        """
        self.collecting = False

    def update_sensor_data(self):
        """
        Update the sensor data.
        """
        if self.collecting:
            try:
                # Simulate sensor data collection
                value = random.uniform(0, 100)
                self.value_label.config(text=str(value))
                # Update the sensor data every 1 second
                self.root.after(1000, self.update_sensor_data)
            except Exception as e:
                # Handle any errors that occur during data collection
                print(f"Error: {e}")

def main():
    """
    Main function to run the Sensor Data Collection program.
    """
    root = tk.Tk()
    app = SensorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()