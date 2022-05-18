from tkinter import *
from functools import partial
from rr import success_msg,failure_msg,scrollable_content,elemental,checker_box,rounded_rectangular_label_overlay,list_viewer,rating_stars,form_field,rounded_rectangular_button_overlay, rounded_rectangular_border, rounded_rectangular_entry, rounded_rectangular_button
import webbrowser
from db_m.insert_book import insert_book
from db_m.search_book_by_author import search_book_by_author
from db_m.search_book_by_ISBN import search_book_by_ISBN
from db_m.search_book_by_title import search_book_by_title
from db_m.search_book_by_genre import search_book_by_genre
from db_m.update_book import update_book
from db_m.check_threshold import check_threshold
from db_m.fill_bookreqform import fill_bookreqform
from db_m.get_book_title import get_book_title
from db_m.get_book_price import get_book_price
from db_m.pdfmaking_cust import printReceipt
from db_m.db import SaleUpdate
from datetime import datetime
from db_m.update_copies import update_copies
from db_m.get_book_copies import get_book_copies
from db_m.get_inventory_level import get_inventory_level
from db_m.plot import stats

def get_isbn(choice,result):
    if(choice.num==-1):
        return ""
    else:
        return str(result[choice.num][0])

def gui_upd_bk(dictA):
    ISBN = dictA['isbn']
    book_title = dictA['title'].get()
    author = dictA['author'].get()
    language_ = dictA['language'].get()
    genre = dictA['genre'].get()
    price = dictA['price'].get()
    copies = dictA['copies'].get()
    rack_number = dictA['rack'].get()
    vendor_name = dictA['stk_nam'].get()
    vendor_mobile = dictA['stk_phn'].get()
    vendor_mailID = dictA['stk_eml'].get()
    review = dictA['review'].get(1.0, "end-1c")
    rating = dictA['rating'].val + 1
    average_procurement_time = dictA['proc_time'].get()

    if "" in [ISBN, book_title, author, language_, price, copies, rack_number, vendor_name, vendor_mobile,  average_procurement_time]:
        failure_msg("Fields marked * cannot be empty!")
        return
    msg = update_book(ISBN, book_title, author, language_, genre, price, copies, rack_number, vendor_name, vendor_mailID, vendor_mobile,  review, rating, average_procurement_time)
    if(msg[0]=='B'):
        success_msg(msg)
    else:
        failure_msg(msg)

def upd_form(dictA):
    isbn = get_isbn(dictA['isbn'],dictA['reslist'])
    if(isbn==""):
        failure_msg("No book chosen")
        return
    info = dictA['reslist'][dictA['isbn'].num]
    canv = dictA['c']
    canv.delete('all')
    root = dictA['root']
    h = 1080*2/3
    w = 1920-250
    canv.create_rectangle(0,0,h,w,width=0)
    canv.grid(row=0, column=1, rowspan=10)
    rounded_rectangular_border(canv,'green',x2=w-10,y2=h,s=10,r=30)
    
    ds = 25

    canv.create_text(w/2,24+ds,text="BOOK UPDATE FORM",fill="green",font=("serif", "24"))
    canv.create_line(w/2-w/24,24+2.5*ds,w/2+w/24,24+2.5*ds,fill="green",width=5)
    
    yl,hl,wl,wr=40+3*ds,45,220,400
    xl = w/2 - wl - wr - 6*ds - 20
    rounded_rectangular_label_overlay(canv,btext="ISBN",color="#f39c12",textcolor="black",fnt=("Bahnschrift", "12"),x1=xl,y1=yl,x2=xl+wl,y2=yl+hl,r=15,s=0,align='c')
    rounded_rectangular_label_overlay(canv,btext=isbn,color="#3498db",textcolor="#f4d03f",fnt=("Consolas", "20","bold"),x1=xl+wl+ds,y1=yl,x2=xl+wl+ds+wr,y2=yl+hl,r=15,s=0,align='c')
    xl=xl+wl+wr+12*ds
    stk_nam = form_field(canv,xl,yl,hl,wl,wr,"Stockist Name","#f39c12",compulsory=True,default=info[8])
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    book_title = form_field(canv,xl,yl,hl,wl,wr,"Book Title","#58d68d",compulsory=True,default=info[1])
    xl=xl+wl+wr+12*ds
    stk_eml = form_field(canv,xl,yl,hl,wl,wr,"Stockist Email","#58d68d",default=info[9])
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    author = form_field(canv,xl,yl,hl,wl,wr,"Author","#58d68d",compulsory=True,default=info[2])
    xl=xl+wl+wr+12*ds
    stk_phn = form_field(canv,xl,yl,hl,wl,wr,"Stockist Contact No.","#f39c12",compulsory=True,default=info[10])
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    language = form_field(canv,xl,yl,hl,wl,wr,"Language","#f39c12",compulsory=True,default=info[3])
    xl=xl+wl+wr+12*ds
    price = form_field(canv,xl,yl,hl,wl,wr,"Price (in Rs.)","#58d68d",compulsory=True,default=info[5])
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    genre = form_field(canv,xl,yl,hl,wl,wr,"Genre","#58d68d",compulsory=False,default=info[4])
    xl=xl+wl+wr+12*ds
    proc_time = form_field(canv,xl,yl,hl,wl,wr,"Procurement Time","#f39c12",compulsory=True,default=info[11])
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    rack = form_field(canv,xl,yl,hl,wl,wr,"Rack Number","#f39c12",compulsory=True,default=info[7])
    xl=xl+wl+wr+12*ds
    review = form_field(canv,xl,yl,3*hl+2*ds,wl,wr,"Review\n(if any)","#5dade2",compulsory=False,field=Text,default=info[13])
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    copies = form_field(canv,xl,yl,hl,wl,wr,"No. of Copies","#58d68d",compulsory=True,default=info[6])

    yl=yl+hl+ds
    stars = rating_stars(canv,xl,yl,hl,wl,"#a569bd",initial=int(info[14])-1)

    args = {'isbn':isbn,'title':book_title,'author':author,'language':language,'genre':genre,'price':price,'copies':copies,'rack':rack,'stk_nam':stk_nam,'stk_eml':stk_eml,'stk_phn':stk_phn,'review':review,'rating':stars,'proc_time':proc_time}
    rounded_rectangular_button_overlay(root=canv,btext="Update",color='red',func=gui_upd_bk,dictA=args,x1=w/2-w/16,x2=200,y1=yl+hl/2,y2=3*hl/2)

