# function to return all employees
import mysql.connector

def all_employee():
    employeeDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="employeeDatabase")
    mycursor = employeeDb.cursor() 
    search_query = "SELECT * FROM employee"
    mycursor.execute(search_query)
    myresult = mycursor.fetchall()
    return myresult
