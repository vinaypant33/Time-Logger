import tkinter as tk 





class Main_Page():

    def __init__(self , height , width , master = None) -> None:
        self.main_app = tk.Tk()
        self.height   = height
        self.width  = width
        self.main_app.geometry(f"{self.width}x{self.height}")


    def defnining_controls(self):
        pass

    def placing_controls(self):
        pass

    
    def calling_main_app(self):
        self.main_app.mainloop() # This calls the main app

    def kill_main_app(self):
        self.main_app.destroy() # This kills the main app



if __name__ == "__main__":
    main_application  = Main_Page(100 ,100)
    main_application.defnining_controls()
    main_application.placing_controls()
    main_application.calling_main_app()