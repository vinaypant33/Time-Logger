import tkinter as tk
from tkinter import ttk
import ttkbootstrap as btk
from tkinter import messagebox

import custom_spinbox


class MainPage():

    '''
    Main class other forms / classes would be called from this class
    '''


    def __init__(self , width  = 500 , height  = 600) -> None:
        # Defining Base Controls :
        self.main_app  = btk.Window()
        self.height  = height
        self.width   = width 
        self.frame_height = 250
        self.main_app.resizable(0 , 0)
        self.x_location = (self.main_app.winfo_screenwidth() // 2) - (self.width // 2)
        self.y_location  = (self.main_app.winfo_screenheight() // 2) - (self.height // 2)
        self.main_app.geometry(f"{self.width}x{self.height}+{self.x_location}+{self.y_location}")

        # Setting up the title and the logo  
        self.main_app.title("Time Logger")



        '''
        Defining controls : 
        Bottom Frame  :  
            canvas
            Scrollbar
            Contntrols Frame 

            Timer Frame
            Task Frame
            Analytics Frame
            
            Theme Frame
            Play Pause Button

            Focus Label : Text for the focus session 
        '''
        self.bottom_frame  = btk.Frame(self.main_app , width=self.width , height=25 , bootstyle  = "info")
        self.bottom_frame.pack_propagate(0)
        # Setting up the canvas for the main frame  : 
        self.main_canvas = tk.Canvas(self.main_app , background="red")
        self.scrollbar  = ttk.Scrollbar(self.main_app, orient=tk.VERTICAL , command=self.main_canvas.yview)
        self.controls_frame = ttk.Frame(self.main_canvas )

        # numerial timer and button and meter widget would be in this frame 
        self.timer_frame = btk.Frame(self.controls_frame , width=self.width - 10 , height=self.frame_height , bootstyle ="info")

        # Second frame : Task list and the number of tasks added in the main frame : 
        self.task_frame  = btk.Frame(self.controls_frame , width=self.width - 10 , height = self.frame_height  , bootstyle  = "secondary")
        # Third Frame  : # Meter Widget showing yestarday today and tomorrow task list 
        self.analytics_frame  = btk.Frame(self.controls_frame , width=self.width -10 , height=self.frame_height , bootstyle = "danger")
        
        self.timer_frame.pack_propagate(0)
        self.task_frame.pack_propagate(0)
        self.analytics_frame.pack_propagate(0)

        # Controls for the bottom frame  :  Each frame would hold the button widget 
        self.theme_frame  = btk.Frame(self.bottom_frame  , width=150 , height = 25 , bootstyle  = "warning")
        self.theme_frame.pack_propagate(0)
        self.theme_checkbox = btk.Checkbutton(self.theme_frame, text="Change Theme" , bootstyle="dark-square-toggle")

    


        text_icon  =  '\u25B6'
        main_text  = "Start Focus Session"
        self.play_pause_button  = btk.Button(self.timer_frame , text=f"{text_icon}  { main_text}")
        self.focus_label  = btk.Label(self.timer_frame , text="Select time ( minutes ) for which the focus session is to be done")


        

        ### Main Controls for Each Frame : 
        # self.timerbox  = btk.Spinbox(self.timer_frame , bootstyle  = "dark" , from_=1, to=100 ) Not gonna use this making a custom control for this 

        ####-------------------Configuring the contros-----------------#######
        self.main_canvas.configure(yscrollcommand=self.scrollbar.set)
        
        #####------------------Binding the Controls-----------------------######
        self.main_canvas.bind('<Configure>' , lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all")))
        self.bottom_frame.bind('<MouseWheel>' , lambda e :self.main_canvas.yview_scroll(-1 * int((e.delta / 120)), "units"))
        self.timer_frame.bind('<MouseWheel>' , lambda e :self.main_canvas.yview_scroll(-1 *int((e.delta / 120)) , "units"))
        self.task_frame.bind('<MouseWheel>' , lambda e :self.main_canvas.yview_scroll(-1 *int((e.delta / 120)) , "units"))
        self.analytics_frame.bind('<MouseWheel>' , lambda e :self.main_canvas.yview_scroll(-1 *int((e.delta / 120)) , "units"))
        # self.timer_frame.bind('<MouseWheel>' , lambda e: messagebox.showerror("aasldkfaklsdfjakjsdf" , "asdfhjakl;dfjklajsdf"))

        self.main_canvas.create_window((0,0) , window=self.controls_frame ,anchor="nw")
        ######------------------Packing the controls------------------------######
        self.focus_label.pack(pady=15)
        custom_spinbox.SpinBox(self.timer_frame)
        self.bottom_frame.pack(side=tk.BOTTOM)
        self.main_canvas.pack(side=tk.LEFT , fill=tk.BOTH , expand=1)
        self.scrollbar.pack(side=tk.RIGHT , fill=tk.Y)
        self.timer_frame.pack()
        self.task_frame.pack()
        self.analytics_frame.pack()
        self.theme_frame.pack(side="left" , anchor="w")
        self.theme_checkbox.pack(side="left" ,anchor="center" , pady=4 , padx=15)
        self.play_pause_button.pack()
        # calling the main loop :
        self.main_app.mainloop()

    


if __name__ == '__main__':
    MainPage()