import tkinter as tk 
from tkinter import ttk
import customtkinter as ctk
import ttkbootstrap as btk 





class Settings():

    def light_dark_theme(self):
        if self.checkbox.cget("text") == "Light":
            self.checkbox.config(text="Dark")
            return "Dark"
        else:
            self.checkbox.config(text="Light")
            return "Light"
        
    


    def __init__(self , master) -> None:
        self.master  = master
        # self.master.resizable(0 , 0)
        # self.master.geometry(f"{width}x{height}+{x_location}+{y_location}")

        # Make the controls for the settings : 
        '''
        switch box and checkbox for the dark and light settings : 
        '''
        self.theme_label = btk.Label(master=master ,  text="Choose Theme : Dark / Light")
        self.checkbox  = btk.Checkbutton(master=self.master , text="Light",bootstyle="square-toggle" , width=100 , command=self.light_dark_theme)





        self.theme_label.place(x = 10 , y = 10)
        self.checkbox.place(x = 10 , y = 50)


        # self.master.mainloop()




if __name__ == "__main__":
    main_window  = Settings()
    