def upd_bk(dictA):
    canv = dictA['c']
    canv.delete('all')
    root = dictA['root']
    h = 1080*2/3
    w = 1920-250
    canv.create_rectangle(0,0,h,w,width=0)
    canv.grid(row=0, column=1, rowspan=10)
    rounded_rectangular_border(canv,'green',x2=w-10,y2=h,s=10,r=30)
    book_search(root,canv,w/2-50,100,w/2,h-150,task="Update Chosen Book",taskfunc=upd_form)

def inf_dat(dictA):
    isbn = get_isbn(dictA['isbn'],dictA['reslist'])
    if(isbn==""):
        failure_msg("No book chosen")
        return
    info = dictA['reslist'][dictA['isbn'].num]
    canv = dictA['c']
    canv.delete('all')
    root = dictA['root']
    h = 1080*2/3
    w = 1920-250
    canv.create_rectangle(0,0,h,w,width=0)
    canv.grid(row=0, column=1, rowspan=10)
    rounded_rectangular_border(canv,'green',x2=w-10,y2=h,s=10,r=30)
    
    ds = 25

    canv.create_text(w/2,24+ds,text="BOOK INFORMATION",fill="green",font=("serif", "24"))
    canv.create_line(w/2-w/24,24+2.5*ds,w/2+w/24,24+2.5*ds,fill="green",width=5)
    
    yl,hl,wl,wr=40+3*ds,45,220,400
    xl = w/2 - wl - wr - 6*ds - 20
    rounded_rectangular_label_overlay(canv,btext="ISBN",color="#f39c12",textcolor="black",fnt=("Bahnschrift", "14"),x1=xl,y1=yl,x2=xl+wl,y2=yl+hl,r=15,s=0,align='c')
    rounded_rectangular_label_overlay(canv,btext=isbn,color="#85c1e9",textcolor="black",fnt=("Consolas", "14","bold"),x1=xl+wl+ds,y1=yl,x2=xl+wl+ds+wr,y2=yl+hl,r=15,s=0,align='c')
    xl=xl+wl+wr+12*ds
    rounded_rectangular_label_overlay(canv,btext="Stockist Name",color="#58d68d",textcolor="black",fnt=("Bahnschrift", "14"),x1=xl,y1=yl,x2=xl+wl,y2=yl+hl,r=15,s=0,align='c')
    rounded_rectangular_label_overlay(canv,btext=info[8],color="#85c1e9",textcolor="black",fnt=("Consolas", "14","bold"),x1=xl+wl+ds,y1=yl,x2=xl+wl+ds+wr,y2=yl+hl,r=15,s=0,align='c')
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    rounded_rectangular_label_overlay(canv,btext="Book Title",color="#58d68d",textcolor="black",fnt=("Bahnschrift", "14"),x1=xl,y1=yl,x2=xl+wl,y2=yl+hl,r=15,s=0,align='c')
    rounded_rectangular_label_overlay(canv,btext=info[1],color="#85c1e9",textcolor="black",fnt=("Consolas", "14","bold"),x1=xl+wl+ds,y1=yl,x2=xl+wl+ds+wr,y2=yl+hl,r=15,s=0,align='c')
    xl=xl+wl+wr+12*ds
    rounded_rectangular_label_overlay(canv,btext="Stockist Email",color="#f39c12",textcolor="black",fnt=("Bahnschrift", "14"),x1=xl,y1=yl,x2=xl+wl,y2=yl+hl,r=15,s=0,align='c')
    rounded_rectangular_label_overlay(canv,btext=info[9],color="#85c1e9",textcolor="black",fnt=("Consolas", "14","bold"),x1=xl+wl+ds,y1=yl,x2=xl+wl+ds+wr,y2=yl+hl,r=15,s=0,align='c')
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    rounded_rectangular_label_overlay(canv,btext="Author",color="#f39c12",textcolor="black",fnt=("Bahnschrift", "14"),x1=xl,y1=yl,x2=xl+wl,y2=yl+hl,r=15,s=0,align='c')
    rounded_rectangular_label_overlay(canv,btext=info[2],color="#85c1e9",textcolor="black",fnt=("Consolas", "14","bold"),x1=xl+wl+ds,y1=yl,x2=xl+wl+ds+wr,y2=yl+hl,r=15,s=0,align='c')
    xl=xl+wl+wr+12*ds
    rounded_rectangular_label_overlay(canv,btext="Stockist Contact No.",color="#58d68d",textcolor="black",fnt=("Bahnschrift", "14"),x1=xl,y1=yl,x2=xl+wl,y2=yl+hl,r=15,s=0,align='c')
    rounded_rectangular_label_overlay(canv,btext=info[10],color="#85c1e9",textcolor="black",fnt=("Consolas", "14","bold"),x1=xl+wl+ds,y1=yl,x2=xl+wl+ds+wr,y2=yl+hl,r=15,s=0,align='c')
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    rounded_rectangular_label_overlay(canv,btext="Language",color="#58d68d",textcolor="black",fnt=("Bahnschrift", "14"),x1=xl,y1=yl,x2=xl+wl,y2=yl+hl,r=15,s=0,align='c')
    rounded_rectangular_label_overlay(canv,btext=info[3],color="#85c1e9",textcolor="black",fnt=("Consolas", "14","bold"),x1=xl+wl+ds,y1=yl,x2=xl+wl+ds+wr,y2=yl+hl,r=15,s=0,align='c')
    xl=xl+wl+wr+12*ds
    rounded_rectangular_label_overlay(canv,btext="Price",color="#f39c12",textcolor="black",fnt=("Bahnschrift", "14"),x1=xl,y1=yl,x2=xl+wl,y2=yl+hl,r=15,s=0,align='c')
    rounded_rectangular_label_overlay(canv,btext=info[5],color="#85c1e9",textcolor="black",fnt=("Consolas", "14","bold"),x1=xl+wl+ds,y1=yl,x2=xl+wl+ds+wr,y2=yl+hl,r=15,s=0,align='c')
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    rounded_rectangular_label_overlay(canv,btext="Genre",color="#f39c12",textcolor="black",fnt=("Bahnschrift", "14"),x1=xl,y1=yl,x2=xl+wl,y2=yl+hl,r=15,s=0,align='c')
    rounded_rectangular_label_overlay(canv,btext=info[4],color="#85c1e9",textcolor="black",fnt=("Consolas", "14","bold"),x1=xl+wl+ds,y1=yl,x2=xl+wl+ds+wr,y2=yl+hl,r=15,s=0,align='c')
    xl=xl+wl+wr+12*ds
    rounded_rectangular_label_overlay(canv,btext="Procurement Time",color="#58d68d",textcolor="black",fnt=("Bahnschrift", "14"),x1=xl,y1=yl,x2=xl+wl,y2=yl+hl,r=15,s=0,align='c')
    rounded_rectangular_label_overlay(canv,btext=info[11],color="#85c1e9",textcolor="black",fnt=("Consolas", "14","bold"),x1=xl+wl+ds,y1=yl,x2=xl+wl+ds+wr,y2=yl+hl,r=15,s=0,align='c')
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    rounded_rectangular_label_overlay(canv,btext="Rack Number",color="#58d68d",textcolor="black",fnt=("Bahnschrift", "14"),x1=xl,y1=yl,x2=xl+wl,y2=yl+hl,r=15,s=0,align='c')
    rounded_rectangular_label_overlay(canv,btext=info[7],color="#85c1e9",textcolor="black",fnt=("Consolas", "14","bold"),x1=xl+wl+ds,y1=yl,x2=xl+wl+ds+wr,y2=yl+hl,r=15,s=0,align='c')
    xl=xl+wl+wr+12*ds
    rounded_rectangular_label_overlay(canv,btext="Review\n(if any)",color="#f39c12",textcolor="black",fnt=("Bahnschrift", "14"),x1=xl,y1=yl,x2=xl+wl,y2=yl+3*hl+2*ds,r=15,s=0,align='c')
    rounded_rectangular_label_overlay(canv,btext=info[13],color="#f4d03f",textcolor="black",fnt=("Consolas", "14","bold"),x1=xl+wl+ds,y1=yl,x2=xl+wl+ds+wr,y2=yl+3*hl+2*ds,r=15,s=0,align='c')
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    rounded_rectangular_label_overlay(canv,btext="Copies",color="#f39c12",textcolor="black",fnt=("Bahnschrift", "14"),x1=xl,y1=yl,x2=xl+wl,y2=yl+hl,r=15,s=0,align='c')
    rounded_rectangular_label_overlay(canv,btext=info[6],color="#85c1e9",textcolor="black",fnt=("Consolas", "14","bold"),x1=xl+wl+ds,y1=yl,x2=xl+wl+ds+wr,y2=yl+hl,r=15,s=0,align='c')
    
    yl=yl+hl+ds
    rating_stars(canv,xl,yl,hl,wl,"#a569bd",initial=int(info[14])-1,not_fixed=False)

