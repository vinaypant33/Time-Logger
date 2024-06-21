import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Create the main application window
root = ttk.Window(themename="cosmo")

# Create a variable to store the checkbox state
checkbox_value = ttk.IntVar()

# Create a checkbox with the variable
checkbox = ttk.Checkbutton(root, text="Check me", variable=checkbox_value)
checkbox.pack(pady=20)

# Function to get and print the current value of the checkbox
def get_checkbox_value():
    print("Checkbox value:", checkbox_value.get())

# Create a button to get the checkbox value
get_value_button = ttk.Button(root, text="Get Value", command=get_checkbox_value)
get_value_button.pack(pady=20)

# Start the main event loop
root.mainloop()
