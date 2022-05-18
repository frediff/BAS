# function to delete book based on ISBN
import mysql.connector

def delete_employee(Id_):
    employeeDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="employeeDatabase")
    mycursor = employeeDb.cursor() 
    delete_query = "DELETE FROM employee WHERE Id = %s"
    values = (Id_,)
    mycursor.execute(delete_query,values)
    employeeDb.commit()
    delete_query = "DELETE FROM attendance WHERE Id = %s"
    values = (Id_,)
    mycursor.execute(delete_query,values)
    employeeDb.commit()