# import tkinter as tk

# def on_button_click(event):
#     print("Button clicked!")

# root = tk.Tk()
# root.title("Round Button Example")

# # Create a canvas widget
# canvas = tk.Canvas(root, width=100, height=100, highlightthickness=0)
# canvas.pack()

# # Draw a circular button on the canvas
# button = canvas.create_oval(10, 10, 90, 90, fill='lightblue', outline='black', width=2)

# # Bind mouse click event to the circular button
# canvas.tag_bind(button, '<Button-1>', on_button_click)

# root.mainloop()


import tkinter as tk

def on_button_click(event):
    print("Button clicked!")

root = tk.Tk()
root.title("Transparent Round Button Example")

# Create a canvas widget
canvas = tk.Canvas(root, width=100, height=100, bg='white', highlightthickness=0)
canvas.pack()

# Load a transparent image for the button
image = tk.PhotoImage(file='button.png')  # Replace 'button.png' with your image file

# Create a button using the image
button = canvas.create_image(50, 50, image=image)

# Bind mouse click event to the button
canvas.tag_bind(button, '<Button-1>', on_button_click)

root.mainloop()
