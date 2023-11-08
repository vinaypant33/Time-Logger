import tkinter as tk 
from tkinter import ttk
from ctypes import windll
import sys
import colors
import fonts
import  styles
import colors
import messagebox
import time 



sys.path.append("View")

# First Class for app : App starting class
class Main_Page():
    # Base functions for setting up the app : 
    # This function will be used for showing the app : 
    def set_appwindow(self ,root):
        GWL_EXSTYLE=-20
        WS_EX_APPWINDOW=0x00040000
        WS_EX_TOOLWINDOW=0x00000080
        hwnd = windll.user32.GetParent(root.winfo_id())
        style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        style = style & ~WS_EX_TOOLWINDOW
        style = style | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
        root.wm_withdraw()
        root.after(1000, lambda: root.wm_deiconify())
    
    def mouse_click(self , event):
        self.x = event.x 
        self.y = event.y

    def mouse_move(self , event):
        self.delta_x  = event.x  - self.x
        self.delta_y = event.y - self.y
        self.new_x  = self.main_app.winfo_x() + self.delta_x
        self.new_y = self.main_app.winfo_y() + self.delta_y
        self.main_app.geometry(f'{self.width}x{self.height}+{self.new_x}+{self.new_y}')
    
    def closing_app(self):
        self.main_app.destroy() # Defining the method before the class but it can only be executed after the class is initialized

    def max_button_clicked(self):
        current_x = self.main_app.winfo_x()
        current_y = self.main_app.winfo_y()
        current_width  = self.main_app.winfo_width()
        current_height   = self.main_app.winfo_height()
        final_x = (current_x)  + current_width // 2
        final_y = (current_y) + current_height //2
        
        messagebox.Messagebox(final_y , final_x , "Maximize Setting Disabled in Current App")

    def min_button_clicked(self):
        self.main_app.overrideredirect(False)
        self.main_app.wm_iconify()
        self.main_app.bind('<FocusIn>' , self.on_deiconify)
        if self.minimized  == False :
            self.minimized == True
            self.main_app.overrideredirect(False)
            self.main_app.state('iconic')
        else:
            self.minimized ==True
            self.main_app.overrideredirect(True)
            self.main_app.state('normal')

    def make_deiconify(self):
        pass

    def close_animation(self): # Obselete function will use alter in some other animation
        self.main_app.overrideredirect(False)
        self.main_app.wm_iconify()
        self.title_bar.bind('<FocusIn>' , self.on_deiconify)
       

    def on_deiconify(self, event): # Will check this function and then convert this in the class
        if self.main_app.wm_state() =='normal' and self.main_app.overrideredirect() != True:
            self.main_app.overrideredirect(True)
            self.set_appwindow(self.main_app)


    # Inititalizing class : 
    def __init__(self , height , width , master = None) -> None:
        self.main_app = tk.Tk()
        self.height   = height
        self.width  = width
        self.main_app.title("Task Tracker")
        # Setting up the app location in the center of the screen 
        self.x_location  = (self.main_app.winfo_screenwidth() // 2) - (self.width //2 )
        self.y_location  = (self.main_app.winfo_screenheight ()//2) - (self.height //2)
        # setting up the page geomerty 
        self.main_app.geometry(f"{self.width}x{self.height}+{self.x_location}+{self.y_location}")
        # making the default titlebar base delete 
        self.main_app.overrideredirect(True)

        # calling the main app function to make the overredirect true  : 
        # Make fucntion to check and make another app.

        '''Variables for the class'''
        # Base variables  :  min max 
        self.minimized  = False
        self.maximized  = False
        self.sidebar_opened  =  False
        self.sidebar_width  = 30

        '''Defining the controls '''
        # Upper Titlebar Control Buttons  : 
        self.title_bar  = tk.Frame(self.main_app , height=25 , background=colors.app_base)
        self.title_bar.pack_propagate(0)
        self.close_button  = tk.Button(self.title_bar,text='\u2716' , height=2 , width=2 , command=self.closing_app)
        self.maximize_button  = tk.Button(self.title_bar , text=u"\U0001F5D6" , height=2 , width=3 , command=self.max_button_clicked) # Will set the command for the same to new form for the message box
        self.minimize_button = tk.Button(self.title_bar , text=u'\u2014' ,height=2 , width =3  , command = self.min_button_clicked)
        # Sidebar and sidebar and Frame : 
        self.sidebar_frame  = tk.Frame(self.main_app , height=self.height , width = self.sidebar_width, background=colors.Blue)
        self.sidebar_frame.pack_propagate(0)
        # Sidebar Buttons : 
        self.open_close_sidebar  = tk.Button(self.sidebar_frame , height = 1  , width = 3 , text="\u2261")
        self.home_button = tk.Button(self.sidebar_frame , height=1 , width=3 , text="\U0001F3E0")
        self.analytics_button  = tk.Button(self.sidebar_frame , height=1,width=3,text="\U0001F4CA")
        self.settings_button  = tk.Button(self.sidebar_frame , height=1, width = 3 , text="\u2699")
        # Sidebar clock frame which will be minimized in the another buttons and classes 
        self.clock_sidebar  = tk.Frame(self.main_app , height=self.height  , width=self.width - self.sidebar_width)
        # Configuring the pre defined controls  : 
        self.title_bar.configure(width=self.width)
        # Configuring the close button with the native method and then the other buttons with the styles class : 
        self.close_button.configure(background=colors.sidebar_base ,  activebackground=colors.Red ,  activeforeground=colors.White  , foreground=colors.White , relief="flat" , bd = 0 )
        styles.styles.button_styles(self.maximize_button ,colors.Dark_Blue , colors.White , colors.Red , colors.Green)
        styles.styles.button_styles(self.minimize_button , colors.Dark_Blue , colors.White , colors.Red , colors.Green)

        styles.styles.button_styles(self.open_close_sidebar , colors.dark_black , colors.White  , colors.app_base , colors.dark_blue_color)
        styles.styles.button_styles(self.home_button , colors.dark_black , colors.White , colors.app_base , colors.dark_blue_color)
        styles.styles.button_styles(self.analytics_button , colors.dark_black , colors.White , colors.app_base , colors.dark_blue_color)
        styles.styles.button_styles(self.settings_button , colors.dark_black , colors.White , colors.app_base , colors.dark_blue_color)
        # Binding the controls : 
        self.title_bar.bind("<Button-1>" , self.mouse_click)
        self.title_bar.bind("<B1-Motion>" , self.mouse_move)


        # Calling the main app : for running the application in the loop
        self.main_app.after(100, lambda: self.set_appwindow(self.main_app)) # To make the icon visible in the application
        
        # Packing the controls : 
        self.title_bar.pack()
        self.close_button.pack(side="right" , padx=1, pady=1)
        self.maximize_button.pack(side="right")
        self.minimize_button.pack(side='right')
        # Sidebar and sidebar controls 
        self.sidebar_frame.pack(side="left")
        self.open_close_sidebar.pack(side="top" , padx=1 ,pady=1)
        self.home_button.pack(side="top" , pady=1, padx=1)
        self.analytics_button.pack(side="top" , pady=1 , padx=1)
        self.settings_button.pack(side="bottom" , padx=1 , pady=1)


        self.main_app.after(10, lambda: self.set_appwindow(self.main_app)) # To make the icon visible in the application
        self.main_app.mainloop() # This calls the main app
        



if __name__ == "__main__":
    main_application  = Main_Page(650 ,450)
