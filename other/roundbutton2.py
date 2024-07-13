import tkinter as tk
from tkinter import Canvas
import ttkbootstrap as ttk

def on_button_click(event):
    print("Round button with + clicked!")

# Create the main window
root = ttk.Window(themename="darkly")

# Create a Canvas
canvas = Canvas(root, width=100, height=100, highlightthickness=0)
canvas.pack(pady=20)

# Draw a round shape (circle) on the Canvas
oval = canvas.create_oval(2, 2, 90, 90, fill="blue", outline="")

# Draw a + symbol in the center of the circle
canvas.create_line(50, 20, 50, 80, fill="white", width=3)  # Vertical line of the +
canvas.create_line(20, 50, 80, 50, fill="white", width=3)  # Horizontal line of the +

# Bind the click event to the round shape
canvas.tag_bind(oval, "<Button-1>", on_button_click)
canvas.tag_bind("line", "<Button-1>", on_button_click)  # Bind the lines too

root.mainloop()
