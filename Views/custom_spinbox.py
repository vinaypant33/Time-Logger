import tkinter as tk 
from tkinter import ttk
import ttkbootstrap as btk 
from ttkbootstrap.constants import *
from tkinter import messagebox


class SpinBox():

    # style = btk.Style()
    # style.configure('Custom.TButton', font=("Helvetica", 12), padding=(10, 5))

    def change_number_adding(self):
        if self.timer_var >= self.max_time:
            messagebox.showerror("Log Timer" , "Error - Unable to increse timer - Please check max time settings")
        elif self.timer_var < self.max_time and 0 <=self.timer_var <= 8:
            self.timer_var+=1
            self.timer_text.configure(text = str(f"0{self.timer_var}"))
        elif self.timer_var < self.max_time and 9 <= self.timer_var <= self.max_time:
            self.timer_var+=1
            self.timer_text.configure(text = str(f"{self.timer_var}"))

    def change_number_subtracting(self):
        if self.timer_var <= 0:
            messagebox.showerror("Log Timer" , "Error - Unable to decrease timer - Please check max time settings")
        elif self.timer_var <= self.max_time and 11 <= self.timer_var :
            self.timer_var-=1
            self.timer_text.configure(text = str(self.timer_var))
        elif self.timer_var <= self.max_time and self.timer_var <= 11:
            self.timer_var-=1
            self.timer_text.configure(text =str(f"0{self.timer_var}"))

        

    def __init__(self , master , height  = 400 , width  = 200) -> None:
        self.master = master
        self.height  = height
        self.width  = width 

        self.timer_var  = 00
        self.max_time = 30



    


        self.main_frame  = btk.Frame(self.master , height=55 , width=150 , bootstyle  = "warning")
        self.main_frame.pack_propagate(0)
        self.side_frame = btk.Frame(self.main_frame , height=55 , width=120 , bootstyle  = "dark")
        self.side_frame.pack_propagate(0)

        self.timer_text = btk.Label(self.side_frame , text="00" , font=("Arial", 18))

        self.add_button = btk.Button(self.main_frame , text="+" , command=self.change_number_adding )
        self.subtract_button = btk.Button(self.main_frame , text="- " , command=self.change_number_subtracting)



        # self.side_frame  = btk.Frame(self.main_frame , height=100 , width=self.width *.6 , bootstyle  = "info")
        # self.side_frame.pack_propagate(0)
        # self.main_text = btk.Label(self.side_frame , text="00" , font=("Arial", 20)) # This frame and the fonts and font size and font type is required 
        # self.add_button = btk.Button(self.main_frame , text="+"  ) 
        # self.subtract_button  = btk.Button(self.main_frame , text="-"  )

        # self.no_breaks_text  = btk.Label(self.master , text="No breaks in focus session !!" )

        # ## setting the focus session button with the play and pause Image : 




        
        # self.main_frame.pack(padx = 50 , pady = 50)
        # self.side_frame.pack(side = "left")
        # self.main_text.pack()
        # self.main_text.place(x = 19 , y = 35)
        # self.add_button.pack(side = "top" , pady=10)
        # self.subtract_button.pack(side = "bottom")

        # self.no_breaks_text.place(x = 25 , y =150)



        self.main_frame.pack(pady = 30)
        self.side_frame.pack(side=tk.LEFT)
        self.timer_text.pack(pady=(12,0))

        self.add_button.pack(side=tk.TOP)
        self.subtract_button.pack(side=tk.BOTTOM )




if __name__ =='__main__':

    main = btk.Window()
    SpinBox(main)

    main.mainloop()