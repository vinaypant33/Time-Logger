import tkinter as tk 
from tkinter import ttk
import ttkbootstrap as btk

from ttkbootstrap.scrolled import ScrolledFrame as scrolled_frame





class Task():
    
    
    def focus_out (self ,  control):
        print("done and done")
    
    def control_added(self , e , control):
        self.start_stop_button  = btk.Button(control , text=self.play_icon)
        self.start_stop_button.pack(side=tk.RIGHT)
        control.bind("<FocusOut>" , lambda e : self.start_stop_button.destroy())
        self.start_stop_button.bind("<Leave>" , lambda e : control.focus())
        
        
        
    
    def __init__(self ,master  , width  = 470 , height  = 100) -> None:
        self.master  = master
        self.height = height
        self.width = width
        
        self.check_var  = btk.IntVar()
        self.check_var.set(0)
        
        self.play_icon   = '\u25B6'
        self.stop_icon  = '\u23F9'
        

        self.main_frame   = btk.Frame(self.master  , height=self.height , width = self.width , bootstyle  ='danger')
        self.main_check = btk.Checkbutton(self.main_frame , variable=self.check_var)
        self.enter_text = btk.Entry(self.main_frame , width=450)
        
        
        

        
        # Configure Controls :
        self.main_frame.pack_propagate(0)
        self.check_var.set(0)
        self.enter_text.pack_propagate(0)
        
        # Binding Controls :
        self.enter_text.bind("<FocusIn>" , lambda e : self.control_added(e=e , control=self.enter_text))
        self.enter_text.bind("<FocusOut>" , lambda e  : print("done and called"))
        
        
        
        self.main_frame.pack()
        self.main_check.pack(side=tk.LEFT , padx=(5, 0), pady=0 )
        self.enter_text.pack(side=tk.LEFT)
        

class Task_Frame():
    
    
    def add_data(self):
        pass
    
    
    def __init__(self , master   , width = 480 ,  height = 460) -> None:
        self.master  = master 
        self.width  = width
        self.height  = height
        
        
        self.main_frame  = btk.Frame(self.master , width=self.width , height=self.height , bootstyle  = 'info')
        self.scroll_frame  = scrolled_frame(self.main_frame , autohide=True , bootstyle='flatly')
        
        
        # Adding  + button for adding controls and button would shift downside with each control added  : 
        self.add_button = btk.Button(self.scroll_frame , text="+" , bootstyle  = 'darkly')
        
        # Configuring Controls : 
        self.main_frame.pack_propagate(0)
        
        # Binding Controls : 
        self.add_button.bind("<Leave>" , lambda e : self.main_frame.focus())
        
        
        
        # Packing Controls :
        self.main_frame.pack()
        self.scroll_frame.pack(fill=tk.BOTH , expand=True)
        self.add_button.pack(side=tk.RIGHT , anchor='ne' , padx=10 , pady=10)
        



if __name__ == '__main__':
    main_window  = btk.Window()
    
    # Task_Frame(main_window)
    Task(main_window)
    
    main_window.mainloop()
        
