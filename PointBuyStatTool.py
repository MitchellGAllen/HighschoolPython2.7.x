#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Mitchell
#
# Created:     08/03/2013
# Copyright:   (c) Mitchell 2013
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

        self.str = 8
        self.dex = 8
        self.con = 8
        self.int = 8
        self.wis = 8
        self.cha = 8

        self.v = IntVar()
        Radiobutton(frame, text="25 Point Buy", value=25, variable = self.v,).grid(row=0,column=0)
        Radiobutton(frame, text="32 Point Buy", value=32, variable = self.v,).grid(row=1,column=0)

        Label(frame, text = "Points Available").grid(row=2,column=0)
        Label(frame, textvariable = self.v).grid(row=2,column=1)
        Label(frame, textvariable = self.str).grid(row=3,column=0)
        Label(frame, textvariable = self.dex).grid(row=4,column=0)
        Label(frame, textvariable = self.con).grid(row=5,column=0)
        Label(frame, textvariable = self.int).grid(row=6,column=0)
        Label(frame, textvariable = self.wis).grid(row=7,column=0)



root = Tk()

app = App(root)

root.mainloop()

if __name__ == '__main__':
    main()
