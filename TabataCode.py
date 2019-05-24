import time

from tkinter import *

def FormatTime(root, Time, TimeLabel):
    Hours = Time//3600
    Minutes = Time//60
    Seconds = Time%60

    displayTime = Hours,':',Minutes,':',Seconds
    
    UpdateDisplay(root, displayTime, TimeLabel)

def UpdateDisplay(root, FormattedTime, TimeLabel):
    TimeLabel.configure(text = FormattedTime)

def Counter(TimeLabel, root, Countdown, WarmUp, Exercise, Rest, Sets, Recovery, Cycles, CoolDown):

    TotalTime = (Countdown+WarmUp+(Cycles*(Sets*(Exercise+Rest)+Recovery))+CoolDown)


    count = Countdown
    for sec in range(Countdown+1):
        FormatTime(root, count, TimeLabel)
        time.sleep(1)
        count-=1
    count = WarmUp
    for sec in range(WarmUp+1):
        FormatTime(root, count, TimeLabel)
        time.sleep(1)
        count-=1
    for cycle in range(Cycles+1):
        for sets in range(Sets+1):
            count=Exercise
            for sec in range(Exercise+1):
                count-=1
                time.sleep(1)
                FormatTime(root, count, TimeLabel)
            count=Rest
            for sec in range(Rest+1):
                count-=1
                time.sleep(1)
                FormatTime(root, count, TimeLabel)
        count = Recovery
        for sec in range(Recovery+1):
            count-=1
            time.sleep(1)
            FormatTime(root, count, TimeLabel)
    count = CoolDown
    for sec in range(CoolDown+1):
        count-=1
        time.sleep(1)
        FormatTime(root, count, TimeLabel)
                   
        
    
def menu():
    root = Tk()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.title("CustomizationMenu")

    widgetFrame = Frame(root)
    widgetFrame.pack(anchor = N, side = 'top', expand = True)

    InitialCountdownLabel = Label(widgetFrame, text = "Initial Countdown:", bg = 'black', fg = 'white')
    InitialCountdownLabel.grid(column = 0, row = 0)
    InitialCountdown = Spinbox(widgetFrame, from_=0, to=300)
    InitialCountdown.grid(column = 1, row = 0)

    WarmUpLabel = Label(widgetFrame, text = "Warm-Up Interval:", bg = 'black', fg = 'white')
    WarmUpLabel.grid(column = 0, row = 1)
    WarmUpTime = Spinbox(widgetFrame, from_=0, to = 100000)
    WarmUpTime.grid(column = 1, row = 1)

    ExerciseIntervalLabel = Label(widgetFrame, text = "Exercise Interval:", bg = 'black', fg = 'white')
    ExerciseIntervalLabel.grid(column = 0, row = 2)
    ExerciseTime = Spinbox(widgetFrame, from_=0, to = 1000000)
    ExerciseTime.grid(column = 1, row = 2)

    RestLabel = Label(widgetFrame, text = 'Rest Interval:', bg = 'black', fg='white')
    RestLabel.grid(column = 0, row = 3)
    RestTime = Spinbox(widgetFrame, from_=0, to = 100000000)
    RestTime.grid(column = 1, row = 3)

    SetNumLabel  = Label(widgetFrame, text = 'Number of Sets:', bg = 'black', fg = 'white')
    SetNumLabel.grid(column = 0, row = 4)
    Set_Num = Spinbox(widgetFrame, from_=0, to = 100000)
    Set_Num.grid(column = 1, row = 4)

    RecoveryLabel = Label(widgetFrame, text = 'Recovery Interval:', bg = 'black', fg = 'white')
    RecoveryLabel.grid(column = 0, row = 5)
    RecoveryTime = Spinbox(widgetFrame, from_=0, to = 100000)
    RecoveryTime.grid(column = 1, row = 5)

    CycleCount = Label(widgetFrame, text = 'Number of Cycles:', bg = 'black', fg= 'white')
    CycleCount.grid(column = 0, row = 6)
    CycleNum = Spinbox(widgetFrame, from_=0, to =100000)
    CycleNum.grid(column = 1, row = 6)

    CoolDownLabel = Label(widgetFrame, text = "Cool Down Time:", bg = 'black', fg = 'white')
    CoolDownLabel.grid(column = 0, row = 7)
    CoolDownTime = Spinbox(widgetFrame, from_ = 0, to=100000)
    CoolDownTime.grid(column = 1, row = 7)

    

    TimeLabel = Label(root, text = "Start Timer")
    TimeLabel.pack()
    Submit = Button(root, width = 50, text = "START", fg='black', bg = 'yellow', command = lambda:Counter(TimeLabel, root, int(InitialCountdown.get()), int(WarmUpTime.get()), int(ExerciseTime.get()), int(RestTime.get()), int(Set_Num.get()), int(RecoveryTime.get()), int(CycleNum.get()), int(CoolDownTime.get())))    
    
    Submit.pack()
    root.bind("<Return>", lambda event: Counter(TimeLabel, root, int(InitialCountdown.get()), int(WarmUpTime.get()), int(ExerciseTime.get()), int(RestTime.get()), int(Set_Num.get()), int(RecoveryTime.get()), int(CycleNum.get()), int(CoolDownTime.get())))    
    root.mainloop()

def main():
    menu()
main()
