import tkinter as tk
import ttkbootstrap as btk 






class Tab_app():


    def toggle_switch(self):
        current_text  = self.theme_label.cget("text")

        if current_text == "Dark":
            self.theme_label.configure(text="Light")
        elif current_text == "Light":
            self.theme_label.configure(text="Dark")


    def __init__(self , width  , height ) -> None:


        
        self.side_ratio  = .20
        self.current_ratio  = 1 - self.side_ratio

        self.height = height
        self.width  = width



        self.tab_based_app   = btk.Window(themename="darkly") # Themes available darkly cyborg and minty cosmo flatly and litera 
        
        self.tab_based_app.title("Log Timer")
        self.tab_based_app.resizable(0 , 0)

        # Make the app in the center of the screen :
        self.x_location  = (self.tab_based_app.winfo_screenwidth() //2 ) - (self.width //2)
        self.y_location  = (self.tab_based_app.winfo_screenheight() //2 ) - (self.height //2 )
        self.tab_based_app.geometry(f"{self.width}x{self.height}+{self.x_location}+{self.y_location}")
        
        self.sidebar = btk.Frame(master=self.tab_based_app , height=(self.height*1) , width=(self.width*self.side_ratio) )
        self.sidebar.pack_propagate(0)


        self.main_frame  = btk.Frame(master=self.tab_based_app , height=self.height*1 , width=(self.width*self.current_ratio) , bootstyle  = "success")
        
        
        self.settings_frame  = btk.Frame(master=self.sidebar ,  height=100 , width=100)
        self.settings_frame.pack_propagate(0)

        self.theme_label  = btk.Label(master=self.settings_frame , text="Light")
        self.dark_light_switch  = btk.Checkbutton(master=self.settings_frame,bootstyle="square-toggle" , command=self.toggle_switch )

        # will add icon for the main app later : with the currnet image : 




     
        







        ###--- Placing Controls -----------###
        self.sidebar.pack(side="left")

        self.main_frame.pack()

        self.settings_frame.pack(side="bottom" , anchor="center" , fill="x")
        # self.theme_label.pack(side="bottom" , anchor="w")
        # self.dark_light_switch.pack(side="bottom" ,  anchor="e" )
        self.theme_label.grid(row=0 , column=0 , columnspan=1 , sticky=tk.W , padx=1)
        self.dark_light_switch.grid(row = 0 , column=1 , columnspan=2 , sticky=tk.E , padx=3)
        self.settings_frame.rowconfigure(0 , weight=1)
        # self.settings_frame.columnconfigure(2 , weight=1)
        # self.theme_label.grid(row = 0 , column=0 , rowspan=10)

        # self.theme_label.place(x = 30 , y = 400)








    def call_app(self):

        self.tab_based_app.mainloop()



if __name__ == "__main__":
    hello = Tab_app(400 , 500)
    hello.call_app()

