import tkinter as tk
from main import *

window = tk.Tk()

#basic window sizing
window.geometry("300x200")

#This is formatting because I am a lazy fuck
greeting0 = tk.Label(text="")
greeting0.pack()

greeting = tk.Label(text="Soup Savior")
greeting.pack()

greeting2 = tk.Label(text="")
greeting2.pack()

#one function to rule them all
def calc_time():
    #needed to calculate duration because zero is hard
    now = datetime.now()

    #first result label
    text = label_next_soup["text"]

    soup_time = next_soup()
    soup_time = str(soup_time)

    format_soup_time = (str(soup_time))
    format_soup_time = format_soup_time[11:]

    format_soup_time = "Next soup at: " +format_soup_time


    label_next_soup["text"] = format_soup_time

    #second result label
    text2 = label_next_soup["text"]

    time_remaining = time_rem()
    format_time_remaining = (str(time_remaining))
    format_time_remaining = format_time_remaining[:-7]

    format_time_remaining = format_time_remaining + " 'till next soup"

    #zero datetime object for adding
    zeros = now-now
    #if its lett than 3:15 till the next one soup is still on
    soup_duration = zeros + timedelta(minutes=15)
    soup_duration = soup_duration + timedelta(hours= 3)

    #comparison to figure out if the soup is on
    if time_remaining > soup_duration:
        label_time_rem["text"] = "SOUP IS ON!!!"
    else:
        label_time_rem["text"] = format_time_remaining



#oh baby its a soup button
button = tk.Button(
    text="When is soup??",
    width=15,
    height=3,
    bg="grey",
    fg="black",
    command=calc_time
)
button.pack()

#more lazy bastard formatting
greeting3 = tk.Label(text="")
greeting3.pack()

#res label 1
label_next_soup = tk.Label(text = " ")
label_next_soup.pack()

#res label 2
label_time_rem = tk.Label(text = " ")
label_time_rem.pack()

#last shitty format I swear
greeting4 = tk.Label(text="")
greeting4.pack()

window.mainloop()