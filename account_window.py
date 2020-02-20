from tkinter import *
from database import change_username, get_password, change_password
from account import Account


class AccountOptions:
    def __init__(self, root):
        self.root = root

        # -------- Username -----------------------------

        # getting user name from account.Account
        username = Account.username
        # username label
        username_txt_lbl = Label(root, text="Username:")
        username_txt_lbl.grid(row=0, column=0, pady=(30, 2), padx=2)

        # username entry for name change and showing username
        self.username_ent = Entry(root, width=20)
        self.username_ent.insert(0, username)
        self.username_ent.configure(state=DISABLED)
        self.username_ent.grid(row=0, column=1, pady=(30, 2))

        # change username mode
        self.change_username_btn = Button(root, text="Change username", command=self.change_username)

        self.change_username_btn.grid(row=1, column=1)

        # Confirm button grid after change username mode is active
        self.confirm_username_btn = Button(root, text="Confirm username", command=self.username_confirm)

        # username changed label after successful name change
        self.username_changed_lbl = Label(self.root, text="Username changed!", fg="GREEN")

        # ------------- Password -------------------------
        # password text
        password_txt_lbl = Label(root, text="Password:")
        password_txt_lbl.grid(row=2, column=0, padx=2, pady=5)

        # password entry for password change
        self.password_ent = Entry(root, width=20)
        self.password_ent.insert(0, "******")
        self.password_ent.configure(state=DISABLED)
        self.password_ent.grid(row=2, column=1, padx=2, pady=5)

        # show password button
        self.show_password_btn = Button(root, text="Show password", command=self.show_password)
        self.show_password_btn.grid(row=3, column=0)

        # change password mode button
        self.change_password_btn = Button(root, text="Change password", command=self.change_password)
        self.change_password_btn.grid(row=3, column=1)

        # label after successful password change
        self.password_changed_lbl = Label(self.root, text="Password changed!", fg="GREEN")

    # --------------- FUNCTIONS -------------------------
    # creates buttons to change username and activates entry
    def change_username(self):
        # set username entry to normal
        self.username_ent.configure(state=NORMAL)
        # grid confirm button and configure change username to cancel username change
        self.confirm_username_btn.grid(row=1, column=0)
        self.change_username_btn.configure(text="Cancel", command=self.cancel_username_change)
        # forget password and username changed labels
        self.clear_changed_labels()

    # actual username changing
    def username_confirm(self):
        # change_username form database using name from entry and account oid from account.Account
        success = change_username(self.username_ent.get(), Account.oid)
        # success is true if username is not used
        if success:
            # forget confirm button and disable entry
            self.confirm_username_btn.grid_forget()
            self.username_ent.configure(state=DISABLED)
            # configure username changed to show changed and grid it
            self.username_changed_lbl.configure(text="Username changed!", fg="GREEN")
            self.username_changed_lbl.grid(row=0, column=2, pady=(30, 2), padx=2)
        else:
            # temp = self.username_ent.get()
            # grid and configure username changed to sho username in use
            self.username_changed_lbl.configure(text="Username already in use!", fg="RED")
            self.username_changed_lbl.grid(row=0, column=2, pady=(30, 2), padx=2)
            # clears entry and when its rewritten forget username_changed_lbl
            sv = StringVar()
            sv.trace("w", lambda name, index, mode, sv=sv: self.clear_changed_labels())
            self.username_ent.configure(textvariable=sv)

    # returns to normal state without changing username
    def cancel_username_change(self):
        # forget confirm button
        self.confirm_username_btn.grid_forget()
        # clears and returns current username to username entry and disables entry
        self.username_ent.delete(0, END)
        self.username_ent.insert(0, Account.username)
        self.username_ent.configure(state=DISABLED)
        # configure change username button back to normal
        self.change_username_btn.configure(text="Change username", command=self.change_username)
        # forget password and username changed labels
        self.clear_changed_labels()

    # shows password on password entry
    def show_password(self):
        # fetches password from database using get_password(Account.oid from account.Account)
        password = get_password(Account.oid)
        # returns password entry to normal state and fills it with password
        self.password_ent.configure(state=NORMAL)
        self.password_ent.delete(0, END)
        self.password_ent.insert(0, password)
        # configures password button to hide password
        self.show_password_btn.configure(text="Hide password", command=self.hide_password)
        # forget password and username changed labels
        self.clear_changed_labels()

    # rewrites password entry to hide passwords and configures show password button
    def hide_password(self):
        self.password_ent.delete(0, END)
        self.password_ent.insert(0, "*****")
        self.show_password_btn.configure(text="Show password", command=self.show_password)

    # shows password and buttons for changing password
    def change_password(self):
        # gets password from database
        self.show_password()
        # configures buttons to confirm new password and to cancels state
        self.show_password_btn.configure(text="Confirm password", command=self.confirm_password)
        self.change_password_btn.configure(text="Cancel", command=self.cancel_password_change)
        # forget password and username changed labels
        self.clear_changed_labels()

    # actual password change
    def confirm_password(self):
        # change_password on database (new password, account oid)
        change_password(self.password_ent.get(), Account.oid)
        # password changed label on screen
        self.password_changed_lbl.grid(row=2, column=2)
        # hide password and disable entry
        self.hide_password()
        self.password_ent.configure(state=DISABLED)

    # cancels password change and returns to normal state
    def cancel_password_change(self):
        # return show and change btns to orginal state
        self.show_password_btn.configure(text="Show password", command=self.show_password)
        self.change_password_btn.configure(text="Change password", command=self.change_password)
        # hide password and disable password entry
        self.hide_password()
        self.password_ent.configure(state=DISABLED)

    def clear_changed_labels(self):
        self.username_changed_lbl.grid_forget()
        self.password_changed_lbl.grid_forget()

