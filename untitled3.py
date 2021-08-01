import requests
import datetime
import json

POST_CODE = "411027"
age = 52

pinCodes = ["411027"]

# Print details flag
print_flag = 'Y'

numdays = 2

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]



for pinCode in pinCodes:    
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
                            if ( session["min_age_limit"] <= age and session["available_capacity"] == 0 ) :
                                message+=pinCode
                                message+="\n Available on: {} \t {} \t{}".format(INP_DATE, center["name"],center["block_name"])
                                message+="\n Price: {}".format( center["fee_type"])
                                message+="\n Available Capacity:".format(session["available_capacity"])
                                if(session["vaccine"] != ''):
                                    message+="\n Vaccine: {} \n ".format(session["vaccine"])
                                count = count + 1
                                print(message)
                            else:
                                b = 25
                                print("No available slots on {} for {}".format(INP_DATE,pinCode))
            else:
                a = 25
                print("No centers slots on {} for {}".format(INP_DATE,pinCode))
        else:
            print("BAD RESPOSNE FOR {} on {}".format(pinCode,INP_DATE))

    if(count == 0):
        print("No Vaccination center avaliable for {}".format(pinCode))
print("Completed...")