import tkinter as tk
from tkinter import ttk


class Settings():

    def __init__(self , width , height , master) -> None:
        self.settings  = master
        self.width  = width 
        self.height  = height

        # Defining the Controls : 
        self.main_frame  = tk.Frame(self.settings , width  = self.width , height  = self.height , background="gray")
        self.main_frame.pack_propagate(0)
        
        # Setting variables for multiple variables : 
        self.current_themes = ["black" , "green" , "blue"]
        self.font_size  = ["Font_1" , "Font_2" , "Font_3"]
        # setting up the combobox for the themes , font size , auto save at reload switch and grouping for the tags 
        



        # Packing the controls  : 
        self.main_frame.pack()
        self.settings.mainloop()

    def destroy_everything(self):
        self.settings.destroy()



if __name__ == '__main__':
    main = Settings(500 ,500 , tk.Tk())
