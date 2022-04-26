# import everything from tkinter module
import schedule
from tkinter import *   
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
import re
import time
import tkinter.messagebox
import threading
import datetime as dt

#from tkinter.ttk import *

ventil1 = 14
ventil2 = 15 
stopSchedule = False
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(ventil1, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(ventil2, GPIO.OUT, initial=GPIO.LOW)

date=dt.datetime.now()

def on1():
    btn_off_1['state'] = NORMAL
    btn_on_1['state'] = DISABLED
    GPIO.output(ventil1, GPIO.HIGH)
    print("on - 1")

def on2():
    btn_off_2['state'] = NORMAL
    btn_on_2['state'] = DISABLED
    GPIO.output(ventil2, GPIO.HIGH)

def off1():
    btn_on_1['state'] = NORMAL
    btn_off_1['state'] = DISABLED
    GPIO.output(ventil1, GPIO.LOW)
    print("off - 1")
    
def off2():
    btn_on_2['state'] = NORMAL
    btn_off_2['state'] = DISABLED
    GPIO.output(ventil2, GPIO.LOW)
    
def on3():
    btn_on_3['state'] = DISABLED
    btn_off_3['state'] = NORMAL
    try:
        schedule.every().day.at(e1.get()).do(on1)
        schedule.every().day.at(e2.get()).do(off1)
    except:
        tkinter.messagebox.showerror(title='Error', message='Time format error')
        e1.delete(0, END)
        e2.delete(0, END)

def on4():
    btn_on_4['state'] = DISABLED
    btn_off_4['state'] = NORMAL
    try:
        schedule.every().day.at(e3.get()).do(on2)
        schedule.every().day.at(e4.get()).do(off2)
    except:
        tkinter.messagebox.showerror(title='Error', message='Time format error')
        e3.delete(0,END)
        e4.delete(0,END)
               
def off3():
    btn_on_3['state'] = NORMAL
    btn_off_3['state'] = DISABLED
    GPIO.output(ventil1, GPIO.LOW)
    global stopSchedule
    stopSchedule = True
    
def off4():
    btn_on_4['state'] = NORMAL
    btn_off_4['state'] = DISABLED
    GPIO.output(ventil2, GPIO.LOW)
    global stopSchedule
    stopSchedule = True

def close():
    global stopSchedule
    stopSchedule = True
    root.destroy()

bgcolor = '#b4f7dc'

root = Tk()
root.attributes('-fullscreen', True)
root.configure(bg=bgcolor)

label = Label(root, text='Поливна система', font= ("Arial", 60), bg= bgcolor)
label.pack(ipadx=10, ipady=10)

label = Label(root, text='РЪЧЕН РЕЖИМ', font= ("Arial", 20), bg= '#99ffcc')
label.place(x=440, y=140)
label = Label(root, text='АВТОМАТИЧЕН РЕЖИМ', font= ("Arial", 20), bg= '#99ffcc')
label.place(x=990, y=140)

#style = Style()
label = Label(root, text='KPAH 1:', font= ("Arial", 30), bg= bgcolor)
label.place(x=120, y=290)
btn_on_1 = Button(root, text = 'ON', height= 10, width=23, bg= 'green', font= 'Arial', fg= 'white', command=on1)
btn_on_1.place(x=320, y=240)

btn_off_1 = Button(root, text = 'OFF', height= 10, width=23, bg= 'red', font= 'Arial', fg= 'white',command=off1)
btn_off_1['state'] = DISABLED
btn_off_1.place(x= 610, y=240)

label = Label(root, text='KPAH 2:', font= ("Arial", 30), bg= bgcolor)
label.place(x=120, y=540)
btn_on_2 = Button(root, text = 'ON', height= 10, width=23, bg= 'green', font= 'Arial', fg= 'white',command=on2)
btn_on_2.place(x=320, y=480)

btn_off_2 = Button(root, text = 'OFF', height= 10, width=23, bg= 'red', font= 'Arial', fg= 'white',command=off2)
btn_off_2['state'] = DISABLED
btn_off_2.place(x= 610, y=480)

label2 = Label(root, text='Час включване:', font= ("Arial", 20), bg= bgcolor)
label2.place(x=940, y=220)
e1 = Entry(root, font=('Exo 20'))
e1.place(x = 1200, y= 215, width= 185, height= 70)

btn_on_3 = Button(root, text = 'ON', height= 2, width=20, bg= 'green', font= "Arial", fg= 'white', command=on3)
btn_on_3.place(x= 940, y=410)

label3 = Label(root, text='Час изключване:', font= ("Arial", 20), bg= bgcolor)
label3.place(x=940, y=320)
e2 = Entry(root, font=('Exo 20'))
e2.place(x = 1200, y= 315, width= 185, height= 70)

btn_off_3 = Button(root, text = 'OFF', height= 2, width=20, bg= 'red', font= "Arial", fg= 'white', command=off3)
btn_off_3.place(x= 1200, y=410)

label4 = Label(root, text='Час включване:', font= ("Arial", 20), bg= bgcolor)
label4.place(x=940, y= 503)
e3 = Entry(root, font=('Exo 20'))
e3.place(x = 1200, y= 495, width= 185, height= 70)

btn_on_4 = Button(root, text= 'ON', height= 2, width=20, bg= 'green', font= "Arial", fg= 'white', command=on4)
btn_on_4.place(x=940, y=710)

label5 = Label(root, text='Час изключване:', font= ("Arial", 20), bg= bgcolor)
label5.place(x=940, y=610)
e4 = Entry(root, font=('Exo 20'))
e4.place(x = 1200, y= 595, width= 185, height= 70)

btn_off_4 = Button(root, text= 'OFF', height= 2, width=20, bg= 'red', font= "Arial", fg= 'white', command=off4)
btn_off_4['state'] = DISABLED
btn_off_4.place(x= 1200, y=710)

c1 = Label(root, font=("Exo", 30, 'bold'), bg= bgcolor, bd =30)
c1.place(x= 800, y= 900)

def clock():
   text_input = time.strftime("%H:%M:%S")
   c1.config(text=text_input)
   c1.after(200, clock)

clock()

def schedule_func():
    while True:
        schedule.run_pending()
        sleep(1)

t1 = threading.Thread(target=schedule_func, args=())

t1.start()

label7 = Label(root, text="2022, Теодор Даракчиев - всички права запазени", font= ("Arial", 20), bg= bgcolor)
label7.place(x=50, y=1000)

exit_button = Button(root, text= "Exit", height= 7, width=15, bg= 'red', font= ("Arial", 14), fg= 'white',command=close)
exit_button.place(x=1600, y=900)

root.mainloop()



