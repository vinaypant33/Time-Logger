import tkinter as tk
from tkinter import ttk
import calendar

def show_calendar():
    year = int(year_entry.get())
    month = int(month_entry.get())
    
    cal = calendar.monthcalendar(year, month)
    
    for widget in calendar_frame.winfo_children():
        widget.destroy()
    
    for week_num, week in enumerate(cal, start=1):
        for day_num, day in enumerate(week, start=1):
            if day == 0:
                continue
            ttk.Label(calendar_frame, text=day).grid(row=week_num, column=day_num)

root = tk.Tk()
root.title("Simple Calendar")

year_label = ttk.Label(root, text="Year:")
year_label.pack()

year_entry = ttk.Entry(root)
year_entry.pack()

month_label = ttk.Label(root, text="Month:")
month_label.pack()

month_entry = ttk.Entry(root)
month_entry.pack()

show_button = ttk.Button(root, text="Show Calendar", command=show_calendar)
show_button.pack()

calendar_frame = ttk.Frame(root)
calendar_frame.pack()

root.mainloop()
