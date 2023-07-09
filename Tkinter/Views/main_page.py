import tkinter as tk  
from tkinter import ttk  
import ttkbootstrap as btk





# Importing Pre made modules  : 
import colors



class main_page():

    def __init__(self , master , width  , height , ) -> None:
        self.main_page  = tk.Tk() # Will change this later with the master 
        # getting the data from calling the class
        self.width = width
        self.height  = height
        # Setting up the data for the app functioning 
        self.x_location  = (self.main_page.winfo_screenwidth() // 2 ) - (self.width // 2)
        self.y_location   = (self.main_page.winfo_screenheight() // 2) - (self.height // 2)

        # Geometry and other theme for the application : 
        self.main_page.geometry(f'{width}x{height}+{self.x_location}+{self.y_location}')


        # Setting up the controls


        # Configuring the controls
        self.main_page.configure(background=colors.app_base)


        # Binding the controls : 
        # self.main_page.bind("<Enter>" , self.main_name)



        # Calling main App : 
        self.main_page.mainloop()
        # self.regular_animation() # This will run after running the main app
        

    def main_name(self , event):
        print("I am Called from inside the class")
        print(event)

    def regular_animation(self  ): # Will be using this function to check for the App maximize and setting upo some animations. ( also min and max button )
        print(" I am being called again and again")
        self.main_page.after(5000 , self.regular_animation)



if __name__ == '__main__':
    main_app = main_page('master' , 300 ,500)
