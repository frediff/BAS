from tkinter import *

def paste_button(c,btext,textcol,x1,y1,x2,y2,r,col,fnt=("Bahnschrift", "12")):
    ids = []
    ids += [c.create_rectangle(x1,y1+r,x2,y2-r,fill=col,outline=col)]
    ids += [c.create_rectangle(x1+r,y1,x2-r,y2,fill=col,outline=col)]
    ids += [c.create_arc(x1,y1,x1+2*r,y1+2*r,start=90, extent=90, fill=col, outline=col)]
    ids += [c.create_arc(x2,y1,x2-2*r,y1+2*r,start=0, extent=90, fill=col, outline=col)]
    ids += [c.create_arc(x1,y2,x1+2*r,y2-2*r,start=180, extent=90, fill=col, outline=col)]
    ids += [c.create_arc(x2,y2,x2-2*r,y2-2*r,start=270, extent=90, fill=col, outline=col)]
    ids += [c.create_text((x1+x2)/2, (y1+y2)/2, text= btext,fill=textcol,font=fnt)]
    return ids

def press(event,c,btext,x1,y1,x2,y2,r,dcol,func,dictA):
    paste_button(c,btext,"black",x1,y1,x2,y2,r,'#CBCAB6')
    if((func!=None)):
        if(dictA!=None):
            func(dictA)
        else:
            func()
    
def after_flash(event,c,btext,x1,y1,x2,y2,r,col):
    #print("Single Click, ButtonRelease-l")
    paste_button(c,btext,"white",x1,y1,x2,y2,r,col)

def hover(event,c,x1,y1,x2,y2,r,col="white"):
    #print("Single Click, ButtonRelease-l")
    c.create_line(x1+r,y2-r/2,x2-r,y2-r/2,fill=col,width=3)

def reborn(event,c,btext,x1,y1,x2,y2,r,col,fnt=("Bahnschrift", "12")):
    paste_button(c,btext,"white",x1,y1,x2,y2,r,col,fnt)

def rounded_rectangular_button(root,btext,color,func=None,dictA=None,ro=0,col=0,x1=0,y1=0,x2=200,y2=70,r=15,s=5,rosp=1,colsp=1,bg=None):
    x1 = x1+s
    y1 = y1+s
    x2 = x2-s
    y2 = y2-s
    if(bg==None):
        c = Canvas(root,width=x2-x1+2*s, height=y2-y1+2*s)
    else:
        c = Canvas(root,width=x2-x1+2*s, height=y2-y1+2*s,bg=bg)
    #root.wm_attributes("-tra", 0.5)
    dcol = 'white'

    paste_button(c,btext,'white',x1,y1,x2,y2,r,color)

    c.create_text((x1+x2)/2, (y1+y2)/2, text= btext,fill="white",font=("Bahnschrift", "12"))
    
    c.bind('<Button-1>',lambda event: press(event,c,btext,x1,y1,x2,y2,r,dcol,func,dictA))
    c.bind('<ButtonRelease-1>',lambda event: after_flash(event,c,btext,x1,y1,x2,y2,r,color))
    c.bind('<Enter>',lambda event:hover(event,c,x1,y1,x2,y2,r))
    c.bind('<Leave>',lambda event:reborn(event,c,btext,x1,y1,x2,y2,r,color))

    c.grid(row=ro, column=col, sticky="NSEW", rowspan=rosp, columnspan=colsp)

def rounded_rectangular_button_overlay(root,btext,color,func=None,dictA=None,x1=0,y1=0,x2=200,y2=70,r=15,s=5,bg=None,fnt=("Bahnschrift", "12")):
    if(bg==None):
        c = Canvas(root,width=x2, height=y2+2*s)
    else:
        c = Canvas(root,width=x2, height=y2+2*s,bg=bg)
    #root.wm_attributes("-tra", 0.5)
    dcol = 'white'
    root.create_window((x1,y1),window=c,anchor=NW)

    x1 = s
    y1 = s
    x2 = x2-s
    y2 = y2-s


    ids = paste_button(c,btext,'white',x1,y1,x2,y2,r,color,fnt=fnt)

    ids += [c.create_text((x1+x2)/2, (y1+y2)/2, text= btext,fill="white",font=fnt)]
    
    c.bind('<Button-1>',lambda event: press(event,c,btext,x1,y1,x2,y2,r,dcol,func,dictA))
    c.bind('<ButtonRelease-1>',lambda event: after_flash(event,c,btext,x1,y1,x2,y2,r,color))
    c.bind('<Enter>',lambda event:hover(event,c,x1,y1,x2,y2,r))
    c.bind('<Leave>',lambda event:reborn(event,c,btext,x1,y1,x2,y2,r,color,fnt))
    return ids

