import tkinter as tk
import ttkbootstrap as btk

main_window = tk.Tk()



## Getting the app in the center of the screen :
screen_height   = main_window.winfo_screenheight()
screen_width = main_window.winfo_screenwidth()

window_height   = 500
window_width  = 400


main_window.geometry(f"{window_width}x{window_height}+{(screen_width //2 ) - (window_width //2)}+{(screen_height //2) - (window_height //2)}")
main_window.resizable(0 , 0)


## Making the sidebar for the main : 

tab_control  = btk.Button(master = main_window)


tab_control.pack()


main_window.mainloop()
main_window.destroy() # This is just to address the opening of second tkinter window problem for now 