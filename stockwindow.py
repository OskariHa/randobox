from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation
from matplotlib import style

matplotlib.use("TkAgg")
style=("seaborn")

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)

class StockWindow:

    def __init__(self, root, toolbar):
        self.root = root
        self.label = Label(root, text="Mega GRAPH")
        self.label.grid(row=0, column=0, pady=10, padx=10)

        self.graphing()

    def graphing(self):
        # draws a graph
        # plot.show()
        canvas = FigureCanvasTkAgg(f, self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0)

        print("lines")

    def animate(self):
        get_data = self.get_data()
        data_list = get_data.split("\n")
        x_list = []
        y_list = []
        for line in data_list:
            if len(line) > 1:
                x, y = line.split(",")
                x_list.append(int(x))
                y_list.append(int(y))

        a.clear()
        a.plot(x_list, y_list)



    def get_data(self):
        # database connection
        data_file = []
        print("getting")
        return data_file
