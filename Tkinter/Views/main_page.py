import tkinter as tk  
from tkinter import ttk  
import ttkbootstrap as btk
from ctypes import windll
import messagebox



# Importing Pre Made Modules : 
import colors
import styles 
import tool_tip

class main_page():

    def main_name(self , event):
        print("I am Called from inside the class")
        print(event)

    def regular_animation(self  ): # Will be using this function to check for the App maximize and setting upo some animations. ( also min and max button )
        self.set_appwindow(self.main_page)
        print(" I am being called again and again")
        self.main_page.after(5000 , self.regular_animation)

    def button_enter_exit(self ,  master , color_name):
        master.configure(background=color_name)

    def minimize_app(self):
        if self.minimized == False:
            self.minimized = True
            self.main_page.overrideredirect(False)
            self.main_page.state('iconic')

        else:
            self.minimized = False
            self.main_page.overrideredirect(True)
            self.main_page.state('normal')


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
        self.new_x  = self.main_page.winfo_x() + self.delta_x
        self.new_y = self.main_page.winfo_y() + self.delta_y
        self.main_page.geometry(f'{self.width}x{self.height}+{self.new_x}+{self.new_y}')

    def min_max(self):
        # Will add the messagebox for the  user : Custom messagebox
        # self.button_x = self.max_button.winfo_x() + self.main_page.winfo_x() - 100
        # self.button_y = self.max_button.winfo_y() + self.main_page.winfo_y() + 30
        self.button_x   = self.main_page.winfo_screenwidth() // 2 - 82
        self.button_y = self.main_page.winfo_screenheight() //2 - 50
        messagebox.Messagebox(165 ,100 , self.button_x , self.button_y , "Maximize Button Disabled ")
        # if self.maximized  ==  False:
        #     self.maximized = True
        #     self.main_page.state('zoomed')
        #     self.max_button.configure(text=u"\U0001F5D7")
        # else:
        #     self.maximized  = False 
        #     self.main_page.state("normal")
        #     self.max_button.configure(text=u"\U0001F5D6" )


    def close_app(self):
        self.main_page.destroy()


    def close_animation(self): # Obselete function will use alter in some other animation
            # if self.main_page.wm_state() == 'normal':
            #     print(" I am being called normal")
            #     self.main_page.overrideredirect(False)
        self.main_page.overrideredirect(False)
        self.main_page.wm_iconify()
        self.main_page.bind('<FocusIn>' , self.on_deiconify)
        # self.current_width  = self.clock_part_timer_sidebar.winfo_width()
        # if self.clock_part_timer_sidebar.winfo_width() == 5:
        #     print(" ab hum hai 5 ")
        #     self.clock_part_timer_sidebar.configure(background=colors.pruple_color)
        #     return None
        # else:
        #     self.clock_part_timer_sidebar.configure(width=self.current_width-5)
            # self.main_page.after(50 , self.close_animation)
    def on_deiconify(self, event):
        if self.main_page.wm_state() =='normal' and self.main_page.overrideredirect() != True:
            self.main_page.overrideredirect(True)
            self.set_appwindow(self.main_page)

    def open_close_sidebar(self): 
        if self.sidebar_opened == True:
            self.sidebar_opened  = False
            self.clock_part_timer_sidebar.configure(width=5 , background=colors.pruple_color)
            self.left_sidebar.configure(background=colors.sidebar_base)
            # self.left_sidebar.configure(background=colors.other_controls_base)
            # self.close_animation() ## Too Expensive function and don't Think animation will look good in this : Will do this in Logo
            self.open_close_button.configure(text='\u2716')
        else:
            self.sidebar_opened == False
            self.sidebar_opened = True
            self.left_sidebar.configure(background=colors.other_controls_base)
            self.clock_part_timer_sidebar.configure(width=self.width -30 , background=colors.other_controls_base)
            
            self.open_close_button.configure(text="\u2261")


    ## All the functions to be defined above :  

    def __init__(self , master , width  , height , ) -> None:
        self.main_page  = tk.Tk() # Will change this later with the master 
        # Getting the data from calling the class
        self.width = width
        self.height  = height
        # Setting up the data for the app functioning 
        self.x_location  = (self.main_page.winfo_screenwidth() // 2 ) - (self.width // 2)
        self.y_location   = (self.main_page.winfo_screenheight() // 2) - (self.height // 2)
        self.maximized  = False
        self.sidebar_opened  = True
        self.minimized  = False
        # Geometry and other theme for the application : 
        self.main_page.geometry(f'{width}x{height}+{self.x_location}+{self.y_location}')
        self.main_page.overrideredirect(True)

        # Setting up the controls
        # Upper titlebar and buttons for the controls : 
        self.titlebar = tk.Frame(self.main_page ,  height=25 , background=colors.sidebar_base)
        self.titlebar.pack_propagate(0)
        self.close_button   = tk.Button(self.titlebar , text='\u2716' , command=self.close_app , height=2 , width=3)
        self.max_button = tk.Button(self.titlebar ,text=u"\U0001F5D6" , height=2 , width=3  , command=self.min_max)
        self.min_button = tk.Button(self.titlebar , text=u'\u2014' ,  height=2 , width=3 , command=self.close_animation)

        # This will be the main page of the : This will be used as the sidebar
        self.clock_part_timer_sidebar = tk.Frame(self.main_page ,  height=self.height , width=self.width - 30 , background=colors.other_controls_base) # Will change the color later
        self.clock_part_timer_sidebar.pack_propagate(0)
        # Sidebar Left for the buttons and contorls : 
        self.left_sidebar  = tk.Frame(self.main_page , height=self.height ,  width=30 , background=colors.other_controls_base)
        self.left_sidebar.pack_propagate(0)
        self.open_close_button   = tk.Button(self.left_sidebar , text="\u2261" , height=1 , command=self.open_close_sidebar) # Will change the text based on the sidebar position 
        self.home_button  = tk.Button(self.left_sidebar , text="\U0001F3E0")
        self.analytics_button  = tk.Button(self.left_sidebar , text="\U0001F4CA")
        self.settings_button  = tk.Button(self.left_sidebar ,  text="\u2699")

        # Temporary button to be used for the main application : 
        self.main_frame  = tk.Frame(self.main_page , background=colors.app_base , height=self.height , width=self.width - 30)

        
        # Configuring the controls
        self.main_page.configure(background=colors.app_base)

        # self.close_button.configure(background=colors.Red , foreground=colors.White , activebackground=colors.Red , activeforeground=colors.Green , bd  = 0  , relief='flat')
        styles.styles.button_styles(self.close_button , colors.sidebar_base , colors.Red , colors.Red , colors.White)
        styles.styles.button_styles(self.max_button , colors.sidebar_base , colors.White , colors.app_base , colors.White)
        styles.styles.button_styles(self.min_button  , colors.sidebar_base , colors.White , colors.app_base , colors.White)
        styles.styles.button_styles(self.open_close_button , colors.hover_2 , colors.White , colors.Red , colors.White)
        styles.styles.button_styles(self.analytics_button ,colors.hover_2, colors.White , colors.Red , colors.White)

        styles.styles.button_styles(self.home_button ,colors.hover_2, colors.White , colors.Red , colors.White)
        styles.styles.button_styles(self.settings_button ,colors.hover_2, colors.White , colors.Red , colors.White)
        self.open_close_button.configure(height=1 , width=2)

        # Binding the controls : 
        self.titlebar.bind("<Button-1>" , self.mouse_click)
        self.titlebar.bind("<B1-Motion>" , self.mouse_move)
        self.open_close_button.bind("<Enter>" , lambda event : self.button_enter_exit(master=self.open_close_button , color_name=colors.app_base))
        self.open_close_button.bind("<Leave>" , lambda event : self.button_enter_exit(master=self.open_close_button , color_name=colors.hover_2))

        self.analytics_button.bind("<Enter>" , lambda event : self.button_enter_exit(master=self.analytics_button , color_name=colors.app_base))
        self.analytics_button.bind("<Leave>" , lambda event : self.button_enter_exit(master=self.analytics_button , color_name=colors.hover_2))

        self.home_button.bind("<Enter>" , lambda event : self.button_enter_exit(master=self.home_button , color_name=colors.app_base))
        self.home_button.bind("<Leave>" , lambda event : self.button_enter_exit(master=self.home_button , color_name=colors.hover_2))

        self.settings_button.bind("<Enter>" , lambda event : self.button_enter_exit(master=self.settings_button , color_name=colors.app_base))
        self.settings_button.bind("<Leave>" , lambda event : self.button_enter_exit(master=self.settings_button , color_name=colors.hover_2))

        # Placing the controls 
        self.titlebar.pack(side='top' ,fill='x')
        self.close_button.pack(side='right')
        self.max_button.pack(side='right')
        self.min_button.pack(side='right') # Placing the upper controls and will be used to control app behaviour. 
        self.left_sidebar.pack(side='left' , fill='y')
        # self.open_close_button.place(x = 10 , y = 30) 
        self.open_close_button.pack(side='top' , padx=(2,2) , pady=(10,10))
        self.home_button.pack(side='top' , padx=(2,2) , pady=(0,10))
        self.analytics_button.pack(side='top' , padx=(2,2) , pady=(0,10))

        self.settings_button.pack(side='bottom' , padx=(2,2) , pady=(0,5))
        self.clock_part_timer_sidebar.pack(side='right')
        # Main Frame to be packed : 
        self.main_frame.pack(fill='y')

        # Calling main App : 
        self.main_page.after(10, lambda: self.set_appwindow(self.main_page)) # To make the icon visible in the application

        tool_tip.ToolTip(self.settings_button , "Settings" , colors.app_base ,  colors.hover_2)
        tool_tip.ToolTip(self.open_close_button , "Open close Sidebar" , colors.app_base ,  colors.hover_2)
        tool_tip.ToolTip(self.home_button , "Home" , colors.app_base ,  colors.hover_2)
        tool_tip.ToolTip(self.analytics_button , "Analytics" , colors.app_base ,  colors.hover_2)
        self.main_page.mainloop()
        




if __name__ == '__main__':
    main_app = main_page('master' , 400 ,600)