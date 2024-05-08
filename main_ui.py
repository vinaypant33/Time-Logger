import tkinter as tk
from tkinter import ttk
import ttkbootstrap as btk 





class Main_app():


    def __init__(self) -> None:
        ''' for theme we can use the cosmo for the light theme 
        for the dark theme we can use the darkly 
        or we can use cyborg '''
        self.window = btk.Window(themename="darkly") 
        self.window.title("Log Timer")

        # Setting the height and width and making it in the center of the screen  : 
        self.window.resizable(0 , 0)
        height  = 700
        width  = 900 
        x_location  = (self.window.winfo_screenwidth() //2 ) - (width //2 )
        y_location  = (self.window.winfo_screenheight() // 2) - ( height // 2)
        self.window.geometry(f"{width}x{height}+{x_location}+{y_location}")

        # Setting up the icon for the main window  : 
        self.window.iconbitmap("main_icon.ico")


        # Setting up the controls : 
        '''
        sidebar for the main app and make the icon for the buttons : setup the icon for the buttons
        make the 
        '''

        self.tabbar_layout = btk.Notebook(self.window , bootstyle  = "info")

        self.dashboard_frame  = btk.Frame(self.tabbar_layout)
        self.tabbar_layout.add(self.dashboard_frame , text="Dashboard")

        self.task_list = btk.Frame(self.tabbar_layout)
        self.tabbar_layout.add(self.task_list , text="Task List")

        self.analytis = btk.Frame(self.tabbar_layout)
        self.tabbar_layout.add(self.analytis , text="Analytics")

        self.settings  = btk.Frame(self.tabbar_layout)
        self.tabbar_layout.add(self.settings , text="Settings")




        # Posting the controls : 
        self.tabbar_layout.pack(pady=30)

        # Starting the main app_main window
        self.window.mainloop()





if __name__ == '__main__':
    Main_app()