def cus_bk(dictA):
    canv = dictA['c']
    canv.delete('all')
    root = dictA['root']
    h = 1080*2/3
    w = 1920-250
    canv.create_rectangle(0,0,h,w,width=0)
    canv.grid(row=0, column=1, rowspan=10)
    rounded_rectangular_border(canv,'green',x2=w-10,y2=h,s=10,r=30)
    book_search(root,canv,w/2-50,100,w/2,h-150,task="Get Info",taskfunc=inf_dat)

def gui_ins_bk(dictA):
    ISBN = dictA['isbn'].get()
    book_title = dictA['title'].get()
    author = dictA['author'].get()
    language_ = dictA['language'].get()
    genre = dictA['genre'].get()
    price = dictA['price'].get()
    copies = dictA['copies'].get()
    rack_number = dictA['rack'].get()
    vendor_name = dictA['stk_nam'].get()
    vendor_mobile = dictA['stk_phn'].get()
    vendor_mailID = dictA['stk_eml'].get()
    review = dictA['review'].get(1.0, "end-1c")
    rating = dictA['rating'].val + 1
    average_procurement_time = dictA['proc_time'].get()


    if "" in [ISBN, book_title, author, language_, price, copies, rack_number, vendor_name, vendor_mobile,  average_procurement_time]:
        failure_msg("Fields marked * cannot be empty!")
        return
    msg = insert_book(ISBN, book_title, author, language_, genre, price, copies, rack_number, vendor_name, vendor_mailID, vendor_mobile,  review, rating, average_procurement_time)
    if(msg[0]=='B'):
        success_msg(msg)
    else:
        failure_msg(msg)