def rounded_rectangular_label(root,btext,color="red",textcolor="white",fnt=("Bahnschrift", "12"),ro=0,col=0,rosp=1,colsp=1,x1=0,y1=0,x2=200,y2=70,r=15,s=5):
    x1 = x1+s
    y1 = y1+s
    x2 = x2-s
    y2 = y2-s
    c = Canvas(root,width=x2-x1+2*s, height=y2-y1+2*s)

    dcol = 'white'

    c.create_rectangle(x1,y1+r,x2,y2-r,fill=color,outline=color)
    c.create_rectangle(x1+r,y1,x2-r,y2,fill=color,outline=color)
    c.create_arc(x1,y1,x1+2*r,y1+2*r,start=90, extent=90, fill=color, outline=color)
    c.create_arc(x2,y1,x2-2*r,y1+2*r,start=0, extent=90, fill=color, outline=color)
    c.create_arc(x1,y2,x1+2*r,y2-2*r,start=180, extent=90, fill=color, outline=color)
    c.create_arc(x2,y2,x2-2*r,y2-2*r,start=270, extent=90, fill=color, outline=color)
    
    c.create_text((x1+x2)/2, (y1+y2)/2, text= btext,fill=textcolor,font=fnt)

    c.grid(row=ro, column=col, rowspan=rosp, columnspan=colsp, sticky="NSEW")
    
def rounded_rectangular_label_overlay(c,btext,color="red",textcolor="white",fnt=("Bahnschrift", "12"),x1=0,y1=0,x2=200,y2=70,r=15,s=5,align='c'):
    x1 = x1+s
    y1 = y1+s
    x2 = x2-s
    y2 = y2-s
    #c = Canvas(root,width=x2-x1+2*s, height=y2-y1+2*s)

    dcol = 'white'

    box = []
    box += [c.create_rectangle(x1,y1+r,x2,y2-r,fill=color,outline=color)]
    box += [c.create_rectangle(x1+r,y1,x2-r,y2,fill=color,outline=color)]
    box += [c.create_arc(x1,y1,x1+2*r,y1+2*r,start=90, extent=90, fill=color, outline=color)]
    box += [c.create_arc(x2,y1,x2-2*r,y1+2*r,start=0, extent=90, fill=color, outline=color)]
    box += [c.create_arc(x1,y2,x1+2*r,y2-2*r,start=180, extent=90, fill=color, outline=color)]
    box += [c.create_arc(x2,y2,x2-2*r,y2-2*r,start=270, extent=90, fill=color, outline=color)]
    
    id = 0
    if(align=='c'):
        id = c.create_text((x1+x2)/2, (y1+y2)/2, text= btext,fill=textcolor,font=fnt)
    else:
        id = c.create_text(x1+40, (y1+y2)/2, text= btext,fill=textcolor,font=fnt,anchor=W)
    return id,box

    #c.grid(row=ro, column=col, rowspan=rosp, columnspan=colsp, sticky="NSEW")

