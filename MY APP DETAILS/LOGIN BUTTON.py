import tkinter as tk
import tkinter.messagebox as mes
tapp = tk.Tk()

def helloCallBack():
    mes.showinfo( "MTRADE APP", "Sucessfully Logged")

B = tk.Button(tapp, activebackground = 'blue',padx=8,text ="LOGIN", command = helloCallBack)

B.pack()
tapp.mainloop()