def ins_bk(dictA):
    canv = dictA['c']
    canv.delete('all')
    root = dictA['root']
    h = 1080*2/3
    w = 1920-250
    canv.create_rectangle(0,0,h,w,width=0)
    canv.grid(row=0, column=1, rowspan=10)
    rounded_rectangular_border(canv,'green',x2=w-10,y2=h,s=10,r=30)
    
    ds = 25

    args = []

    canv.create_text(w/2,24+ds,text="BOOK ENTRY FORM",fill="green",font=("serif", "24"))
    canv.create_line(w/2-w/24,24+2.5*ds,w/2+w/24,24+2.5*ds,fill="green",width=5)
    
    yl,hl,wl,wr=40+3*ds,45,220,400
    xl = w/2 - wl - wr - 6*ds - 20
    book_title = form_field(canv,xl,yl,hl,wl,wr,"Book Title","#58d68d",compulsory=True)
    xl=xl+wl+wr+12*ds
    stk_nam = form_field(canv,xl,yl,hl,wl,wr,"Stockist Name","#f39c12",compulsory=True)
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    isbn = form_field(canv,xl,yl,hl,wl,wr,"ISBN","#f39c12",compulsory=True)
    xl=xl+wl+wr+12*ds
    stk_eml = form_field(canv,xl,yl,hl,wl,wr,"Stockist Email","#58d68d")
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    author = form_field(canv,xl,yl,hl,wl,wr,"Author","#58d68d",compulsory=True)
    xl=xl+wl+wr+12*ds
    stk_phn = form_field(canv,xl,yl,hl,wl,wr,"Stockist Contact No.","#f39c12",compulsory=True)
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    language = form_field(canv,xl,yl,hl,wl,wr,"Language","#f39c12",compulsory=True)
    xl=xl+wl+wr+12*ds
    price = form_field(canv,xl,yl,hl,wl,wr,"Price (in Rs.)","#58d68d",compulsory=True)
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    genre = form_field(canv,xl,yl,hl,wl,wr,"Genre","#58d68d",compulsory=True)
    xl=xl+wl+wr+12*ds
    proc_time = form_field(canv,xl,yl,hl,wl,wr,"Procurement Time","#f39c12",compulsory=True)
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    rack = form_field(canv,xl,yl,hl,wl,wr,"Rack Number","#f39c12",compulsory=True)
    xl=xl+wl+wr+12*ds
    review = form_field(canv,xl,yl,3*hl+2*ds,wl,wr,"Review\n(if any)","#5dade2",compulsory=False,field=Text)
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    copies = form_field(canv,xl,yl,hl,wl,wr,"No. of Copies","#58d68d",compulsory=True)

    yl=yl+hl+ds
    stars = rating_stars(canv,xl,yl,hl,wl,"#a569bd")

    args = {'isbn':isbn,'title':book_title,'author':author,'language':language,'genre':genre,'price':price,'copies':copies,'rack':rack,'stk_nam':stk_nam,'stk_eml':stk_eml,'stk_phn':stk_phn,'review':review,'rating':stars,'proc_time':proc_time}

    rounded_rectangular_button_overlay(root=canv,btext="Submit",color='red',func=gui_ins_bk,dictA=args,x1=w/2-w/16,x2=200,y1=yl+hl/2,y2=3*hl/2)

