#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mallen
#
# Created:     29/11/2012
# Copyright:   (c) mallen 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

def stats(s, d, cn, i, w, ch):
    rolls = [s, d, cn, i, w, ch]
    return rolls

def roll():
    import random
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    roll3 = random.randint(1,6)
    roll4 = random.randint(1,6)
    roll = [roll1, roll2, roll3, roll4]
    roll.sort()
    roll.pop(0)
    return roll[0] + roll[1] + roll[2]

from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.v = StringVar()
        Label(master, textvariable=self.v).pack(side=LEFT)

        Button(frame, text = "Roll Stats", command=self.rolls).pack(side=LEFT)

    def rolls(self):
        self.v.set(stats(roll(),roll(),roll(),roll(),roll(),roll()))



root = Tk()

app = App(root)

root.mainloop()

if __name__ == '__main__':
    main()