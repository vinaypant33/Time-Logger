import tkinter as tk
from tkinter import ttk
import customtkinter as ctk


from pubsub import pub  






class TaskAdd():
    """
    This will be the main class and all the controls will be added with this class

    """

    def text_update(self , event):
        self.current_text = self.current_text_title.get()
        if len(self.current_text) + 1 <= 0:
            print("length cannot be less than ")

    def open_top_form(self , event ,  current_text):
        Top_Control(x_location=self.placement_x , y_location=self.placement_y , current_text=current_text)



    def add_task(self ):
        self.each_task  = ctk.CTkFrame(self.scrollable_frame , width=self.scrollable_frame.winfo_width() , height=30  ,corner_radius=0)
        self.each_task.pack_propagate(0)
        self.checkbox  = ctk.CTkCheckBox(self.each_task , text="" , border_width=1  , height=1 , width=1 , corner_radius=0)
        self.current_text_title  = ctk.CTkEntry(self.each_task , placeholder_text="Enter Task" ,  border_width=1 , corner_radius=1 , width=200)
        self.default_timer = ctk.CTkLabel(self.each_task , text="00:00:00" , font=("Arial" , 18 , "bold"))
        self.current_text = self.current_text_title.get()
        self.current_text_title.focus_force()
        self.current_text_title.bind('<KeyPress>' , lambda event : self.text_update(event))
        self.current_text_title.bind('<Double-1>' , lambda event: self.open_top_form(event , current_text=self.current_text))

        # self.current_text_title.configure(text = current_text)
        # self.current_text_title.insert( 0 )
        self.progress_bar  = ctk.CTkProgressBar(self.each_task , border_color="black" , corner_radius=0 , border_width=0 , height=15)
        # self.progress_bar.configure()
        self.progress_bar.set(value=0)
        self.progress_bar["minimum"] = 0
        self.progress_bar["maximum"] = 100
        self.start_stop_button  = ctk.CTkButton(self.each_task , text="\u25B6" , corner_radius=0 , border_width=0 , width = 25)
        self.checkbox.pack(padx = 1 , side = "left" , anchor = "w")
        self.current_text_title.pack(side = "left" , padx = 3 , anchor = "w")
        self.default_timer.pack(side = "left" , padx = 3 , anchor = "w")
        self.progress_bar.pack(side = "left" , padx = 3 , anchor  = "w")
        self.each_task.pack(padx=2 , pady = 5)
        self.start_stop_button.pack(side = "left" , anchor = "w" , padx = (5 , 0))



    def count_change(self ,current_text):
        self.count = 0 # The form count is added to the last and the text would be added in the main form  : 
        self.each_task  = ctk.CTkFrame(self.scrollable_frame , width=self.scrollable_frame.winfo_width() , height=30  ,corner_radius=0)
        self.each_task.pack_propagate(0)
        self.checkbox  = ctk.CTkCheckBox(self.each_task , text="" , border_width=1  , height=1 , width=1 , corner_radius=0)
        self.current_text_title  = ctk.CTkEntry(self.each_task , placeholder_text="Enter Task" ,  border_width=1 , corner_radius=1 , width=200)
        self.default_timer = ctk.CTkLabel(self.each_task , text="00:00:00" , font=("Arial" , 18 , "bold"))
        # self.current_text_title.configure(text = current_text)
        self.current_text_title.insert( 0 , current_text)
        self.progress_bar  = ctk.CTkProgressBar(self.each_task , border_color="black" , corner_radius=0 , border_width=0 , height=15)
        # self.progress_bar.configure()
        self.progress_bar.set(value=0)
        self.progress_bar["minimum"] = 0
        self.progress_bar["maximum"] = 100
        self.start_stop_button  = ctk.CTkButton(self.each_task , text="\u25B6" , corner_radius=0 , border_width=0 , width = 25)
    
        self.checkbox.pack(padx = 1 , side = "left" , anchor = "w")
        self.current_text_title.pack(side = "left" , padx = 1 , anchor = "w")
        self.default_timer.pack(side = "left" , padx = 1 , anchor = "w")
        self.progress_bar.pack(side = "left" , padx = 1 , anchor  = "w")
        self.each_task.pack(padx=2 , pady = 5)
        self.start_stop_button.pack(side = "left" , anchor = "w" , padx = (15 , 0))



    def add_button_clicked(self): # this function to be used later for now usign this func in the double click scenario 
        # To check if the top level is called once
        self.count+=1
        if self.count > 1:
            print("One Form is Already Open - Close the open form first")
        else:
            current_x  = self.master.winfo_x()
            current_y = self.master.winfo_y()
            print(current_x)
            Top_Control(x_location=current_x , y_location=current_y)

     



    def __init__(self , master , width , height) -> None:
        self.master = master
        self.width  = width
        self.height  = height
        self.count  = 0


        self.placement_x = self.master.winfo_x()
        self.placement_y = self.master.winfo_y()

      
      
         # Sets the appearance mode of the application
        ctk.set_appearance_mode("dark")        # System and light are available
        # Supported themes: green, dark-blue, blue # Sets the color of the widget
        ctk.set_default_color_theme("blue")
        # Controls for the main task app :
        # Container for the main app 
        self.task_frame  = ctk.CTkFrame(self.master , height=self.height , width=self.width , corner_radius=0  , border_width=1 , fg_color="#333333" )
        self.task_frame.pack_propagate(0)
        # Add Button it will show the top level app which will in turn allow to add text controls : 
        self.add_button  = ctk.CTkButton(self.task_frame , text="+" , width=40 , corner_radius=0 , command=self.add_task , fg_color="#202020" )
        # Scrollable frame : This will be the container for the main application and the tasks would be added in here : 
        self.scrollable_frame  = ctk.CTkScrollableFrame(self.task_frame , height=self.height -30 , width=self.width , corner_radius=0 )
        # Subscribing from the pbsub and checking messageboxes :
        pub.subscribe(self.count_change,"closing")
        pub.subscribe(self.count_change , "enterpressed")
        self.task_frame.pack()
        self.add_button.pack(anchor = "ne" , padx = 5 , pady = 5)
        self.scrollable_frame.pack()