def gui_ins_req(dictA):
    ISBN = dictA['isbn'].get()
    book_title = dictA['title'].get()
    author = dictA['author'].get()
    language_ = dictA['language'].get()
    genre = dictA['genre'].get()
    review = dictA['review'].get(1.0, "end-1c")
    rating = dictA['rating'].val + 1


    if "" in [book_title, author, language_]:
        failure_msg("Fields marked * cannot be empty!")
        return
    if(ISBN == ""):
        ISBN = "0000000000"
    msg = fill_bookreqform(ISBN, book_title, author, language_, genre, review, rating)
    if(msg[0]=='B'):
        success_msg(msg)
    else:
        failure_msg(msg)

def req_bk(dictA):
    canv = dictA['c']
    canv.delete('all')
    root = dictA['root']
    h = 1080*2/3
    w = 1920-250
    canv.create_rectangle(0,0,h,w,width=0)
    canv.grid(row=0, column=1, rowspan=10)
    rounded_rectangular_border(canv,'#8B8B00',x2=w-10,y2=h,s=10,r=30)
    
    ds = 25

    canv.create_text(w/2,24+ds,text="BOOK REQUISITION FORM",fill="green",font=("serif", "24"))
    canv.create_line(w/2-w/24,24+2.5*ds,w/2+w/24,24+2.5*ds,fill="green",width=5)
    
    yl,hl,wl,wr=40+3*ds,45,220,400
    xl = w/2 - wl - wr - 6*ds - 20
    isbn = form_field(canv,xl,yl,hl,wl,wr,"ISBN (if known)","#58d68d",compulsory=False)
    xl=xl+wl+wr+12*ds
    book_title = form_field(canv,xl,yl,hl,wl,wr,"Book Title","#f39c12",compulsory=True)
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    author = form_field(canv,xl,yl,hl,wl,wr,"Author","#f39c12",compulsory=True)
    xl=xl+wl+wr+12*ds
    genre = form_field(canv,xl,yl,hl,wl,wr,"Genre","#58d68d",compulsory=False)
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    language = form_field(canv,xl,yl,hl,wl,wr,"Language","#58d68d",compulsory=True)
    xl=xl+wl+wr+12*ds
    review = form_field(canv,xl,yl,2*hl+ds,wl,wr,"Review\n(if any)","#5dade2",compulsory=False,field=Text)
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    stars = rating_stars(canv,xl,yl,hl,wl,"#a569bd")

    args = {'isbn':isbn,'title':book_title,'author':author,'language':language,'genre':genre,'review':review,'rating':stars}

    rounded_rectangular_button_overlay(root=canv,btext="Submit",color='red',func=gui_ins_req,dictA=args,x1=w/2-w/16,x2=200,y1=yl+hl/2,y2=3*hl/2)

