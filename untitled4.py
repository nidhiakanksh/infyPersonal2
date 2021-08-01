# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 11:50:30 2017
@author: Moondra
"""

import threading
import time
myList=[1,2,3,4,5,6,7,8,9,10]

def creates_items():
      global myList
      while True:
          time.sleep(1)
          print("Enter a number")
          try:
              x=int(input())
          except Exception as e:
              print(e)
              
          myList=[x]+myList
          print("Number has been added")

def limits_items():
    while True:
        global myList
        time.sleep(2)
        if(len(myList)>0):
            myList.pop()
            print("Autodeleting!!!")
            print(myList)
        else:
            print("Listening")

creator1 = threading.Thread(target  = creates_items)

limitor = threading.Thread(target = limits_items, daemon = True)

print(limitor.isDaemon())


creator1.start()
limitor.start()

# print("Enter a number")
# x=input()
# print(x)

creator1.join()
limitor.join()






