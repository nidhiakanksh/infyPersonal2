# -*- coding: utf-8 -*-
"""
Created on Thu May  6 21:37:13 2021

@author: akanksh.belchada
"""

import mysql.connector
#Connecting to Server
mydb = mysql.connector.connect(
  host="localhost",
  user='root',
  password='GaTech340/340',

)

mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS  coWin_slot_request_registry_db")

except Exception as e:
    print(e)
    
show_db_query = "SHOW DATABASES"

mycursor.execute(show_db_query)
for db in mycursor:
    print(db)
    
    
mydb = mysql.connector.connect(
  host="localhost",
  user='root',
  password='GaTech340/340',
  database="coWin_slot_request_registry_db"

)

mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE TABLE IF NOT EXISTS regisrty(MOBILE_NO VARCHAR(10) PRIMARY KEY , PINCODE INTEGER, AGE INTEGER, FLAG INTEGER, RESPONSE_MSG VARCHAR(1000))")
except Exception as e:
    print(e)



mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE TABLE IF NOT EXISTS requests_served (MOBILE_NO VARCHAR(10) PRIMARY KEY , PINCODE INTEGER, AGE INTEGER, MESSAGE VARCHAR(1000))")
except Exception as e:
    print(e)



print(type(mycursor.execute("SHOW TABLES")))
for x in mycursor:
  print(x)



print("Enter Mobile Number:") 
mobile_no=input()
print("Enter Age:")
age=input()
print("Enter PIN-CODE:")
pincode=input()
flag=0
  
try:
    insert_values="INSERT INTO regisrty values ({},{},{},{},'None')".format(mobile_no,pincode,age,flag)
    mycursor.execute(insert_values) 
    mydb.commit()
 
except Exception as e:
    print(e)
    











