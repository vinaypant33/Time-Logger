import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import ttkbootstrap as ttk


from PIL import Image
Image.CUBIC = Image.BICUBIC

from pubsub import pub  # Used for message passing //  

# Import Manually coded Modules : 
from custom_controls import spinbox
from custom_controls import task_frame


class MainPage():


    def clock_timer_loading(self ):
        self.spinbox_meter_frame.configure(height = 500 , width = 400)
        self.main_spinbox.closing_all()


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

        # Frames ( scrollable Main Frame and other Frames in whcih the controls would be defined )
        self.scrollabe_frame = ctk.CTkScrollableFrame(self.window , width=self.width , corner_radius= 0  )
        self.clock_timer_frame  = ctk.CTkFrame(self.scrollabe_frame , width=self.width - 10 , height=300 ,corner_radius= 0 )
        self.clock_timer_frame.pack_propagate(0)
        self.task_work_frame  = ctk.CTkFrame(self.scrollabe_frame , width=self.width , height=400 , corner_radius=0 )
        self.analytics_frame  = ctk.CTkFrame(self.scrollabe_frame , width=self.width , height=300 , corner_radius=  0 )

        self.focus_label   = ctk.CTkLabel(self.clock_timer_frame , text="Start Focus Session")
        self.description_label = ctk.CTkLabel(self.clock_timer_frame , text="Select time ( minutes ) for which the focus session to be done")
        
        self.spinbox_meter_frame  = ctk.CTkFrame(self.clock_timer_frame , height=230 , width=200 )
        self.spinbox_meter_frame.pack_propagate(0)

        # External Classes Called for Spinbox and Taskframe
        self.main_spinbox  = spinbox.Spinbox(self.spinbox_meter_frame , height=100 , width=100)

        self.task_frame  = task_frame.TaskFrame(self.task_work_frame , width=400 , height=400)

        #-------------Packing the controls----------------------
        self.scrollabe_frame.pack(expand  = True , fill = "y")
        self.clock_timer_frame.pack(pady = 10 , padx=10)
        self.task_work_frame.pack()
        self.analytics_frame.pack(padx=10 , pady =10)

        self.focus_label.pack()
        self.description_label.pack()

        self.spinbox_meter_frame.pack()
        



        # # scrollable frame in which all the elements would be added :
        # self.scollable_frame = ctk.CTkScrollableFrame(self.window , fg_color="red"  , width=self.width , height=self.height , corner_radius=0)
        

        # self.focus_meter_frame  = ctk.CTkFrame(self.scollable_frame , height=300  ,width=self.width , fg_color="yellow" , corner_radius=0)
        # # self.focus_meter_frame.pack_propagate(0)

        # self.focus_label  = ctk.CTkLabel(self.focus_meter_frame , text="Start Focus Session" )
        # self.description_label  = ctk.CTkLabel(self.focus_meter_frame , text = " Select time ( minutes ) for which the focus session to be done ")

        # self.spinbox_meter_frame  = ctk.CTkFrame(self.focus_meter_frame , height=500 , width= 200 ) # Previous height and width is 200 x 200
        # self.spinbox_meter_frame.pack_propagate(0)

        # # Calling the spin box class for packing the spin box control
        


        # self.middle_task_frame  = ctk.CTkFrame(self.scollable_frame, height=400 , width=self.width - 10, fg_color="green" , corner_radius=0)
        # self.middle_task_frame.pack_propagate(0)

        
        

        # self.tempbutton  = ctk.CTkButton(self.scollable_frame , text="I am the button")


        # ## Cehcking the incoming messages from other modules and classes :
        # pub.subscribe(self.clock_timer_loading , "focusclicked") 
        
        # #--------------Setting property of controls-------------




        # #---------------Binding the controls--------------------



        # #---------------Placing the controls -------------------
        # self.scollable_frame.pack(expand = "true" , fill = "both")
        # # self.scollable_frame.place(x = 0 , y = 0)
        # # self.scollable_frame.pack()
        # self.focus_meter_frame.pack(side = "left")
        # # self.focus_meter_frame.place(x = 0 , y = 0)
        
        # # self.focus_label.pack()

        # # self.description_label.pack()
        # # self.spinbox_meter_frame.pack(padx = 10 , pady =10)
        # # self.middle_task_frame.pack(padx = 10 , pady  = 10)

        # # self.middle_task_frame.pack(side = "top")
        # self.middle_task_frame.place(x =0 , y = 240)
        # # self.middle_task_frame.pack()

        # # self.task_frame  = task_frame.TaskFrame(self.middle_task_frame , width=400 , height=400)
        # # self.main_spinbox  = spinbox.Spinbox(self.spinbox_meter_frame , height=100 , width=100)

        # self.tempbutton.pack()
        # #---------------Calling the main app--------------------

        self.window.mainloop()







if __name__ == '__main__':

    main_app  = MainPage()