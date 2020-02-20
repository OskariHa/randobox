from tkinter import *
from database import admin_delete_account, admin_get_account_info, change_account_status, create_account


# account data from db using admin_get_account_info
def data_connection():
    print("getting data from db")
    accounts = admin_get_account_info()
    return accounts


class AdminAccountWindow:

    def __init__(self, root, toolbar):
        self.root = root
        self.toolbar = toolbar

        self.r = IntVar()
        self.clicked = StringVar()
        self.r.set(0)

        # ------ headers for username status and oid ---------------------
        # # username label
        self.username_lbl = Label(root, text="username")
        self.username_lbl.grid(row=0, column=0)
        # status label
        self.status_lbl = Label(root, text="status")
        self.status_lbl.grid(row=0, column=1)
        # oid label
        self.id_lbl = Label(root, text="id")
        self.id_lbl.grid(row=0, column=2)

        # ------------ toolbar buttons ---------------------

        # delete mode button
        self.delete_btn = Button(toolbar, text="Delete mode", command=self.admin_delete)
        self.delete_btn.pack(side=RIGHT, padx=2, pady=2)
        # Delete confirm
        self.delete_confirm_btn = Button(self.toolbar, text="DELETE!", command=self.deleting,
                                         fg="RED")
        # account creation button
        self.create_account_btn = Button(toolbar, text="Create account", command=self.create_account)
        self.create_account_btn.pack(side=RIGHT, padx=2, pady=2)
        # account creation confirmation button
        self.new_confirm_btn = Button(self.root, text="Create account", command=self.confirm_account)
        # edit button
        self.edit_btn = Button(toolbar, text="Edit", command=self.edit_account)
        self.edit_btn.pack(side=RIGHT, padx=2, pady=2)

        # ----------- account data handling ---------------
        # get account data for all accounts from db
        self.accounts = data_connection()

        # create arrays for account data labels
        self.usernames = []
        self.statuses = []
        self.ids = []
        self.rdy_btns = []

        self.create_labels()

        # ------------- Status changing ---------------
        # oid number for data reference
        self.oid_num = IntVar()

        # options for status and set group_member as default
        self.options = ["admin", "group_leader", "group_member", "pleb"]
        self.clicked.set(self.options[2])

        # create drop down menu to change status
        self.drop_menu = OptionMenu(self.root, self.clicked, *self.options)
        # confirm status change button
        self.confirm_btn = Button(self.toolbar, text="Confirm status change",
                                  command=self.confirm_status)

        # ------------ Account creation ----------------
        # Account creation entry and error label
        self.create_new_username_ent = Entry(self.root, width=20)
        self.error_lbl = Label(self.root, text="Username already exists", fg="RED")

    # ************** Create labels for frame **********
    # create labels to show on frame
    def create_labels(self):
        # loop through accounts data
        for i, account in enumerate(self.accounts, 2):
            # create labels for each account
            username = Label(self.root, text=account[0])
            status = Label(self.root, text=account[1])
            id_lbl = Label(self.root, text=account[2])
            rd_btn = Radiobutton(self.root, variable=self.r, value=i)

            # grid
            username.grid(row=i, column=0)
            status.grid(row=i, column=1)
            id_lbl.grid(row=i, column=2)
            rd_btn.grid(row=i, column=3)

            # add account labels to lists for later use
            self.usernames.append(username)
            self.statuses.append(status)
            self.ids.append(id_lbl)
            self.rdy_btns.append(rd_btn)

    # ************* CREATE ACCOUNT BUTTON FUNCTIONS ***********************
    # activate account creation visually
    def create_account(self):
        # new entry for account name
        self.create_new_username_ent.grid(row=1, column=0)
        # drop down menu for status
        self.drop_menu.grid(row=1, column=1)
        # confirm button to initiate account creation
        self.new_confirm_btn.grid(row=1, column=2, columnspan=2)
        # configure create account button to cancel account creation
        self.create_account_btn.configure(text="Cancel", command=self.cancel_create_account)

        # disable edit and delete button while new account is created
        self.edit_btn.configure(state=DISABLED)
        self.delete_btn.configure(state=DISABLED)

    # cancel account creation visually
    def cancel_create_account(self):
        # grid_forget new account creation labels
        self.create_new_username_ent.grid_forget()
        self.new_confirm_btn.grid_forget()
        self.drop_menu.grid_forget()
        self.error_lbl.grid_forget()

        # re-activate edit and delete button
        self.edit_btn.configure(state=ACTIVE)
        self.delete_btn.configure(state=ACTIVE)
        # return create_account_btn to original function
        self.create_account_btn.configure(text="Create account", command=self.create_account)

    # create account to database
    def confirm_account(self):
        # username and status from entry and drop down menu
        account_name = self.create_new_username_ent.get()
        status = self.clicked.get()
        # default password for new accounts
        password = "vixl"

        # database create_account (username from entry, default password,
        # # status from drop down menu
        create = create_account(account_name, password, status)

        # if account name is in use
        if not create:
            # forget create_account button and replace it with error label
            self.create_account_btn.grid_forget()
            self.error_lbl.grid(row=1, column=2, columnspan=2)
            # function to remove error label after entry is written
            sv = StringVar()
            sv.trace("w", lambda name, index, mode, sv=sv: self.wrong_name())
            # add function to entry
            self.create_new_username_ent.configure(textvariable=sv)

        # if account is created in db return to normal state
        else:
            # forget account creation entries
            self.create_new_username_ent.grid_forget()
            self.new_confirm_btn.grid_forget()
            self.drop_menu.grid_forget()
            # re-activate edit and delete
            self.edit_btn.configure(state=ACTIVE)
            self.delete_btn.configure(state=ACTIVE)
            # configure create account button back to original
            self.create_account_btn.configure(text="Create account", command=self.create_account)

    # function to remove username in use label
    def wrong_name(self):
        self.error_lbl.grid_forget()
        self.new_confirm_btn.grid(row=1, column=2, columnspan=2)

    # ************* DELETE BUTTON FUNCTIONS ***********************
    # enter delete mode
    def admin_delete(self):
        # disable other toolbar buttons
        self.edit_btn.configure(state=DISABLED)
        self.create_account_btn.configure(state=DISABLED)
        # configure delete button to cancel delete mode
        self.delete_btn.configure(command=self.cancel_delete_mode)
        # add confirm delete button
        self.delete_confirm_btn.pack(side=RIGHT, padx=2, pady=2)

    # actual deleting
    def deleting(self):
        # check that one radio button is selected
        if self.r.get() != 0:
            # d_num is list position of selected account labels
            d_num = self.r.get() - 2
            # delete oid is oid of selected account in accounts list
            delete_oid = self.accounts[d_num][2]
            # database.admin_delete_account(oid of account) deletes account from db
            admin_delete_account(delete_oid)

            # forget account labels from frame
            self.usernames[d_num].grid_forget()
            self.statuses[d_num].grid_forget()
            self.ids[d_num].grid_forget()
            self.rdy_btns[d_num].grid_forget()
            # sets radiobutton setting to 0
            self.r.set(0)

    # returns to original state
    def cancel_delete_mode(self):
        # activate toolbar buttons
        self.edit_btn.configure(state=ACTIVE)
        self.create_account_btn.configure(state=ACTIVE)
        # configure delete button to activate delete mode
        self.delete_btn.configure(command=self.admin_delete)
        # grid forget confirm button
        self.delete_confirm_btn.pack_forget()

    # ************* EDIT BUTTON FUNCTIONS ***********************
    def edit_account(self):
        # check that radiobutton is selected
        if self.r.get() != 0:
            # account position on data lists
            self.oid_num = self.r.get() - 2
            # canceled status for re-grid if edit is canceled
            self.canceled_status = self.statuses[self.oid_num]

            # grid drop down menu and confirm button and remove old status from frame
            self.statuses[self.oid_num].grid_forget()
            self.drop_menu.grid(row=self.r.get(), column=1)
            self.confirm_btn.pack(side=RIGHT, padx=2, pady=2)

            # disable radio buttons
            for btn in self.rdy_btns:
                btn.configure(state=DISABLED)
            # disable toolbar buttons
            self.delete_btn.configure(state=DISABLED)
            self.create_account_btn.configure(state=DISABLED)
            # configure edit button to cancel edit
            self.edit_btn.configure(text="Cancel", command=self.cancel_edit)

    def confirm_status(self):
        # forget drop menu and grid new status
        self.drop_menu.grid_forget()
        new_lbl = Label(self.root, text=self.clicked.get())
        new_lbl.grid(row=self.r.get(), column=1)

        # replace old status with new status in status labels list
        self.statuses[self.oid_num] = new_lbl
        self.confirm_btn.pack_forget()

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

    # return to basic state after edit or edit cancel
    def edit_reactivate(self):
        # activate delete, radio and edit button
        self.delete_btn.configure(state=ACTIVE)
        self.create_account_btn.configure(state=ACTIVE)
        for btn in self.rdy_btns:
            btn.configure(state=ACTIVE)
        self.edit_btn.configure(text="Edit", command=self.edit_account)
