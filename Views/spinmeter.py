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

        if self.current_seconds_count <= self.var_sec : 
            if self.cycle_seconds_count <= self.seconds_max_cycle:
                self.current_seconds_count+=1
                if self.current_seconds_count >= 60:
                    self.current_seconds_count == 0
                    self.cycle_seconds_count+=1
                    self.second_meter.configure(amountused = 0)
                self.second_meter.configure(amountused = self.current_seconds_count)
                self.master_frame.after(1000 , self.increment)
            else:
                return
        else:
            return
        
        # if self.current_seconds_count == self.var_sec:
        #     return
        # elif self.current_seconds_count < self.var_sec:
        #     self.current_seconds_count+=1
        #     if self.current_minutes_count
        #     self.second_meter.configure(amountused = self.current_seconds_count)
        # self.master_frame.after(1000 , self.increment)

 
    def timer(self , hour_time):
        # print(f"hour time is {hour_time}")
        self.var_hour  = hour_time
        self.var_min = (60*self.var_hour)
        self.var_sec = (60* self.var_min)
        self.seconds_max_cycle = self.var_sec // 60
        self.minutes_max_cycle  = self.var_min // 60

        self.increment()


        

        # self.increment()

        # print(self.var_hour)
        # print(self.var_min)
        # print(self.var_sec)

        # for i in range(self.var_hour):
        #     for j in range(self.var_min):
        #         for k in range(self.var_sec):
                    



    def __init__(self , master ,  height = 300 ,width = 300) -> None:
        self.master = master 
        self.height  = height 
        self.width  = width

        self.var_hour  = 0
        self.var_min  = 0
        self.var_sec = 0

        self.cycle_seconds_count  = 0
        self.cycle_minutes_count  = 0

        self.current_seconds_count  = 0 
        self.current_minutes_count  = 0
        self.current_hours_count  = 0

        self.seconds_max_cycle = 0
        self.minutes_max_cycle  = 0


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
        

    
    
