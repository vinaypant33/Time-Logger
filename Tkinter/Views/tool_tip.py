import tkinter as tk 
import tkinter.ttk as ttk

import colors 
import fonts
import threading



class ToolTip():

    def __init__(self , widget , text , enter_color , exit_color) -> None:
        self.widget = widget 
        self.text = text
        self.enter_color  = enter_color
        self.exit_color  = exit_color

        self.widget.bind("<Enter>" , self.show_tooltip)
        self.widget.bind("<Leave>" , self.hide_tooltip)


    def show_tooltip(self , event):
        self.widget.configure(background = self.enter_color)
        self.tool_tip = tk.Toplevel(self.widget)
        self.tool_tip.overrideredirect(True)
        x_loc = self.widget.winfo_rootx() +25
        y_loc = self.widget.winfo_rooty() + 25
        self.tool_tip.geometry(f'+{x_loc}+{y_loc}')
        self.label  = tk.Label(self.tool_tip , text=self.text).pack()
        self.widget.after(1000 , self.hide_through_delay)


    def hide_tooltip(self, event):
        self.widget.configure(background = self.exit_color)
        if self.tool_tip:
            self.tool_tip.destroy()

    def hide_through_delay(self):
        if self.tool_tip:
            self.tool_tip.destroy()