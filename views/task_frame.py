import tkinter as tk 
from tkinter import ttk
import ttkbootstrap as btk

from ttkbootstrap.scrolled import ScrolledFrame as scrolled_frame
from ttkbootstrap.dialogs import Messagebox
from pubsub import pub



class Task():
    
    
    def focus_out (self ,  control):
        print("done and done")
    
    def control_added(self , e , control):
        self.start_stop_button  = btk.Button(control , text=self.play_icon)
        self.start_stop_button.pack(side=tk.RIGHT)
        control.bind("<FocusOut>" , lambda e : self.start_stop_button.destroy())
        self.start_stop_button.bind("<Leave>" , lambda e : control.focus())
        
        
        
        
    
    def __init__(self ,master  , width  = 470 , height  = 50) -> None:
        self.master  = master
        self.height = height
        self.width = width
        
        self.check_var  = btk.IntVar()
        self.check_var.set(0)
        
        self.play_icon   = '\u25B6'
        self.stop_icon  = '\u23F9'
        
    
        self.main_frame   = btk.Frame(self.master  , height=self.height , width = self.width )
        self.main_check = btk.Checkbutton(self.main_frame , variable=self.check_var)
        self.enter_text = btk.Entry(self.main_frame , width=450)
        
        # Configure Controls :
        # self.main_frame.pack_propagate(0)
        self.check_var.set(0)
        self.enter_text.pack_propagate(0)
        
        # Binding Controls :
        self.enter_text.bind("<FocusIn>" , lambda e : self.control_added(e=e , control=self.enter_text))
        # self.enter_text.bind("<Leave>" , lambda e  : self.enter_text.icursor(0)) # sets teh cursor to the beginning 
        self.enter_text.bind("<Leave>"  , lambda e: self.enter_text.xview_moveto(0))
        self.enter_text.bind("<Enter>"  , lambda e: self.enter_text.xview_moveto(1))
        self.enter_text.bind("<Shift-Return>"  , lambda e: self.enter_text.xview_moveto(1))
        
        
        
        # self.enter_text.bind("<Shift-Return>" , lambda e : pub.sendMessage('shift'))
        # self.enter_text.bind("<Escape>" , lambda e : pub.sendMessage('escape'))
        
        
        # self.enter_text.bind("<Shift-Return>", lambda e : Task_Frame.add_data(self))
        # self.enter_text.bind("<Escape>" , lambda e : self.main_frame.focus())
        
        self.main_frame.pack(padx=(0 , 5))
        self.main_check.pack(side=tk.LEFT , padx=(5, 0), pady=0 )
        self.enter_text.pack(side=tk.LEFT)
        

class Task_Frame():
    
    
    def add_data(self):
        
        empty_data = any(text_element.enter_text.get() == "" for text_element in self.task_manager)
        if empty_data == True:
            Messagebox.show_error("Task Data Cannot Be Empty !! Enter Task Data" , "Time Logger")
        else:
            self.add_button.destroy()
            task  = Task(self.scroll_frame)
            self.task_manager.append(task)
            self.add_button = btk.Button(self.scroll_frame , text="+" , bootstyle  = 'primary' , command=self.add_data)
            self.add_button.pack(side=tk.RIGHT , anchor='ne' , padx=10 , pady=10)
            task.enter_text.focus()
            task.enter_text.bind("<Escape>" , lambda e : task.main_frame.focus())
            task.enter_text.bind("<Shift-Return>" , lambda e : self.add_data())
            


    
    
    def __init__(self , master   , width = 480 ,  height = 460) -> None:
        self.master  = master 
        self.width  = width
        self.height  = height
        
        self.task_manager  = []
        self.entry_manager_count  = 0
        
        self.button_style  = btk.Style()
        self.button_style.configure('custom.TButton' ,background=  '#303030')
        
        self.main_frame  = btk.Frame(self.master , width=self.width , height=self.height , bootstyle  = 'info')
        self.scroll_frame  = scrolled_frame(self.main_frame , autohide=True , bootstyle='flatly')
        
        
        # Adding  + button for adding controls and button would shift downside with each control added  : 
        self.add_button = btk.Button(self.scroll_frame , text="+" ,command=self.add_data ,bootstyle  = 'primary')
        
        # Configuring Controls : 
        self.main_frame.pack_propagate(0)
        
        # Binding Controls : 
        self.add_button.bind("<Leave>" , lambda e : self.main_frame.focus())
        
        
        
        
        # Packing Controls :
        self.main_frame.pack()
        self.scroll_frame.pack(fill=tk.BOTH , expand=True)
        self.add_button.pack(side=tk.RIGHT , anchor='ne' , padx=10 , pady=10)
        pub.subscribe(self.add_data , 'shift')
        



if __name__ == '__main__':
    main_window  = btk.Window()
    
    Task_Frame(main_window)
    # Task(main_window)
    
    main_window.mainloop()
        
