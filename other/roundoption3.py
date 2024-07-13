import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def on_button_click():
    print("Transparent button clicked!")

# Create the main window
root = ttk.Window(themename="darkly")

# Get the background color of the window
bg_color = root.cget("background")

# Create a style for the transparent button
style = ttk.Style()
style.configure("Transparent.TButton",
                background=bg_color,
                relief="flat",
                borderwidth=0,
                font=("Arial", 20),
                foreground="white")

# Create a transparent button using ttk.Button with custom style
transparent_button = ttk.Button(root, text="+", style="Transparent.TButton", command=on_button_click)
transparent_button.pack(pady=20)

root.mainloop()
