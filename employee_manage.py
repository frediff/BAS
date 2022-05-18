from tkinter import *
from rr import success_msg,failure_msg,scrollable_content,elemental,checker_box,rounded_rectangular_label_overlay,list_viewer,rating_stars,form_field,rounded_rectangular_button_overlay, rounded_rectangular_border, rounded_rectangular_entry, rounded_rectangular_button
from db_m.insert_employee import insert_employee
from db_m.all_employee import all_employee
from db_m.update_employee_mobile import update_employee_mobile
from db_m.update_employee_wage import update_employee_wage
from db_m.update_employee_mail import update_employee_mail
from db_m.update_employee_name import update_employee_name
from db_m.delete_employee import delete_employee

def get_id(choice,result):
    if(choice.num==-1):
        return ""
    else:
        return str(result[choice.num][0])

def gui_ins_emp(dictA):
    name = dictA['n'].get()
    mail_id = dictA['e'].get()
    mobile = dictA['m'].get()
    wage = dictA['w'].get()    

    if "" in [name, mobile, wage]:
        failure_msg("Fields marked * cannot be empty!")
        return
    msg = insert_employee(name,mail_id,mobile,wage)
    if(type(msg)==type("msg")):
        failure_msg(msg)
    else:
        success_msg("Employee is registered successfully with ID : "+str(msg[0][0]))

def ins_emp(dictA):
    canv = dictA['c']
    canv.delete('all')
    root = dictA['root']
    h = 1080*2/3
    w = 1920-250
    canv.create_rectangle(0,0,h,w,width=0)
    canv.grid(row=0, column=1, rowspan=10)
    rounded_rectangular_border(canv,'green',x2=w-10,y2=h,s=10,r=30)
    
    ds = 25

    canv.create_text(w/2,24+ds,text="EMPLOYEE REGISTRATION FORM",fill="green",font=("serif", "24"))
    canv.create_line(w/2-w/24,24+2.5*ds,w/2+w/24,24+2.5*ds,fill="green",width=5)
    
    yl,hl,wl,wr=40+3*ds,45,220,400
    xl = w/2 - wl - wr - 6*ds - 20
    name = form_field(canv,xl,yl,hl,wl,wr,"Name","#58d68d",compulsory=True)
    xl=xl+wl+wr+12*ds
    wage = form_field(canv,xl,yl,hl,wl,wr,"Wage (in Rs.)","#f39c12",compulsory=True)
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    mob = form_field(canv,xl,yl,hl,wl,wr,"Contact No.","#f39c12",compulsory=True)
    xl=xl+wl+wr+12*ds
    eml = form_field(canv,xl,yl,hl,wl,wr,"Email ID","#58d68d")
    xl=xl-wl-wr-12*ds

    args = {'n':name,'w':wage,'m':mob,'e':eml}
    rounded_rectangular_button_overlay(root=canv,btext="Submit",color='red',func=gui_ins_emp,dictA=args,x1=w/2-w/16,x2=200,y1=yl+hl/2,y2=3*hl/2)

def employee_search(parent,canv,x1,y1,w,h,task="Nothing",taskfunc=None,threshold=False):
    ds = 25

    
    result = []

    c = Canvas(canv,height=h,width=w)
    canv.create_window((x1,y1),window=c,height=h,width=w,anchor=NW)

    dictA = {'parent':parent,'r':result,'canv':c,'x1':x1,'y1':y1,'w':w,'h':h,'root':canv,'t':task,'tf':taskfunc}
    spider_lists(dictA)
    
    #list_viewer(canv,x1+10,y1-10,w-10,h-10,'#28b463',result)

def reformat(strings,space):
    space = '\t'*space
    string_result = []
    for string in strings:
        a,b = str(string[0]),str(string[1])
        string_result += [a+' '*(13-a.__len__())+space+b]
    return string_result

def spider_lists(dictA):
    canv = dictA['canv']
    result = dictA['r']
    x1 = dictA['x1']
    y1 = dictA['y1']
    w = dictA['w']
    h = dictA['h']
    root = dictA['root']
    task = dictA['t']
    func = dictA['tf']

    parent = dictA['parent']


    canv.delete('all')
    result = all_employee()
    string_result = reformat(result,7)
    choice = list_viewer(canv,10,10,w-10,h-10,'#28b463',string_result)

    rounded_rectangular_label_overlay(root,"Employee ID",color="#f5b041",textcolor="black",fnt=("Bahnschrift", "12"),x1=x1,y1=y1-80,x2=x1+2*w/5-40,y2=y1-10,r=15,s=5)
    rounded_rectangular_label_overlay(root,"Employee Name",color="#f5b041",textcolor="black",fnt=("Bahnschrift", "12"),x1=x1+2*w/5+5-40,y1=y1-80,x2=x1+w-40,y2=y1-10,r=15,s=5)

    rounded_rectangular_button_overlay(root=root,btext=task,color='green',func=func,dictA={'id':choice,'reslist':result,'c':root,'root':parent},x1=w/2-100,x2=200,y1=y1+430,y2=60,s=0)
    #rounded_rectangular_button_overlay(root=root,btext='Change Details',color='green',func=upd_emp,dictA=canv,x1=w/4-150,x2=200,y1=y1+250,y2=60,s=0)
    #rounded_rectangular_button_overlay(root=root,btext='Remove Employee',color='red',func=del_emp,dictA=canv,x1=3*w/4-150,x2=200,y1=y1+250,y2=60,s=0)


