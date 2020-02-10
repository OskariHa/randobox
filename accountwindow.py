from tkinter import *
from database import admin_delete_account, admin_get_account_info


class AdminAccountWindow:

    def __init__(self, root):
        self.root = root
        self.data_connection()
        username_lbl = Label(root, text="username")
        status_lbl = Label(root, text="status")
        id_lbl = Label(root, text="id")

        username_lbl.grid(row=0, column=0)
        status_lbl.grid(row=0, column=1)
        id_lbl.grid(row=0, column=2)

        accounts = self.data_connection()
        for i, account in enumerate(accounts, 1):
            username = Label(root, text=account[0])
            status = Label(root, text=account[1])
            ids = Label(root, text=account[2])

            username.grid(row=i, column=0)
            status.grid(row=i, column=1)
            ids.grid(row=i, column=2)

        print(accounts[1][0])

    def data_connection(self):
        print("getting data from db")
        accounts = admin_get_account_info()
        print(accounts)
        return accounts