def book_search(parent,canv,x1,y1,w,h,task="Nothing",taskfunc=None,threshold=False):
    ds = 25

    if(threshold):
        result = []
        c = Canvas(canv,height=h,width=w)
        canv.create_window((x1,y1),window=c,height=h,width=w,anchor=NW)
        dictA = {'parent':parent,'r':result,'canv':c,'x1':x1,'y1':y1,'w':w,'h':h,'root':canv,'threshold':1,'t':task,'tf':taskfunc}
        spider_lists(dictA)
    else:
        result = []

        canv.create_text(w/2,24+ds,text="BOOKS SEARCH",fill="green",font=("serif", "24"))
        canv.create_line(w/2-w/12,24+2.5*ds,w/2+w/12,24+2.5*ds,fill="green",width=5)
    
        rounded_rectangular_label_overlay(canv,"Search By",color="#5dade2",textcolor="Black",fnt=("Bahnschrift", "12"),x1=20,y1=y1-80+80,x2=200,y2=y1+20+80,r=15,s=5)

        #rounded_rectangular_label_overlay(canv,"ISBN",color="#f5b041",textcolor="black",fnt=("Bahnschrift", "12"),x1=x1,y1=y1-80,x2=x1+2*w/5-40,y2=y1-10,r=15,s=5)
        #rounded_rectangular_label_overlay(canv,"Book Title",color="#f5b041",textcolor="black",fnt=("Bahnschrift", "12"),x1=x1+2*w/5+5-40,y1=y1-80,x2=x1+w-40,y2=y1-10,r=15,s=5)
    
        query = form_field(canv,20,y1+120,40,100,w-220,"Query","#58d68d",compulsory=True)


        radios = ["ISBN","Title","Author","Genre"]
        choice = checker_box(canv,x1=210,y1=y1-20,items=radios)

        c = Canvas(canv,height=h,width=w)
        canv.create_window((x1,y1),window=c,height=h,width=w,anchor=NW)

        dictA = {'parent':parent,'r':result,'canv':c,'x1':x1,'y1':y1,'w':w,'h':h,'root':canv,'q':query,'c':choice,'t':task,'tf':taskfunc}

        rounded_rectangular_button_overlay(root=canv,btext="Search It",color='red',func=spider_lists,dictA=dictA,x1=w/2-100,x2=100,y1=y1+180,y2=60,s=0)
    
    #list_viewer(canv,x1+10,y1-10,w-10,h-10,'#28b463',result)

def book_query(field,query):
    result = 0
    if(field==0):
        try:
            int(query)
            result = search_book_by_ISBN(int(query))
        except ValueError:
            failure_msg("Sorry ISBN query should be an integer")
            return []
    if(field==1):
        result = search_book_by_title(query)
    if(field==2):
        result = search_book_by_author(query)
    if(field==3):
        result = search_book_by_genre(query)
    return result

def reformat(strings,space):
    space = '\t'*space
    string_result = []
    for string in strings:
        a,b = str(string[0]),str(string[1])
        string_result += [a+' '*(13-a.__len__())+space+b]
    return string_result

def spider_lists(dictA):
    if(dictA.get('threshold')==None):
        canv = dictA['canv']
        result = dictA['r']
        x1 = dictA['x1']
        y1 = dictA['y1']
        w = dictA['w']
        h = dictA['h']
        root = dictA['root']
        query = dictA['q'].get()

        if(query==""):
            failure_msg("Sorry query cannot be empty")
            return

        field = dictA['c'].idx
        if(field==-1):
            failure_msg("Please choose whether to search by ISBN, Author, Title or Genre")
            return
        parent = dictA['parent']
        func = dictA['tf']
        task = dictA['t']

        canv.delete('all')
        result = book_query(field,query)
        string_result = reformat(result,3)
        choice = list_viewer(canv,10,10,w-10,h-10,'#28b463',string_result)

        rounded_rectangular_label_overlay(root,"ISBN",color="#f5b041",textcolor="black",fnt=("Bahnschrift", "12"),x1=x1,y1=y1-80,x2=x1+2*w/5-40,y2=y1-10,r=15,s=5)
        rounded_rectangular_label_overlay(root,"Book Title",color="#f5b041",textcolor="black",fnt=("Bahnschrift", "12"),x1=x1+2*w/5+5-40,y1=y1-80,x2=x1+w-40,y2=y1-10,r=15,s=5)

        rounded_rectangular_button_overlay(root=root,btext=task,color='green',func=func,dictA={'isbn':choice,'reslist':result,'c':root,'root':parent},x1=w/2-150,x2=200,y1=y1+250,y2=60,s=0)
    else:
        canv = dictA['canv']
        result = dictA['r']
        x1 = dictA['x1']
        y1 = dictA['y1']
        w = dictA['w']
        h = dictA['h']
        root = dictA['root']
        parent = dictA['parent']

        canv.delete('all')
        result = check_threshold()
        string_result = reformat(result,7)

        choice = list_viewer(canv,10,10,w-10,h-10,'#28b463',string_result)
        task = dictA['t']
        func = dictA['tf']

        rounded_rectangular_label_overlay(root,"ISBN",color="#f5b041",textcolor="black",fnt=("Bahnschrift", "12"),x1=x1,y1=y1-80,x2=x1+2*w/5-40,y2=y1-10,r=15,s=5)
        rounded_rectangular_label_overlay(root,"Book Title",color="#f5b041",textcolor="black",fnt=("Bahnschrift", "12"),x1=x1+2*w/5+5-40,y1=y1-80,x2=x1+w-40,y2=y1-10,r=15,s=5)
        rounded_rectangular_button_overlay(root=root,btext=task,color='green',func=func,dictA={'isbn':choice,'reslist':result,'c':root,'root':parent},x1=w/2-125,x2=250,y1=h+220,y2=60,s=0)

class basket:
    def __init__(self,shopped={},wmap={}):
        self.cart = shopped
        self.widget_map = wmap

order = basket()

