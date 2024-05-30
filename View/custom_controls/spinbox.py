import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

from tkinter import messagebox

from pubsub import pub

'''
Spinbox is to be done of three controls + button - button and the frame with the label
'''

class Spinbox():

    

    def focus_button_clicked(self):
        pub.sendMessage("focusclicked" )
    

    def change_number_adding(self):
        if self.timer_var >= self.max_time:
            messagebox.showerror("Log Timer" , "Error - Unable to increse timer - Please check max time settings")
        elif self.timer_var < self.max_time and 0 <=self.timer_var <= 8:
            self.timer_var+=1
            self.main_text.configure(text = str(f"0{self.timer_var}"))
        elif self.timer_var < self.max_time and 9 <= self.timer_var <= self.max_time:
            self.timer_var+=1
            self.main_text.configure(text = str(f"{self.timer_var}"))

    
    def change_number_subtracting(self):
        if self.timer_var <= 0:
            messagebox.showerror("Log Timer" , "Error - Unable to decrease timer - Please check max time settings")
        elif self.timer_var <= self.max_time and 11 <= self.timer_var :
            self.timer_var-=1
            self.main_text.configure(text = str(self.timer_var))
        elif self.timer_var <= self.max_time and self.timer_var <= 11:
            self.timer_var-=1
            self.main_text.configure(text =str(f"0{self.timer_var}"))


    def __init__(self , master, height = 400 , width   = 200) -> None:

        self.istrue  = False

        # Max Minutes timer variabel and with the max cap of 30 Minutes : 
        self.timer_var  = 00
        self.max_time = 30
        self.master = master # will change this late with the master control 

        self.height = height
        self.width   = width

        self.main_frame  = ctk.CTkFrame(self.master , height=self.height , width=self.width , corner_radius=0)
        self.main_frame.pack_propagate(0)
        # self.side_frame  = ctk.CTkFrame(self.main_frame , height=self.height ,width=140 , fg_color="green", corner_radius=0)
        self.side_frame  = ctk.CTkFrame(self.main_frame , height=self.height , width=self.width *.6,  corner_radius=0 , fg_color="#4682B4")
        self.side_frame.pack_propagate(0)
        self.main_text = ctk.CTkLabel(self.side_frame , text="00" , font=("Arial", 20)) # This frame and the fonts and font size and font type is required 
        self.add_button = ctk.CTkButton(self.main_frame , text="+"  , height=50 , corner_radius=0 , command=self.change_number_adding) 
        self.subtract_button  = ctk.CTkButton(self.main_frame , text="-"  , height=50 , corner_radius=0 , command=self.change_number_subtracting)

        self.no_breaks_text  = ctk.CTkLabel(self.master , text="No breaks in focus session !!" , height=50)

        ## setting the focus session button with the play and pause Image : 
        text  = '\u25B6'
        main_text  = "  Start Focus Session"
        self.play_pause_button  = ctk.CTkButton(self.master , text=f"{text }{ main_text}" , command=self.focus_button_clicked)
        



        
        self.main_frame.pack(padx = 50 , pady = 50)
        self.side_frame.pack(side = "left")
        # self.main_text.pack(pady = 10)
        self.main_text.place(x = 19 , y = 35)
        self.add_button.pack(side = "top")
        self.subtract_button.pack(side = "bottom")

        self.no_breaks_text.place(x = 25 , y =150)

        # self.play_pause_button.pack()
        self.play_pause_button.place(x=33  , y=190)
        # self.no_breaks_text.pack(side="bottom")

        # self.side_frame.grid(row = 0 , column = 0)
        # self.main_text.grid(row = 0 , column = 0 , rowspan  = 2 , columnspan  = 2)

        # self.add_button.grid(row = 0 , column =1 , pady = 1)
        # self.subtract_button.grid(row = 1 , column = 1 , pady = 1)

        # self.master.mainloop()
    def closing_all(self):
        self.main_frame.pack_forget()
        self.no_breaks_text.place_forget()
        self.play_pause_button.place_forget()


