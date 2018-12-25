from tkinter import *

import tkinter as tk
import tkinter.messagebox as mes
tapp = tk.Tk()
CheckVar1 = IntVar()
C1 = Checkbutton(tapp, text = "Keep me logged in", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C1.pack()
tapp.mainloop()