def man_emp(dictA):
    canv = dictA['c']
    canv.delete('all')
    root = dictA['root']
    h = 1080*2/3
    w = 1920-250
    canv.create_rectangle(0,0,h,w,width=0)
    canv.grid(row=0, column=1, rowspan=10)
    ds = 25
    rounded_rectangular_border(canv,'#c82907',x2=w-10,y2=h,s=10,r=30)
    canv.create_text(w/2,24+ds,text="SELECT EMPLOYEE",fill="#c82907",font=("serif", "24"))
    canv.create_line(w/2-w/24,24+2.5*ds,w/2+w/24,24+2.5*ds,fill="#c82907",width=5)
    employee_search(root,canv,30,200,w-80,h-300,task="Choose This Employee",taskfunc=cho_emp)



def cho_emp(dictA):
    id = get_id(dictA['id'],dictA['reslist'])
    if(id==""):
        failure_msg("No employee chosen")
        return
    info = dictA['reslist'][dictA['id'].num]
    canv = dictA['c']
    canv.delete('all')
    root = dictA['root']
    h = 1080*2/3
    w = 1920-250
    canv.create_rectangle(0,0,h,w,width=0)
    canv.grid(row=0, column=1, rowspan=10)
    rounded_rectangular_border(canv,'green',x2=w-10,y2=h,s=10,r=30)
    
    ds = 25

    canv.create_text(w/2,24+ds,text="UPDATE EMPLOYEE DETAILS FORM",fill="green",font=("serif", "24"))
    canv.create_line(w/2-w/24,24+2.5*ds,w/2+w/24,24+2.5*ds,fill="green",width=5)
    

    yl,hl,wl,wr=40+3*ds,45,220,400
    xl = w/2 - wl - wr - 6*ds - 20
    rounded_rectangular_label_overlay(canv,btext="Employee ID",color="#f39c12",textcolor="black",fnt=("Bahnschrift", "12"),x1=xl+(w-wl-ds-wr)/2,y1=yl,x2=xl+wl+(w-wl-ds-wr)/2,y2=yl+hl,r=15,s=0,align='c')
    rounded_rectangular_label_overlay(canv,btext=id,color="#3498db",textcolor="#f4d03f",fnt=("Consolas", "20","bold"),x1=xl+wl+ds+(w-wl-ds-wr)/2,y1=yl,x2=xl+wl+ds+wr+(w-wl-ds-wr)/2,y2=yl+hl,r=15,s=0,align='c')
    
    yl=yl+hl+ds
    name = form_field(canv,xl,yl,hl,wl,wr,"Name","#58d68d",compulsory=True,default=info[1])
    xl=xl+wl+wr+12*ds
    wage = form_field(canv,xl,yl,hl,wl,wr,"Wage (in Rs.)","#f39c12",compulsory=True,default=info[4])
    xl=xl-wl-wr-12*ds

    yl=yl+hl+ds
    mob = form_field(canv,xl,yl,hl,wl,wr,"Contact No.","#f39c12",compulsory=True,default=info[3])
    xl=xl+wl+wr+12*ds
    eml = form_field(canv,xl,yl,hl,wl,wr,"Email ID","#58d68d",default=info[2])
    xl=xl-wl-wr-12*ds

    args = {'id':id,'n':name,'w':wage,'m':mob,'e':eml}
    rounded_rectangular_button_overlay(root=canv,btext="Change Details",color='#239b56',func=gui_upd_emp,dictA=args,x1=w/4,x2=200,y1=yl+2*hl,y2=3*hl/2)
    rounded_rectangular_button_overlay(root=canv,btext="Remove Employee",color='red',func=del_emp,dictA={'d':dictA,'id':id},x1=3*w/4,x2=200,y1=yl+2*hl,y2=3*hl/2)

def gui_upd_emp(dictA):
    id = dictA['id']
    name = dictA['n'].get()
    mail_id = dictA['e'].get()
    mobile = dictA['m'].get()
    wage = dictA['w'].get()    

    if "" in [name, mobile, wage]:
        failure_msg("Fields marked * cannot be empty!")
        return
    else:
        update_employee_mail(id,mail_id)
        update_employee_name(id,name)
        update_employee_wage(id,wage)
        update_employee_mobile(id,mobile)   
        success_msg("Employee details updated successfully!")

def del_emp(dictA):
    delete_employee(dictA['id'])
    success_msg("Employee removed from database successfully!")
    man_emp(dictA['d'])

    
