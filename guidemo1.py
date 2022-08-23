from tkinter import *
from tkinter import messagebox
def Ok():
    uname=e1.get()
    password=e2.get()
    messagebox.showinfo("","login succesfill")
    print(uname)
    print(password)
def no():
    uname=e1.get()
    password=e2.get()
    messagebox.showinfo("exit","quit")
    
root=Tk()
root.title("login")
root.geometry("500x500")
Label(root,text="username").place(x=10,y=10)
Label(root,text="password").place(x=10,y=40)
e1=Entry(root)
e1.place(x=140,y=10)
e2=Entry(root)
e2.place(x=140,y=40)
e2.config(show="*")
Button(root,text="Login",command=Ok,height=2,width=10).place(x=10,y=100)
Button(root,text="quit",command=quit,height=2,width=10).place(x=400,y=100)
root.mainloop()
