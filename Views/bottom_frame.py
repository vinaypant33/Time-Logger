import tkinter as tk
from tkinter import ttk
import ttkbootstrap as btk

from pubsub import pub
# from tkinter import messagebox
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.dialogs.dialogs import Messagebox
import ttkbootstrap.icons
from ttkbootstrap.tooltip import ToolTip

import time
from time import sleep
import winsound # make the beep sound and will cahnge this later





class Bottom_Frame():


    def __init__(self , master ,  width ,  height) -> None:
        self.master  = master 
        self.width  = width // 4
        self.height = height - 2


        # Controls for the main Frame :: Master 
        self.first_frame = btk.Frame(self.master ,  width = self.width , height=self.height , bootstyle  = "info")
        self.second_frame  = btk.Frame(self.master , width=self.width , height  = self.height , bootstyle  = "warning")
        self.third_frame  = btk.Frame(self.master  , width = self.width , height=self.height , bootstyle  = "info")
        self.fourth_frame  = btk.Frame(self.master , width= self.width , height=self.height ,bootstyle  = "warning")


        # Configuring the controls :
        self.first_frame.pack_propagate(0)
        self.second_frame.pack_propagate(0)
        self.third_frame.pack_propagate(0)
        self.fourth_frame.pack_propagate(0)

        
        # Binding the controls :
        


        # Packing Controls :
        self.first_frame.pack(side=tk.LEFT)
        self.second_frame.pack(side=tk.LEFT)
        self.third_frame.pack(side=tk.LEFT)
        self.fourth_frame.pack(side=tk.LEFT)