class Top_Control(TaskAdd):

    def on_close(self , event ):
        # This function is executed when each widget inside the top level is being destroyed
        if event.widget == self.main_app:
            # self.current_text  = self.task_name.get()
            pub.sendMessage("closing" , current_text  = self.current_text)
            
    
    def return_pressed(self ,event):
        pub.sendMessage("enterpressed" , current_text = self.current_text)
        self.task_name.delete( 0 ,tk.END)


    def temporary_function(self):
        print(self.task_name.get())

    def text_update(self):
        self.current_text  = self.task_name.get()
        


    def __init__(self , master = None , width  = 450 , height  = 400, x_location = 0, y_location  = 0 , count  = 1 , current_text = "Enter Task") -> None:

       
        self.master = master
        self.width = width
        self.height  = height
        self.x = x_location
        self.y = y_location
       
        self.current_text = current_text
        # self.y = self.y - self.master.winfo_height() // 2

        
        # Calling the main top level and to be closed
        self.main_app  = ctk.CTkToplevel()

  
        self.main_app.resizable(0 , 0)
        self.main_app.attributes("-topmost" , True)
        self.main_app.title("Log Timer")
        self.x = (self.main_app.winfo_screenwidth() //2 ) - (self.main_app.winfo_width() //2)
        self.y = (self.main_app.winfo_screenheight() //2) - (self.main_app.winfo_height() // 2)
        self.main_app.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}") # This to be changed to the location of x and y

        # Setting up the controls for the top level :
        self.task_name  = ctk.CTkEntry(self.main_app  , border_color="grey" , corner_radius=0 , border_width=1)
        self.task_name.insert(0 , self.current_text)
        self.grid_frame = ctk.CTkScrollableFrame(self.main_app , corner_radius=0)
        self.comment_box  = ctk.CTkTextbox(self.grid_frame , corner_radius=0 , width=300 )
        self.comment_box_button  = ctk.CTkButton(self.grid_frame, text="Add Comment" , corner_radius= 0 , fg_color="#333333" , width  = 300)
        self.checklist_button  = ctk.CTkButton(self.grid_frame ,text = "Checklist" , corner_radius=0 , command=self.temporary_function , width = 90 , fg_color="#333333")

        """ 
        Function to define that would add checklist in the main app scrollbar and the color scheme to be changed as well : 
        """

        ## Binding the controls : 
        self.current_text  = self.task_name.get()
        self.task_name.bind('<KeyPress>' , lambda event : self.text_update())
        # self.main_app.bind("<Destroy>" , lambda event: self.on_close(event))    # Will solve this later and to make sure the text works in closing the form 
        self.task_name.bind("<Return>" , lambda event  :  self.return_pressed(event))


        # Placing the controls in the main app : 
        self.task_name.pack(fill = "x" , padx = 5)
        self.grid_frame.pack(side = "top" , anchor=  "w" , fill="both" , expand = True , pady = 10)
        self.comment_box.grid( row = 0 , column  = 0 , columnspan  = 16 , rowspan = 16)
        self.comment_box_button.grid(row = 17 , column  = 0 , pady = 10 )
        self.checklist_button.grid(row = 0 , column = 18 , padx = 25)







if __name__ == "__main__":

    window = ctk.CTk()
    window.resizable(0 , 0 )
    TaskAdd(window , 600 , 600)

    window.mainloop()