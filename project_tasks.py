from tkinter import *
from datetime import date, datetime, timedelta
from database import submit_tasks, show_table, fetch_tasks


class DailyTasks:
    daily_or_weekly = 0  # 0 = daily_tasks, 1 = weekly_tasks

    def __init__(self, root, toolbar):
        self.root = root

        # todays strings
        self.todays_date = date.today()
        self.todays_date_str = self.todays_date.strftime("%d.%m")
        # tomorrows date string
        self.tomorrows_date = date.today() + timedelta(days=1)
        self.tomorrows_date_str = self.tomorrows_date.strftime("%d.%m")
        # different formatting for database
        self.date_n_year = self.todays_date.strftime("%m.%d.%y")
        self.tomorrow_date_n_year = self.tomorrows_date.strftime("%m.%d.%y")

        # --------------- data for screen --------------------
        # empty data lists for dates,tasks,and done
        self.dates = []
        self.tasks_list = []
        self.done = []
        self.get_data()

        # list of date labels
        self.date_lbls = self.create_date_lbls()

        # ---------- ENTRIES -------------
        # list of entries for tasks and done
        self.entries = []
        # Number of entries shown on frame
        self.num_of_entries_list = [
            "5",
            "10",
            "15"
        ]
        # string shown on option menu
        self.num_of_entries_str = StringVar()
        # set default string
        self.num_of_entries_str.set(self.num_of_entries_list[0])
        # int for entries + 1 for aesthetics
        self.num_of_entries = int(self.num_of_entries_str.get()) + 1
        # function to create entries
        self.create_entries()

        # --------- toolbar buttons -------------------
        # submits data from entries
        self.submit_btn = Button(toolbar, text="Submit", command=self.submit_task)
        # reverts back to first loaded entries
        self.revert_btn = Button(toolbar, text="Revert Changes", command=self.revert_changes)
        # opens entries for editing
        self.edit_btn = Button(toolbar, text="Edit", command=self.edit)
        # variable to show edit button is not pressed
        self.edit_btn_pressed = False

        # change number of entries
        self.num_of_entries_menu = OptionMenu(toolbar, self.num_of_entries_str, *self.num_of_entries_list,
                                              command=self.more_entries)

        # pack buttons to toolbar submit / edit / revert
        self.revert_btn.pack(side=RIGHT, padx=2, pady=2)
        self.edit_btn.pack(side=RIGHT, padx=2, pady=2)
        self.submit_btn.pack(side=RIGHT, padx=2, pady=2)

        self.num_of_entries_menu.pack(side=LEFT, padx=2, pady=2)

        # top label tasks
        self.main_tasks_lbl = Label(root, text="Tasks")
        self.main_tasks_lbl.grid(row=0, column=1, pady=(5, 15))

        # date label for grids
        self.top_date_lbl = Label(root, text="DATE")
        self.top_date_lbl.grid(row=1, column=0)

        # task label for grids
        self.top_plan_lbl = Label(root, text="TASK")
        self.top_plan_lbl.grid(row=1, column=1)

        # completed label for grids
        self.top_done_lbl = Label(root, text="COMPLETED")
        self.top_done_lbl.grid(row=1, column=2)

    # change the number of entries on screen
    def more_entries(self, event):
        self.clear_old()
        self.date_lbls = self.create_date_lbls()
        self.num_of_entries = int(self.num_of_entries_str.get()) + 1
        self.entries = []
        self.create_entries()

    # clear all entries on frame
    def clear_old(self):
        for i in self.entries:
            i[0].grid_forget()
            i[1].grid_forget()
            i[2].grid_forget()

    # create entries for tasks and completed
    def create_entries(self):
        # loop for num of entries to create entries
        for i in range(self.num_of_entries):
            # create date labels from date_lbls for saved dates
            date_lbl = Label(self.root, text=self.date_lbls[i], width=10)
            # create empty entries for task and done
            task_en = Entry(self.root, width=40)
            done_en = Entry(self.root, width=40)

            # grid -- date / task / done
            date_lbl.grid(row=i + 2, column=0)
            task_en.grid(row=i + 2, column=1)
            done_en.grid(row=i + 2, column=2)

            # fill task and done entries from database
            task_en.insert(0, self.tasks_list[i])
            done_en.insert(0, self.done[i])

            # disable all but first 2 entries on task and done
            if i >= 2:
                task_en.config(state="disabled")
                done_en.config(state="disabled")

            # add date,task,done entries to entries list for later access
            self.entries.append([date_lbl, task_en, done_en])

    # submits data from entries to database
    def submit_task(self):
        # self.dates = []
        # self.dates.append(self.dates)

        # empty lists for updated data
        self.tasks_list = []
        self.done = []

        # update lists with current data from entries (needed for revert)
        for en in self.entries:
            self.tasks_list.append(en[1].get())
            self.done.append(en[2].get())

        # get data from lists for list of list for database
        temp = []
        for i in range(len(self.done)):
            temp += [(self.dates[i], self.tasks_list[i], self.done[i])]

        # update database with database.submit_tasks(table name, temp list of entries)
        submit_tasks("daily_tasks", temp)

    # reverts inputs in entries to loaded values
    def revert_changes(self):
        for i, entry in enumerate(self.entries, start=0):
            # Empty entries
            entry[1].delete(0, END)
            entry[2].delete(0, END)

            # Fill entries
            entry[1].insert(0, self.tasks_list[i])
            entry[2].insert(0, self.done[i])

    # Format date labels for frame from "mm.dd.yy" to "dd.mm"
    def create_date_lbls(self):
        temp_list = []
        # self.dates list from get_data
        for d in self.dates:
            to_date = datetime.strptime(d, "%m.%d.%y")
            to_string = datetime.strftime(to_date, "%d.%m")
            temp_list.append(to_string)
        return temp_list

    # Fill data lists from database
    def get_data(self):
        # database.fetch_tasks(table name) returns list of list (dates,tasks,done)
        mega_list = fetch_tasks("daily_tasks")

        for li in mega_list:
            self.dates.append(li[0])
            self.tasks_list.append(li[1])
            self.done.append(li[2])
        print("getting data")
        # if current date is not first on a list add it to position 0
        if self.date_n_year not in self.dates[0]:
            self.dates.insert(0, self.date_n_year)
            self.tasks_list.insert(0, "")
            self.done.insert(0, "")

    # edit opens and closes entries for editing
    def edit(self):
        # takes self.edit_btn_pressed to resolve if entries are normal or disabled
        if self.edit_btn_pressed:
            self.edit_btn_pressed = False
            # runs through every(task,done)entry after first 2 that are open at all times
            for x in range(2, self.num_of_entries):
                self.entries[x][1].config(state=DISABLED)
                self.entries[x][2].config(state=DISABLED)
        else:
            self.edit_btn_pressed = True
            # runs through every(task,done)entry after first 2 that are open at all times
            for x in range(2, self.num_of_entries):
                self.entries[x][1].config(state=NORMAL)
                self.entries[x][2].config(state=NORMAL)
