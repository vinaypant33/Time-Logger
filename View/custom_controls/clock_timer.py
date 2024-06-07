# Implementing New code for clock timer : 

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

from math import pi,cos, sin





from ttkbootstrap import Meter





from PIL import Image

Image.CUBIC  = Image.BICUBIC


class CustomMeter(ctk.CTkCanvas):



    def __init__(self , master , width = 100 , height = 100 , start_angle  = 0 , end_angle  = 360 , **kwargs) -> None:
        self.master  = master

        self.width  = width
        self.height  = height

        # self.canvas  = ctk.CTkCanvas(master  , width = self.width  , height = self.height )

        # self.canvas.create_arc(0 , 0 ,100, 100, start =  0 , extent = 290 ,fill='blue', outline='black')

        self.meter   = Meter(master=self.master)

        self.meter.pack()

        # self.canvas.pack()


        # self.canvas.grid(row = 0 , column  = 0)








if __name__ == '__main__':
    window  = ctk.CTk()

    CustomMeter(master = window)


    window.mainloop()
























# import tkinter as tk 
# from tkinter import ttk
# import customtkinter as ctk

# from math import pi, sin, cos


# class CustomMeter(ctk.CTkCanvas):
#     def __init__(self, parent, width=200, height=200, start_angle=0, end_angle=360, **kwargs):
#         super().__init__(parent, width=width, height=height, **kwargs)
#         self.width = width
#         self.height = height
#         self.start_angle = start_angle
#         self.end_angle = end_angle
#         self.angle_range = end_angle - start_angle
#         self.value = 0

#         self.arc = None
#         self.create_meter_arc()
#         self.create_text(width // 2, height // 2, text="0%", font=("Helvetica", 12, "bold"), fill="green", tags="text")

#     def create_meter_arc(self):
#         if self.arc:
#             self.delete(self.arc)
#         self.arc = self.create_arc(
#             10, 10, self.width - 10, self.height - 10,
#             start=self.start_angle, extent=0,
#             outline="green", width=5, style=tk.ARC, tags="arc"
#         )

#     def set_value(self, value):
#         self.value = max(0, min(100, value))  # Ensure value is between 0 and 100
#         extent = (self.value / 100) * self.angle_range
#         self.itemconfig(self.arc, extent=extent)
#         self.itemconfig("text", text=f"{self.value}%")
#         self.update()


# if __name__ =="__main__":

#     window  = tk.Tk()
#     hehe  = tk.Frame(window , background="black", height=400 , width=400)
#     hehe.pack_propagate(0)
#     name = CustomMeter(hehe)
#     hehe.pack()
#     name.pack()
#     window.mainloop()