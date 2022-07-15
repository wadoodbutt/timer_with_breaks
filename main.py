from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
TIMER_GREEN = "#9DFFC5"
FONT_NAME = "Palatino Linotype"

timen = None
counter = 1

global reset_minutes
global reset_seconds

reset_minutes = "25"
reset_seconds = "00"


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer(minutes=reset_minutes, seconds=reset_seconds):
    if counter % 2 == 0:
        timer_label.config(text=" B R E A K ", bg=YELLOW, fg=RED, font=(FONT_NAME, 20, "bold"))
        timer_label.place(x=130, y=35)
    else:
        timer_label.config(text="Pomodora Timer", fg=TIMER_GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
        timer_label.place(x=100, y=50)
    window.after_cancel(timen)
    count_down(minutes, seconds)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer(minutes="25", seconds="00"):
    global reset_minutes, reset_seconds
    if int(minutes) < 10:
        minutes = "0" + minutes
    if int(seconds) < 10:
        seconds = "0" + seconds

    reset_seconds = seconds
    reset_minutes = minutes
    count_down(minutes, seconds)


def custom_timer():
    top = Toplevel(window, bg=YELLOW)
    top.minsize(width=300, height=200)

    minutes = Spinbox(top, from_=0, to=60)
    minutes.grid(column=0, row=1)
    minute_label = Label(top, text="Minutes", fg="black", bg=YELLOW, font=(FONT_NAME, 12, "bold"))
    minute_label.grid(column=0, row=0)

    seconds = Spinbox(top, from_=0, to=60)
    seconds.grid(column=3, row=1)
    seconds_label = Label(top, text="Seconds", fg="black", bg=YELLOW, font=(FONT_NAME, 12, "bold"))
    seconds_label.grid(column=3, row=0)

    global reset_minutes, reset_seconds
    reset_minutes = str(minutes.get())
    reset_seconds = str(seconds.get())
    ok_button = Button(top, text="Ok", command=lambda: start_timer(str(minutes.get()), str(seconds.get())))
    ok_button.grid(column=1, row=5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(minutes, seconds):
    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    global reset_minutes, reset_seconds, timen, counter
    if int(minutes) == 0 and int(seconds) == 0:
        counter += 1
        if counter % 2 == 0:
            reset_timer("00", "05")
        else:
            reset_timer(minutes=reset_minutes, seconds=reset_seconds)
        timer_label.update()
        return

    if seconds == "00" or seconds == 0 or seconds == "0":
        timen = window.after(1000, count_down, int(minutes) - 1, "59")
    else:
        if int(seconds) < 11:
            timen = window.after(1000, count_down, int(minutes), "0" + str(int(seconds) - 1))
        else:
            timen = window.after(1000, count_down, int(minutes), int(seconds) - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(bg=YELLOW)

window.minsize(width=400, height=400)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.place(x=100, y=85)

timer = canvas.create_text(100, 130, text="00:00", fill=TIMER_GREEN, font=(FONT_NAME, 35, "italic"))

start_button = Button(text="Start", command=start_timer)
start_button.place(x=50, y=310)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.place(x=300, y=310)

custom_time_button = Button(text="Customize Time", command=custom_timer)
custom_time_button.place(x=140, y=350)

timer_label = Label(text="Pomodora Timer", fg=TIMER_GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
timer_label.place(x=100, y=50)

window.mainloop()
