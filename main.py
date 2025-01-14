import math
from math import floor
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_mark = '✔'
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(text, text=f"00:00")
    label.config(text='Timer')
    tick_mark_label.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        choice = long_break_sec
        label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        choice = short_break_sec
        label.config(text="Break", fg=PINK)
    else:
        choice = work_sec
        label.config(text='Work', fg=GREEN)

    countdown(choice)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(number):
    count_min = math.floor(number / 60)
    count_sec = number % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(text, text=f"{count_min}:{count_sec}")

    if number > 0:
        global timer
        timer = window.after(1000, countdown, number-1)
    else:
        start_timer()
        work_completed = floor(reps/2)
        marks = ''
        for _ in range(work_completed):
            marks += check_mark
        tick_mark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Application")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 50, 'normal'), foreground=GREEN, background=YELLOW)
label.grid(row=0, column=1)

start_button = Button(text='Start', command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

tick_mark_label = Label(font=(FONT_NAME, 20, 'normal'), foreground=GREEN, background=YELLOW)
tick_mark_label.grid(row=3, column=1)

window.mainloop()