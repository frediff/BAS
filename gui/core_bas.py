from tkinter import *
from functools import partial
from book_inventory import stat_bk,ins_bk, upd_bk, sell_bk, req_bk, stk_bk, inv_bk, cus_bk
from employee_manage import ins_emp,man_emp
from rr import rounded_rectangular_button, rounded_rectangular_label_overlay,scrollable_content
from PIL import Image, ImageTk

#def move(event,canv,samp):
#    #h = canv.itemcget(samp,'text')
#    x,y=canv.coords(samp)
#    canv.coords(samp,x,y+1)

def run_app():
    root = Tk(className = " BOOK SHOP AUTOMATION SOFTWARE")
    root.wm_attributes("-zoomed", True)
    c = Canvas(root,highlightthickness=0)
    img = ImageTk.PhotoImage(Image.open("bbg1.jpg").point(lambda p: p * 0.6))

    h = 1080*2/3
    w = 1920-250
    canv = Canvas(c,height=h,width=w,highlightthickness=0)
    canv.grid(row=0,column=1,rowspan=10)
    
    canv.create_text(w/2,h/2-h/4,text="Welcome!",font=("Ubuntu","108","italic"),fill="black")
    rounded_rectangular_label_overlay(canv,"Click on any of the buttons on the left side to do the desired task", color='#1e8449',x1=w/4+96-40,y1=h/2,y2=h/2+80,x2=3*w/4+96-40,fnt=("Ubuntu","16"))
    rounded_rectangular_label_overlay(canv,"\u2190", color='#21618c',x1=w/4-40,y1=h/2,y2=h/2+80,x2=w/4+86-40,fnt=("Ubuntu","48"))
    
    #samp = canv.create_text((w/2,h/2+h/4),text="0",font=("Ubuntu","12","italic"),fill="black")
    #canv.itemconfig(samp,text="jjb")
    #canv.tag_bind(samp,'<Button-4>',lambda event:move(event,canv,samp))
    #canv.tag_bind(samp,'<Button-5>',lambda event:move(event,canv,samp))
    #canv.tag_bind(samp,'<Down>',lambda event:movedo(event,canv,samp))
    
    c.create_image(0,1080*2/3,anchor=NW,image=img)
    c.create_text(1920/2,1080*4/5,text="BIBLIO HOUSE", fill="white", font=("Courier", "100"))
    c.pack(expand=True, fill=BOTH)
    c.create_line(1920/2-1920/8,1080*4.3/5,1920/2+1920/8,1080*4.3/5,width=8,fill='white')
    c.create_line(1920/2-1920/8,1080*3.5/5,1920/2+1920/8,1080*3.5/5,width=8,fill='white')
    
    rounded_rectangular_button(root=c,btext="Add a Book",color='green',func=ins_bk,dictA={'c':canv,'root':root},ro=0,col=0,x2=250)
    rounded_rectangular_button(root=c,btext="Add an Employee",color='green',func=ins_emp,dictA={'c':canv,'root':root},ro=1,col=0,x2=250)
    rounded_rectangular_button(root=c,btext="Update Book Details",color='green',func=upd_bk,dictA={'c':canv,'root':root},ro=2,col=0,x2=250)
    rounded_rectangular_button(root=c,btext="Manage Employees",color='green',func=man_emp,dictA={'c':canv,'root':root},ro=3,col=0,x2=250)

    rounded_rectangular_button(root=c,btext="Sell Books",color='#8B8B00',func=sell_bk,dictA={'c':canv,'root':root},ro=4,col=0,x2=250)
    rounded_rectangular_button(root=c,btext="Book Requistion",color='#8B8B00',func=req_bk,dictA={'c':canv,'root':root},ro=5,col=0,x2=250)
    rounded_rectangular_button(root=c,btext="Customer Query",color='#8B8B00',func=cus_bk,dictA={'c':canv,'root':root},ro=6,col=0,x2=250)

    rounded_rectangular_button(root=c,btext="Book Stock Levels",color='#c82907',func=stk_bk,dictA={'c':canv,'root':root},ro=7,col=0,x2=250)
    rounded_rectangular_button(root=c,btext="Get Inventory Levels",color='#c82907',func=inv_bk,dictA={'c':canv,'root':root},ro=8,col=0,x2=250)
    rounded_rectangular_button(root=c,btext="Sales Statistics",color='blue',func=stat_bk,dictA={'c':canv,'root':root},ro=9,col=0,x2=250)

    #rounded_rectangular_button_overlay(root=c,btext='\u2302',color='red',func=None,dictA={'c':canv,'root':root},x1=20,y1=0,x2=80,y2=70,r=15,s=5,bg=None)


    root.mainloop()
