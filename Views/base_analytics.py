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




class Base_Analytics():


    def __init__(self , master , height = 400 , width  = 500) -> None:
        self.master = master 
        self.height  = height
        self.width  = width

        self.yesterday_frame  = btk.Frame(self.master , height=height, width  = (self.width //3) )
        self.today_frame  = btk.Frame(self.master , height=height , width=(self.width //3) )
        self.streak_days = btk.Frame(self.master , height=self.height , width=(self.width //3) )


        self.yesterday_frame.pack(side=tk.LEFT)
        self.today_frame.pack(side=tk.LEFT)
        self.streak_days.pack(side=tk.LEFT)

        '''
        3 Frames one meter for yesterday one for today and one for tomorrow
        Meter Widget for each frame 
        inside text in each meter frame
        '''


        ## Meter Widgets : 
        self.yestarday_meter  = btk.Meter(self.yesterday_frame , metersize=162 ,bootstyle="primary", subtextstyle="primary" , subtext="Hours - Yesterday" , amountused=0,metertype="full" ,interactive=True, meterthickness=15 ,amounttotal=24)
        self.today_meter  =btk.Meter(self.today_frame ,metersize=163 ,  bootstyle = "primary" , subtext="Hours - Today" , subtextstyle="primary" , amountused=0,metertype="full" ,interactive=True, meterthickness=15 , amounttotal=24 )
        self.streak_meter  = btk.Meter(self.streak_days, metersize=162, bootstyle="primary" , subtext="Days - Streak" , subtextstyle="primary" , amountused=0,metertype="full",interactive=True , meterthickness=15 ,amounttotal=100)





        self.yestarday_meter.pack()
        self.today_meter.pack()
        self.streak_meter.pack()

