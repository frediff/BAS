# function for inserting employee to the database
import mysql.connector

# function to check whether the mobile number of the employee is corect or not
def check_mobile(mobile):
    if( len(str(mobile)) == 10 and str(mobile).isdigit()):
        return True
    else:
        return False
    
# function to check whether the name of the employee is correct or not
def check_name(name):
     if(str(name).isdigit()):
         return False
     else:
         return True
     
# function to check whether the wage of the employee is correct or not
def check_wage(wage):
     if(str(wage).isdigit()):
         return True
     else:
         return False
     
def insert_employee(name_,mailId,mobile,wage):
    #checking correctness of the employee mobile
    if( not check_mobile(mobile)):
         return "Please enter valid Mobile Number!!"
    #checking correctness of the employee name
    if( not check_name(name_)):
         return "Please enter valid Name!!"
    #checking correctness of the employee wage
    if( not check_wage(wage)):
         return "Please enter valid wage!!"
    employeeDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="employeeDatabase")
    mycursor = employeeDb.cursor()
    search_query_1 = "SELECT Id FROM employee WHERE mobile = %s"
    values = (mobile,)
    mycursor.execute(search_query_1,values)
    myresult_1 = mycursor.fetchall() 
    if myresult_1:
        return "This mobile number is already registered with us!!"
    #inserting empoyee details to the database
    insert_query = "INSERT INTO employee (name_,mailId,mobile,wage) VALUES (%s,%s,%s,%s)"
    record = (name_,mailId,mobile,wage)
    mycursor.execute(insert_query, record)
    employeeDb.commit()
    search_query_1 = "SELECT Id FROM employee WHERE mobile = %s"
    values = (mobile,)
    mycursor.execute(search_query_1,values)
    myresult_1 = mycursor.fetchall() 
    search_query_2 = "SELECT Id FROM employee WHERE name_ = %s"
    values = (name_,)
    mycursor.execute(search_query_2,values)
    myresult_2 = mycursor.fetchall() 
    if employeeDb.is_connected():
           mycursor.close()
           employeeDb.close()
    return myresult_2
       