def rounded_rectangular_entry(root,ro=0,col=0,rosp=1,colsp=1,x1=0,y1=0,x2=200,y2=70,r=15,s=5):

    x1 = x1+s
    y1 = y1+s
    x2 = x2-s
    y2 = y2-s
    c = Canvas(root,width=x2-x1+2*s, height=y2-y1+2*s, highlightthickness=0)

    
    
    c.create_line(x1+r,y1,x2-r,y1,fill="black",width=3)
    c.create_line(x2,y1+r,x2,y2-r,fill="black",width=3)
    c.create_line(x2-r,y2,x1+r,y2,fill="black",width=3)
    c.create_line(x1,y2-r,x1,y1+r,fill="black",width=3)

    c.create_arc(x1,y1,x1+2*r,y1+2*r,start=90, extent=90, fill="black", style=ARC,width=3)
    c.create_arc(x2,y1,x2-2*r,y1+2*r,start=0, extent=90,  fill="black",style=ARC,width=3)
    c.create_arc(x1,y2,x1+2*r,y2-2*r,start=180, extent=90, fill="black",style=ARC,width=3)
    c.create_arc(x2,y2,x2-2*r,y2-2*r,start=270, extent=90, fill="black",style=ARC,width=3)


    #c.bind('<Button-1>',lambda event:usr_inp(event,c,x1,y1,x2,y2,r,count-1))
    #c.bind('<Key>',lambda event:update_entry(event,c,x1,y1,x2,y2,r,idx))
    c.grid(row=ro, column=col, rowspan=rosp, columnspan=colsp, sticky="NSEW")

    return c

def rounded_rectangular_border(c,col,x1=0,y1=0,x2=200,y2=70,r=15,s=5,wid=5):
    x1 = x1+s
    y1 = y1+s
    x2 = x2-s
    y2 = y2-s
    c.create_line(x1+r,y1,x2-r,y1,fill=col,width=wid)
    c.create_line(x2,y1+r,x2,y2-r,fill=col,width=wid)
    c.create_line(x2-r,y2,x1+r,y2,fill=col,width=wid)
    c.create_line(x1,y2-r,x1,y1+r,fill=col,width=wid)

    c.create_arc(x1,y1,x1+2*r,y1+2*r,start=90, extent=90, outline=col, style=ARC,width=wid)
    c.create_arc(x2,y1,x2-2*r,y1+2*r,start=0, extent=90,  outline=col,style=ARC,width=wid)
    c.create_arc(x1,y2,x1+2*r,y2-2*r,start=180, extent=90, outline=col,style=ARC,width=wid)
    c.create_arc(x2,y2,x2-2*r,y2-2*r,start=270, extent=90, outline=col,style=ARC,width=wid)

def form_field(canv,xl,yl,hl,wl,wr,ftext,col,ds=20,compulsory=False,default="",field=Entry):
    rounded_rectangular_label_overlay(canv,ftext,color=col,textcolor="black",x1=xl,y1=yl,x2=xl+wl,y2=yl+hl,s=0,fnt=("Bahnschrift", "14"))
    xr,yr,hr = xl+wl+ds,yl,hl
    e1 = field(canv, font=("Consolas", "14","bold"), relief=FLAT,  borderwidth=0,highlightthickness=0 ,bg="#d5dbdb")
    if(field==Entry):
        e1.insert(0,default)
    else:
        e1.insert('1.0',default)
        e1.config(yscrollcommand=True)
    canv.create_window((xr+wr/2,yr+hr/2),window=e1,height=hr-ds,width=wr-ds)
    canv.create_text(xl+wl+ds/2,yl+hr/2+5,text=":",font=("Courier","36","bold"))
    rounded_rectangular_border(canv,'black',x1=xr,y1=yr,x2=xr+wr,y2=yr+hr,s=0,wid=3)
    if(compulsory):
        canv.create_text(xr+wr,yr,text="*",font=("Courier","24"),anchor=NW,fill="red")
    return e1

def progressive_rater(event,l1,l2,l3,l4,l5,num,state=None):
    if(num>=0):
        l1.config(text='\u2605')
    if(num>=1):
        l2.config(text='\u2605')
    if(num>=2):
        l3.config(text='\u2605')
    if(num>=3):
        l4.config(text='\u2605')
    if(num>=4):
        l5.config(text='\u2605')
    if(state!=None):
        if((state.val==num)):
            state.val = num-1
            if(num==0):
                l1.config(text='\u2606')
            if(num==1):
                l2.config(text='\u2606')
            if(num==2):
                l3.config(text='\u2606')
            if(num==3):
                l4.config(text='\u2606')
            if(num==4):
                l5.config(text='\u2606')

        else:
            state.val = num

