import tkinter as tk
from tkinter import Canvas
import ttkbootstrap as ttk

def on_button_click(event):
    print("Round button clicked!")

# Create the main window
root = ttk.Window(themename="darkly")

# Create a Canvas
canvas = Canvas(root, width=100, height=100, highlightthickness=0)
canvas.pack(pady=20)

# Draw a round shape (circle) on the Canvas
oval = canvas.create_oval(10, 10, 90, 90, fill="blue", outline="")

# Bind the click event to the round shape
canvas.tag_bind(oval, "<Button-1>", on_button_click)

root.mainloop()
