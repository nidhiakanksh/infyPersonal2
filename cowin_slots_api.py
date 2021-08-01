import requests
import datetime
import json
import mysql.connector

pincode_query="SELECT PINCODE FROM regisrty"
age_query="SELECT AGE FROM regisrty"
mobile_no_query="SELECT MOBILE_NO FROM regisrty"
flag_query="SELECT FLAG FROM regisrty"


pincode_list=[]
age_list=[]
mobile_no_list=[]
flag_list=[]

mydb = mysql.connector.connect(
      host="localhost",
      user='root',
      password='GaTech340/340',
      database="coWin_slot_request_registry_db"
    )        
        
        
def load_records():
    global pincode_list
    global age_list
    global flag_list
    global mobile_no_list
    
    
    mycursor = mydb.cursor()
    mycursor.execute(age_query)
    age_list=mycursor.fetchall()
    print("age_list")
    print(age_list)
    
    mycursor = mydb.cursor()
    mycursor.execute(pincode_query)
    pincode_list=mycursor.fetchall()
    print("pincode_list")
    print(pincode_list)
    
    mycursor = mydb.cursor()
    mycursor.execute(mobile_no_query)
    mobile_no_list=mycursor.fetchall()
    print("mobile_no_list")
    print(mobile_no_list)
    
    
    mycursor = mydb.cursor()
    mycursor.execute(flag_query)
    flag_list=mycursor.fetchall()
    myList=[1,2,4]
    print(type(myList))
    print(type(flag_list))
    print("flag_list")
    print(flag_list)


print_flag = 'Y'
numdays = 7

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]



def update_response_msg(message,mobile_no):
    mycursor = mydb.cursor()
    update_response_msg="UPDATE regisrty SET FLAG=1, RESPONSE_MSG='{}' where MOBILE_NO='{}'".format(message,mobile_no)
    try:
        mycursor.execute(update_response_msg)
        mydb.commit()
    except Exception as e:
        print(e)
    


def drop_record(mobile_no):
     mycursor = mydb.cursor()
     drop_record_query="DELETE FROM regisrty WHERE MOBILE_NO='{}'".format(mobile_no)
     try:
        mycursor.execute(drop_record_query)
        mydb.commit()
        print("RECORD DROPPED!")
        
     except Exception as e:
        print(e)
        
def update_requests_served_table(mobile_no,pinCode,age,message):
    mycursor = mydb.cursor()
    try:
        insert_record="INSERT INTO requests_served VALUES ({},{},{},{})".format(mobile_no,pinCode,age,message)
        mycursor.execute(insert_record) 
        mydb.commit()
        print("SERVED REQUEST UPDATED!")  
    except Exception as e:
        print(e)
   




# for pin in list(pincode_list):
#     print("\t".format(pin))

# message='New update'
# mobile_no='123456789'
# update_response_msg(message,mobile_no)

load_records()
for pinCode,age,flag,mobile_no in zip(pincode_list,age_list,flag_list,mobile_no_list):    
    pinCode=pinCode[0]
    age=age[0]
    flag=flag[0]
    mobile_no=mobile_no[0]
    print(pinCode,age,flag,mobile_no)
    count = 0
    message=""
    for INP_DATE in date_str:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pinCode, INP_DATE)
        response = requests.get(URL)
        if response.ok:
          
            resp_json = response.json()
            # print(json.dumps(resp_json, indent = 1))
            flag = False
            if resp_json["centers"]:    
                if(print_flag=='y' or print_flag=='Y'):
                    for center in resp_json["centers"]:
                        for session in center["sessions"]:
                            if ( session["min_age_limit"] <= age and session["available_capacity"]>0 ) :
                                message+=str(pinCode)
                                message+="\n Available on: {} \t {} \t{}".format(INP_DATE, center["name"],center["block_name"])
                                message+="\n Price: {}".format( center["fee_type"])
                                message+="\n Available Capacity:".format(session["available_capacity"])
                                if(session["vaccine"] != ''):
                                    message+="\n Vaccine: {}".format(session["vaccine"])
                                message+="\n"
                                count = count + 1
                                
                            else:
                                b = 25
                              #  print("No available slots on {}".format(INP_DATE))
            else:
                a = 25
               # print("No available slots on {}".format(INP_DATE))
        else:
            print("BAD Response for {} on {}".format(pinCode,INP_DATE))

    if(count == 0):
        message="No Vaccination center avaliable."
        update_response_msg(message,mobile_no[0])
    else:
        print("Vaccination Center available")
        # update_response_msg(message,mobile_no)
        drop_record(mobile_no)
        update_requests_served_table(mobile_no,pinCode,age,message)
        
print("Completed...")





