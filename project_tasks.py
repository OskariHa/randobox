from tkinter import *
from datetime import date, datetime, timedelta
from database import submit_tasks, show_table, fetch_tasks


class DailyTasks:
    daily_or_weekly = 0  # 0 = daily_tasks, 1 = weekly_tasks

    def __init__(self, root, toolbar):
        self.root = root

        self.todays_date = date.today()
        self.tomorrows_date = date.today() + timedelta(days=1)
        self.todays_date_str = self.todays_date.strftime("%d.%m")
        self.tomorrows_date_str = self.tomorrows_date.strftime("%d.%m")
        self.date_n_year = self.todays_date.strftime("%m.%d.%y")
        self.tomorrow_date_n_year = self.tomorrows_date.strftime("%m.%d.%y")

        self.dates = []
        self.tasks_list = []
        self.done = []
        self.get_data()

        self.date_lbls = self.create_date_lbls()
        print(self.dates)

        self.entries = []
        self.num_of_entries = 6
        self.create_entries()

        # toolbar buttons
        self.submit_btn = Button(toolbar, text="Submit", command=self.submit_task)
        self.revert_btn = Button(toolbar, text="Revert Changes", command=self.revert_changes)
        self.edit_btn = Button(toolbar, text="Edit", command=self.edit)
        self.edit_btn_pressed = False
        self.revert_btn.pack(side=RIGHT, padx=2, pady=2)
        self.edit_btn.pack(side=RIGHT, padx=2, pady=2)
        self.submit_btn.pack(side=RIGHT, padx=2, pady=2)

        # top labels
        self.main_tasks_lbl = Label(root, text="Tasks")
        self.main_tasks_lbl.grid(row=0, column=1, pady=(5, 15))
        self.top_date_lbl = Label(root, text="DATE")
        self.top_date_lbl.grid(row=1, column=0)
        self.top_plan_lbl = Label(root, text="TASK")
        self.top_plan_lbl.grid(row=1, column=1)
        self.top_done_lbl = Label(root, text="COMPLETED")
        self.top_done_lbl.grid(row=1, column=2)

        # testing buttons
        self.show_db_btn = Button(root, text="show db", command=show_table)
        self.show_data_btn = Button(root, text="show data", command=self.get_data)
        self.show_db_btn.grid(row=12, column=1)
        self.show_data_btn.grid(row=12, column=2)

    def create_entries(self):
        for i in range(self.num_of_entries):
            date_lbl = Label(self.root, text=self.date_lbls[i], width=10)
            task_en = Entry(self.root, width=30)
            done_en = Entry(self.root, width=30)

            date_lbl.grid(row=i + 2, column=0)
            task_en.grid(row=i + 2, column=1)
            done_en.grid(row=i + 2, column=2)

            task_en.insert(0, self.tasks_list[i])
            done_en.insert(0, self.done[i])

            if i >= 2:
                task_en.config(state="disabled")
                done_en.config(state="disabled")

            self.entries.append([date_lbl, task_en, done_en])

    def submit_task(self):
        #  **** update lists with current data ****
        # self.dates = []
        # self.dates.append(self.dates)
        self.tasks_list = []
        self.done = []

        for en in self.entries:
            self.tasks_list.append(en[1].get())
            self.done.append(en[2].get())

        # **** get data from lists ****
        temp = []
        i = 0
        while i < len(self.done):
            temp += [(self.dates[i], self.tasks_list[i], self.done[i])]
            i += 1
        for t in temp:
            print(t)
        # temp = [("30.1", "fiasko", "ei tullu")]
        submit_tasks("daily_tasks", temp)

    # reverts inputs in entries to loaded values
    def revert_changes(self):
        # Empty entry's
        self.days_task1_entry.delete(0, END)
        self.days_task2_entry.delete(0, END)
        self.days_task3_entry.delete(0, END)
        self.days_task4_entry.delete(0, END)
        self.days_task5_entry.delete(0, END)
        self.days_task6_entry.delete(0, END)

        self.days_done1_entry.delete(0, END)
        self.days_done2_entry.delete(0, END)
        self.days_done3_entry.delete(0, END)
        self.days_done4_entry.delete(0, END)
        self.days_done5_entry.delete(0, END)
        self.days_done6_entry.delete(0, END)

        # Fill entry's
        self.days_task1_entry.insert(0, self.tasks_list[0])
        self.days_task2_entry.insert(0, self.tasks_list[1])
        self.days_task3_entry.insert(0, self.tasks_list[2])
        self.days_task4_entry.insert(0, self.tasks_list[3])
        self.days_task6_entry.insert(0, self.tasks_list[5])

        self.days_done1_entry.insert(0, self.done[0])
        self.days_done2_entry.insert(0, self.done[1])
        self.days_done3_entry.insert(0, self.done[2])
        self.days_done4_entry.insert(0, self.done[3])
        self.days_done5_entry.insert(0, self.done[4])
        self.days_done6_entry.insert(0, self.done[5])

    # Format date labels for frame from "mm.dd.yy" to "dd.mm"
    def create_date_lbls(self):
        temp_list = []
        for d in self.dates:
            to_date = datetime.strptime(d, "%m.%d.%y")
            to_string = datetime.strftime(to_date, "%d.%m")
            temp_list.append(to_string)
        return temp_list

    # Fill data lists from database
    def get_data(self):
        mega_list = fetch_tasks("daily_tasks")
        print(mega_list)
        for li in mega_list:
            # print(li)
            self.dates.append(li[0])
            self.tasks_list.append(li[1])
            self.done.append(li[2])
        print("getting data")
        if self.date_n_year not in self.dates[0]:
            self.dates.insert(0, self.date_n_year)
            self.tasks_list.insert(0, "")
            self.done.insert(0, "")
        print(self.dates)

    def edit(self):

        if self.edit_btn_pressed:
            self.edit_btn_pressed = False
            # Disable entry's
            # self.days_task1_entry.config(state="disabled")
            # self.days_task2_entry.config(state="disabled")
            self.days_task3_entry.config(state="disabled")
            self.days_task4_entry.config(state="disabled")
            self.days_task5_entry.config(state="disabled")
            self.days_task6_entry.config(state="disabled")

            # self.days_done1_entry.config(state="disabled")
            # self.days_done2_entry.config(state="disabled")
            self.days_done3_entry.config(state=DISABLED)
            self.days_done4_entry.config(state=DISABLED)
            self.days_done5_entry.config(state=DISABLED)
            self.days_done6_entry.config(state=DISABLED)
        else:
            self.edit_btn_pressed = True
            # Enable entry's
            # self.days_task1_entry.config(state="disabled")
            # self.days_task2_entry.config(state="disabled")
            self.days_task3_entry.config(state=NORMAL)
            self.days_task4_entry.config(state=NORMAL)
            self.days_task5_entry.config(state=NORMAL)
            self.days_task6_entry.config(state=NORMAL)

            # self.days_done1_entry.config(state="disabled")
            # self.days_done2_entry.config(state="disabled")
            self.days_done3_entry.config(state=NORMAL)
            self.days_done4_entry.config(state=NORMAL)
            self.days_done5_entry.config(state=NORMAL)
            self.days_done6_entry.config(state=NORMAL)
