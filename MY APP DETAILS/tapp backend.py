
########################login successful window#########(5)
def login_sucess():
  global successwin
  successwin = Toplevel(window)
  successwin.title("MTRADE APP")
  successwin.geometry("150x100")




#####MENU LIST IN LOGIN WINDOW###############################
  mb =  Menubutton ( successwin, text="MENU", relief=RAISED, activebackground='green',direction=LEFT )
  mb.grid()
  mb.menu =  Menu ( mb, tearoff = 0 )
  mb["menu"] =  mb.menu
  markets = IntVar()
  news = IntVar()
  mystocks = IntVar()
  commodities = IntVar()
  mutualfunds = IntVar()
  currencies = IntVar()
  mb.menu.add_checkbutton ( label="MARKETS",variable=markets )
  mb.menu.add_checkbutton ( label="NEWS",variable=news)
  mb.menu.add_checkbutton ( label="MTSTOCKS",variable=mystocks )
  mb.menu.add_checkbutton ( label="COMMODITIES",variable=news)
  mb.menu.add_checkbutton ( label="MUTUAL FUNDS",variable=mutualfunds )
  mb.menu.add_checkbutton ( label="CURRENCIES",variable=currencies)
  mb.pack()
  ##Label(successwin, text = "Thank You Successfully Logged").pack()
  ##Button(successwin, text = "OK", command =dellogwin).pack()


############################wrong password window###############(6) 
def password_not_recognised():
  global passwindow
  passwindow = Toplevel(window)
  passwindow.title("Login Window")
  passwindow.geometry("150x100")
  Label(passwindow, text = "Worng Password Try Agian").pack()
  ##Button(passwindow, text = "OK", command =delpasswin).pack()

  
 
#######################Not entered anything in username n password#(7)
def user_not_found():
  global emptyspace
  emptyspace = Toplevel(window)
  emptyspace.title("Login Window")
  emptyspace.geometry("150x100")
  Label(emptyspace, text = "Incorrect Username Enter Correct Username").pack()
  ##Button(emptyspace, text = "OK", command =emptyspacewin).pack()


####################registered user##############(4)
def register_user():
  print("working")
   
  username_info = username.get()
  password_info = password.get()
 
  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()
 
  username_entry.delete(0, END)
  password_entry.delete(0, END)
 
  Label(regwindow, text = "Registration Successful", fg = "green" ,font = ("calibri", 11)).pack()


######################login verification###################(5)
def login_verify():
   
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)
 
  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
    else:
        password_not_recognised()
 
  else:
        user_not_found()
   


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
 
