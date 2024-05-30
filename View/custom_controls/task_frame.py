import tkinter as tk
from tkinter import ttk
import customtkinter as ctk



class TaskFrame():

    def add_button_clicked(self):
        print("I am again clicked")

    def __init__(self , master = "sdf" , width = 400 ,  height  = 500) -> None:
        self.master = ctk.CTk() # For the demo code will change this code later to the frame 
        self.height  = height
        self.width  = width
        self.task_frame  = ctk.CTkFrame(self.master  , height=self.height , width=self.width , fg_color="green" , corner_radius=0 , border_color="blue" , border_width=0)
        self.task_frame.pack_propagate(0)
        self.add_button   = ctk.CTkButton(self.task_frame , text="+" , width=50 , corner_radius=0 , command = self.add_button_clicked)

        self.add_button.pack(side = "right" , anchor = "ne" , padx = 5 , pady = 5 )

        self.task_frame.pack()

        self.master.mainloop() ## This line will be deleted later for now considering this as the main application 
        # self.master.pack()



class CurrentTask(TaskFrame):

    def __init__(self, master="sdf", width=400, height=500) -> None:
        super().__init__(master, width, height)

        print("i am initialized")

name = TaskFrame()
        