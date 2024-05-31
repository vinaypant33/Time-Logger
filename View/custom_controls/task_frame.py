import tkinter as tk
from tkinter import ttk
import customtkinter as ctk


class TaskAdd():

    def __init__(self , x_location  , y_location) -> None:
        self.main_app = ctk.CTkToplevel()  # This is the second frame which will have the same theme and properties

        self.x = x_location 
        self.y  = y_location 

        # self.main_app.lift()
        # self.main_app.focus_force() # These are not working as the app size is larger than the main app.
        self.main_app.attributes('-topmost', True) # For showing the app to the top level : 


        # Set the title and make the top level in the center of the main app  : 
        self.main_app.title("Log Timer")

        self.main_app.geometry(f"{400}x{400}+{self.x}+{self.y}")




        self.main_app.mainloop()


class TaskFrame():

    def add_button_clicked(self):
        # Check the current size of the window and the current location and make the app visible in the main app  :
        self.current_x  =  (self.master.winfo_x())
        self.curernt_y  = (self.master.winfo_y()+ 50) 

        self.top_level  = TaskAdd(self.current_x , self.curernt_y)
        
        

        # This would be called after the double clicking the controls and call the main top level frame 

        # """
        # Controls with the task name button and other controls to be added in the scrollable frame : 
        # This would be changed later and the task are to be added from the top level whcih in turn includes the task and other properties 
        # in the main scrollable frame
        
        # """
        # self.each_task  = ctk.CTkFrame(self.scrollable_frame , width=self.scrollable_frame.winfo_width() , height=30 , fg_color="white" ,corner_radius=0)
        # self.each_task.pack_propagate(0)
        # self.checkbox  = ctk.CTkCheckBox(self.each_task , text="" , border_width=1 , border_color="blue" , height=1 , width=1 , corner_radius=0)
        # self.current_text_title  = ctk.CTkEntry(self.each_task , placeholder_text="Enter Task" , border_color="black" , border_width=1 , corner_radius=1 , width=200)
        # self.default_timer = ctk.CTkLabel(self.each_task , text="00:00:00" , font=("Arial" , 18 , "bold"))

        # self.progress_bar  = ctk.CTkProgressBar(self.each_task , border_color="black" , corner_radius=0 , border_width=0 , height=15)
        # # self.progress_bar.configure()
        # self.progress_bar.set(value=0)
        # self.progress_bar["minimum"] = 0
        # self.progress_bar["maximum"] = 100
    
        # self.checkbox.pack(padx = 1 , side = "left" , anchor = "w")
        # self.current_text_title.pack(side = "left" , padx = 1 , anchor = "w")
        # self.default_timer.pack(side = "left" , padx = 1 , anchor = "w")
        # self.progress_bar.pack(side = "left" , padx = 1 , anchor  = "w")
        # self.each_task.pack(padx=2 , pady = 5)




    def __init__(self , master = "sdf" , width = 400 ,  height  = 500) -> None:
        self.master = ctk.CTk() # For the demo code will change this code later to the frame 
        self.height  = height
        self.width  = width
        self.task_frame  = ctk.CTkFrame(self.master  , height=self.height , width=self.width , fg_color="green" , corner_radius=0 , border_color="blue" , border_width=0)
        self.task_frame.pack_propagate(0)
        self.add_button   = ctk.CTkButton(self.task_frame , text="+" , width=50 , corner_radius=0 , command = self.add_button_clicked)

        # self.add_button.pack(side = "right" , anchor = "ne" , padx = (0 , 0) , pady = (0 , 0 )
        self.add_button.pack(anchor = "ne" , padx = 5 , pady = 5)


        self.scrollable_frame  = ctk.CTkScrollableFrame(self.task_frame , height=self.height - 50 , width=self.width + 100 , fg_color="blue")


        self.scrollable_frame.pack(side="bottom" , anchor  = "ne")

        self.task_frame.pack()
        self.master.mainloop() ## This line will be deleted later for now considering this as the main application 
        # self.master.pack()



class CurrentTask(TaskFrame):

    def __init__(self, master="sdf", width=400, height=500) -> None:
        super().__init__(master, width, height)

        print("i am initialized")

name = TaskFrame()
        