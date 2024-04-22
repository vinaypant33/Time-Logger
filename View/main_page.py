from PIL import Image
Image.CUBIC = Image.BICUBIC

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import ttkbootstrap as btk
from ttkbootstrap.constants import *



class Main_page():


    def __init__(self , window_width ,  window_height , root) -> None:
        # self.main_window = btk.tk.Tk()
        self.main_window = btk.Window(themename="darkly")

        # Make the geometry of the app and the postion in the center of the screen 
        self.height  = window_height
        self.width  = window_width

        self.x_location = ((self.main_window.winfo_screenwidth() // 2) - (self.width //2))
        self.y_location = ((self.main_window.winfo_screenheight() //2 ) - (self.height //2))

        self.main_window.geometry(f'{self.width}x{self.height}+{self.x_location}+{self.y_location}')
        self.main_window.title("Log Timer")
        self.main_window.resizable(0 , 0)

        # Make the controls for the main app : 
        meter  = btk.Notebook(master=self.main_window , bootstyle='dark' ,  height=self.height , width=self.width) #Notebook(bootstyle="info")
        
        timer_frame  = btk.Frame(meter)
        tasks_frame = btk.Frame(meter)
        settings_frame  = btk.Frame(meter)

        meter.add(timer_frame , text="Timer")
        meter.add(tasks_frame , text="Tasks")
        meter.add(settings_frame , text="Settings")
        

        # Meter widget for the main app : 
        value_meter = btk.Meter(master = timer_frame,metersize=200,padding=5,amountused=0,metertype="full",subtext="Minutes",interactive=False)

    


        ## Packing the controls : 
        meter.pack()
        value_meter.pack(pady=30)

    

        ## Running the main app :
        self.main_window.mainloop()




Main_page(500 , 600 , "adf")