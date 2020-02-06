from tkinter import *
from project_tasks import DailyTasks
from timer import Timer
from loginwindow import LoginWindow


def do_nothing():
    print("MORO")


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
subMenu.add_command(label="Stats", command=do_nothing)
subMenu.add_command(label="Accounts", command=do_nothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=do_nothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=do_nothing)

# ***** Toolbar ******

toolbar = Frame(root, bg="grey")

insertButt = Button(toolbar, text="Insert Image", command=do_nothing)
# insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Insert Image", command=do_nothing)
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

tasks = DailyTasks(drawing_frame, toolbar)

root.mainloop()
