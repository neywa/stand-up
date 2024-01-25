import os
from tkinter import *
from tkinter import ttk
# import tkinter as tk
# import time


def countdown(total_seconds=60, total_minutes=60):
    if total_seconds == 60:
        total_seconds -= 1
        total_minutes -= 1
        timer_text.config(text=f"{total_minutes}:{total_seconds}")
        mainframe.after(1000, countdown, total_seconds, total_minutes)        
    elif total_seconds == 1 and total_minutes != 0:
        total_seconds += 59
        timer_text.config(text=f"{total_minutes}:00")
        mainframe.after(1000, countdown, total_seconds, total_minutes)        
    elif total_seconds == 0 and total_minutes > 0:
        total_seconds = 59
        total_minutes -= 1
        timer_text.config(text=f"{total_minutes}:{total_seconds}")
        mainframe.after(1000, countdown, total_seconds, total_minutes)        
    elif total_seconds < 11 and total_seconds > 0:
        total_seconds -= 1
        timer_text.config(text=f"{total_minutes}:0{total_seconds}")
        mainframe.after(1000, countdown, total_seconds, total_minutes)   
    elif total_seconds == 0 and total_minutes == 0:
        pass
    else:
        total_seconds -= 1
        timer_text.config(text=f"{total_minutes}:{total_seconds}")
        mainframe.after(1000, countdown, total_seconds, total_minutes)        


root = Tk()
root.title("Stand up")
# window.config(padx=100, pady=50)
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

timer_text = ttk.Label(mainframe, text="TIMER", width=5)
timer_text.grid(column=1, row=1, sticky=E)

start_button = ttk.Button(mainframe, text="Start", command=countdown)
start_button.grid(column=2, row=1, sticky=W)

mainframe.mainloop()
