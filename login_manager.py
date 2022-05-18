from cryptography.fernet import Fernet
import base64
import bcrypt
from tkinter import *
from functools import partial
from rr import rounded_rectangular_label, rounded_rectangular_button, rounded_rectangular_entry
OK_LOGIN=False

def check(dictA):
    e2 = dictA['e2']
    e1 = dictA['e1']
    hashed = dictA['hashed']
    usid = dictA['usid']
    ini = dictA['ini']
    password = str(e2.get()).encode('utf-8')
    userid = str(e1.get())

    if((userid==usid) and bcrypt.checkpw(password, hashed)):
        global OK_LOGIN
        OK_LOGIN = True
        ini.destroy()
    else:
        w = Toplevel()
        w.title("FAILURE")
        msg = Message(w, text = "Incorrect Credentials",width=200)
        msg.config(bg='red', fg="white", font=("Bahnschrift", "12"), borderwidth=8)
        msg.pack(fill=BOTH,ipadx=20)

def store_credential(dictA):
    e2 = dictA['e2']
    e1 = dictA['e1']
    ini = dictA['ini']
    if((str(e1.get())=="") or (str(e2.get())=="")):
        w = Toplevel()
        w.title("FAILURE")
        msg = Message(w, text = "Password or UserID cannot be empty!",width=200)
        msg.config(bg='red', fg="white", font=("Bahnschrift", "12"), borderwidth=8)
        msg.pack(fill=BOTH,ipadx=20)
    else:
        password = str(e2.get()).encode('utf-8')
        userid = str(e1.get())
        with open("usr.use","w") as f:
            f.write(userid)
        f.close()
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password, salt)
        with open("keys.adm","wb") as f:
            f.write(hashed)
        f.close()
        global OK_LOGIN
        OK_LOGIN = True
        ini.destroy()  
    

def disable_event():
    pass

def login():
    try:
        with open("keys.adm","rb") as f:
            hashed = f.read()
        f.close()
        with open("usr.use","r") as f:
            usid = f.read()
        f.close()
        ini = Tk(className = " LOGIN WINDOW")
        rounded_rectangular_label(ini,"ADMIN LOGIN","#EE4000","white",("Bahnschrift", "20"),0,0,1,2,x2=600)
        rounded_rectangular_label(ini,"USER ID  :","#CBCAB6","black",("Bahnschrift", "12"),1,0,1,1)
        rounded_rectangular_label(ini,"PASSWORD :","#CBCAB6","black",("Bahnschrift", "12"),2,0,1,1)
        
        e1 = Entry(rounded_rectangular_entry(ini,ro=1,col=1,x2=400),font=("Consolas", "14","bold"), relief=FLAT,  borderwidth=0,highlightthickness=0 ,bg="#E3E3E3")
        e1.place(height=50,width=380,x=10,y=10)
        e2 = Entry(rounded_rectangular_entry(ini,ro=2,col=1,x2=400),font=("Bahnschrift", "12"), show='\u2b24', relief=FLAT,  borderwidth=0,highlightthickness=0, bg="#E3E3E3")
        e2.place(height=50,width=380,x=10,y=10)
        
        dictA = {
            'e2' : e2,
            'e1' : e1,
            'hashed' : hashed,
            'usid' : usid,
            'ini' : ini
        }
        
        rounded_rectangular_button(ini,"SIGN IN","springgreen4",ro=3,colsp=2,func=check,dictA=dictA,x1=100,x2=500)
        
        ini.mainloop()
    except OSError:
        
        ini = Tk(className = " NEW USER SIGNUP WINDOW")

        rounded_rectangular_label(ini,"ADMIN SIGNUP","#EE4000","white",("Bahnschrift", "20"),0,0,1,2,x2=600)
        rounded_rectangular_label(ini,"CREATE USER ID  :","#CBCAB6","black",("Bahnschrift", "12"),1,0,1,1)
        rounded_rectangular_label(ini,"CREATE PASSWORD :","#CBCAB6","black",("Bahnschrift", "12"),2,0,1,1)
        
        e1 = Entry(rounded_rectangular_entry(ini,ro=1,col=1,x2=400),font=("Consolas", "14","bold"), relief=FLAT,  borderwidth=0,highlightthickness=0 ,bg="#E3E3E3")
        e1.place(height=50,width=380,x=10,y=10)
        e2 = Entry(rounded_rectangular_entry(ini,ro=2,col=1,x2=400),font=("Bahnschrift", "12"), show='\u2b24', relief=FLAT,  borderwidth=0,highlightthickness=0, bg="#E3E3E3")
        e2.place(height=50,width=380,x=10,y=10)

        dictA = {
            'e2' : e2,
            'e1' : e1,
            'ini' : ini
        }
        rounded_rectangular_button(ini,"SIGN UP","springgreen4",ro=3,colsp=2,func=store_credential,dictA=dictA,x1=100,x2=500)
        
        ini.mainloop()
    return OK_LOGIN
