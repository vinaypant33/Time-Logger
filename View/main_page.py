import tkinter as tk
from tkinter import ttk
import customtkinter as ctk



import ttkbootstrap as ttk

from PIL import Image
Image.CUBIC = Image.BICUBIC



# Import Manually coded Modules : 
from custom_controls import spinbox


class MainPage():


    def __init__(self) -> None:
        self.window  = ctk.CTk()

        

        # Sets the appearance mode of the application
        ctk.set_appearance_mode("dark")        # System and light are available
        
        # Supported themes: green, dark-blue, blue # Sets the color of the widget
        ctk.set_default_color_theme("blue")


        # Setting some parameters for the main window : 
        self.window.title("Log Timer")
        # For now setting the height and width of the app as manually later will change the code 
        self.height  = 600
        self.width   = 600

        self.x_location  = (self.window.winfo_screenwidth() // 2) - (self.width //2 )
        self.y_location  = (self.window.winfo_screenheight() //2) - (self.height //2)

        self.window.geometry(f"{self.width}x{self.height}+{self.x_location}+{self.y_location}")

        self.window.resizable(0 , 0)

        #-------------- Defining the Controls-------------------
        # scrollable frame in which all the elements would be added :
        self.scollable_frame = ctk.CTkScrollableFrame(self.window , width = self.width ,  height=self.height)

        self.focus_meter_frame  = ctk.CTkFrame(self.scollable_frame , height=300  ,width=self.width-10)
        self.focus_meter_frame.pack_propagate(0)

        self.focus_label  = ctk.CTkLabel(self.focus_meter_frame , text="Start Focus Session" )
        self.description_label  = ctk.CTkLabel(self.focus_meter_frame , text = " Select time ( minutes ) for which the focus session to be done ")

        self.spinbox_meter_frame  = ctk.CTkFrame(self.focus_meter_frame , height=500 , width= 200 )
        self.spinbox_meter_frame.pack_propagate(0)

        # Calling the spin box class for packing the spin box control
        self.main_spinbox  = spinbox.Spinbox(self.spinbox_meter_frame , height=100 , width=100)


        #--------------Setting property of controls-------------




        #---------------Binding the controls--------------------



        #---------------Placing the controls -------------------
        self.scollable_frame.pack()
        self.focus_meter_frame.pack(side = "left")
        
        self.focus_label.pack()

        self.description_label.pack()
        self.spinbox_meter_frame.pack(padx = 10 , pady =10)


        #---------------Calling the main app--------------------

        self.window.mainloop()







if __name__ == '__main__':

    main_app  = MainPage()