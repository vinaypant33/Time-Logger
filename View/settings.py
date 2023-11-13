import tkinter as tk



class Settings():

    def __init__(self , width , height , master) -> None:
        self.settings  = master
        self.width  = width 
        self.height  = height

        # Defining the Controls : 
        self.main_frame  = tk.Frame(self.settings , width  = self.width , height  = self.height , background="blue")

        self.main_frame.pack()
        self.settings.mainloop()

    def destroy_everything(self):
        self.settings.destroy()



if __name__ == '__main__':
    main = Settings(200 ,200 , tk.Tk())
