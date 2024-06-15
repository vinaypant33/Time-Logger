import tkinter as tk
from tkinter import ttk
import ttkbootstrap as btk
from tkinter import messagebox




class TaskList():

    

    def adding_tasklist(self):
        print("I am called")
        self.progressstyle = ttk.Style()
        self.progressstyle.configure("Thick.TProgressbar", thickness=20)
        self.task_frame = btk.Frame(self.controls_frame , width=900 , height=135 ,bootstyle = "success")
        self.task_frame.pack_propagate(0)
        self.check_var = btk.BooleanVar(value=False)
        # self.check_var.set(False)

        self.taskcheckbutton  = btk.Checkbutton(self.task_frame , variable=self.check_var)
        self.task_entry = btk.Entry(self.task_frame , width=40 )
        self.timer_text  = btk.Label(self.task_frame , text="00:00:00" , font = ("satoshi" , 12, "bold"))
        self.progressbar  = btk.Progressbar(self.task_frame , style = "Thick.TProgressbar" )

        self.start_stop_button  = btk.Button(self.task_frame , text='\u23F8' , width=1) # '\u23F8' "\u25B6"

        self.task_frame.pack()
        self.taskcheckbutton.pack(side=tk.LEFT)
        self.task_entry.pack(side=tk.LEFT ,padx =(5,0))
        self.timer_text.pack(side=tk.LEFT , padx=(5,0))
        self.progressbar.pack(side=tk.LEFT , padx =(5,0))
        self.start_stop_button.pack(side=tk.RIGHT , padx=(3,5))

        self.main_canvas.update_idletasks()
        self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))


    def add_controls(self):

        self.temp_frame  = btk.Frame(self.controls_frame , height=200 , width=self.width , bootstyle  = "info")
        self.temp_frame.pack(padx=10 , pady=10)
        self.main_canvas.update_idletasks()
        self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))

    '''
    Main class other forms / classes would be called from this class
    '''


    def __init__(self ,master ,  width  = 500 , height  = 600) -> None:
        # Defining Base Controls :
        self.main_app  = master
        self.height  = height
        self.width   = width 
        self.frame_height = 250

        # Setting up the canvas for the main frame  : 
        self.main_canvas = tk.Canvas(self.main_app , background="red")
        self.scrollbar  = ttk.Scrollbar(self.main_app, orient=tk.VERTICAL , command=self.main_canvas.yview)
        self.controls_frame = ttk.Frame(self.main_canvas)
        ##############-----------Main Controls------------------------##################
        self.add_button  = btk.Button(self.main_app , text="Add Frame" , command=self.adding_tasklist)
        ####-------------------Configuring the contros-----------------#######
        self.main_canvas.configure(yscrollcommand=self.scrollbar.set)
        #####------------------Binding the Controls-----------------------######
        self.main_canvas.bind('<Configure>' , lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all")))
        # self.bottom_frame.bind('<MouseWheel>' , lambda e :self.main_canvas.yview_scroll(-1 * int((e.delta / 120)), "units"))
        self.controls_frame.bind("<Enter>" , lambda e : self.adding_tasklist)
        self.main_canvas.create_window((0,0) , window=self.controls_frame ,anchor="nw")
        ######------------------Packing the controls------------------------######
    
        self.main_canvas.pack(side=tk.LEFT , fill=tk.BOTH , expand=1)
        # self.controls_frame.pack()
        self.scrollbar.pack(side=tk.RIGHT , fill=tk.Y)
        self.add_button.pack(side=tk.BOTTOM, pady=10 , padx=10 , anchor="se")

        print(self.controls_frame.winfo_width())
        print(self.controls_frame.winfo_height())


    


if __name__ == '__main__':
   window  = btk.Window()
   TaskList(window)
   window.mainloop()