def flush(event,l1,l2,l3,l4,l5,state):
    if(state.val<0):   
        l1.config(text='\u2606')
    if(state.val<1):   
        l2.config(text='\u2606')
    if(state.val<2):   
        l3.config(text='\u2606')
    if(state.val<3):   
        l4.config(text='\u2606')
    if(state.val<4):    
        l5.config(text='\u2606')


class fixed_rate_stars:
    def __init__(self, ncl = -1):
        self.val = ncl

def rating_stars(canv,xl,yl,hl,wl,col,ds=20,initial=-1,not_fixed=True):
    rounded_rectangular_label_overlay(canv,'Rating',color=col,textcolor="black",x1=xl,y1=yl,x2=xl+wl,y2=yl+hl,s=0,fnt=("Bahnschrift", "14"))
    
    canv.create_text(xl+wl+ds/2,yl+hl/2+5,text=":",font=("Courier","36","bold"))
    c = Canvas(canv,height=hl,width=5*hl)
    #c.place(x=xl+wl+ds,y=yl-10,anchor=NW)
    canv.create_window((xl+wl+ds,yl-ds/2),height=64,width=5*64,anchor=NW,window=c)

    if(initial>=0):    
        l1 = Label(c,text="\u2605",fg="#001fff",font=("Courier","64"))
    else:
        l1 = Label(c,text="\u2606",fg="#001fff",font=("Courier","64"))
    if(initial>=1):    
        l2 = Label(c,text="\u2605",fg="#001fff",font=("Courier","64"))
    else:
        l2 = Label(c,text="\u2606",fg="#001fff",font=("Courier","64"))
    if(initial>=2):    
        l3 = Label(c,text="\u2605",fg="#001fff",font=("Courier","64"))
    else:
        l3 = Label(c,text="\u2606",fg="#001fff",font=("Courier","64"))
    if(initial>=3):    
        l4 = Label(c,text="\u2605",fg="#001fff",font=("Courier","64"))
    else:
        l4 = Label(c,text="\u2606",fg="#001fff",font=("Courier","64"))
    if(initial>=4):    
        l5 = Label(c,text="\u2605",fg="#001fff",font=("Courier","64"))
    else:
        l5 = Label(c,text="\u2606",fg="#001fff",font=("Courier","64"))

    state = fixed_rate_stars(initial)

    if(not_fixed):
        l1.bind('<Button-1>',lambda event: progressive_rater(event,l1,l2,l3,l4,l5,0,state))
        l1.bind('<Enter>',lambda event:progressive_rater(event,l1,l2,l3,l4,l5,0))
        l1.bind('<Leave>',lambda event:flush(event,l1,l2,l3,l4,l5,state))
        

        l2.bind('<Button-1>',lambda event: progressive_rater(event,l1,l2,l3,l4,l5,1,state))
        l2.bind('<Enter>',lambda event:progressive_rater(event,l1,l2,l3,l4,l5,1))
        l2.bind('<Leave>',lambda event:flush(event,l1,l2,l3,l4,l5,state))
        

        l3.bind('<Button-1>',lambda event: progressive_rater(event,l1,l2,l3,l4,l5,2,state))
        l3.bind('<Enter>',lambda event:progressive_rater(event,l1,l2,l3,l4,l5,2))
        l3.bind('<Leave>',lambda event:flush(event,l1,l2,l3,l4,l5,state))
        

        l4.bind('<Button-1>',lambda event: progressive_rater(event,l1,l2,l3,l4,l5,3,state))
        l4.bind('<Enter>',lambda event:progressive_rater(event,l1,l2,l3,l4,l5,3))
        l4.bind('<Leave>',lambda event:flush(event,l1,l2,l3,l4,l5,state))
        

        l5.bind('<Button-1>',lambda event: progressive_rater(event,l1,l2,l3,l4,l5,4,state))
        l5.bind('<Enter>',lambda event:progressive_rater(event,l1,l2,l3,l4,l5,4))
        l5.bind('<Leave>',lambda event:flush(event,l1,l2,l3,l4,l5,state))
        
    l1.grid(row=0,column=0)
    l2.grid(row=0,column=1)
    l3.grid(row=0,column=2)
    l4.grid(row=0,column=3)
    l5.grid(row=0,column=4)
    return state

