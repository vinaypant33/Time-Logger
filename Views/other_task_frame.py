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
from tkinter import messagebox

from PIL import Image
Image.CUBIC = Image.BICUBIC




class Task_List():

    def starting_timer(self):
        # print("Start Timer")
        pub.sendMessage("starttimer" , task_name  = self.task_entry.get())

    def entry_count (Self ,e  , value): 
        if len(value) > 90 : 
            messagebox.showerror("Time Logger" , "Task Max Length Exceeded")

    def adding_tasklist(self , e = 0):
        
        # check if each of the entry widgets is not empty : 
        for each in self.entry_manager:
            if each.get() == "":
                messagebox.showerror("Task Logger" , "Task description cannot be empty")
                return
       
        self.task_frame = btk.Frame(self.controls_frame , width=400 , height=30)
        self.check_var = btk.BooleanVar(value=False)
        self.taskcheckbutton  = btk.Checkbutton(self.task_frame , variable=self.check_var)
        self.task_entry = btk.Entry(self.task_frame , width=70)
        self.entry_manager.append(self.task_entry)
         # Theme for the progressbar // will make seperate theme class in seperate file later : 
        self.progressstyle = ttk.Style()
        self.progressstyle.configure("Thick.Horizontal.TFloodgauge", thickness=10)


        # self.timer_text  = btk.Label(self.task_frame , text="  01:00:00 " , font = ("satoshi" , 12, "bold"))
        # self.spent_text = btk.Label(self.task_frame , text="  00:00:00" , font = ("satoshi" , 12, "bold"))

        #ToolTip(b2, text="This is dangerous", bootstyle=(DANGER, INVERSE))

        # Defining Tooltip for the controls  : 
        # ToolTip(self.timer_text , text="Max Time Allocated" , bootstyle=("primary", "inverse"))
        # ToolTip(self.timer_text , text="Max Time Allocated" , delay=300)
        # ToolTip(self.spent_text , text="Time Spent in Task" , delay=300)

        # self.progressbar  = ttk.Progressbar(self.task_frame , bootstyle  = "danger"  , value=20)
        # self.tempmeter  = btk.Meter(self.task_frame , metersize=100 , amounttotal=10 , amountused=4)
        

        # self.start_stop_button  = btk.Button(self.task_frame , text='\u25B6' , width=3 , command=self.starting_timer , bootstyle  = "light"  ) # '\u23F8' "\u25B6"  \u23F9

        self.task_entry.bind("<KeyPress>" , lambda e : self.entry_count(e , self.task_entry.get()))
        self.task_entry.bind("<Shift-Return>", lambda e : self.adding_tasklist())
        self.task_entry.bind("<Escape>" , lambda e : self.task_frame.focus())

        self.task_frame.pack(padx=(3,4) , pady=3)
        self.taskcheckbutton.pack(side=tk.LEFT)
        self.task_entry.pack(side=tk.LEFT ,padx =(5,0))
        # self.timer_text.pack(side=tk.LEFT , padx=(5,0))
        # self.progressbar.pack(side=tk.LEFT , padx =(5,0)) # making anohter completion time instead of progressbar 
        # self.spent_text.pack(side=tk.LEFT , padx =(5, 0))
        # self.start_stop_button.pack(side=tk.LEFT , padx=(3,5))

        self.main_canvas.update_idletasks()
        self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))

        # To check the count and increment the same : 
        self.entry_widget_count+=1
        self.task_entry.focus()
    
    def add_controls(self):

        self.temp_frame  = btk.Frame(self.controls_frame , height=200 , width=self.width )
        self.temp_frame.pack(padx=10 , pady=10)
        self.main_canvas.update_idletasks()
        self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))

    '''
    Main class other forms / classes would be called from this class
    '''


    def __init__(self ,master ,  width  = 500 , height  = 600) -> None:
        
        
        self.entry_manager  = []
        # Entry manager makes track of all the entry widgets called and makes sure none of the entry widgets is empty
        self.entry_widget_count = 0 # Entry wounc will be changed later when the app is connected to database



        # Defining Base Controls :
        self.main_app  = master
        self.height  = height
        self.width   = width 
        self.frame_height = 250

        # Setting up the canvas for the main frame  : 
        self.main_canvas = tk.Canvas(self.main_app )
        self.scrollbar  = ttk.Scrollbar(self.main_app, orient=tk.VERTICAL , command=self.main_canvas.yview)
        self.controls_frame = ttk.Frame(self.main_canvas)
        ##############-----------Main Controls------------------------##################
        add_text  = "\u002B"
        add_task  = " Add Task"

        self.add_button  = btk.Button(self.controls_frame , text=f"{add_text}" , command=self.adding_tasklist , bootstyle = "primary")
        ####-------------------Configuring the contros-----------------#######
        self.main_canvas.configure(yscrollcommand=self.scrollbar.set)
        #####------------------Binding the Controls-----------------------######
        self.main_canvas.bind('<Configure>' , lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all")))
        # self.bottom_frame.bind('<MouseWheel>' , lambda e :self.main_canvas.yview_scroll(-1 * int((e.delta / 120)), "units"))
        self.controls_frame.bind("<Enter>" , lambda e : self.adding_tasklist)
        self.main_canvas.create_window((0,0) , window=self.controls_frame ,anchor="nw")
        ######------------------Packing the controls------------------------######

        self.main_canvas.pack(side=tk.LEFT , fill=tk.BOTH , expand=1)
        # self.controls_frame.pack()
        self.scrollbar.pack(side=tk.RIGHT , fill=tk.Y)
        self.add_button.pack(side=tk.BOTTOM, pady=10 , padx=10 , anchor="se")

        # for i in range(100):
        #     i = btk.Button(self.controls_frame , text=i).pack()

        # print(self.controls_frame.winfo_width())
        # print(self.controls_frame.winfo_height())


    


if __name__ == '__main__':
   window  = btk.Window(themename="flatly")
   window.geometry("500x500")
   Task_List(window)
   window.mainloop()