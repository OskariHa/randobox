from tkinter import *
from project_tasks import DailyTasks
from timer import Timer
from loginwindow import LoginWindow
from stockwindow_updating import StockWindowUpdating
from stockwindow_static import StockWindowStatic
from admin_account_window import AdminAccountWindow
from account_window import AccountOptions
from account import Account
from minesweep import MineSweep


# frame for apps and toolbar
global drawing_frame, toolbar


# start stockwindow updating
def open_stocks_updating():
    switch_frame()
    stocks = StockWindowUpdating(drawing_frame, toolbar)

# start stock window static
def open_stocks_static():
    switch_frame()
    stocks = StockWindowStatic(drawing_frame, toolbar)


# start project_tasks.DailyTasks(frame, toolbar)
def open_tasks():
    switch_frame()
    tasks = DailyTasks(drawing_frame, toolbar)


# start account_class.AccountOptions(frame)
def account_info():
    switch_frame()
    AccountOptions(drawing_frame)


# run minesweep
def minesweep():
    switch_frame()
    MineSweep(drawing_frame, toolbar)


# start accountwindow.AdminAccountWindow(frame,toolbar)
def admin_account_window():
    switch_frame()
    AdminAccountWindow(drawing_frame, toolbar)


# switching app to display on frame
def switch_frame():
    global drawing_frame, toolbar
    toolbar.destroy()
    toolbar = Frame(root, bg="green")
    toolbar.pack(side=TOP, fill=X)

    drawing_frame.destroy()
    drawing_frame = Frame(root)
    drawing_frame.pack()
    print("frame swiped")


# end program
def close_program():
    print("exit by x")
    sys.exit()


# login window for login
login_window = Tk()
login_window.minsize(width=300, height=200)
login_window.protocol("WM_DELETE_WINDOW", close_program)
# title and icon
login_window.title("randobox - Login")
login_window.iconbitmap(default="images/kekw.ico")
# frame for login
login_window_frame = Frame(login_window, bd=1, relief=RAISED)
login_window_frame.pack(pady=(20, 0), anchor=CENTER)
# login app and mainloop for login window
LoginWindow(login_window_frame, login_window)
login_window.mainloop()

root = Tk()
root.title("randobox")
root.minsize(width=800, height=600)
root.iconbitmap(default="images/kekw.ico")
# ***** Main Menu ******

menu = Menu(root)
root.config(menu=menu)

# basic menu for apps
subMenu = Menu(menu)
menu.add_cascade(label="Project", menu=subMenu)
subMenu.add_command(label="Tasks", command=open_tasks)
subMenu.add_command(label="Exit", command=close_program)

# stock menu
stockmenu = Menu(menu)
menu.add_cascade(label="Stocks", menu=stockmenu)
stockmenu.add_command(label="Updating", command=open_stocks_updating)
stockmenu.add_command(label="Static", command=open_stocks_static)

# minesweep menu
minesweepMenu = Menu(menu)
menu.add_cascade(label="MineSweep", menu=minesweepMenu)
minesweepMenu.add_command(label="Play", command=minesweep)

# account menu for account settings
accountMenu = Menu(menu)
menu.add_cascade(label="Account", menu=accountMenu)
accountMenu.add_command(label="Change account info", command=account_info)

# check account status to create admin menu
if Account.status == "master" or Account.status == "admin":
    adminMenu = Menu(menu)
    menu.add_cascade(label="Admin", menu=adminMenu)
    adminMenu.add_command(label="Accounts", command=admin_account_window)

# ***** Toolbar ******
toolbar = Frame(root, bg="green")
toolbar.pack(side=TOP, fill=X)

# ***** Status Bar *****
statusbar = Frame(root, bd=1, relief=SUNKEN)
# watermark on status bar
watermark = Label(statusbar, text=" |  © 2020 Oskari Haikka")
watermark.pack(side=RIGHT)
# timer to start after login
timer = Timer(statusbar, RIGHT)
# pack on bottom
statusbar.pack(side=BOTTOM, fill=X)

# ******** Start up *****************
# Frame to draw apps on
drawing_frame = Frame(root)
drawing_frame.pack()
# opening page
open_tasks()
# mainloop for program
root.mainloop()
