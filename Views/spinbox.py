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


class SpinBox():


    def add_button_clicked(self):
        if self.timer_var >= self.max_time:
            Messagebox.show_error("Error - Unable to Increase Time" , "Time Logger")
        elif self.timer_var < self.max_time and 0 <=self.timer_var <= 8:
            self.timer_var+=1
            self.main_text.configure(text = str(f"0{self.timer_var}"))
        elif self.timer_var < self.max_time and 9 <= self.timer_var <= self.max_time:
            self.timer_var+=1
            self.main_text.configure(text = str(f"{self.timer_var}"))
    
    def subtract_button_clicked(self):
        if self.timer_var <= 0:
            Messagebox.show_error( "Error - Unable to decrease timer - Please check max time settings" ,"Log Timer" )
        elif self.timer_var <= self.max_time and 11 <= self.timer_var :
            self.timer_var-=1
            self.main_text.configure(text = str(self.timer_var))
        elif self.timer_var <= self.max_time and self.timer_var <= 11:
            self.timer_var-=1
            self.main_text.configure(text =str(f"0{self.timer_var}"))

    def __init__(self , master ,  height  = 400 , width  = 200) -> None:
        self.master  = master
        self.height  = height
        self.width = width
        

        # Defining Constants for the main app  : 
        self.timer_var  = 0
        self.max_time  = 30

        # Defining Controls  : 
        self.main_frame  = btk.Frame(self.master , height= 55 , width=150 , bootstyle  = "warning")
        self.side_frame  = btk.Frame(self.main_frame , height=55 , width=120 , bootstyle  = "primary")
        self.main_text  = btk.Label(self.side_frame , text="00" , font=("Arial" , 20 , "bold") ,style="info.TLabel", background="#4582EC", foreground="#ffffff")
        self.add_button  = btk.Button(self.main_frame , text="+" , command=self.add_button_clicked)
        self.subtract_button  = btk.Button(self.main_frame , text="-" , command=self.subtract_button_clicked)
        self.no_breaks_text = btk.Label(self.master  ,text="No breaks in focus session")

        # Configuring Controls  : 
        self.main_frame.pack_propagate(0)
        self.side_frame.pack_propagate(0)

        # Packing Controls :
        self.main_frame.pack(pady=30)
        self.side_frame.pack(side=tk.LEFT)
        self.main_text.pack(pady=(12 , 0))
        self.no_breaks_text.pack(pady=(12, 0))
        self.add_button.pack(side=tk.TOP)
        self.subtract_button.pack(side=tk.BOTTOM , fill=tk.BOTH)


    def __del__(self):
        try:
            self.main_frame.pack_forget()
        except Exception as e:
            print(e)
        