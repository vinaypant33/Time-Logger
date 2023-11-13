import tkinter as tk
import colors
import fonts




class Messagebox():

    def close_messagebox(self):
        self.messagebox.destroy()

    def __init__(self , x_location , y_location , current_message  =None) -> None:
       
        self.messagebox  =  tk.Tk()
        self.height = 100 
        self.width  = 250
        self.x = x_location - (self.height // 2)
        self.y = y_location - (self.width // 2) 

        # Removing the title bar and Setting up the geometry
        self.messagebox.overrideredirect(True)
        self.messagebox.geometry(f"{self.width}x{self.height}+{self.y}+{self.x}")

        self.messagebox.configure(background=colors.sidebar_base)


        self.titlebar = tk.Frame(self.messagebox , background=colors.app_base , height=20  , width=self.width)
        self.titlebar.pack_propagate(0)
        self.closing_button  = tk.Button(self.titlebar , text='\u2716' , background=colors.app_base , foreground=colors.White , activebackground=colors.Red , activeforeground=colors.Black ,bd = 0 , relief="flat" , command=self.close_messagebox)

        self.message = tk.Label(self.messagebox , text=current_message  , font=fonts.super_small_font_bold, background=colors.sidebar_base, foreground=colors.White)  


        # Packing the controls 
        self.titlebar.pack(side="top")
        self.closing_button.pack(side="right")
        self.message.pack(side="top" , pady=10 , padx=2)
        self.messagebox.mainloop()



if __name__ == "__main__":

    messagebox = Messagebox(200,100 , "I am the current Message in messagebox")

