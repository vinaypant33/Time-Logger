import colors
import fonts
import tkinter.ttk as ttk
import tkinter as tk 



class styles():

    def button_styles(master , bg_color , fg_color , active_bg , active_fg):
        master.configure(background=bg_color , foreground=fg_color , activebackground=active_bg , activeforeground=active_fg , bd  = 0  , relief='flat')

    def button_entry_exit(master , colorname):
        master.configure(background=colorname)



class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None

        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = ttk.Label(self.tooltip, text=self.text)
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()


class main_tool_tip():
    def __init__(self , widget , message) -> None:
        self.widget  = widget
        self.text  = message

