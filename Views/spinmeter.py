import tkinter as tk
from tkinter import ttk
import ttkbootstrap as btk

from pubsub import pub
# from tkinter import messagebox
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.dialogs.dialogs import Messagebox
import ttkbootstrap.icons
from ttkbootstrap.tooltip import ToolTip

import time
from time import sleep
import winsound # make the beep sound and will cahnge this later


from PIL import Image
Image.CUBIC = Image.BICUBIC




class SpinMeter():


    def increment(self):
        completion_toast  = ToastNotification(title="Time Logger" , message="Focus Session Completed - Timer will Reset in 10 Seconds"  , duration=3)
        
        self.current_seconds_cycle_value+=1
        self.second_meter.configure(amountused = self.current_seconds_cycle_value)
        if self.current_seconds_cycle_value == 60:
            self.current_seconds_cycle_value = 0
            self.current_minutes_cycle_value+=1
            # completion_toast.show_toast()
            self.minutes_meter.configure(amountused  = self.current_minutes_cycle_value)
            self.second_meter.configure(amountused = 0)
            if self.current_minutes_cycle_value == 60:
                self.current_minutes_cycle_value = 0
                self.current_hours_cycle_value+=1
                self.hours_meter.configure(amountused = self.current_hours_cycle_value)
                if self.current_hours_cycle_value == self.hours_selected:
                    completion_toast.show_toast()
                    winsound.Beep(1000 , 1000) # Temporary sound and will be changed later 
                    return
        self.master_frame.after(1000 , self.increment)


 
    def timer(self , hour_time):

        self.hours_selected = hour_time
        self.calculated_total_minutes = (60*self.hours_selected)
        self.calculated_total_seconds = (60 * self.calculated_total_minutes)
        self.minutes_cycle = self.calculated_total_minutes // 60
        self.seconds_cycle = self.calculated_total_seconds //60

        print(f"Minutes are {self.calculated_total_minutes} and seconds are {self.calculated_total_seconds} while minutes cycle is {self.minutes_cycle} and seconds cycle is {self.seconds_cycle}")
        self.increment()
                    



    def __init__(self , master ,  height = 300 ,width = 300) -> None:
        self.master = master 
        self.height  = height 
        self.width  = width


        '''
        Calculation for the total cycles in seconds and minutes and make the loop using the seconds and minutes  : 

        '''
        self.hours_selected  = 0
        self.calculated_total_minutes  = 0
        self.calculated_total_seconds  = 0
        self.calculated_total_hours = 0

        self.minutes_cycle  = 0
        self.seconds_cycle  = 0

        self.current_seconds_cycle_value = 0
        self.current_minutes_cycle_value  = 0
        self.current_hours_cycle_value  = 0

        self.master_frame  = btk.Frame(self.master , width=self.width , height = self.height )
        self.second_meter  = btk.Meter(self.master_frame , metersize=150 , bootstyle="primary" , subtextstyle="primary" , subtext="seconds" , amountused=0 , amounttotal=60 , interactive=True , meterthickness=15)
        self.minutes_meter  = btk.Meter(self.master_frame , metersize=150 , bootstyle="primary" , subtextstyle="primary" , subtext="Minutes" , amountused=0 , amounttotal=60 , interactive=True , meterthickness=15)
        self.hours_meter = btk.Meter(self.master_frame , metersize=150 , bootstyle="primary" , subtextstyle="primary" , subtext="Hours" , amountused=0 , amounttotal=24 , interactive=True , meterthickness=15)


        self.master_frame.pack(pady=(30 , 0))
        self.second_meter.pack(side=tk.RIGHT)
        self.minutes_meter.pack(side=tk.RIGHT)
        self.hours_meter.pack(side=tk.RIGHT)

        # Subscribing messages : 
        pub.subscribe(self.timer , "playclicked")

    def delete(self):
        self.master_frame.destroy()
        

    
    
