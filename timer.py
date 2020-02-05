from tkinter import *


class Timer:

    def __init__(self, root, side):
        self.root = root
        self.running = False
        self.t = StringVar()
        self.t.set("00:00:00")
        self.d = str(self.t.get())
        timer_lbl = Label(root, textvariable=self.t)
        timer_lbl.pack(side=side)
        self.start()

    def reset(self):
        self.t.set("00:00:00")

    def start(self):
        self.running = True
        timer = self.t
        self.timer()

    def stop(self):
        self.running = False

    def timer(self):
        if self.running:
            self.d = str(self.t.get())
            h, m, s = map(int, self.d.split(":"))

            h = int(h)
            m = int(m)
            s = int(s)
            if s < 59:
                s += 1
            elif s == 59:
                s = 0
                if m < 59:
                    m += 1
                elif m == 59:
                    m = 0
                    h += 1
            if h < 10:
                h = str(0) + str(h)
            else:
                h = str(h)
            if m < 10:
                m = str(0) + str(m)
            else:
                m = str(m)
            if s < 10:
                s = str(0) + str(s)
            else:
                s = str(s)
            self.d = h + ":" + m + ":" + s
            self.t.set(self.d)
            if self.running:
                self.root.after(1000, self.start)


'''
root = Tk()
btn1 = Button(root, text="MOIIIS")
btn1.grid(row=0, column=0)
btn2 = Button(root, text="MOIIIS")
btn2.grid(row=0, column=2)
btn3 = Button(root, text="MOIIIS")
btn3.grid(row=1, column=1)
d = Timer(root, 0, 1)
root.mainloop()
'''