def sell_bk(dictA):
    global order
    if(dictA.get('back')==None):
        order.cart = {}
    canv = dictA['c']
    canv.delete('all')
    root = dictA['root']
    h = 1080*2/3
    w = 1920-250
    canv.create_rectangle(0,0,h,w,width=0)
    canv.grid(row=0, column=1, rowspan=10)
    rounded_rectangular_border(canv,'#8B8B00',x2=w-10,y2=h,s=10,r=30)
    book_search(root,canv,w/2-50,100,w/2,h-150,task="Add to Cart",taskfunc=add_tocart)

def add_tocart(dictA):
    global order
    isbn = get_isbn(dictA['isbn'],dictA['reslist'])
    if(isbn==""):
        failure_msg("No book chosen")
    else:
        if(order.cart.get(isbn)==None):
            order.cart[isbn]=1
        else:
            order.cart[isbn]+=1
        canv = dictA['c']
        root = dictA['root']
        w = 1920-250
        rounded_rectangular_button_overlay(root=canv,btext="Show Cart",color='#2ecc71',func=reveal_cart,dictA={'c':canv,'root':root},x1=w/4-150,x2=200,y1=100+250+80,y2=60,s=0)

def reveal_cart(dictA):
    global order
    #print(order.cart)
    canv = dictA['c']
    root = dictA['root']
    canv.delete('all')
    collection = []
    y = 100
    count = 0
    w = 1920-250
    h = 1080*2/3
    ds = 25
    rounded_rectangular_border(canv,'#8B8B00',x2=w-10,y2=h,s=10,r=30)
    canv.create_text(w/2,24+ds,text="SHOPPING BASKET",fill="green",font=("serif", "24"))
    canv.create_line(w/2-w/24,24+2.5*ds,w/2+w/24,24+2.5*ds,fill="green",width=5)
    bg = '#b3b6b7'
    c = Canvas(canv)
    canv.create_window((25,100),height=h*2.1/3,width=w-60,window=c,anchor=NW)
    y = 0
    for book in order.cart:
        collection = elemental(c,order,book,get_book_title(book),order.cart[book],30,y,1920-400,60,collection,bg=bg)
        y += 10 + 70
        count += 1

    rounded_rectangular_button_overlay(root=canv,btext="<< Go Back",color='#21618c',func=sell_bk,dictA={'c':canv,'root':root,'back':1},x1=30,x2=200,y1=30,y2=60,s=0)
    rounded_rectangular_button_overlay(root=canv,btext="Check Out >>",color='#068e0a',func=chk_ot,dictA={'c':canv,'root':root, 'o':order},x1=1920-500,x2=170,y1=h-80,y2=60,s=0)
    scrollable_content(c,0,0,w-70,h*2.1/3,collection,bg)
    #gg = collection[0]
    #x,y = canv.coords(gg)
    #canv.coords(gg,x,y+90)

def chk_ot(dictA):
    order = dictA['o']
    cust_order = []
    DATE = datetime.now()
    Formatted_date = DATE.strftime('%d-%m-%Y')
    for isbn in order.cart:
        cust_order += [(str(isbn)+" [" + get_book_title(isbn) + "]", order.cart[isbn], int(get_book_price(isbn)))]
        SaleUpdate(isbn,order.cart[isbn],int(get_book_price(isbn)),Formatted_date)
        ini_cp = int(get_book_copies(isbn))
        ini_cp -= int(order.cart[isbn])
        update_copies(isbn,ini_cp)
    canv = dictA['c']
    canv.delete('all')
    root = dictA['root']
    h = 1080*2/3
    w = 1920-250
    canv.create_rectangle(0,0,h,w,width=0)
    canv.grid(row=0, column=1, rowspan=10)
    rounded_rectangular_border(canv,'green',x2=w-10,y2=h,s=10,r=30)
    
    ds = 25

    canv.create_text(w/2,24+ds,text="CUSTOMER INFO FORM",fill="green",font=("serif", "24"))
    canv.create_line(w/2-w/24,24+2.5*ds,w/2+w/24,24+2.5*ds,fill="green",width=5)
    
    yl,hl,wl,wr=40+3*ds,45,220,400
    xl = w/2 - wl - wr - 6*ds - 20
    name = form_field(canv,xl,yl,hl,wl,wr,"Name","#58d68d",compulsory=True)
    xl=xl+wl+wr+12*ds
    mob = form_field(canv,xl,yl,hl,wl,wr,"Contact No.","#f39c12",compulsory=True)
    xl=xl-wl-wr-12*ds

    args = {'n':name,'m':mob,'r':cust_order}
    rounded_rectangular_button_overlay(root=canv,btext="Print Receipt",color='#d35400',func=gui_receipt,dictA=args,x1=w/2-w/16,x2=200,y1=yl+hl/2,y2=3*hl/2)

