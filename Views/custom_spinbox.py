import tkinter as tk 
from tkinter import ttk
import ttkbootstrap as btk 
from ttkbootstrap.constants import *
from tkinter import messagebox

from ttkbootstrap import Style
import time
from time import sleep ## Just to make the timer and test it in the meter frame 
import winsound


import main_page

from ttkbootstrap.toast import ToastNotification # To make the toast notifications 
from pubsub import pub   # library used for message passing


from PIL import Image
Image.CUBIC  = Image.BICUBIC

class SpinBox():

    # style = btk.Style()
    # style.configure('Custom.TButton', font=("Helvetica", 12), padding=(10, 5))

    

    def change_number_adding(self):
        if self.timer_var >= self.max_time:
            messagebox.showerror("Log Timer" , "Error - Unable to increse timer - Please check max time settings")
        elif self.timer_var < self.max_time and 0 <=self.timer_var <= 8:
            self.timer_var+=1
            self.timer_text.configure(text = str(f"0{self.timer_var}"))
        elif self.timer_var < self.max_time and 9 <= self.timer_var <= self.max_time:
            self.timer_var+=1
            self.timer_text.configure(text = str(f"{self.timer_var}"))

    def change_number_subtracting(self):
        if self.timer_var <= 0:
            messagebox.showerror("Log Timer" , "Error - Unable to decrease timer - Please check max time settings")
        elif self.timer_var <= self.max_time and 11 <= self.timer_var :
            self.timer_var-=1
            self.timer_text.configure(text = str(self.timer_var))
        elif self.timer_var <= self.max_time and self.timer_var <= 11:
            self.timer_var-=1
            self.timer_text.configure(text =str(f"0{self.timer_var}"))

        

    def __init__(self , master , height  = 400 , width  = 200) -> None:

        
        self.master = master
        self.height  = height
        self.width  = width 

        self.timer_var  = 00
        self.max_time = 30

        self.main_frame  = btk.Frame(self.master , height=55 , width=150 , bootstyle  = "warning")
        self.main_frame.pack_propagate(0)
        self.side_frame = btk.Frame(self.main_frame , height=55 , width=120 , bootstyle  = "primary")
        self.side_frame.pack_propagate(0)

        self.timer_text = btk.Label(self.side_frame , text="00" , font=("Arial", 18) , style="info.TLabel", background="#4582EC", foreground="#ffffff")

        self.add_button = btk.Button(self.main_frame , text="+" , command=self.change_number_adding )
        self.subtract_button = btk.Button(self.main_frame , text="- " , command=self.change_number_subtracting)

        # self.side_frame  = btk.Frame(self.main_frame , height=100 , width=self.width *.6 , bootstyle  = "info")
        # self.side_frame.pack_propagate(0)
        # self.main_text = btk.Label(self.side_frame , text="00" , font=("Arial", 20)) # This frame and the fonts and font size and font type is required 
        # self.add_button = btk.Button(self.main_frame , text="+"  ) 
        # self.subtract_button  = btk.Button(self.main_frame , text="-"  )

        # self.no_breaks_text  = btk.Label(self.master , text="No breaks in focus session !!" )

        # ## setting the focus session button with the play and pause Image : 

        # self.main_frame.pack(padx = 50 , pady = 50)
        # self.side_frame.pack(side = "left")
        # self.main_text.pack()
        # self.main_text.place(x = 19 , y = 35)
        # self.add_button.pack(side = "top" , pady=10)
        # self.subtract_button.pack(side = "bottom")

        # self.no_breaks_text.place(x = 25 , y =150)

        self.main_frame.pack(pady = 30)
        self.side_frame.pack(side=tk.LEFT)
        self.timer_text.pack(pady=(12,0))

        self.add_button.pack(side=tk.TOP)
        self.subtract_button.pack(side=tk.BOTTOM )
    
    def close_all(self):
        self.main_frame.pack_forget()


class SpinMeterBox():

  
    

    def increment(self , value):
        if value < self.max_value:
            self.timer_meter.configure(amountused = value)
            self.timer_meter.after(6000 , self.increment , value+1) # fChange this in teh producttion to 60000 
        elif value == self.max_value:
            self.timer_meter.configure(amountused = value)
            winsound.Beep(1000 ,2000)
            toast  = ToastNotification("Time Logger" , "Focus Session Ended Resetting Timer : 00" , 40000)
            toast.show_toast()

            # Pubsub send message to reset the timer : 
            self.timer_meter.after(4000 , pub.sendMessage("timer_complete"))
            # pub.sendMessage("timer_complete")
           
        else:
            winsound.Beep(1000 , 2000)




    def starting_timer(self , max_value):
        self.max_value  = max_value
        self.timer_meter.configure(amounttotal = max_value)
        self.increment(0)


        # self.master.after(1000 , self.increment)
        # Start the function to the timer
        # time.sleep(2)
        # for i in range(max_value):
        #     # time.sleep(1)
        #     self.master.after(1000, self.increment, i)


    def __init__(self , master  , height = 400 ,  width = 400) -> None:
        self.master  = master 
        self.height = height
        self.width = width

        # Make the control for the main button : 
        self.timer_meter  = btk.Meter(self.master , metersize=150 , bootstyle="primary" , subtextstyle="primary" , subtext="Minutes" , amountused=0 , amounttotal=60 , interactive=True , meterthickness=15)

        self.timer_meter.pack()

    def close_all(self):
        self.timer_meter.pack_forget()


if __name__ =='__main__':

    main = btk.Window()
    SpinBox(main)

    main.mainloop()