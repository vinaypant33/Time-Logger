import ttkbootstrap as btk 
import tkinter as tk
# from ttkbootstrap import Style
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import ttk

# As the meter widget is not working we are importing the Bicubic import :
from PIL import Image
Image.CUBIC = Image.BICUBIC

import calendar


# Settings class for the settings top page : or the settings frame


from settings import Settings
class Main_app():

    def show_hide_sidebar(self):
        if self.sidebar.winfo_width() == 70:
            self.sidebar.config(width=850)
            self.open_close_button.config(text="\u2770")
            self.open_close_button.place(x= 850,  y  = 662)
            self.app_icon.pack_forget()
            self.app_icon.place_forget()
            self.settings_text  = f"{self.settings_unicode} {self.settings_text_1}"
            self.settings_button.config(text=self.settings_text)
            self.timer_and_task_frame.place(x  = 4 , y = 10)
            # Place forget the widgets and frame : 
            self.settings_frame.place_forget()
            self.meter_widget_frame.place_forget()
            self.calender_widget_frame.place_forget()
            self.task_frame.place_forget()

        else:
            self.sidebar.config(width=70)
            self.open_close_button.config(text="\u2771")
            self.open_close_button.place(x= 70,  y  = 662)
            self.app_icon.place(x = 3 , y = 10)
            self.settings_text  = f"{self.settings_unicode} "
            self.settings_button.config(text=self.settings_text)
            self.settings_frame.place_forget()
            self.timer_and_task_frame.place_forget()
            self.meter_widget_frame.place(x = 80 , y = 10)
            self.calender_widget_frame.place(x=490 , y = 10)
            self.task_frame.place(x = 80 , y = 320)



    def show_settings(self):
        # app = btk.Toplevel(title="Log Timer")
        # app.iconbitmap("main_icon.ico")
        # app.resizable(0 , 0)
        # width  = 600
        # self.top_level_x  = (self.window.winfo_x() //2 ) + (self.window.winfo_width() // 2)
        # self.top_level_y = (self.window.winfo_y() //2 ) + (self.window.winfo_height() - 500)
        # app.geometry(f"{600}x{600}+{self.top_level_x}+{self.top_level_y}")
        # app.mainloop()
        # pass # Make the main frame and will load the frame to this side bar 
        if self.sidebar.winfo_width() == 850:
                
            if self.settings_frame.winfo_ismapped() == False:
                self.settings_frame.place(x  = 4 , y = 10)
                self.timer_and_task_frame.place_forget()
                Settings(self.settings_frame)
            if self.settings_frame.winfo_ismapped() == True:
                self.settings_frame.place_forget()
                self.timer_and_task_frame.place(x=4,y=10)
        else:
            pass

    def __init__(self) -> None:
        
        '''
        Sections : 
        Functions
        Importing Images 
        Defining Controls
        Configuring Controls 
        Binding Controls
        Placing Controls

        '''

        # Theme  : for Light : cosmo and minty - for meter widget : flatly , litera ,  for dark  : darkly cyborg 

        # Defining Window, Size, Geometry icon and  x and y location
        self.window = btk.Window(themename="darkly") # themename  = "minty"
        self.window.title("Log Timer")
        self.window.resizable(0 , 0)
        height  = 700
        width  = 900 
        x_location  = (self.window.winfo_screenwidth() //2 ) - (width //2 )
        y_location  = (self.window.winfo_screenheight() // 2) - ( height // 2)
        self.window.geometry(f"{width}x{height}+{x_location}+{y_location}")
        self.window.iconbitmap("main_icon.ico")
    
        # ------------- Importing Images  ----------------- #
        image = Image.open('hourglass.png')
        image = image.resize((60, 60))  # Resize the image as needed
        self.logo_image  = ImageTk.PhotoImage(image=image)


        # ----------------- Styles to be used in the main app -------------- #
        # Setting up the style for the app : It can be changed later as it works for the whole app  :
        # style = Style(theme='darkly')
        style  = ttk.Style()
        style.configure('Custom.TFrame', background='red')  

        border_radius   = ttk.Style()
        border_radius.configure("Custom.TButton" )

        

        # Setting up the controls for the main app  : 
        self.sidebar  = btk.Frame(self.window , width=70  , height=500 , style="darkly") # width 200 to be changed to 400 or 500 depending on the timer 
        self.sidebar.pack_propagate(False)

        self.app_icon = btk.Label(self.sidebar , image=self.logo_image , style="minty")


        home_icon_unicode = "\U0001F3E0"
        text = "Dashboard"
        self.label_text = f"{home_icon_unicode} {text}"

        analytics_unicode  = "\U0001F4CA"
        text_a = "Analytics"
        analytics_text  = f"{analytics_unicode} {text_a}"

        task_unicode  = "\U0001F4CB"
        text_task = "Task List"
        task_text   = f"{task_unicode} {text_task}"

        self.settings_unicode  = "\u2699"
        self.settings_text_1  = "Settings"
        # self.settings_text  = f"{settings_unicode} {settings_text}"
        self.settings_text  = f"{self.settings_unicode}"
        

        # self.dashboard_button  = btk.Button(master=self.sidebar , text=self.label_text  , style='toolbutton' , width=100 , )
        # self.analytics_button = btk.Button(master=self.sidebar , text=analytics_text , style='toolbutton' , width=100 , compound='left' )
        # self.task_button  = btk.Button(master=self.sidebar , text=task_text , style="error" , width=100 )

        self.settings_button   = btk.Button(master=self.sidebar , text=self.settings_text, command=self.show_settings)
        
        self.open_close_button  = btk.Button(master=self.window , text="\u2771" , command=self.show_hide_sidebar) # The text would be changed depending on the sidebar width U+2771
        
        self.settings_frame   = btk.Frame(master=self.sidebar  , height=650 , width = 830 , style="minty")
        self.settings_frame.pack_propagate(0)

        self.timer_and_task_frame = btk.Frame(master = self.sidebar , height = 650 , width = 830 ) # Only task list would be added in here which will be used to add task with another frame

        self.meter_widget_frame = btk.Frame(master=self.window,  height = 300 , width = 400 , style='danger.TFrame') # Would check other methods and themes availabel for the frame and for other controls 
        self.calender_widget_frame  = btk.Frame(master=self.window , height=300 , width=400 , bootstyle="warning")
        self.task_frame  = btk.Frame(master = self.window , height=340 , width=810 , bootstyle  = "dark.TFrame")
        self.meter_widget_frame.pack_propagate(0)
        self.calender_widget_frame.pack_propagate(0)
        self.task_frame.pack_propagate(0)


        ## ----- Controls for the main frame  : 

        '''
        Meter widget for the main frame 
        Make calender for the main frame
        Make another frame for adding the tasks make another from for that and add tags and other things in the settings page 
        Frame to be scrollable and make the scrollable table with the mainframe 
        '''
        self.meter_timer  = btk.Meter(master=self.meter_widget_frame ,metersize=250,amounttotal=60 , bootstyle="success", subtextstyle="warning" , interactive=True , subtext="Seconds")
        self.total_timer_label = btk.Label(self.meter_widget_frame , text="00:00:00" , font=("Arial", 22, "bold"))
        """
        metersize=180,
    padding=5,
    amountused=25,
    metertype="semi",
    subtext="miles per hour",
    interactive=True,
        """

        self.calender  = btk.DateEntry(master = self.calender_widget_frame)
        self.calender.pack()
    

        # ------------------------------ # 
        # Placing the controls and setting up the frames to contain everything  : 
        self.sidebar.pack(side='left' , fill='y')
        # self.app_icon.pack(pady=(30,0)) # Top right bottom left can be used for the pady and padxd
        self.app_icon.place(x = 3 , y = 10)
        # self.dashboard_button.pack(pady=(30 , 0))
        # self.task_button.pack(pady=(10,0))
        # self.analytics_button.pack(pady=(10 , 0))

        self.settings_button.pack(side='left', anchor='sw', padx=3, pady=10)
        # self.open_close_button.pack(side='right' , anchor="sw" , padx=3 , pady=10)
        self.open_close_button.place(x = 70 , y = 662)
        # self.settings_frame.pack(pady=10 , padx=0 , anchor="w") # Make the settings frame pack in the sidebar app :: Pack is not working make the place 
        
        # self.timer_and_task_frame.place(x  = 4 , y = 10)

        self.meter_widget_frame.place(x = 80 , y = 10)
        self.calender_widget_frame.place(x=490 , y = 10)
        self.task_frame.place(x = 80 , y = 320)


        # self.meter_widget_frame.pack(side="top" , anchor='nw' , padx=10 , pady=10)
        # self.calender_widget_frame.pack(side="top" , anchor="ne" , padx=10 , pady=10)

        self.meter_timer.pack(pady=(10,0))
        self.total_timer_label.pack(pady=1)


        # Starting the main app_main window
        self.window.mainloop()





if __name__ == '__main__':
    Main_app()


