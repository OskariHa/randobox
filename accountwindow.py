from tkinter import *
from database import admin_delete_account, admin_get_account_info



class AdminAccountWindow:

    def __init__(self, root, toolbar):
        self.root = root
        self.toolbar = toolbar
        self.data_connection()
        self.r = IntVar()

        # Create labels for rows
        self.username_lbl = Label(root, text="username")
        self.status_lbl = Label(root, text="status")
        self.id_lbl = Label(root, text="id")
        self.username_lbl.grid(row=0, column=0)
        self.status_lbl.grid(row=0, column=1)
        self.id_lbl.grid(row=0, column=2)

        # Create buttons for toolbar
        self.delete_btn = Button(toolbar, text="Delete", command=self.admin_delete)
        self.delete_btn.pack(side=RIGHT, padx=2, pady=2)
        self.edit_btn = Button(toolbar, text="Edit", command=self.edit_account)
        self.edit_btn.pack(side=RIGHT, padx=2, pady=2)

        self.accounts = self.data_connection()

        self.usernames = []
        self.statuses =[]
        self.ids = []
        self.rdy_btns = []

        for i, account in enumerate(self.accounts, 1):
            username = Label(root, text=account[0])
            status = Label(root, text=account[1])
            id_lbl = Label(root, text=account[2])
            rd_btn = Radiobutton(root, variable=self.r, value=i)

            username.grid(row=i, column=0)
            status.grid(row=i, column=1)
            id_lbl.grid(row=i, column=2)
            rd_btn.grid(row=i, column=3)

            self.usernames.append(username)
            self.statuses.append(status)
            self.ids.append(id_lbl)
            self.rdy_btns.append(rd_btn)

        print(self.accounts[1][0])

    def data_connection(self):
        print("getting data from db")
        accounts = admin_get_account_info()
        print(accounts)
        return accounts

    def admin_delete(self):
        self.selected = self.r.get()
        print(self.selected)
        for i, account in enumerate(self.accounts):
            if account[2] == self.selected:
                #admin_delete_account()
                self.usernames[i].grid_forget()
                self.statuses[i].grid_forget()
                self.ids[i].grid_forget()
                self.rdy_btns[i].grid_forget()
                print(account[0])
                print(account[1])
                print(account[2])

    def edit_account(self):
        options = ["admin", "group_leader", "group_member"]
        selected = self.r.get()
        self.clicked = StringVar()
        self.position = IntVar()
        self.clicked.set(options[2])

        for i, account in enumerate(self.accounts):
            if account[2] == selected:
                self.statuses[i].grid_forget()
                self.drop_menu = OptionMenu(self.root, self.clicked, *options)
                self.drop_menu.grid(row=i+1, column=1)
                self.position = i+1
                self.confirm_btn = Button(self.toolbar, text="Confirm status change", command=self.confirm_status)
                self.confirm_btn.pack(side=RIGHT, padx=2, pady=2)

    def confirm_status(self):
        self.drop_menu.grid_forget()
        new_lbl = Label(self.root, text=self.clicked.get())
        new_lbl.grid(row=self.position, column=1)
        self.confirm_btn.pack_forget()

