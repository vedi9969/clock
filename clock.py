from tkinter import *
import time
import tkinter.messagebox as msg

def clock():
        
        clock_lb = time.strftime('%I:%M:%S %p')
        clock_lb.configure(text = clock_lb)
        clock_lb.after(1000, clock)
        
        clock_lb = Label(app, font = "ds-digital", bg = "#00008B")
        clock_lb.pack(anchor = 'center')
        
def exit():
        app.destroy()

app = Tk()
app.title("CLOCK")
app.geometry("500x600")
app.configure(bg = "#00008B")

clock1_img = PhotoImage(file = 'C:\\Users\\Lenovo\\Downloads\\CLOCK (1).png')
alarm_img = PhotoImage(file = 'C:\\Users\\Lenovo\\Downloads\\button (13).png')
clock_img = PhotoImage(file = 'C:\\Users\\Lenovo\\Downloads\\button (14).png')
timer_img = PhotoImage(file = 'C:\\Users\\Lenovo\\Downloads\\button (15).png')
stop_img = PhotoImage(file ='C:\\Users\\Lenovo\\Downloads\\button (16).png')
exit_img = PhotoImage(file = 'C:\\Users\\Lenovo\\Downloads\\button (5).png')

Label(app, image = clock1_img, bd = 0,  bg = "#00008B").place(x = 125, y= 50)

alarm_btn = Button(app, text = "Alarm", image = alarm_img, bg = "#00008B", bd = 0)
alarm_btn.place(x = 50, y = 200)

clock_btn = Button(app, text = "Clock", image = clock_img, bg = "#00008B", bd = 0, command = clock)
clock_btn.place(x = 265, y = 200)

timer_btn = Button(app, text = "Timer", image = timer_img, bg = "#00008B", bd = 0)
timer_btn.place(x = 50, y = 340)

stop_btn = Button(app, text = "Stopwatch", image = stop_img, bg = "#00008B", bd = 0)
stop_btn.place(x = 265, y = 340)

exit_btn = Button(app, text = "Exit", image = exit_img, bg = "#00008B", bd = 0,command = exit)
exit_btn.place(x = 190, y = 460)


app.mainloop()
