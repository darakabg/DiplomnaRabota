# import everything from tkinter module
import schedule
from tkinter import *   
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
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
"""
def schedule_func(): 
    while True:
        print("tuk")
        schedule.run_pending()
        sleep(1)
        global stopSchedule
        if stopSchedule:
            print("bye timer!")
            break
"""
def on3():
    btn_off_3['state'] = DISABLED
    btn_on_3['state'] = NORMAL
    GPIO.output(ventil1, GPIO.HIGH)

def on4():
    btn_on_3['state'] = NORMAL
    btn_off_3['state'] = DISABLED
    GPIO.output(ventil2, GPIO.HIGH)


def off3():
    btn_on_4['state'] = NORMAL
    btn_off_4['state'] = DISABLED
    GPIO.output(ventil1, GPIO.LOW)
    
def off4():
    btn_on_4['state'] = NORMAL
    btn_off_4['state'] = DISABLED
    GPIO.output(ventil2, GPIO.LOW)

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

#style = Style()
label = Label(root, text='KPAH 1:', font= ("Arial", 30), bg= bgcolor)
label.place(x=120, y=220)
btn_on_1 = Button(root, text = 'ON', height= 10, width=23, bg= 'green', font= 'Arial', fg= 'white', command=on1)
btn_on_1.place(x=320, y=160)

btn_off_1 = Button(root, text = 'OFF', height= 10, width=23, bg= 'red', font= 'Arial', fg= 'white',command=off1)
btn_off_1['state'] = DISABLED
btn_off_1.place(x= 610, y=160)

label = Label(root, text='KPAH 2:', font= ("Arial", 30), bg= bgcolor)
label.place(x=120, y=520)
btn_on_2 = Button(root, text = 'ON', height= 10, width=23, bg= 'green', font= 'Arial', fg= 'white',command=on2)
btn_on_2.place(x=320, y=460)

btn_off_2 = Button(root, text = 'OFF', height= 10, width=23, bg= 'red', font= 'Arial', fg= 'white',command=off2)
btn_off_2['state'] = DISABLED
btn_off_2.place(x= 610, y=460)

def schedule_func():
    label2 = Label(root, text='Час включване:', font= ("Arial", 20), bg= bgcolor)
    label2.place(x=940, y=180)
    e1 = Entry(root)
    e1.place(x = 1200, y= 165, width= 185, height= 70)

    btn_on_3 = Button(root, text = 'ON', height= 2, width=20, bg= 'green', font= "Arial", fg= 'white', command=on3)
    btn_on_3.place(x= 940, y=350)

    label3 = Label(root, text='Час изключване:', font= ("Arial", 20), bg= bgcolor)
    label3.place(x=940, y=260)
    e2 = Entry(root)
    e2.place(x = 1200, y= 255, width= 185, height= 70)

    btn_off_3 = Button(root, text = 'OFF', height= 2, width=20, bg= 'red', font= "Arial", fg= 'white', command=off3)
    btn_off_3.place(x= 1200, y=350)

    label4 = Label(root, text='Час включване:', font= ("Arial", 20), bg= bgcolor)
    label4.place(x=940, y= 473)
    e3 = Entry(root)
    e3.place(x = 1200, y= 455, width= 185, height= 70)

    btn_on_4 = Button(root, text= 'ON', height= 2, width=20, bg= 'green', font= "Arial", fg= 'white', command=on4)
    btn_on_4.place(x=940, y=650)

    label5 = Label(root, text='Час изключване:', font= ("Arial", 20), bg= bgcolor)
    label5.place(x=940, y=570)
    e4 = Entry(root)
    e4.place(x = 1200, y= 555, width= 185, height= 70)

    btn_off_4 = Button(root, text= 'OFF', height= 2, width=20, bg= 'red', font= "Arial", fg= 'white', command=off4)
    btn_off_4['state'] = DISABLED
    btn_off_4.place(x= 1200, y=650)
        
    schedule.every().day.at(e4).do(on1)
    schedule.every().day.at(e5).do(off1)

    #"schedule.every().day.at(schedule_func()).do()

    #schedule.every().day.at("15:15").do(on1)
    #schedule.every().day.at("15:16").do(off1)


def temp_sensor():
    label5 = Label(root, text="Temperature: ")
    label6 = Label(root, text="Humidity: ")

t1 = threading.Thread(target=schedule_func, args=())

t1.start()

exit_button = Button(root, text= "Exit", height= 7, width=15, bg= 'red', font= ("Arial", 14), fg= 'white',command=close)
exit_button.place(x=1600, y=900)

root.mainloop()

