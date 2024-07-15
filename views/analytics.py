import tkinter as tk
from tkinter import ttk
import ttkbootstrap as btk

from PIL import Image
Image.CUBIC = Image.BICUBIC



class Analytics():
    
    def __init__(self , master  ,  width  = 480 , height  = 300) -> None:
        self.master  = master
        self.width = width
        self.height  = height
        
        self.main_frame  = btk.Frame(self.master , width=self.width , height=self.height , bootstyle = 'info')
        
        self.streak_days  = btk.Meter(self.main_frame , metersize=162 ,bootstyle="primary", subtextstyle="primary" , subtext="Streak" , 
                                        amountused=0,metertype="full" ,interactive=False, meterthickness=15 ,amounttotal=100,
                                        )
        
        self.daily_goal  = btk.Meter(self.main_frame , metersize=162 , bootstyle='primary' , subtextstyle='primary' , subtext='Hours Today',
                                        amountused=0 , metertype='full' , interactive=False , meterthickness=15 , amounttotal=24)
        
        self.yestarday_goal  = btk.Meter(self.main_frame , metersize=162 , bootstyle='primary' , subtextstyle='primary' , subtext='Hours Yesterday',
                                        amountused=0 , metertype='full' , interactive=False , meterthickness=15 , amounttotal=100 )
        
        
        
        # self.main_frame.pack_propagate(0)
        
        
        self.main_frame.pack(pady=(100 , 0))
        self.streak_days.pack(side=tk.RIGHT)
        self.daily_goal.pack(side=tk.RIGHT)
        self.yestarday_goal.pack(side=tk.RIGHT)
        


if __name__ == '__main__':
    main_window  = btk.Window()
    Analytics(main_window)
    
    main_window.mainloop()