def move(event,canv,ids,lid,boxes):
    for samp in ids:
        x,y = canv.coords(samp)
        
        canv.coords(samp,x,y-8*(2*event.num-9))
    
    x1,y1,x2,y2 = canv.coords(lid)
    canv.coords(lid,x1,y1+8*(2*event.num-9),x2,y2+8*(2*event.num-9))

    for box in boxes:
        r1 = box[0]
        r2 = box[1]
        a1 = box[2]
        a2 = box[3]
        a3 = box[4]
        a4 = box[5]

        x1,y1,x2,y2 = canv.coords(r1)
        canv.coords(r1,x1,y1-8*(2*event.num-9),x2,y2-8*(2*event.num-9))

        x1,y1,x2,y2 = canv.coords(r2)
        canv.coords(r2,x1,y1-8*(2*event.num-9),x2,y2-8*(2*event.num-9))

        x1,y1,x2,y2 = canv.coords(a1)
        canv.coords(a1,x1,y1-8*(2*event.num-9),x2,y2-8*(2*event.num-9))

        x1,y1,x2,y2 = canv.coords(a2)
        canv.coords(a2,x1,y1-8*(2*event.num-9),x2,y2-8*(2*event.num-9))

        x1,y1,x2,y2 = canv.coords(a3)
        canv.coords(a3,x1,y1-8*(2*event.num-9),x2,y2-8*(2*event.num-9))

        x1,y1,x2,y2 = canv.coords(a4)
        canv.coords(a4,x1,y1-8*(2*event.num-9),x2,y2-8*(2*event.num-9))

def scroll(event,canv,ids,lid,boxes):
    x1,y1,x2,y2 = canv.coords(lid)
    ds = (y1+y2)/2 - event.y
    canv.coords(lid,x1,event.y-(y2-y1)/2,x2,event.y+(y2-y1)/2)

    for samp in ids:
        x,y = canv.coords(samp)
        
        canv.coords(samp,x,y+ds)
        
    for box in boxes:
        r1 = box[0]
        r2 = box[1]
        a1 = box[2]
        a2 = box[3]
        a3 = box[4]
        a4 = box[5]

        x1,y1,x2,y2 = canv.coords(r1)
        canv.coords(r1,x1,y1+ds,x2,y2+ds)

        x1,y1,x2,y2 = canv.coords(r2)
        canv.coords(r2,x1,y1+ds,x2,y2+ds)

        x1,y1,x2,y2 = canv.coords(a1)
        canv.coords(a1,x1,y1+ds,x2,y2+ds)

        x1,y1,x2,y2 = canv.coords(a2)
        canv.coords(a2,x1,y1+ds,x2,y2+ds)

        x1,y1,x2,y2 = canv.coords(a3)
        canv.coords(a3,x1,y1+ds,x2,y2+ds)

        x1,y1,x2,y2 = canv.coords(a4)
        canv.coords(a4,x1,y1+ds,x2,y2+ds)

