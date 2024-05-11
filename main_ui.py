import ttkbootstrap as btk 
import tkinter as tk
# from ttkbootstrap import Style
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import ttk

class Main_app():


    def show_hide_sidebar(self):
        if self.sidebar.winfo_width() == 70:
            self.sidebar.config(width=850)
            self.open_close_button.config(text="\u2771")
            self.open_close_button.place(x= 850,  y  = 662)
            self.app_icon.pack_forget()
            self.app_icon.place_forget()
            self.settings_text  = f"{self.settings_unicode} {self.settings_text_1}"
            self.settings_button.config(text=self.settings_text)
        else:
            self.sidebar.config(width=70)
            self.open_close_button.config(text="\u2770")
            self.open_close_button.place(x= 70,  y  = 662)
            self.app_icon.place(x = 3 , y = 10)
            self.settings_text  = f"{self.settings_unicode} "
            self.settings_button.config(text=self.settings_text)
    


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
        self.window = btk.Window(themename="cyborg")
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

        self.app_icon = btk.Label(self.sidebar , image=self.logo_image , style="darkly")


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

        self.settings_button   = btk.Button(master=self.sidebar , text=self.settings_text )
        
        self.open_close_button  = btk.Button(master=self.window , text="\u2770" , command=self.show_hide_sidebar) # The text would be changed depending on the sidebar width U+2771
        

 
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


        # Starting the main app_main window
        self.window.mainloop()


if __name__ == '__main__':
    Main_app()