def gui_receipt(dictA):
    name = dictA['n'].get()
    mob = dictA['m'].get()
    orders = dictA['r']
    path = printReceipt(name,mob,orders)
    webbrowser.open_new(path)
    success_msg("Order successful!")

def gt_lev(dictA):
    global order
    isbn = get_isbn(dictA['isbn'],dictA['reslist'])
    if(isbn==""):
        failure_msg("No book chosen")
    else:
        info = dictA['reslist'][dictA['isbn'].num]
        success_msg("Currently "+str(info[6])+" copies of the book is available","STOCK")

def procure(dictA):
    isbn = get_isbn(dictA['isbn'],dictA['reslist'])
    if(isbn==""):
        failure_msg("No book chosen")
        return
    canv = dictA['c']
    canv.delete('all')
    root = dictA['root']
    h = 1080*2/3
    w = 1920-250
    canv.create_rectangle(0,0,h,w,width=0)
    canv.grid(row=0, column=1, rowspan=10)
    rounded_rectangular_border(canv,'#c82907',x2=w-10,y2=h,s=10,r=30)

def scarce_bk(dictA):
    canv = dictA['c']
    canv.delete('all')
    root = dictA['root']
    h = 1080*2/3
    w = 1920-250
    canv.create_rectangle(0,0,h,w,width=0)
    canv.grid(row=0, column=1, rowspan=10)
    ds = 25
    rounded_rectangular_border(canv,'#c82907',x2=w-10,y2=h,s=10,r=30)
    canv.create_text(w/2,24+ds,text="BOOKS BELOW THRESHOLD",fill="#c82907",font=("serif", "24"))
    canv.create_line(w/2-w/24,24+2.5*ds,w/2+w/24,24+2.5*ds,fill="#c82907",width=5)
    book_search(root,canv,30,200,w-80,h-300,task="Send Request to Vendor",taskfunc=procure,threshold=True)

def stk_bk(dictA):
    canv = dictA['c']
    canv.delete('all')
    root = dictA['root']
    h = 1080*2/3
    w = 1920-250
    canv.create_rectangle(0,0,h,w,width=0)
    canv.grid(row=0, column=1, rowspan=10)
    rounded_rectangular_border(canv,'#c82907',x2=w-10,y2=h,s=10,r=30)
    book_search(root,canv,w/2-50,100,w/2,h-150,task="Get Stock Level",taskfunc=gt_lev)

    rounded_rectangular_button_overlay(root=canv,btext="See books below threshold stock level",color='red',func=scarce_bk,dictA=dictA,x1=w/4-250,x2=400,y1=500,y2=80)

def gt_inv(dictA):
    global order
    isbn = get_isbn(dictA['isbn'],dictA['reslist'])
    if(isbn==""):
        failure_msg("No book chosen")
    else:
        info = dictA['reslist'][dictA['isbn'].num]
        success_msg("Currently the inventory level for this book is "+str(get_inventory_level(info[0])),"INVENTORY LEVEL")

def inv_bk(dictA):
    canv = dictA['c']
    canv.delete('all')
    root = dictA['root']
    h = 1080*2/3
    w = 1920-250
    canv.create_rectangle(0,0,h,w,width=0)
    canv.grid(row=0, column=1, rowspan=10)
    rounded_rectangular_border(canv,'#c82907',x2=w-10,y2=h,s=10,r=30)
    book_search(root,canv,w/2-50,100,w/2,h-150,task="Get Inventory Level",taskfunc=gt_inv)

def gt_inf(dictA):
    global order
    isbn = get_isbn(dictA['isbn'],dictA['reslist'])
    if(isbn==""):
        failure_msg("No book chosen")
    else:
        canv = dictA['c']
        root = dictA['root']
        h = 1080*2/3
        w = 1920-250

def que_bk(dictA):
    canv = dictA['c']
    canv.delete('all')
    root = dictA['root']
    h = 1080*2/3
    w = 1920-250
    canv.create_rectangle(0,0,h,w,width=0)
    canv.grid(row=0, column=1, rowspan=10)
    rounded_rectangular_border(canv,'#c82907',x2=w-10,y2=h,s=10,r=30)
    book_search(root,canv,w/2-50,100,w/2,h-150,task="Show Book Info",taskfunc=gt_inf)

def stat_bk(dictA):
    canv = dictA['c']
    canv.delete('all')
    root = dictA['root']
    h = 1080*2/3
    w = 1920-250
    canv.create_rectangle(0,0,h,w,width=0)
    canv.grid(row=0, column=1, rowspan=10)
    rounded_rectangular_border(canv,'green',x2=w-10,y2=h,s=10,r=30)
    book_search(root,canv,w/2-50,100,w/2,h-150,task="Get Sales Statistics",taskfunc=stat_gr)

def stat_gr(dictA):
    isbn = get_isbn(dictA['isbn'],dictA['reslist'])
    if(isbn==""):
        failure_msg("No book chosen")
        return
    stats(isbn)

