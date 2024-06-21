import tkinter as tk 
from tkinter import ttk
import ttkbootstrap as btk
from tkinter import messagebox
from ttkbootstrap import Style
import time
from time import sleep
import winsound
from ttkbootstrap.toast import ToastNotification
from pubsub import pub

from PIL import Image
Image.CUBIC = Image.BICUBIC



class Spinbox():

    def __init__(self , master ,  height  = 400 , width = 200) -> None:
        
        self.master  = master
        self.height = height 
        self.width = width
        self.timer_var  = 00
        self.max_time = 30





        # Defining Controls : 
        self.main_frame  = btk.Frame(self.master , height  = 55 , width  = 150 , bootstyle = "warning")
        self.side_frame  = btk.Frame(self.main_frame , height  = 55 , width = 120 , bootstyle = "primary")
        self.timer_text  = btk.Label(self.side_frame , text = "00" , font=("Arial" , 18 , "bold") , style="info.TLabel" , background="#4582EC", foreground="#ffffff")
        self.add_button   = btk.Button(self.main_frame , text="+" )
        self.subtract_button = btk.Button(self.main_frame , text="-" )




        # Configuring Controls : 
        self.main_frame.pack_propagate(0)
        self.side_frame.pack_propagate(0)

        # Packing Contorls :
        self.main_frame.pack(pady=30)
        self.side_frame.pack(side = tk.LEFT)
        self.timer_text.pack(pady=(12 ,0))
        self.add_button.pack(side= tk.TOP )
        self.subtract_button.pack(side= tk.BOTTOM , fill=tk.BOTH)

    # def __del__(self):
    #     self.main_frame.pack_forget()


class SpinMeterBox():

    def __init__(self , master , height = 400 , width  = 400) -> None:
        self.master = master
        self.height  = height
        self.width  = width


        # Defining Controls  : 
        self.minutes_meter  =  btk.Meter(self.master  ,  metersize=150 , bootstyle="primary" , subtext="Seconds" , amounttotal=60 , amountused=0 , interactive=True , meterthickness=15)
        self.seconds_meter = btk.Meter(self.master  ,  metersize=150 , bootstyle="primary" , subtext="Minutes" , amounttotal=60 , amountused=0 , interactive=True , meterthickness=15)
        
        self.minutes_meter.pack(side=tk.RIGHT)
        self.seconds_meter.pack(side=tk.LEFT)

    
    def close_all(self):
        self.master.pack_forget() # To close the application.



if __name__ =='__main__':
    # main   = btk.Window()
    # # SpinMeterBox(main)
    # Spinbox(main)
    # main.mainloop()


    main = btk.Window()
    
    Spinbox(master=main)
    main.mainloop()
