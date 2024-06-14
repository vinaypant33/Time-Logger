import tkinter as tk 
from tkinter import ttk
import ttkbootstrap as btk 





class SpinBox():

    def __init__(self , master , height  = 400 , width  = 200) -> None:
        self.master = master
        self.height  = height
        self.width  = width 


        self.main_frame  = btk.Frame(self.master , height=100 , width=149 , bootstyle  = "warning")
        self.main_frame.pack_propagate(0)

        self.side_frame  = btk.Frame(self.main_frame , height=100 , width=self.width *.6 , bootstyle  = "info")
        self.side_frame.pack_propagate(0)
        self.main_text = btk.Label(self.side_frame , text="00" , font=("Arial", 20)) # This frame and the fonts and font size and font type is required 
        self.add_button = btk.Button(self.main_frame , text="+"  ) 
        self.subtract_button  = btk.Button(self.main_frame , text="-"  )

        self.no_breaks_text  = btk.Label(self.master , text="No breaks in focus session !!" )

        ## setting the focus session button with the play and pause Image : 

        



        
        self.main_frame.pack(padx = 50 , pady = 50)
        self.side_frame.pack(side = "left")
        self.main_text.pack()
        self.main_text.place(x = 19 , y = 35)
        self.add_button.pack(side = "top")
        self.subtract_button.pack(side = "bottom")

        self.no_breaks_text.place(x = 25 , y =150)



        self.main_frame.pack()




if __name__ =='__main__':

    main = btk.Window()
    SpinBox(main)

    main.mainloop()