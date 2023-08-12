import tkinter as tk  
import tkinter.ttk as ttk 
import customtkinter as ctk 






class right_sidebar_controls():

    # There will be two stages for the application : Intial Stage and Invoke Stage 

    def __init__(self ,master , curent_task , time_taken ) -> None:
        self.master = tk.Tk()  # Will be used to paste the controls  and this will be used for the other controls
        ## Will check the current height of the control
        self.master_height = self.master.winfo_height()
        self.master_width  = self.master.winfo_width()


        self.timer_frame = tk.Frame(self.master_width , height=self.master_height  * 0.8 , width=self.master_width)

        

        


    