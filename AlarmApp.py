from tkinter import *
import datetime as dt
import time
import pygame

# defining the function for the alarm clock
def alarm(setAlarmTimer):
    pygame.init()
    pygame.mixer.init()
    music_file = "Mohbad-Ronaldo.mp3"
    pygame.mixer.music.load(music_file)

    while True:
        actualTime = dt.datetime.now()
        currentTime = actualTime.strftime("%H:%M:%S")
        if currentTime == setAlarmTimer:
            print("Alarm Time reached!")
            pygame.mixer.music.play()
            time.sleep(20)
            pygame.mixer.music.stop()
            break
        time.sleep(1)

    pygame.mixer.quit()

def getAlarmTime():
    hours = int(hour.get())
    minutes = int(minute.get())
    seconds = int(second.get())
    alarm_set_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    alarm(alarm_set_time)

# creating the GUI for the application
guiWindow = Tk()
guiWindow.title("The Alarm Clock")
guiWindow.geometry("464x300")
guiWindow.config(bg="#87BDD8")
guiWindow.resizable(width=True, height=True)

timeFormat = Label(
    guiWindow,
    text="Remember to set time in 24-hour format!",
    fg="black",
    bg="#87BDD8",
    font=("Times New Roman", 15)
).place(
    x=50,
    y=250
)

timequote = Label(
    guiWindow,
    text="""   Time is a finite resource; manage it wisely, 
        for how we invest our moments determines 
             the dividends of our future.""",
    fg="black",
    bg="#87BDD8",
    font=("Garamond", 15, "bold italic")
).place(
    x=30,
    y=150
)

add_time = Label(
    guiWindow,
    text="Hour     Minute     Second",
    font=("Times New Roman", 15),
    fg="black",
    bg="#87BDD8"
).place(
    x=230,
    y=10
)

setAlarm = Label(
    guiWindow,
    text="Set Time for Alarm: ",
    font=("Times New Roman", 15),
    fg="white",
    bg="#034F84",
    relief="solid",
).place(
    x=5,
    y=50
)

hour = StringVar()
minute = StringVar()
second = StringVar()

hourTime = Entry(
    guiWindow,
    textvariable=hour,
    bg="#FEFBD8",
    width=4,
    font=(20)
).place(
    x=220,
    y=50
)
minuteTime = Entry(
    guiWindow,
    textvariable=minute,
    bg="#FEFBD8",
    width=4,
    font=(20)
).place(
    x=305,
    y=50
)
secondTime = Entry(
    guiWindow,
    textvariable=second,
    bg="#FEFBD8",
    width=4,
    font=(20)
).place(
    x=390,
    y=50
)

submit = Button(
    guiWindow,
    text="Set The Alarm",
    font=("Times New Roman", 15),
    fg="white",
    bg="#82B74B",
    width=15,
    command=getAlarmTime,
).place(
    x=140,
    y=100
)

guiWindow.mainloop()