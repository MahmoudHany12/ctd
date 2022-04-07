import hashlib
from tkinter import *
import re
password='SuperHardPassword99'
PASHASH1 = hashlib.md5(password.encode("utf-8")).hexdigest()
def fcomp():
    e1=a1.get()
    e2=a2.get()
    PASHASH2 = hashlib.md5(e2.encode("utf-8")).hexdigest()
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if e1 == "guest" and PASHASH2 == PASHASH1:
        msg = Message(m, text = "you logged in").place(x=100,y= 100)
    elif regex.search(e1) == None or regex.search(e2) == None:
        msg = Message(m, text = " don't enter special char ").place(x=100,y= 100)
    elif e1=="" or e2=="":
        msg = Message(m, text = " you didn't enter  ").place(x=100,y= 100)
    else :  msg = Message(m, text = " wrong password or username ").place(x=100,y= 100)
m = Tk()
m.geometry("900x300")
m.title('                       LOGIN      ')
Label(m, text='Username').grid(row=0)
Label(m, text='password').grid(row=1)
a1 = Entry(m)
a2 = Entry(m)
a1.grid(row=0, column=1)
a2.grid(row=1, column=1)
a2.config(show = '*')
button = Button(m, text='login', width=20,fg ="blue",command=fcomp).place(x=240,y= 200)
m.mainloop()
