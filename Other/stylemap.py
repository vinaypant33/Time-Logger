import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create a ttk button
# button = ttk.Button(root, text="Sample Button")
# button.pack()

# Get the style map for the button style
style = ttk.Style()
style_map = style.map('Custom.TButton')

# Print the style map to see all available attributes
print(style_map)

root.mainloop()
