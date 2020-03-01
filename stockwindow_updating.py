from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style, animation

matplotlib.use("TkAgg")
style.use("ggplot")


class StockWindowUpdating:

    def __init__(self, root, toolbar):
        self.root = root
        self.toolbar = toolbar

        # create table base
        self.f = Figure(figsize=(5, 5), dpi=100)
        self.a = self.f.add_subplot(111)

        # label on top to describe graph
        self.label = Label(root, text="Mega GRAPH")
        self.label.grid(row=0, column=0, pady=10, padx=10)

        # draws the graph
        self.graphing()

        # updates graph from file
        self.ani = animation.FuncAnimation(self.f, self.animate, interval=1000)

    def graphing(self):
        # creates canvas and draw it
        canvas = FigureCanvasTkAgg(self.f, self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0)

    def animate(self, i):
        # gets data from file
        get_data = self.get_data()
        # clean data
        data_list = get_data.split("\n")
        # x and y positions
        x_list = []
        y_list = []
        for line in data_list:
            # checks if line has data on it
            if len(line) > 1:
                x, y = line.split(",")
                x_list.append(int(x))
                y_list.append(int(y))

        # clears table base and adds new data to it
        self.a.clear()
        self.a.plot(x_list, y_list)

    def get_data(self):
        # database connection
        file = open("dataFiles/test.txt", "r").read()
        return file
