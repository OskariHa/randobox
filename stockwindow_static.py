
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style, animation
from datetime import datetime
from webscrape import get_air_rune
import csv

matplotlib.use("TkAgg")
style.use("ggplot")


class StockWindowStatic:

    def __init__(self, root, toolbar):
        self.root = root
        self.toolbar = toolbar

        # create table base
        self.f = Figure(figsize=(5, 5), dpi=100)
        self.a = self.f.add_subplot(111)


        # draws the graph
        self.graphing()

        self.options = [
            "Stock - Nokia(csv)",
            "Rs - Air_Rune(web)"
        ]

        self.selected = StringVar()
        self.selected.set(self.options[0])

        # updates graph from file
        self.draw()

        # label on top to describe graph
        self.label = Label(root, textvariable= self.selected)
        self.label.grid(row=0, column=0, pady=10, padx=10)

        self.graphs_menu = OptionMenu(toolbar, self.selected, *self.options,
                                      command=self.change_graph)
        self.graphs_menu.pack()

    def change_graph(self, event):
        self.graphing()
        self.draw()

    def graphing(self):
        # creates canvas and draw it
        canvas = FigureCanvasTkAgg(self.f, self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0)

    def draw(self):
        # gets data from file
        get_data = self.get_data()
        # clean data
        data_list = get_data
        # x and y positions
        x_list = []
        y_list = []
        for line in data_list:
            x = line[0]
            y = line[1]

            x_list.append(x)
            y_list.append(float(y))

        # clears table base and adds new data to it
        self.a.clear()
        self.a.plot(x_list, y_list)

    def get_data(self):
        # database connection
        if self.selected.get() == "Stock - Nokia(csv)":
            with open("dataFiles/nokia.csv", newline="") as f:
                reader = csv.reader(f)
                data = list(reader)

            file = []
            for d in data[1:]:
                to_date = datetime.strptime(d[0], "%Y-%m-%d")
                date = datetime.strftime(to_date, "%d.%m")
                file.append([date, d[3]])
            file.reverse()

        elif self.selected.get() == "Rs - Air_Rune(web)":
            with open("dataFiles/rs_air_rune.csv", newline="") as f:
                reader = csv.reader(f)
                data = list(reader)

            file = []
            for d in data[1:]:
                if d:
                    file.append([d[0], d[1]])

            today = datetime.today()
            today_str = today.strftime("%d.%m")
            print(today_str)
            print(file[0][0])

            if today_str not in file[len(file)-1][0]:
                dd = get_air_rune()
                current_prize = "".join(filter(str.isdigit, dd))
                temp_list = [today_str, current_prize]
                with open("dataFiles/rs_air_rune.csv", 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(temp_list)
                file.append(temp_list)

        return file
