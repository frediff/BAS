# Creates employee database and also two tables called "employee" and "attendance" to store employee details and employee attendance respectively.
import mysql.connector

#creating employee database
employeeDb = mysql.connector.connect(host="localhost",user="root",password="Book@123",database="employeeDatabase")
mycursor = employeeDb.cursor()

#creating employee table
mycursor.execute("CREATE TABLE employee(Id INT AUTO_INCREMENT PRIMARY KEY, name_ VARCHAR(255), mailId VARCHAR(255), mobile BIGINT UNSIGNED, wage INT UNSIGNED)")

#creating attendance table
mycursor.execute("CREATE TABLE attendance(Id INT, date_ DATE, status_ VARCHAR(1))")