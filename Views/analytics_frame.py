import tkinter as tk
from tkinter import ttk
import ttkbootstrap as btk


from PIL import Image
Image.CUBIC  = Image.BICUBIC



class Analytics():


    def __init__(self ,master, width ,  height) -> None:
        self.master  = master
        self.width    = width
        self.height  = height

        self.yesterday_frame  = btk.Frame(self.master , height=height, width  = (self.width //3) )
        self.today_frame  = btk.Frame(self.master , height=height , width=(self.width //3) )
        self.streak_days = btk.Frame(self.master , height=self.height , width=(self.width //3) )


        self.yesterday_frame.pack(side=tk.LEFT)
        self.today_frame.pack(side=tk.LEFT)
        self.streak_days.pack(side=tk.LEFT)

        '''
        3 Frames one meter for yesterday one for today and one for tomorrow
        Meter Widget for each frame 
        inside text in each meter frame
        '''


        ## Meter Widgets : 
        self.yestarday_meter  = btk.Meter(self.yesterday_frame , metersize=162 ,bootstyle="primary", subtextstyle="primary" , subtext="Hours - Yesterday" , amountused=0,metertype="full" ,interactive=True, meterthickness=15 ,amounttotal=24)
        self.today_meter  =btk.Meter(self.today_frame ,metersize=163 ,  bootstyle = "primary" , subtext="Hours - Today" , subtextstyle="primary" , amountused=0,metertype="full" ,interactive=True, meterthickness=15 , amounttotal=24 )
        self.streak_meter  = btk.Meter(self.streak_days, metersize=162, bootstyle="primary" , subtext="Days - Streak" , subtextstyle="primary" , amountused=0,metertype="full",interactive=True , meterthickness=15 ,amounttotal=100)





        self.yestarday_meter.pack()
        self.today_meter.pack()
        self.streak_meter.pack()






if __name__ == '__main__':
    main_window  = btk.Window()
    Analytics(main_window , width=300 , height=300)
    main_window.mainloop()