def select(event,count,c,ids,boxes,choice,colh,col):
    if(choice.num==-1):
        choice.num = count
        choice.val = c.itemcget(ids[count],'text')
        box = boxes[count]
        r1 = box[0]
        r2 = box[1]
        a1 = box[2]
        a2 = box[3]
        a3 = box[4]
        a4 = box[5]

        c.itemconfig(r1,fill=colh,outline=colh)
        c.itemconfig(r2,fill=colh,outline=colh)
        c.itemconfig(a1,fill=colh,outline=colh)
        c.itemconfig(a2,fill=colh,outline=colh)
        c.itemconfig(a3,fill=colh,outline=colh)
        c.itemconfig(a4,fill=colh,outline=colh)
    elif(choice.num==count):
        choice.num = -1
        choice.val = ""
        box = boxes[count]
        r1 = box[0]
        r2 = box[1]
        a1 = box[2]
        a2 = box[3]
        a3 = box[4]
        a4 = box[5]

        c.itemconfig(r1,fill=col,outline=col)
        c.itemconfig(r2,fill=col,outline=col)
        c.itemconfig(a1,fill=col,outline=col)
        c.itemconfig(a2,fill=col,outline=col)
        c.itemconfig(a3,fill=col,outline=col)
        c.itemconfig(a4,fill=col,outline=col)

    else:
        
        choice.val = c.itemcget(ids[count],'text')
        box = boxes[count]
        r1 = box[0]
        r2 = box[1]
        a1 = box[2]
        a2 = box[3]
        a3 = box[4]
        a4 = box[5]

        c.itemconfig(r1,fill=colh,outline=colh)
        c.itemconfig(r2,fill=colh,outline=colh)
        c.itemconfig(a1,fill=colh,outline=colh)
        c.itemconfig(a2,fill=colh,outline=colh)
        c.itemconfig(a3,fill=colh,outline=colh)
        c.itemconfig(a4,fill=colh,outline=colh)

        box = boxes[choice.num]
        r1 = box[0]
        r2 = box[1]
        a1 = box[2]
        a2 = box[3]
        a3 = box[4]
        a4 = box[5]

        c.itemconfig(r1,fill=col,outline=col)
        c.itemconfig(r2,fill=col,outline=col)
        c.itemconfig(a1,fill=col,outline=col)
        c.itemconfig(a2,fill=col,outline=col)
        c.itemconfig(a3,fill=col,outline=col)
        c.itemconfig(a4,fill=col,outline=col)

        choice.num = count

class list_choice:
    def __init__(self, ncl = "", num=-1):
        self.val = ncl
        self.num = num

def list_viewer(canvas,x,y,w,h,col,list_items=[""],colh="#f4d03f"):
    c = Canvas(canvas,height=h,width=w)
    choice = list_choice()
    x1 = 0
    y1 = 0
    x2 = w
    y2 = h
    r = 15

    c.create_rectangle(x1,y1+r,x2,y2-r,fill=col,outline=col)
    c.create_rectangle(x1+r,y1,x2-r,y2,fill=col,outline=col)
    c.create_arc(x1,y1,x1+2*r,y1+2*r,start=90, extent=90, fill=col, outline=col)
    c.create_arc(x2,y1,x2-2*r,y1+2*r,start=0, extent=90, fill=col, outline=col)
    c.create_arc(x1,y2,x1+2*r,y2-2*r,start=180, extent=90, fill=col, outline=col)
    c.create_arc(x2,y2,x2-2*r,y2-2*r,start=270, extent=90, fill=col, outline=col)
    
    c.create_line(w-19.75,0,w-19.75,h,width=18,fill='#d5f5e3')
    lid = c.create_line(w-20,10,w-20,h/4+10,width=9,capstyle=ROUND,fill='#186a3b')
    

    count = 0
    ids = []
    boxes = []
    for content in list_items:
        #rounded_rectangular_label_overlay(c,btext,color="red",textcolor="white",fnt=("Bahnschrift", "12"),x1=0,y1=0,x2=200,y2=70,r=15,s=5):
        obj,box = rounded_rectangular_label_overlay(c,btext=content,color="#82e0aa",textcolor="black",fnt=("Consolas","12"),x1=5,y1=5+count*40,x2=w-40,y2=5+count*40+30,r=15,s=0,align='l')
        #obj = c.create_text(5,5+count*20,text=content,font=("Consolas","12"),anchor=NW,fill="black")
        c.tag_bind(obj,'<Button-1>',lambda event,count=count:select(event,count,c,ids,boxes,choice,colh,"#82e0aa"))
        c.tag_bind(box[1],'<Button-1>',lambda event,count=count:select(event,count,c,ids,boxes,choice,colh,"#82e0aa"))
        ids += [obj]
        boxes += [box]
        count += 1

    tcount = count
    count = 0
    
    c.bind('<Button-4>',lambda event:move(event,c,ids,lid,boxes))
    c.bind('<Button-5>',lambda event:move(event,c,ids,lid,boxes))

    c.tag_bind(lid,'<B1-Motion>',lambda event:scroll(event,c,ids,lid,boxes))
    id = canvas.create_window((x,y),window=c,height=h,width=w,anchor=NW)
    return choice
