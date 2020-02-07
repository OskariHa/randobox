from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style, animation

matplotlib.use("TkAgg")
style.use("ggplot")

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)


def animate(i):
    get_data = open("dataFiles/test.txt", "r").read()
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


class StockWindow:

    def __init__(self, root, toolbar):
        self.toolbar = toolbar
        self.root = root
        self.label = Label(root, text="Mega GRAPH")
        self.label.grid(row=0, column=0, pady=10, padx=10)

        self.graphing()
        self.ani = animation.FuncAnimation(f, animate, interval=1000)

    def graphing(self):
        # draws a graph
        # plot.show()
        canvas = FigureCanvasTkAgg(f, self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0)

        print("lines")

    def get_data(self):
        # database connection
        file = open("dataFiles/test.txt", "r").read()
        print("getting")
        return file

