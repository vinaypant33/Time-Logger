import tkinter as tk
from tkinter import ttk
import ttkbootstrap as btk
from tkinter import messagebox
from pubsub import pub



import custom_spinbox
import tasklist
import analytics_frame


class MainPage():


    def stop_focus_session(self):
        self.custom_spinbox  = custom_spinbox.SpinBox(self.timer_frame)
        self.meterbox.close_all()
        self.stop_button.pack_forget()
        self.play_pause_button.pack()


    def start_focus_session(self):
        self.play_pause_button.pack_forget()
        self.custom_spinbox.close_all()
        self.meterbox  = custom_spinbox.SpinMeterBox(self.timer_frame)

        text_icon  =  '\u23F8'# Unicode character for the button icon # '\u23F8' "\u25B6"  \u23F9
        main_text  = "Stop Focus Session"
        self.stop_button  = btk.Button(self.timer_frame , text=f"{text_icon}  { main_text}" , command=self.stop_focus_session)
        self.stop_button.pack(pady = 5)
        self.current_value  = self.custom_spinbox.timer_text.cget("text")
        
        self.meterbox.starting_timer(int(self.current_value))

    

    def theme_change(self):

        # print(self.checkbox_value.get())

        if self.checkbox_value.get() == 0:
            self.theme_checkbox.configure(text="Light Theme")
        elif self.checkbox_value.get() ==1:
            self.theme_checkbox.configure(text="Dark Theme")

            # Theme Dark Theme :  Bootstyle to be changed : 
            '''
            
            '''
            
            self.bottom_frame.configure(bootstyle  = "dark")
            # self.theme_checkbox.configure( style="info.TCheckbox" , foreground = "#ffffff" , background  = "#1E1E1E")
            # style="info.TLabel", background="#4582EC", foreground="#ffffff" will change the data for the cehckbox using this 
            
            self.task_frame.configure(bootstyle  = "dark")







        # self.theme_checkbox.configure(text="Dark Theme")


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

        ## Const Variables for the controls  : 
        button_front_style  = "light"

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
        self.checkbox_value = btk.IntVar()


        self.bottom_frame  = btk.Frame(self.main_app , width=self.width , height=28 , bootstyle  = "info")
        self.bottom_frame.pack_propagate(0)
        # Setting up the canvas for the main frame  : 
        self.main_canvas = tk.Canvas(self.main_app , background="red")
        self.scrollbar  = ttk.Scrollbar(self.main_app, orient=tk.VERTICAL , command=self.main_canvas.yview)
        self.controls_frame = ttk.Frame(self.main_canvas )

        # numerial timer and button and meter widget would be in this frame 
        self.timer_frame = btk.Frame(self.controls_frame , width=self.width - 10 , height=self.frame_height )
        
        self.seperator  = btk.Separator(self.controls_frame )

        # Second frame : Task list and the number of tasks added in the main frame : 
        self.task_frame  = btk.Frame(self.controls_frame , width=self.width - 10 , height = self.frame_height )
        # Third Frame  : # Meter Widget showing yestarday today and tomorrow task list 
        self.seperator1  = btk.Separator(self.controls_frame )
        self.analytics_frame  = btk.Frame(self.controls_frame , width=self.width -10 , height=self.frame_height )
        
        self.timer_frame.pack_propagate(0)
        self.task_frame.pack_propagate(0)
        self.analytics_frame.pack_propagate(0)

        # Controls for the bottom frame  :  Each frame would hold the button widget 
        self.theme_frame  = btk.Frame(self.bottom_frame  , width=125 , height = 28 )
        self.theme_frame.pack_propagate(0)
        self.theme_checkbox = btk.Checkbutton(self.theme_frame, text="Light Theme" , bootstyle="dark-square-toggle" , command=self.theme_change , variable=self.checkbox_value)

        # Settings button : 
        settings  = '\u2699'
        settings_text = " Settings"

        self.settings_frame  = btk.Frame(self.bottom_frame , width=125 , height=28 )
        self.settings_frame.propagate(0)
        self.settings_button   = btk.Button(self.settings_frame , text=f"{settings}{settings_text}" , bootstyle  = button_front_style)

        analytics = '\U0001F4C9'
        analytics_text  = " Analytics"
        self.small_analytics_frame  = btk.Frame(self.bottom_frame , width=125 , height=28 )
        self.small_analytics_frame.pack_propagate(0)
        self.analytics_button  = btk.Button(self.small_analytics_frame , text=f'{analytics}{analytics_text}' , bootstyle  = button_front_style)


        about = '\u2139'
        about_text = " About"
        self.about_frame = btk.Frame(self.bottom_frame , width=125 , height=28 )
        self.about_frame.pack_propagate(0)
        self.about_button = btk.Button(self.about_frame , text=f'{about}{about_text}' , bootstyle  = button_front_style)

        text_icon  =  '\u25B6' # Unicode character for the button icon
        main_text  = "Start Focus Session"
        self.play_pause_button  = btk.Button(self.timer_frame , text=f"{text_icon}  { main_text}" , command=self.start_focus_session )
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
        self.custom_spinbox  = custom_spinbox.SpinBox(self.timer_frame)
        self.bottom_frame.pack(side=tk.BOTTOM)
        self.main_canvas.pack(side=tk.LEFT , fill=tk.BOTH , expand=1)
        self.scrollbar.pack(side=tk.RIGHT , fill=tk.Y)
        self.timer_frame.pack()
        self.seperator.pack(fill=tk.X , pady=4)
        self.task_frame.pack()
        self.seperator1.pack(fill=tk.X , pady = 4)
        self.analytics_frame.pack()
        self.theme_frame.pack(side="left" , anchor="w" , pady = 1)
        self.theme_checkbox.pack(side="left" ,anchor="center" , pady=4 , padx=15)
        
        
        self.settings_frame.pack(side=tk.LEFT , anchor="w" , pady=1)
        self.settings_button.pack(side=tk.LEFT , anchor="center" , pady=0 , padx = (25 , 0))
        self.small_analytics_frame.pack(side=tk.LEFT , anchor="w" , pady=1)
        self.analytics_button.pack(side=tk.LEFT , anchor="center" , pady=0 , padx = (25 , 0))
        self.about_frame.pack(side=tk.LEFT , anchor="w" , padx=0  , pady= (1 ,0))
        self.about_button.pack(anchor="center")
        self.play_pause_button.pack()
        tasklist.TaskList(self.task_frame)
        analytics_frame.Analytics(self.analytics_frame , width=500 , height=250)
        # calling the main loop :

        

        # Checking for the pubsub messages :
        pub.subscribe(self.stop_focus_session, "timer_complete")



        self.main_app.mainloop()

    



if __name__ == '__main__':
    MainPage()