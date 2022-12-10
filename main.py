from datetime import datetime, timedelta, date
import tkinter as tk




def next_soup():
    now = datetime.now()
    soup_time = datetime(2022, 12, 7, 20, 30, 00, 00)
    #print (soup_time)

    while soup_time < now:
        soup_time = soup_time + timedelta(hours=3) + timedelta(minutes=30)
    return(soup_time)

#nxt = next_soup()
#print(nxt)


def time_rem():
    now = datetime.now()
    soup_time = next_soup()
    time_remaining = soup_time - now
    return (time_remaining)

#rem = time_rem()
#print(rem)


"""

    #print(soup_time)


    format_soup_time = (str(soup_time))
    format_soup_time = format_soup_time[11:]
    #print(format_soup_time)

    format_time_remaining = (str(time_remaining))
    format_time_remaining = format_time_remaining[:-7]
    #print(format_time_remaining)
    return()
"""



"""
if time_remaining > soup_duration:
    print("SOUP IS ON!!!!")

print("Next soup at :", format_soup_time)

print(format_time_remaining, " Till soup!")
"""



"""
time_in_seconds = 3

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')

countdown(time_in_seconds)
"""


