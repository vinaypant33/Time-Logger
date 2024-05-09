import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Centered Notebook Headers")

style = ttk.Style()

# Create a custom style for the notebook tab headers
style.layout('Centered.TNotebook.Tab', [
    ('Notebook.tab', {
        'sticky': 'nswe', 
        'children': [
            ('Notebook.label', {'side': 'left', 'sticky': ''}),
            ('Notebook.focus', {'side': 'left', 'sticky': '', 'children':
                [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                    [('Notebook.label', {'side': 'left', 'sticky': ''})]
                })]
            })
        ]
    })
])

# Configure the custom style
style.configure('Centered.TNotebook.Tab', padding=[10, 5], font=('TkDefaultFont', 10))

notebook = ttk.Notebook(root, style='Centered.TNotebook')
notebook.pack(fill='both', expand=True)

for i in range(5):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=f'Tab {i+1}')

root.mainloop()
