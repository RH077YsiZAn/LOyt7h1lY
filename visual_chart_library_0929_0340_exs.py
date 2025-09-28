# 代码生成时间: 2025-09-29 03:40:27
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class VisualChartLibrary:
    """
    A tkinter application to visualize charts using matplotlib.
    This class provides a simple GUI to plot different types of charts.
    """

    def __init__(self, root):
        self.root = root
        self.root.title('Visual Chart Library')
        self.root.geometry('800x600')

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Create file and plot menus
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.plot_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.menu_bar.add_cascade(label='Plot', menu=self.plot_menu)

        # Exit option in the file menu
        self.file_menu.add_command(label='Exit', command=self.root.quit)

        # Plot options in the plot menu
        self.plot_menu.add_command(label='Line Chart', command=lambda: self.plot_chart('line'))
        self.plot_menu.add_command(label='Bar Chart', command=lambda: self.plot_chart('bar'))
        self.plot_menu.add_command(label='Scatter Chart', command=lambda: self.plot_chart('scatter'))
        self.plot_menu.add_command(label='Pie Chart', command=lambda: self.plot_chart('pie'))

        # Create a canvas to display the plot
        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack(fill='both', expand=True)

    def plot_chart(self, chart_type):
        """
        Plots a chart based on the given chart type.
        """
        try:
            # Generate some data for plotting
            x = [1, 2, 3, 4, 5]
            y = [2, 3, 5, 7, 11]

            # Create a new figure and axis for plotting
            fig, ax = plt.subplots()

            # Plot the data based on the chart type
            if chart_type == 'line':
                ax.plot(x, y)
            elif chart_type == 'bar':
                ax.bar(x, y)
            elif chart_type == 'scatter':
                ax.scatter(x, y)
            elif chart_type == 'pie':
                ax.pie(y, labels=x, autopct='%1.1f%%')
            else:
                print('Invalid chart type')
                return

            # Set the title and labels
            ax.set_title(chart_type + ' Chart')
            ax.set_xlabel('X-axis')
            ax.set_ylabel('Y-axis')

            # Clear the previous plot from the canvas
            self.canvas.delete('all')

            # Add the new plot to the canvas
            canvas = FigureCanvasTkAgg(fig, master=self.canvas)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)

        except Exception as e:
            print(f'Error plotting chart: {e}')

# Create the main window and pass it to the VisualChartLibrary class
root = tk.Tk()
app = VisualChartLibrary(root)
root.mainloop()