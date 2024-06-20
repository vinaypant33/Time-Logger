import tkinter as tk 
from tkinter import ttk
import ttkbootstrap as btk
from tkinter import messagebox

from pubsub import pub




class MainPage():

    def __init__(self , width  = 500 , height  = 600) -> None:
        self.mainapp  = btk.Window()
        self.height  = height
        self.width  = width
        self.mainapp.resizable(0,0)
        self.x_location  = (self.mainapp.winfo_screenwidth()//2) - (self.width //2)
        self.y_location  = (self.mainapp.winfo_screenheight() //2) - (self.height //2)
        self.mainapp.geometry(f"{self.width}x{self.height}+{self.x_location}+{self.y_location}")
        self.mainapp.title("Task Logger")

        # Constants : App Constants 
        self.frame_width = self.width - 10
        self.frame_height  = 300
        self.checkbox_value  = btk.IntVar() # For True and False of checkbox 
        self.bottom_frame__height  = 40
        self.bottom_frame_dividedwidth  = self.width // 4 

        settings_icon  = '\u2699'
        settings_text = "  Settings"

        analytics_icon  = '\U0001F4C9'
        analytics_text = "  Analytics"

        about_icon = '\u2139'
        about_text = " About"



        '''
        MainPage Interface : Widgets :
        canvas  : For scrollable frame 
        scrollbar  : For scrolling 
        3 Frames for 3 Control sections  :  timer frame, task frame, analytics frame
        bottom frame and seperator for all frames 
        '''
        
        # Defining Controls :  
        self.canvas  = tk.Canvas(self.mainapp)
        self.scrollbar  = ttk.Scrollbar(self.mainapp , orient=tk.VERTICAL , command=self.canvas.yview)
        self.controls_frame  = btk.Frame(self.canvas)

        self.tiemr_frame  = btk.Frame(self.controls_frame, width = self.frame_width , height = self.frame_height )
        self.timer_seperator  = btk.Separator(self.controls_frame)
        self.task_frame  = btk.Frame(self.controls_frame , width=self.frame_width , height = self.frame_height )
        self.task_seperator = btk.Separator(self.controls_frame)
        self.analytics_frame  = btk.Frame(self.controls_frame , width=self.frame_width , height=self.frame_height )

        self.bottom_frame  = btk.Frame(self.mainapp , width=self.width , height  = self.bottom_frame__height , bootstyle  ='dark')
        self.theme_frame_1 = btk.Frame(self.bottom_frame , width=self.bottom_frame_dividedwidth ,height=self.bottom_frame__height - 2)
        self.theme_frame_2 = btk.Frame(self.bottom_frame , width=self.bottom_frame_dividedwidth , height=self.bottom_frame__height - 2)
        self.theme_frame_3 = btk.Frame(self.bottom_frame , width=self.bottom_frame_dividedwidth , height = self.bottom_frame__height - 2)
        self.theme_frame_4 = btk.Frame(self.bottom_frame , width=self.bottom_frame_dividedwidth , height = self.bottom_frame__height -2)


        # Other Wdgets  :  Buttons,Checkboxes etc.
        self.light_dark_checkbox  = btk.Checkbutton(self.theme_frame_1 , text="Light Theme" , bootstyle = "dark-square-toggle" , variable=self.checkbox_value)
        self.settings_button = btk.Button(self.theme_frame_2 , text=f"{settings_icon}{settings_text}")
        self.analytics_button  = btk.Button(self.theme_frame_3 , text=f"{analytics_icon}{analytics_text}")
        self.about_button  = btk.Button(self.theme_frame_4 , text=f"{about_icon}{about_text}")

        # Configuring Controls :
        self.tiemr_frame.pack_propagate(0)
        self.task_frame.pack_propagate(0)
        self.analytics_frame.pack_propagate(0)
        self.bottom_frame.pack_propagate(0)
        self.theme_frame_1.pack_propagate(0)
        self.theme_frame_2.pack_propagate(0)
        self.theme_frame_3.pack_propagate(0)
        self.theme_frame_4.pack_propagate(0)


        # Binding Coontrols : All Controls  ::
        self.canvas.create_window((0,0) , window=self.controls_frame , anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>" , lambda e : self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.tiemr_frame.bind("<MouseWheel>" , lambda e :self.canvas.yview_scroll(-1 *int((e.delta / 120)) , "units"))
        self.task_frame.bind("<MouseWheel>" , lambda e :self.canvas.yview_scroll(-1 *int((e.delta / 120)) , "units"))
        self.bottom_frame.bind("<MouseWheel>" , lambda e :self.canvas.yview_scroll(-1 *int((e.delta / 120)) , "units"))
        self.analytics_frame.bind("<MouseWheel>" , lambda e :self.canvas.yview_scroll(-1 *int((e.delta / 120)) , "units"))



        ## Packing Controls :: 
        self.bottom_frame.pack(side=tk.BOTTOM )
        self.canvas.pack(side=tk.LEFT , fill=tk.BOTH , expand=1)
        self.scrollbar.pack(side=tk.RIGHT , fill=tk.Y)
        self.tiemr_frame.pack()
        self.timer_seperator.pack(fill=tk.X)
        self.task_frame.pack()
        self.task_seperator.pack(fill=tk.X)
        self.analytics_frame.pack()
        self.theme_frame_1.pack(side=tk.LEFT , anchor="w")
        self.theme_frame_2.pack(side=tk.LEFT  , anchor = "w")
        self.theme_frame_3.pack(side=tk.LEFT , anchor="w")
        self.theme_frame_4.pack(side=tk.LEFT , anchor="w")

        self.light_dark_checkbox.pack(padx=5 , pady= 10 , fill=tk.X)
        self.settings_button.pack(pady=5 , fill=tk.X)
        self.analytics_button.pack(pady=5 , fill=tk.X)
        self.about_button.pack(pady=5 , fill=tk.X)
        
        

        # Make the window ::
        self.mainapp.mainloop()



    def __del__ (self) -> None:
        print("Class Deleted")
    







if __name__ == '__main__':

    page  = MainPage()
    # del page 
