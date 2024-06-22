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


    def __init__(self , master ,  height = 300 ,width = 300) -> None:
        self.master = master 
        self.height  = height 
        self.width  = width

        self.master_frame  = btk.Frame(self.master , width=self.width , height = self.height )
        self.second_meter  = btk.Meter(self.master_frame , metersize=150 , bootstyle="primary" , subtextstyle="primary" , subtext="seconds" , amountused=0 , amounttotal=60 , interactive=True , meterthickness=15)
        self.minutes_meter  = btk.Meter(self.master_frame , metersize=150 , bootstyle="primary" , subtextstyle="primary" , subtext="Minutes" , amountused=0 , amounttotal=60 , interactive=True , meterthickness=15)
        self.hours_meter = btk.Meter(self.master_frame , metersize=150 , bootstyle="primary" , subtextstyle="primary" , subtext="Hours" , amountused=0 , amounttotal=24 , interactive=True , meterthickness=15)


        self.master_frame.pack(pady=(30 , 0))
        self.second_meter.pack(side=tk.RIGHT)
        self.minutes_meter.pack(side=tk.RIGHT)
        self.hours_meter.pack(side=tk.RIGHT)

    def delete(self):
        self.master_frame.destroy()
        

    
