from tkinter import *
from project_tasks import DailyTasks
from timer import Timer
from loginwindow import LoginWindow
from stockwindow import StockWindow
from accountwindow import AdminAccountWindow
from account_class import AccountOptions
from account import Account

global drawing_frame, toolbar


def do_nothing():
    print("MORO")


def open_stocks():
    switch_frame()
    stocks = StockWindow(drawing_frame, toolbar)


def open_tasks():
    switch_frame()
    tasks = DailyTasks(drawing_frame, toolbar)


def account_info():
    switch_frame()
    AccountOptions(drawing_frame)


def admin_account_window():
    switch_frame()
    AdminAccountWindow(drawing_frame, toolbar)


def switch_frame():
    global drawing_frame, toolbar
    toolbar.destroy()
    toolbar = Frame(root, bg="green")
    toolbar.pack(side=TOP, fill=X)

    drawing_frame.destroy()
    drawing_frame = Frame(root)
    drawing_frame.pack()
    print("frame swiped")


def login_status123(yees):
    if yees:
        loginstatus = True


def close_program():
    print("exit by x")
    sys.exit()


loginstatus = False

login_window = Tk()
login_window.minsize(width=300, height=200)
login_window.protocol("WM_DELETE_WINDOW", close_program)
login_window.title("KEKW - Login")
login_window.iconbitmap(default="images/kekw.ico")
login_window_frame = Frame(login_window, bd=1, relief=RAISED)
login_window_frame.pack(pady=(20, 0), anchor=CENTER)
LoginWindow(login_window_frame, login_window)
login_window.mainloop()

root = Tk()
root.title("KEKW")
root.minsize(width=800, height=600)
root.iconbitmap(default="images/kekw.ico")
# ***** Main Menu ******

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Tasks", command=open_tasks)
subMenu.add_command(label="Stocks", command=open_stocks)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=close_program)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=do_nothing)

accountMenu = Menu(menu)
menu.add_cascade(label="Account", menu=accountMenu)
accountMenu.add_command(label="Change account info", command=account_info)

if Account.status == "master" or Account.status == "admin":
    print(Account.status)
    adminMenu = Menu(menu)
    menu.add_cascade(label="Admin", menu=adminMenu)
    adminMenu.add_command(label="Accounts", command=admin_account_window)

# ***** Toolbar ******

toolbar = Frame(root, bg="green")

# insertButt = Button(toolbar, text="Insert Image", command=do_nothing)
# insertButt.pack(side=LEFT, padx=2, pady=2)
# printButt = Button(toolbar, text="Insert Image", command=do_nothing)
# printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ***** Status Bar *****

statusbar = Frame(root, bd=1, relief=SUNKEN)
status = Label(statusbar, text="Preparing to do nothing...")
watermark = Label(statusbar, text=" |  © 2020 Oskari Haikka")
watermark.pack(side=RIGHT)
timer = Timer(statusbar, RIGHT)
status.pack(side=LEFT)
statusbar.pack(side=BOTTOM, fill=X)

# ****** Actual stuff ********
drawing_frame = Frame(root)
drawing_frame.pack()

open_tasks()

root.mainloop()
