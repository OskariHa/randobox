from tkinter import *
from database import admin_delete_account, admin_get_account_info, change_account_status, create_account


class AdminAccountWindow:

    def __init__(self, root, toolbar):
        self.root = root
        self.toolbar = toolbar
        self.r = IntVar()
        self.clicked = StringVar()
        self.r.set(0)

        # Create labels for rows
        self.username_lbl = Label(root, text="username")
        self.status_lbl = Label(root, text="status")
        self.id_lbl = Label(root, text="id")
        self.username_lbl.grid(row=0, column=0)
        self.status_lbl.grid(row=0, column=1)
        self.id_lbl.grid(row=0, column=2)

        # Create buttons for toolbar
        self.delete_btn = Button(toolbar, text="Delete mode", command=self.admin_delete)
        self.delete_btn.pack(side=RIGHT, padx=2, pady=2)
        self.create_account_btn = Button(toolbar, text="Create account", command=self.create_account)
        self.create_account_btn.pack(side=RIGHT, padx=2, pady=2)
        self.edit_btn = Button(toolbar, text="Edit", command=self.edit_account)
        self.edit_btn.pack(side=RIGHT, padx=2, pady=2)

        # get accounts
        self.accounts = self.data_connection()
        # create labels and arrays for them
        self.usernames = []
        self.statuses = []
        self.ids = []
        self.rdy_btns = []
        self.create_labels()

        # Edit buttons and menus
        self.position = IntVar()
        self.oid_num = IntVar()
        self.options = ["admin", "group_leader", "group_member", "pleb"]
        self.clicked.set(self.options[2])
        self.drop_menu = OptionMenu(self.root, self.clicked, *self.options)
        self.confirm_btn = Button(self.toolbar, text="Confirm status change", command=self.confirm_status)

        # Create account buttons
        self.create_new_username_ent = Entry(self.root, width=20)
        self.new_confirm_btn = Button(self.root, text="Create account", command=self.confirm_account)
        self.error_lbl = Label(self.root, text="Username already exists", fg="RED")

        # Delete confirm
        self.delete_confirm_btn = Button(self.toolbar, text="DELETE!", command=self.deleting, fg="RED")

    def data_connection(self):
        print("getting data from db")
        accounts = admin_get_account_info()
        print(accounts)
        return accounts

    # ************* CREATE ACCOUNT BUTTON FUNCTIONS ***********************
    def create_labels(self):
        for i, account in enumerate(self.accounts, 2):
            username = Label(self.root, text=account[0])
            status = Label(self.root, text=account[1])
            id_lbl = Label(self.root, text=account[2])
            rd_btn = Radiobutton(self.root, variable=self.r, value=i)

            username.grid(row=i, column=0)
            status.grid(row=i, column=1)
            id_lbl.grid(row=i, column=2)
            rd_btn.grid(row=i, column=3)

            self.usernames.append(username)
            self.statuses.append(status)
            self.ids.append(id_lbl)
            self.rdy_btns.append(rd_btn)

    def create_account(self):
        self.create_new_username_ent.grid(row=1, column=0)
        self.drop_menu.grid(row=1, column=1)
        self.new_confirm_btn.grid(row=1, column=2, columnspan=2)
        self.create_account_btn.configure(text="Cancel", command=self.cancel_create_account)
        self.edit_btn.configure(state=DISABLED)
        self.delete_btn.configure(state=DISABLED)

    def cancel_create_account(self):
        self.create_new_username_ent.grid_forget()
        self.new_confirm_btn.grid_forget()
        self.drop_menu.grid_forget()
        self.error_lbl.grid_forget()
        self.edit_btn.configure(state=ACTIVE)
        self.delete_btn.configure(state=ACTIVE)
        self.create_account_btn.configure(text="Create account", command=self.create_account)

    def confirm_account(self):
        account_name = self.create_new_username_ent.get()
        status = self.clicked.get()
        password = "vixl"

        create = create_account(account_name, password, status)

        if not create:
            self.create_account_btn.grid_forget()
            self.error_lbl.grid(row=1, column=2, columnspan=2)
            sv = StringVar()
            sv.trace("w", lambda name, index, mode, sv=sv: self.wrong_name())
            self.create_new_username_ent.configure(textvariable=sv)

        else:
            # return to normal state
            self.create_new_username_ent.grid_forget()
            self.new_confirm_btn.grid_forget()
            self.drop_menu.grid_forget()
            self.edit_btn.configure(state=ACTIVE)
            self.delete_btn.configure(state=ACTIVE)
            self.create_account_btn.configure(text="Create account", command=self.create_account)

    def wrong_name(self):
        self.error_lbl.grid_forget()
        self.new_confirm_btn.grid(row=1, column=2, columnspan=2)

    # ************* DELETE BUTTON FUNCTIONS ***********************
    def admin_delete(self):
        self.edit_btn.configure(state=DISABLED)
        self.create_account_btn.configure(state=DISABLED)
        self.delete_btn.configure(command=self.cancel_delete_mode)
        self.delete_confirm_btn.pack(side=RIGHT, padx=2, pady=2)

    def deleting(self):
        print(self.r.get())
        if self.r.get() != 0:
            d_num = self.r.get() - 2
            print(d_num)
            delete_oid = self.accounts[d_num][2]
            print(delete_oid)
            admin_delete_account(delete_oid)

            self.usernames[d_num].grid_forget()
            self.statuses[d_num].grid_forget()
            self.ids[d_num].grid_forget()
            self.rdy_btns[d_num].grid_forget()
            self.r.set(0)

    def cancel_delete_mode(self):
        self.edit_btn.configure(state=ACTIVE)
        self.create_account_btn.configure(state=ACTIVE)
        self.delete_btn.configure(command=self.admin_delete)
        self.delete_confirm_btn.pack_forget()

    # ************* EDIT BUTTON FUNCTIONS ***********************
    def edit_account(self):
        # store positions and old status
        if self.r.get() != 0:
            self.position = self.r.get()
            self.oid_num = self.r.get() - 2
            self.canceled_status = self.statuses[self.oid_num]

            # grid drop down menu and confirm button and remove old status from frame
            self.statuses[self.oid_num].grid_forget()
            self.drop_menu.grid(row=self.r.get(), column=1)
            self.confirm_btn.pack(side=RIGHT, padx=2, pady=2)

            # disable radio and delete button and edit edit button
            for btn in self.rdy_btns:
                btn.configure(state=DISABLED)
            self.delete_btn.configure(state=DISABLED)
            self.create_account_btn.configure(state=DISABLED)
            self.edit_btn.configure(text="Cancel", command=self.cancel_edit)

    def confirm_status(self):
        # forget drop menu and grid new status
        print(self.accounts[self.oid_num][2])
        self.drop_menu.grid_forget()
        new_lbl = Label(self.root, text=self.clicked.get())
        new_lbl.grid(row=self.r.get(), column=1)
        # replace old status with new status in status labels list
        print(self.statuses)
        self.statuses[self.oid_num] = new_lbl
        self.confirm_btn.pack_forget()
        print(self.statuses)
        print(self.accounts[self.oid_num][2])
        # connect to database and edit status
        change_account_status(self.accounts[self.oid_num][2], self.clicked.get())

        # activate delete, radio and edit button
        self.edit_reactivate()

    # cancel edit mode
    def cancel_edit(self):
        # forget created buttons
        self.drop_menu.grid_forget()
        self.confirm_btn.pack_forget()

        # re grid old status
        self.canceled_status.grid(row=self.r.get(), column=1)

        # activate delete, radio and edit button
        self.edit_reactivate()

    def edit_reactivate(self):
        # activate delete, radio and edit button
        self.delete_btn.configure(state=ACTIVE)
        self.create_account_btn.configure(state=ACTIVE)
        for btn in self.rdy_btns:
            btn.configure(state=ACTIVE)
        self.edit_btn.configure(text="Edit", command=self.edit_account)
