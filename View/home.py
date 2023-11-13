import tkinter as tk
from tkinter import ttk
import colors
import fonts 
import styles
import messagebox
import time

class Home():

    # def check_word_limit(self , event ):
    #     if len(self.entrybox.get()) > 100:
    #         print("I am exceeded")

    # def adding_data(self ):
    #     if len(self.entrybox.get()) > 0:
    #         self.currnet_string = self.entrybox.get()
    #         self.external_messagebox  = entry_box(self.controls_frame , self.currnet_string , self.current_index)
    #         self.current_index+=1
    #         # self.main_entry_box.insert(tk.END , self.currnet_string)
    #         self.currnet_string = ""
    #         self.entrybox.delete(0  ,tk.END)
    #         self.master_frame.configure()
    #     else : 
    #         self.entrybox.delete(0  ,tk.END)
    #         messagebox.Messagebox((self.home_page.winfo_x())  + (self.home_page.winfo_width() //2 ) , (self.home_page.winfo_y())  + (self.home_page.winfo_height() //2 ) , "Please Enter the Task Name")
            
        

        
    # def enter_adding_data(self , event ) : # This will be deleted later and will make a single function for adding the text.
    #     if len(self.entrybox.get()) > 0 :
    #         self.currnet_string = self.entrybox.get()
    #         self.external_messagebox  = entry_box(self.controls_frame , self.currnet_string , self.current_index)
    #         self.current_index+=1
    #         # self.main_entry_box.insert(tk.END , self.currnet_string)
    #         self.currnet_string = ""
    #         self.entrybox.delete(0  ,tk.END)
    #         self.master_frame.configure()
    #     else:
    #         self.entrybox.delete(0  ,tk.END)
    #         messagebox.Messagebox((self.home_page.winfo_x())+ (self.home_page.winfo_width() //2) , self.home_page.winfo_y() + (self.home_page.winfo_height() //2 ) , "Empty Message : Please Enter the Message")

    

    def __init__(self , width  , height , master ) -> None:
        self.home_page  = master
        self.width  = width 
        self.height  = height 
        self.word_limit  = 100 
        self.currnet_string = ""
        self.current_index  = 0
        self.is_added  = False
    
    def adding_controls(self):
        self.master_frame  = tk.Frame(self.home_page , height= self.height , width =self.width , background='red')
        self.textbox_frame   = tk.Frame(self.master_frame , height=30 , width=self.width , background='yellow')
       
        self.canvas  = tk.Canvas(self.master_frame , height=self.height , background='green')
        self.control_frame  = tk.Frame(self.canvas , height=self.height , width=self.width , background=colors.Dark_Burgundy)
        self.scrollbar = ttk.Scrollbar(self.master_frame , orient="vertical" , command=self.canvas.yview) 
        for them in range (30):
            self.button = tk.Button(self.control_frame , text="Button").pack()
        # Configuring the controls  :
        self.master_frame.pack_propagate(0)
        self.textbox_frame.pack_propagate(0)
        # self.canvas_frame.pack_propagate(0)
        # self.control_frame.pack_propagate(0)

        # Setting up the canvas for the main controls :
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.canvas.create_window((0,0) , window=self.control_frame ,anchor="nw")
        self.control_frame.bind("<Configure>" , lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        # Packing the controls :
        self.master_frame.pack(side="top" , fill="both")
        self.textbox_frame.pack(side="top" , padx=5 , pady=2)
        self.scrollbar.pack(side="right" , fill="y")
        self.canvas.pack(side="top" , fill="both")
        self.control_frame.pack(side="top" , fill="both")
        # Calling the main loop :
        self.home_page.mainloop()

if __name__ == '__main__':
    main_home  = Home(400 , 400 , tk.Tk())
    if main_home.is_added == False: 
        main_home.adding_controls()
        main_home.is_added = True
    