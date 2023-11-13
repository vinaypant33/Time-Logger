import tkinter as tk
from tkinter import ttk
import colors
import fonts 
import messagebox
import styles

class Home():

    def check_word_limit(self , event ):
        if len(self.entrybox.get()) > 100:
            print("I am exceeded")

    def adding_data(self):
        if len(self.entrybox.get()) > 0:
            self.currnet_string = self.entrybox.get()
            self.external_messagebox  = entry_box(self.master_frame , self.currnet_string , self.current_index)
            self.current_index+=1
            self.currnet_string = ""
            self.entrybox.delete(0  ,tk.END)
            self.master_frame.configure()
        else:
            x_location  = self.home_page.winfo_x() + self.home_page.winfo_width() // 2
            y_location  = self.home_page.winfo_y() + self.home_page.winfo_height() //2
            messagebox.Messagebox(x_location  , y_location  , "No Task is added : Please enter the text")

    def adding_enter_data(self , event):
        if len(self.entrybox.get()) > 0:
            self.currnet_string = self.entrybox.get()
            self.external_messagebox  = entry_box(self.master_frame , self.currnet_string , self.current_index)
            self.current_index+=1
            self.currnet_string = ""
            self.entrybox.delete(0  ,tk.END)
            self.master_frame.configure()
        else:
            x_location  = self.home_page.winfo_x() + self.home_page.winfo_width() // 2
            y_location  = self.home_page.winfo_y() + self.home_page.winfo_height() //2
            messagebox.Messagebox(x_location  , y_location  , "No Task is added : Please enter the text")
        

    def __init__(self , width  , height , master ) -> None:
        self.home_page = master
        # Temporary Code to check every thign 
        # self.home_page.configure(background = "red")
        self.width  = width  
        self.height = height 
        # self.home_page.geometry(f"{self.width}x{self.height}")
        self.word_limit  = 40
        self.currnet_string  = "" # This will be changed each time a new text is added in the the textbox
        self.current_index  = 0
        self.is_added  = False

        # For the text boxes and other controls  : 
    def adding_controls(self):
        self.textbox_frame  = tk.Frame(self.home_page , height= 30 , width = self.width )
        self.textbox_frame.pack_propagate(0)
        self.master_frame = tk.Frame(self.home_page ,  height  = self.height , width= self.width )
        self.master_frame.pack_propagate(0) # Will check this and make the app visible in here
        self.added_text_frame  = tk.Frame(self.home_page ,   width=self.width )
        # Entry box and the button within the frame : 
        self.entrybox  = tk.Entry(self.textbox_frame ,width  =35 ,   font = fonts.small_font_bold )
        self.add_button  = tk.Button(self.textbox_frame , text="Add Task" , command=self.adding_data)
        self.scroll = ttk.Scrollbar(self.master_frame , orient="vertical" )
        
        # Configuring the controls :
        styles.styles.button_styles(self.add_button , colors.app_base , colors.White, colors.Red , colors.dark_black)
        self.entrybox.configure(bd= 0 , relief="sunken")
        # Binding the controls : 
        self.entrybox.bind("<KeyPress>" , self.check_word_limit)
        self.entrybox.bind('<Return>' , self.adding_enter_data)
        # packing the controls
        # packing frames : 
        self.textbox_frame.pack(side='top' , padx =1 , pady=1 )
        self.added_text_frame.pack(side='top' , padx=1 , pady=1)
        self.entrybox.pack(side='left',padx=5)
        self.add_button.pack(side='right',  padx=5)
        self.scroll.pack(side="right" , fill="y")
        self.master_frame.pack()

        self.home_page.mainloop()

    def destroy_everything(self):
        self.textbox_frame.destroy()
        self.master_frame.destroy()
        self.added_text_frame.destroy()
        self.entrybox.destroy()
        self.add_button.destroy()
        self.scroll.destroy()
        self.home_page.destroy()

    

class entry_box():

    def __init__(self , master ,current_text  , current_index) -> None:
        self.master  = master
        self.current_index  = current_index
        self.current_text  =current_text
        # Defining and adding control 
        self.text  = tk.Text(self.master , height=2 , font = fonts.small_font_bold)
        self.text.insert(tk.END , self.current_text)
        self.text.configure(state="disabled")
        self.text.pack(padx=5 , pady=5)




if __name__ == '__main__':
    main_home  = Home(400 , 400 , tk.Tk())
    if main_home.is_added == False: 
        main_home.adding_controls()
        main_home.is_added = True
    