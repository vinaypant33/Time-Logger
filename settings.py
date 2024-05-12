import tkinter as tk 
from tkinter import ttk
import customtkinter as ctk
import ttkbootstrap as btk 





class Settings():


    def __init__(self , master , x_location, y_location ,  height  , width , theme) -> None:
        self.master  =btk.Window(themename=theme)
        self.master.resizable(0 , 0)
        self.master.geometry(f"{width}x{height}+{x_location}+{y_location}")



        self.master.mainloop()




if __name__ == "__main__":
    main_window  = Settings(100 , 100 , 200 , 200 ,300 , "darkly")
    

