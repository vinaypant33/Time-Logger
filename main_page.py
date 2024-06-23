import os
import sys


import tkinter as tk
from tkinter import ttk
import ttkbootstrap as btk

from pubsub import pub
# from tkinter import messagebox
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.dialogs.dialogs import Messagebox
import ttkbootstrap.icons
from ttkbootstrap.tooltip import ToolTip

from Views import spinbox
from Views import spinmeter
from Views import other_task_frame
from Views import base_analytics

# emoji  = ttkbootstrap.icons.Emoji
# print(emoji.get('winking face')) Can be used later to make the emojis

main_window  = btk.Window(themename="flatly")
'''
Light Themes  :  flatly, journal, 
Dark Theme  :  solar, darkly, 
'''
 
'''
get the theme name from the main window and make it the main theme of the controls 
bg_color = root.cget("background")

USER_THEMES = {
    "supercosmo": {
        "type": "light",
        "colors": {
            "primary": "#2780e3",
            "secondary": "#7E8081",
            "success": "#3fb618",
            "info": "#9954bb",
            "warning": "#ff7518",
            "danger": "#ff0039",
            "light":"#F8F9FA",
            "dark": "#373A3C",
            "bg": "#ffffff",
            "fg": "#373a3c",
            "selectbg": "#7e8081",
            "selectfg": "#ffffff",
            "border": "#ced4da",
            "inputfg": "#373a3c",
            "inputbg": "#fdfdfe"
        }
    }
}

'''

# Functions :: For the main application  ::
# bg_color = main_window.cget("background")
# print(bg_color)


# style = btk.Style()
# colors = set()
# for element in style.element_names():
#     for option in ('background', 'foreground', 'bordercolor', 'lightcolor', 'darkcolor', 'troughcolor', 'selectcolor'):
#         color = style.lookup(element, option)
#         if color:
#             colors.add(color)
#             print(color)
    

def task_timer(task_name):
    print(task_name)

def set_hourly_time(hourly_time):
    global current_hourly_time
    current_hourly_time = hourly_time
   


def another_play_clicked():
    if current_hourly_time == 0:
       Messagebox.show_error("The Hours Cannot be Zero" , "Time Logger" , alert=True , parent=all_task_frame)
    else:
        try:
            anohter_text.destroy()
            another_timer.delete()
            another_play_button.destroy()
        except Exception as e:
            print(e)
        global another_timer_meter
        another_timer_meter = spinmeter.SpinMeter(timer_frame)
        global another_pause_button
        another_pause_button = btk.Button(timer_frame ,text=f"{pause_icon}{pause_text}" , command=pause_clicked)
        another_pause_button.pack(pady=(20 , 0))


def pause_clicked():
    try:
        timer_meter.delete()
        pause_button.destroy()
    except Exception as e:
        print(e)
    
    try:
        another_timer_meter.delete()
        another_pause_button.destroy()
    except Exception as e:
        print("Error " and e)
    global anohter_text
    anohter_text  = btk.Label(timer_frame , text="Select time to start focus session !!!")
    anohter_text.pack(pady=  (15 , 0))
    global another_timer
    another_timer  = spinbox.SpinBox(timer_frame)
    global another_play_button
    another_play_button  = btk.Button(timer_frame , text=f"{play_icon}{play_text}" , command=another_play_clicked)
    another_play_button.pack(pady=(3,0))


def play_clicked():
    if current_hourly_time == 0:
        Messagebox.show_error("The Hours Cannot be Zero" , "Time Logger" , alert=True , parent=all_task_frame)
    else:
        counter_spinbox.delete()
        play_pause_button.destroy()
        text.destroy()
        global timer_meter
        timer_meter  = spinmeter.SpinMeter(timer_frame)
        global pause_button 
        pause_button  = btk.Button(timer_frame , text=f"{pause_icon}{pause_text}" , command=pause_clicked)
        pause_button.pack(pady=(20 , 0))
        pub.sendMessage("playclicked" , hour_time = current_hourly_time)


# App Constants and General Parts : 
main_window.title("Time Logger")
window_width  = 500
window_height  = 700
x_location = ( main_window.winfo_screenwidth() //2 ) - (window_width // 2)
y_location  = (main_window.winfo_screenheight() //2) - (window_height  // 2)
main_window.resizable(0 , 0)
main_window.geometry(f"{window_width}x{window_height}+{x_location}+{y_location}")


# Other App Constants  :
frame_width  = window_width
bottom_frame_height  = 30
frame_width  = window_width - 10
frame_height  = 300
current_hourly_time  = 0

play_icon  = '\u25B6'
pause_icon  = '\u23F9' # Unicode character for the button icon # '\u23F8' "\u25B6"  \u23F9
play_text  = "  Start Focus Session"
pause_text = "  Stop Focus Session"


############## Defining Controls ##################
bottom_frame  = btk.Frame(main_window , width=window_width , height=bottom_frame_height , bootstyle  = "info")

canvas  = tk.Canvas(main_window)
scrollbar  = ttk.Scrollbar(main_window , orient=tk.VERTICAL , command=canvas.yview)
controls_frame = ttk.Frame(canvas)

timer_frame = btk.Frame(controls_frame , width=frame_width , height = frame_height , bootstyle  = "")
all_task_frame   = btk.Frame(controls_frame , width=frame_width , height = frame_height )
analytics_frame  = btk.Frame(controls_frame  , width=frame_width , height = frame_height )
text  = btk.Label(timer_frame , text="Select time to start focus session !!!")
play_pause_button  = btk.Button(timer_frame , text=f"{play_icon}{play_text}" , command=play_clicked)

############## Configuring Controls #################
canvas.configure(yscrollcommand=scrollbar)
timer_frame.pack_propagate(0)
all_task_frame.pack_propagate(0)
analytics_frame.pack_propagate(0)


############### Binding Controls ####################
canvas.bind("<Configure>" , lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
timer_frame.bind('<MouseWheel>' , lambda e :canvas.yview_scroll(-1 *int((e.delta / 120)) , "units"))
all_task_frame.bind('<MouseWheel>' , lambda e :canvas.yview_scroll(-1 *int((e.delta / 120)) , "units"))
analytics_frame.bind('<MouseWheel>' , lambda e :canvas.yview_scroll(-1 *int((e.delta / 120)) , "units"))
canvas.create_window((0,0) , window=controls_frame , anchor='nw')


#################### Packing Controls ###############
bottom_frame.pack(side=tk.BOTTOM)
canvas.pack(side=tk.LEFT , fill=tk.BOTH , expand=True)
scrollbar.pack(side=tk.RIGHT , fill=tk.Y)
timer_frame.pack()
all_task_frame.pack()
analytics_frame.pack()
text.pack(pady=(15 , 0))



# Set the height and width - for the frames  : 
counter_spinbox  = spinbox.SpinBox(timer_frame)
main_task_list  = other_task_frame.Task_List(all_task_frame)
analytics  = base_analytics.Base_Analytics(analytics_frame)
play_pause_button.pack(pady=(3,0))





pub.subscribe(set_hourly_time , 'hour')
pub.subscribe(task_timer , "starttimer")




main_window.mainloop()