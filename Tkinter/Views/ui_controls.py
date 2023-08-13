import tkinter as tk  
import tkinter.ttk as ttk 
import customtkinter as ctk 






class right_sidebar_controls():

    # There will be two stages for the application : Intial Stage and Invoke Stage 

    def __init__(self) -> None:  # Make 3 attributes for master current task time taken 
        self.master = tk.Tk()  # Will be used to paste the controls  and this will be used for the other controls
        self.master.geometry("300x400")
        
        ## Will check the current height of the control
        # self.master_height = self.master.winfo_height()
        # self.master_width  = self.master.winfo_width()

        self.master_height = 400 # Using this a s temporary width height and later will cange the same to the amster control
        self.master_width  = 300

        # Setting up the Base Controls  : 

        self.timer_frame  = tk.Frame(self.master , width=self.master_width* 0.9, height=self.master_height * 0.9 , background="red")
        self.timer_frame.pack_propagate(0)
        
        # Making the dumy canvas and making it transparent for the app
        self.main_canvas  = tk.Canvas(self.timer_frame , height=self.master_height * 0.6 , width=self.master_width * 0.9 , bd=1 , bg="green")

        coord = 0, 0, 360, 360
        self.arc = self.main_canvas.create_oval(50 , 50 ,200,200) # Check for the same and make the minute and hour hand with the diff colors maybe by the dots which will be placed 
        
        self.master.after(5000 , self.clear_canvas)
        
        ## Packing the main controls and calling the main app 
        self.timer_frame.pack()
        self.main_canvas.pack()
        self.master.mainloop()


    def clear_canvas(self):
        self.main_canvas.delete('all')
    
    def delete_all(self):
        self.master.destroy()



if __name__ == '__main__':
    sidebar_check  = right_sidebar_controls()



        

        


    