#25C9

class radio_button:
    def __init__(self, idx=-1):
        self.idx = idx

def checker_radio(event,radio,canv,c,num):
    if(radio.idx == -1):
        canv.itemconfig(c[num],text='\u25C9')
        radio.idx = num
    elif(radio.idx == num):
        canv.itemconfig(c[num],text='\u25cb')
        radio.idx = -1
    else:
        canv.itemconfig(c[radio.idx],text='\u25cb')
        canv.itemconfig(c[num],text='\u25C9')
        radio.idx = num

def checker_box(canv,x1,y1,items=["ISBN","Title","Author","Genre"]):
    c = []
    radio = radio_button()
    c1 = canv.create_text(x1,y1,text="\u25cb",font=("Consolas","48"),fill="blue",anchor=NW)
    c2 = canv.create_text(x1+200,y1,text="\u25cb",font=("Consolas","48"),fill="blue",anchor=NW)
    c3 = canv.create_text(x1,y1+60,text="\u25cb",font=("Consolas","48"),fill="blue",anchor=NW)
    c4 = canv.create_text(x1+200,y1+60,text="\u25cb",font=("Consolas","48"),fill="blue",anchor=NW)
    s=50
    dh = 35
    t1 = canv.create_text(x1+s,y1+dh,text="ISBN",font=("Bahnschrift", "12"),fill="blue",anchor=NW)
    t2 = canv.create_text(x1+200+s,y1+dh,text="Title",font=("Bahnschrift", "12"),fill="blue",anchor=NW)
    t3 = canv.create_text(x1+s,y1+60+dh,text="Author",font=("Bahnschrift", "12"),fill="blue",anchor=NW)
    t4 = canv.create_text(x1+200+s,y1+60+dh,text="Genre",font=("Bahnschrift", "12"),fill="blue",anchor=NW)


    c = [c1,c2,c3,c4]
    canv.tag_bind(c1,'<Button-1>',lambda event:checker_radio(event,radio,canv,c,0))
    canv.tag_bind(c2,'<Button-1>',lambda event:checker_radio(event,radio,canv,c,1))
    canv.tag_bind(c3,'<Button-1>',lambda event:checker_radio(event,radio,canv,c,2))
    canv.tag_bind(c4,'<Button-1>',lambda event:checker_radio(event,radio,canv,c,3))

    return radio

def delete_elem(dictA):
    c = dictA['c']
    coll = dictA['coll']
    id = dictA['i']
    order = dictA['o']

    order.cart.pop(order.widget_map[id])
    order.widget_map.pop(id)

    lx,ly = c.coords(id)
    c.delete(id)
    i = coll.index(id)
    coll.remove(id)
    itr = i
    #print(coll.__len__())
    while (itr<(coll.__len__())):
        cx,cy = c.coords(coll[itr])
        c.coords(coll[itr],lx,ly)
        lx,ly = cx,cy
        itr += 1

def plus(dictA):
    id = dictA['i']
    c = dictA['c']
    order = dictA['o']
    idc = dictA['idc']
    v = c.itemcget(id,'text')
    #print(v)
    #print('---')
    order.cart[order.widget_map[idc]] += 1
    c.itemconfig(id,text=str(int(v)+1))

def minus(dictA):
    id = dictA['i']
    c = dictA['c']
    order = dictA['o']
    idc = dictA['idc']
    v = c.itemcget(id,'text')
    if(int(v)>1):
        order.cart[order.widget_map[idc]] -= 1
        c.itemconfig(id,text=str(int(v)-1))

