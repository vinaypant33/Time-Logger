import tkinter as tk  
import tkinter.ttk as ttk  
import customtkinter as ctk 


import colors 
import fonts
import  styles




class Messagebox():



    def __init__(self , width , height , x_location ,  y_location , current_message) -> None:
        self.messagebox  = tk.Tk()
        self.width  = width 
        self.height  = height
        self.message = current_message
        self.messagebox.geometry(f'{self.width}x{self.height}+{x_location}+{y_location}')
        # Removing the titlebar : 
        self.messagebox.overrideredirect(True) 
        self.titlebar = tk.Frame(self.messagebox , height=15  , background=colors.app_base)
        self.close_button  =tk.Button(self.titlebar , text='\u2716' , command=self.close_app)
        self.text_box  = tk.Text(self.messagebox)
        self.text_box.tag_configure("center", justify="center")
        # Configure the contorls :
        self.messagebox.configure(background=colors.sidebar_base)
        self.close_button.configure(styles.styles.button_styles(self.close_button , colors.Red , colors.White , colors.app_base  , colors.Red))
        self.text_box.insert(tk.END , self.message)
        self.text_box.configure(background=colors.sidebar_base , foreground=colors.White , bd=0 , state='disabled')
        # Placing Controls : 
        self.titlebar.pack(side='top' , fill='x')
        self.close_button.pack(side='right' , padx=(0,0))
        self.text_box.pack(side='top' , padx=(20,20) , pady=(10,10))
        # Make the app visible
        self.messagebox.mainloop()
    def close_app(self):
        self.messagebox.destroy()

if __name__ == '__main__':
    namew_hehe = Messagebox(200,100,100,100 , "Mera naam vinay mera kaam hehe")




