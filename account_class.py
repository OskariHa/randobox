from tkinter import *
from database import change_username, get_password, change_password
from account import Account


class AccountOptions:
    def __init__(self, root):
        self.root = root

        # Info labels
        # Username
        username = Account.username
        username_txt_lbl = Label(root, text="Username:")
        self.username_ent = Entry(root, width=20)
        self.username_ent.insert(0, username)
        self.username_ent.configure(state=DISABLED)
        self.change_username_btn = Button(root, text="Change username", command=self.change_username)

        username_txt_lbl.grid(row=0, column=0, pady=(30, 2), padx=2)
        self.username_ent.grid(row=0, column=1, pady=(30, 2))
        self.change_username_btn.grid(row=1, column=1)

        # Confirm button
        self.confirm_username_btn = Button(root, text="Confirm username", command=self.username_confirm)
        self.username_changed_lbl = Label(self.root, text="Username changed!", fg="GREEN")

        # Password
        password_txt_lbl = Label(root, text="Password:")
        self.password_ent = Entry(root, width=20)
        self.password_ent.insert(0, "******")
        self.password_ent.configure(state=DISABLED)
        self.show_password_btn = Button(root, text="Show password", command=self.show_password)
        self.change_password_btn = Button(root, text="Change password", command=self.change_password)

        password_txt_lbl.grid(row=2, column=0, padx=2, pady=5)
        self.password_ent.grid(row=2, column=1, padx=2, pady=5)
        self.show_password_btn.grid(row=3, column=0)
        self.change_password_btn.grid(row=3, column=1)

        self.password_changed_lbl = Label(self.root, text="Password changed!", fg="GREEN")

    def change_username(self):
        self.username_ent.configure(state=NORMAL)
        self.confirm_username_btn.grid(row=1, column=0)
        self.change_username_btn.configure(text="Cancel", command=self.cancel_username_change)
        self.username_changed_lbl.grid_forget()
        self.password_changed_lbl.grid_forget()

    def username_confirm(self):
        print(Account.username)
        print(self.username_ent.get())
        print(Account.oid)
        succes = change_username(self.username_ent.get(), Account.oid)
        if succes:
            self.confirm_username_btn.grid_forget()
            self.username_changed_lbl.configure(text="Username changed!", fg="GREEN")
            self.username_changed_lbl.grid(row=0, column=2, pady=(30, 2), padx=2)
            self.username_ent.configure(state=DISABLED)
        else:
            temp = self.username_ent.get()
            self.username_changed_lbl.configure(text="Username already in use!", fg="RED")
            self.username_changed_lbl.grid(row=0, column=2, pady=(30, 2), padx=2)
            sv = StringVar()
            sv.trace("w", lambda name, index, mode, sv=sv: self.wrong_username())
            self.username_ent.configure(textvariable=sv)

    def wrong_username(self):
        self.username_changed_lbl.grid_forget()

    def cancel_username_change(self):
        self.confirm_username_btn.grid_forget()
        self.username_ent.delete(0, END)
        self.username_ent.insert(0, Account.username)
        self.change_username_btn.configure(text="Change username", command=self.change_username)
        self.username_ent.configure(state=DISABLED)

    def show_password(self):
        password = get_password(Account.oid)
        self.password_ent.configure(state=NORMAL)
        self.password_ent.delete(0, END)
        self.password_ent.insert(0, password)
        self.show_password_btn.configure(text="Hide password", command=self.hide_password)
        self.username_changed_lbl.grid_forget()
        self.password_changed_lbl.grid_forget()

    def hide_password(self):
        self.password_ent.delete(0, END)
        self.password_ent.insert(0, "*****")
        self.show_password_btn.configure(text="Show password", command=self.show_password)

    def change_password(self):
        self.show_password()
        self.show_password_btn.configure(text="Confirm password", command=self.confirm_password)
        self.change_password_btn.configure(text="Cancel", command=self.cancel_password_change)
        self.username_changed_lbl.grid_forget()
        self.password_changed_lbl.grid_forget()

    def confirm_password(self):
        change_password(self.password_ent.get(), Account.oid)
        self.password_changed_lbl.grid(row=2, column=2)
        self.hide_password()
        self.password_ent.configure(state=DISABLED)

    def cancel_password_change(self):
        self.show_password_btn.configure(text="Show password", command=self.show_password)
        self.change_password_btn.configure(text="Change password", command=self.change_password)
        self.hide_password()
        self.password_ent.configure(state=DISABLED)

