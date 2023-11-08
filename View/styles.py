import sys
sys.path.append("View")
import colors
import fonts
import tkinter.ttk as ttk
import tkinter as tk 



class styles():

    def button_styles(master , bg_color , fg_color , active_bg , active_fg):
        master.configure(background=bg_color , foreground=fg_color , activebackground=active_bg , activeforeground=active_fg , bd  = 0  , relief='flat')

    def button_entry_exit(master , colorname):
        master.configure(background=colorname)