def elemental(canv,order,label1,label1a,label2,x,y,w,h,collection,bg='#f4d03f'):
    c = Canvas(canv,height=h,width=610,bg=bg)
    idc = canv.create_window((x,y),window=c,height=h,width=w,anchor=NW)
    collection += [idc]
    order.widget_map[idc] = label1
    rounded_rectangular_label_overlay(c,btext=label1+ "\t" + label1a,color="#16a085",textcolor="white",fnt=("Ubuntu", "16"),x1=0,y1=0,x2=w-400,y2=h,r=15,s=0,align='c')
    id,box = rounded_rectangular_label_overlay(c,btext=str(label2),color="#2980b9",textcolor="white",fnt=("Ubuntu", "16"),x1=w-380,y1=0,x2=w-300,y2=h,r=15,s=0,align='c')
    #print(c.itemcget(id,'text'))
    rounded_rectangular_button_overlay(c,btext='\u274C',color="red",func=delete_elem,dictA={'coll':collection,'i':idc,'c':canv, 'o':order},x1=w-280,y1=0,x2=80,y2=h,r=15,s=0,bg=bg,fnt=("Consolas","36"))
    rounded_rectangular_button_overlay(c,btext='+',color="#239b56",func=plus,dictA={'idc':idc, 'i':id,'c':c, 'o':order},x1=w-180,y1=0,x2=80,y2=h,r=15,s=0,bg=bg,fnt=("Consolas","36"))
    rounded_rectangular_button_overlay(c,btext='-',color="#6c3483",func=minus,dictA={'idc':idc, 'i':id,'c':c, 'o':order},x1=w-80,y1=0,x2=80,y2=h,r=15,s=0,bg=bg,fnt=("Consolas","36"))
    return collection

def movec(event,collection,c,lid):
    for samp in collection:
        x,y = c.coords(samp)
        
        c.coords(samp,x,y-8*(2*event.num-9))
    x1,y1,x2,y2 = c.coords(lid)
    c.coords(lid,x1,y1+8*(2*event.num-9),x2,y2+8*(2*event.num-9))

def scrollc(event,collection,c,lid):
    x1,y1,x2,y2 = c.coords(lid)
    ds = (y1+y2)/2 - event.y
    c.coords(lid,x1,event.y-(y2-y1)/2,x2,event.y+(y2-y1)/2)

    for samp in collection:
        x,y = c.coords(samp)
        
        c.coords(samp,x,y+ds)

def scrollable_content(c,x1,y1,w,h,collection,bg='#f4d03f'):
    x2 = x1 + w
    y2 = y1 + h
    r = 15
    col =  bg
    c.create_rectangle(x1,y1+r,x2,y2-r,fill=col,outline=col)
    c.create_rectangle(x1+r,y1,x2-r,y2,fill=col,outline=col)
    c.create_arc(x1,y1,x1+2*r,y1+2*r,start=90, extent=90, fill=col, outline=col)
    c.create_arc(x2,y1,x2-2*r,y1+2*r,start=0, extent=90, fill=col, outline=col)
    c.create_arc(x1,y2,x1+2*r,y2-2*r,start=180, extent=90, fill=col, outline=col)
    c.create_arc(x2,y2,x2-2*r,y2-2*r,start=270, extent=90, fill=col, outline=col)
    
    c.create_line(w-19.75,0,w-19.75,h,width=18,fill='#d5f5e3')
    
    lid = c.create_line(w-20,10,w-20,h/4+10,width=9,capstyle=ROUND,fill='#186a3b')
    
    c.bind('<Button-4>',lambda event:movec(event,collection,c,lid))
    c.bind('<Button-5>',lambda event:movec(event,collection,c,lid))

    c.tag_bind(lid,'<B1-Motion>',lambda event:scrollc(event,collection,c,lid))
    
def failure_msg(msg):
    w = Toplevel()
    w.title("FAILURE")
    msg = Message(w, text = msg,width=400)
    msg.config(bg='red', fg="white", font=("Bahnschrift", "20"), borderwidth=8)
    msg.pack(fill=BOTH,ipadx=20)

def success_msg(msg,default="SUCCESS"):
    w = Toplevel()
    w.title(default)
    msg = Message(w, text = msg,width=400)
    msg.config(bg='#28be1c', fg="white", font=("Bahnschrift", "20"), borderwidth=8)
    msg.pack(fill=BOTH,ipadx=20)