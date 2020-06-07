from tkinter import *



def create_login(login_usrname, login_psw, login_usr_entry, login_pssw_entry, window):
    login_user_label = Label(window, text="Benutzername").pack()
    login_usr_entry = Entry(window, textvariable=login_usrname)
    login_usr_entry.pack()
    login_psw_label = Label(window, text="Password").pack()
    login_pssw_entry = Entry(window, textvariable=login_psw, show="*")
    login_pssw_entry.pack()

    Login_button = Button(window, text="Submit").pack()