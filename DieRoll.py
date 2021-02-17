#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mallen
#
# Created:     30/10/2012
# Copyright:   (c) mallen 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame()
        frame.grid()

        Label(frame, text = "Dice Size").grid(row=0, column=0)

        self.d = Entry(frame)
        self.d.grid(row=0, column=1)

        self.y = Entry(frame)
        self.y.grid(row=1,column=1)

        Label(frame, text = "Number of Dice").grid(row=1, column=0)

        Button(frame, text = "Roll", command=self.d2).grid(row=2, column=0)

        self.two = StringVar()
        Label(frame, textvariable=self.two).grid(row=2, column=1)

        Button(frame, text = "Roll Percent", command=self.dper).grid(row=3,column=0)

        self.per = StringVar()
        Label(frame, textvariable=self.per).grid(row=3,column=1)

    def d2(self):
        import random
        roll = 0
        n = int(self.y.get())
        while n > 0:
            roll = roll + (random.randint(1, int(self.d.get())))
            n = n - 1
        self.two.set(roll)

    def dper(self):
        import random
        a = random.randint(1,10)
        b = random.randint(1,10)
        if a == 10 and b == 10:
            self.per.set(100)
        elif a == 10 and b < 10:
            self.per.set(b)
        elif a < 10 and b == 10:
            self.per.set(a * 10)
        else:
            self.per.set((a * 10) + b)

root = Tk()

app = App(root)

root.mainloop()


if __name__ == '__main__':
    main()
