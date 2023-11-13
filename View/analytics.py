import tkinter as tk




class Analytics():


    def __init__(self , width , height , master ) -> None:
        self.settings_app = tk.Tk()
        self.width = width 
        self.height = height
        
        # Defining the Controls : 
        self.first_frame  =tk.Frame(self.settings_app ,self.width , self.height)
        self.first_frame.pack_propagate(0)
        self.first_frame.configure(background="yellow")

        self.first_frame.pack()
        self.first_frame.pack_forget()

        self.settings_app.mainloop()