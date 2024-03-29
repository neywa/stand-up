from tkinter import *
from tkinter import ttk
from playsound import playsound

reset = "false"
# Defining 2 counter functions. Source:
# https://stackoverflow.com/questions/74511438/how-to-create-a-countdown-timer-which-continues-to-count-after-pressing-a-button
def countdown60(total_seconds=0, total_minutes=1):
    if total_seconds == 60:
        total_seconds -= 1
        total_minutes -= 1
        timer_text.config(text=f"{total_minutes}:{total_seconds}")
        mainframe.after(1000, countdown60, total_seconds, total_minutes)        
    elif total_seconds == 1 and total_minutes != 0:
        total_seconds += 59
        timer_text.config(text=f"{total_minutes}:00")
        mainframe.after(1000, countdown60, total_seconds, total_minutes)        
    elif total_seconds == 0 and total_minutes > 0:
        total_seconds = 59
        total_minutes -= 1
        timer_text.config(text=f"{total_minutes}:{total_seconds}")
        mainframe.after(1000, countdown60, total_seconds, total_minutes)        
    elif total_seconds < 11 and total_seconds > 0:
        total_seconds -= 1
        timer_text.config(text=f"{total_minutes}:0{total_seconds}")
        mainframe.after(1000, countdown60, total_seconds, total_minutes)   
    elif total_seconds == 0 and total_minutes == 0:
        playsound('bell.mp3')
        countdown60()
    else:
        total_seconds -= 1
        timer_text.config(text=f"{total_minutes}:{total_seconds}")
        mainframe.after(1000, countdown60, total_seconds, total_minutes)        

def countdown30(total_seconds=30, total_minutes=0):
    if total_seconds == 60:
        total_seconds -= 1
        total_minutes -= 1
        timer_text.config(text=f"{total_minutes}:{total_seconds}")
        mainframe.after(1000, countdown30, total_seconds, total_minutes)
    elif total_seconds == 1 and total_minutes != 0:
        total_seconds += 59
        timer_text.config(text=f"{total_minutes}:00")
        mainframe.after(1000, countdown30, total_seconds, total_minutes)
    elif total_seconds == 0 and total_minutes > 0:
        total_seconds = 59
        total_minutes -= 1
        timer_text.config(text=f"{total_minutes}:{total_seconds}")
        mainframe.after(1000, countdown30, total_seconds, total_minutes)
    elif total_seconds < 11 and total_seconds > 0:
        total_seconds -= 1
        timer_text.config(text=f"{total_minutes}:0{total_seconds}")
        mainframe.after(1000, countdown30, total_seconds, total_minutes)
    elif total_seconds == 0 and total_minutes == 0:
        playsound('bell.mp3')
        countdown30()
    else:
        total_seconds -= 1
        timer_text.config(text=f"{total_minutes}:{total_seconds}")
        mainframe.after(1000, countdown30, total_seconds, total_minutes)

def reset():
    reset = "true"
    timer_text.config(text=f"00:00")

# Building the GUI with tkinter
root = Tk()
root.title("Stand up")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

timer_text = ttk.Label(mainframe, text="00:00")
timer_text.grid(column=1, row=0, pady=5)

sixty_button = ttk.Button(mainframe, text="60 min", command=countdown60)
sixty_button.grid(column=0, row=1, padx=5)

thirty_button = ttk.Button(mainframe, text="30 min", command=countdown30)
thirty_button.grid(column=1, row=1, padx=5)

stop_button = ttk.Button(mainframe, text="Reset", command=reset)
stop_button.grid(column=2, row=1, padx=5)

mainframe.mainloop()
