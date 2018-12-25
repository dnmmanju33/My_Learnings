from tkinter import *
import os
import back

#########REGISTERATION SCREEN##################(2)
def register():
  global regwindow
  regwindow = Toplevel(window)
  regwindow.title("App Registeration")
  regwindow.geometry("300x250")
   
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()
 
  Label(regwindow, text = "Please enter details below").pack()
  Label(regwindow, text = "").pack()

  Label(regwindow, text = "Username * ").pack()
  username_entry = Entry(regwindow, textvariable = username)
  username_entry.pack()
  
  Label(regwindow, text = "Password * ").pack()
  password_entry =  Entry(regwindow, textvariable = password)
  password_entry.pack()
  
  Label(regwindow, text = "").pack()
  Button(regwindow, text = "Register", width = 10, height = 1, command = register_user).pack()
  Button(regwindow, text = "Exit", width = 10, height = 1, command = regwindow.destroy).pack()
 

#############################Login screen###################(3)
def login():
  global logwindow
  logwindow = Toplevel(window)
  logwindow.title("Login")
  logwindow.geometry("300x250")
  Label(logwindow, text = "Please enter details below to login").pack()
  Label(logwindow, text = "").pack()
 
  global username_verify
  global password_verify
   
  username_verify = StringVar()
  password_verify = StringVar()
 
  global username_entry1
  global password_entry1
   
  Label(logwindow, text = "Username * ").pack()
  username_entry1 = Entry(logwindow, textvariable = username_verify)
  username_entry1.pack()
  Label(logwindow, text = "").pack()
  Label(logwindow, text = "Password * ").pack()
  password_entry1 = Entry(logwindow, textvariable = password_verify)
  password_entry1.pack()
  Label(logwindow, text = "").pack()
  Button(logwindow, text = "Login", width = 10, height = 1, command = login_verify).pack()
  Button(logwindow, text = "Exit", width = 10, height = 1, command = logwindow.destroy).pack()


###########ENTRY WINDOW#############(1)
def main_window():
  global window
  window = Tk()
  window.geometry("300x400")
  window.title("MTRADE APP")
  logo=PhotoImage(file='C:\\Users\\ADMIN\\Desktop\\download.png')
  Label(window, image=logo, bg='red').pack()
  Button(text = "Login", height = "2", width = "20", command = login).pack()
##  window.checkbox = Checkbutton(window, text="Keep me logged in", bg='white').pack()
##  fbutton = Button(window, text="Forget your password?").pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2", width = "20", command = register).pack()
  Button(text = "Exit", height = "2" , width = "20", command = window.destroy).pack()
  
  window.mainloop()
 
main_window()
