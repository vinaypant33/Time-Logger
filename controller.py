import os
import sys

import tkinter as tk
import ttkbootstrap as btk 

from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.tooltip import ToolTip
import ttkbootstrap.icons as Icon
from ttkbootstrap.scrolled import ScrolledFrame as scrolled_frame


import ctypes
import platform


# For message passing  : 
from pubsub import pub


from views import timer
from views.task_frame import Task_Frame
from views.analytics import Analytics


# Defining App Constants  : 
primary_color  = ''
window_base_color  = '#000000'
window_width  = 510
window_height  = 700
frame_height  = 460
frame_width = 480

main_application  = btk.Window(themename='flatly')

'''
Light Themes  : flatly, journal
Dark Themes : solar darkly
'''

# Functions for the main applicatoin : 


# Defining main window : parameters  : 
main_application.title("Time Logger")

main_application.resizable( 0 , 0)
main_application.overrideredirect =True
# main_application.place_window_center()  # This will be used to make the top level later : 
# position_center   This can be used to place the widget in the center of the app  : 
# place_window_center()  This can be used to make the application in the center of the screen

x_position  =  (main_application.winfo_screenwidth() // 2) - (window_width // 2)
y_position  = (main_application.winfo_screenheight() //2 )  - (window_height // 2)

main_application.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# main_application.configure(bg="#656565") # color for the main application  :: #000000    #2b2b2b #656565

main_application.configure(bg=window_base_color)

'''
Bottom Frame 
Three Frames : 
    timer frame
    task frame 
    analytics frame 

    seperator in between each frame and make constants for the main application 


'''



# Defining Contorls :
frame_style = btk.Style()
frame_style.configure('custom.TFrame' , background=  '#ffffff')
bottom_frame  = btk.Frame(main_application , height=30 , style='custom.TFrame')

# Controls for the bottom frame  : 
settings_icon = "\u2699"
alarm_icon = '\u23F0'
stopwatch_icon = '\u23F1'

label_style  = btk.Style()
label_style.configure("custom.TLabel" ,font = ('Helvetica' , 1) )


settings_button  = btk.Label(bottom_frame , text= f"{settings_icon} Settings" , style='custom.TLabel')
settings_button.pack(side=tk.LEFT , pady=(3) ,padx=10)

alarm_button  = btk.Label(bottom_frame , text= f"{alarm_icon} Alarm" , style='custom.TLabel')
alarm_button.pack(side=tk.LEFT , pady=(3) ,padx=(95))

stopwatch_button  = btk.Label(bottom_frame , text= f"{stopwatch_icon} Stopwatch" , style='custom.TLabel')
stopwatch_button.pack(side=tk.RIGHT , pady=(3) ,padx=10)

main_scrolled_frame   = scrolled_frame(main_application , width=window_width , height=window_width  ,autohide=True )
tiemr_frame = btk.Frame(main_scrolled_frame , width=frame_width , height=frame_height - 150 )
# timer_seperator  = btk.Separator(main_scrolled_frame , bootstyle  = 'danger' )
task_frame = btk.Frame(main_scrolled_frame , width=frame_width , height=frame_height )
analytics_frame  = btk.Frame(main_scrolled_frame , width=frame_width , height=frame_height - 100 )

# Configuring Controls : 
tiemr_frame.pack_propagate(0)
task_frame.pack_propagate(0)
bottom_frame.pack_propagate(0)
analytics_frame.pack_propagate(0)





# Packing Controls : 
# bottom_frame.pack(side=tk.BOTTOM  ,fill='x' , anchor='s')
main_scrolled_frame.pack(expand=True , fill='both')
tiemr_frame.pack(pady=0)
# Calling the timer class Timer function : 
timer.Timer(tiemr_frame)
Task_Frame(task_frame)
Analytics(analytics_frame)
# timer_seperator.pack(fill='x')
task_frame.pack(pady=0)
analytics_frame.pack()




main_application.mainloop()