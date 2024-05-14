import ttkbootstrap as btk 






class Tab_app():


    def __init__(self , width  , height ) -> None:
        self.height = height
        self.width  = width



        self.tab_based_app   = btk.Window() # Themes available darkly cyborg and minty cosmo flatly and litera 
        
        self.tab_based_app.title("Log Timer")
        self.tab_based_app.resizable(0 , 0)

        # Make the app in the center of the screen :
        self.x_location  = (self.tab_based_app.winfo_screenwidth() //2 ) - (self.width //2)
        self.y_location  = (self.tab_based_app.winfo_screenheight() //2 ) - (self.height //2 )
        self.tab_based_app.geometry(f"{self.width}x{self.height}+{self.x_location}+{self.y_location}")

        self.sidebar = btk.Frame()












    def call_app(self):
        self.tab_based_app.mainloop()



if __name__ == "__main__":
    hello = Tab_app(400 , 500)
    hello.call_app()

