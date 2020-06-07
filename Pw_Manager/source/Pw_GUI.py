from tkinter import *
from tkinter.ttk import *
import GUI_func




def RegisterWindow():
    register_win = Toplevel(root)
    register_win.title("Registrierung")
    register_win.geometry("300x300")

    global username
    global password
    global user_entry
    global psw_entry
    global status
    username = StringVar()
    user_entry = Entry()
    password = StringVar()
    psw_entry = Entry()
    GUI_func.create_login(username, password, user_entry, psw_entry, register_win)


def Main_Window():
    global root
    root = Tk()
    root.geometry("300x300")
    root.title("MainWindow")

    global login_username
    global login_password
    global login_user_entry
    global login_psw_entry
    login_username = StringVar()
    login_user_entry = Entry()
    login_password = StringVar()
    login_psw_entry = Entry()
    GUI_func.create_login(login_username, login_password, login_user_entry, login_psw_entry, root)
    Register_button = Button(text="Register", command=RegisterWindow).pack()



    root.mainloop()


Main_Window()