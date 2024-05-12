import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

def list_themes():
    themes = Style().themes  # Get the list of available themes
    for i, theme in enumerate(themes):
        label = ttk.Label(frame, text=f"{i + 1}. {theme}", style='success.TLabel')
        label.grid(row=i, column=0, padx=10, pady=5, sticky='w')

root = tk.Tk()
root.title("List of Themes Example")

# Create a frame to display the list of themes
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

# Display the list of themes
list_themes()

root.mainloop()
