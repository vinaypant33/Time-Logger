import tkinter as tk 
from tkinter import ttk

import ttkbootstrap as btk


main = btk.Window()
main.geometry("400x400")

canvas  = tk.Canvas(main ,background="red")

canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Scrollbar to the canvas frame : 
scrollbar  = ttk.Scrollbar(main , orient=tk.VERTICAL , command=canvas.yview)
scrollbar.pack(side=tk.RIGHT ,fill=tk.Y)

# 
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

for i in range(50):  # Example of adding 50 labels
    label = tk.Label(frame, text=f"Label {i + 1}")
    label.pack(pady=5, padx=10)

# 


main.mainloop()