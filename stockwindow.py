from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style, animation

matplotlib.use("TkAgg")
style.use("ggplot")


class StockWindow:

    def __init__(self, root, toolbar):

        self.f = Figure(figsize=(5, 5), dpi=100)
        self.a = self.f.add_subplot(111)
        self.toolbar = toolbar
        self.root = root
        self.label = Label(root, text="Mega GRAPH")
        self.label.grid(row=0, column=0, pady=10, padx=10)

        self.graphing()
        self.ani = animation.FuncAnimation(self.f, self.animate, interval=1000)

    def graphing(self):
        # draws a graph
        # plot.show()
        canvas = FigureCanvasTkAgg(self.f, self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0)

    def animate(self, i):
        get_data = self.get_data()
        data_list = get_data.split("\n")
        x_list = []
        y_list = []
        for line in data_list:
            if len(line) > 1:
                x, y = line.split(",")
                x_list.append(int(x))
                y_list.append(int(y))

        self.a.clear()
        self.a.plot(x_list, y_list)

    def get_data(self):
        # database connection
        file = open("dataFiles/test.txt", "r").read()
        return file
