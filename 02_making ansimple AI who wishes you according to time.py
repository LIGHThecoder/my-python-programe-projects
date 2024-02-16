

'''
Author : Nikhil Rajendra Gaikwad

date: 16/02/24


Topic : making an programe that wish you according to time.

'''

# programe to show time current time at input

import time

showtime=int(time.strftime("%H"))
# print(showtime)

raw=input("what's going on? how are you\n")


if(showtime<=12):
    print("ok! Good MORNING brother. hope you will gave great time")

elif(showtime>12 and showtime<=18):
    print("ok! Good AFTERNOON brother. hope you will gave great time")

else:
    print("ok! Good EVENING brother. hope you will gave great time")
























