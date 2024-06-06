import customtkinter as ctk

from PIL import Image
Image.CUBIC = Image.BICUBIC





class Analytics():


    def __init__(self , master    , width = 600 ,  height = 500) -> None:
        self.master = master
        self.width  = width
        self.height = height

        self.master.configure(height = self.height , width = self.width)

        self.analytics_frame = ctk.CTkFrame(self.master , height=self.height , width=self.width)

        # App Controls  :  number and text and circular meterbox
        self.yestarday_frame = ctk.CTkFrame(self.master  , width=140  , corner_radius=0)
        self.yestarday_frame.grid_propagate(0)
        self.yestarday_frame.pack_propagate(0)

        self.today_frame =ctk.CTkFrame(self.master , width = 300 , corner_radius=0)
        self.today_frame.grid_propagate(0)
        self.today_frame.pack_propagate(0)

        self.streak_frame = ctk.CTkFrame(self.master , width  = 140 , corner_radius=0)
        self.streak_frame.grid_propagate(0)
        self.streak_frame.pack_propagate(0)



        self.yestarday_text  = ctk.CTkLabel(self.yestarday_frame , text="Yesterday")
        self.yesterday_count  = ctk.CTkLabel(self.yestarday_frame , text="0")
        self.yesterday_time  =ctk.CTkLabel(self.yestarday_frame ,text="Hours")



        """
        Will define the meter and the meter count with the text to show the current hours passed today  : on Hold for now  : 
        """


        self.streak_text  = ctk.CTkLabel(self.streak_frame , text="Streak")
        self.streak_count  = ctk.CTkLabel(self.streak_frame , text="0")
        self.streak_days_text  = ctk.CTkLabel(self.streak_frame , text="Days")


        # Packing the Controls : 
        self.yestarday_frame.grid(row = 0 , column = 0 , columnspan=1)
        self.today_frame.grid(row = 0 , column =1 ,  columnspan  = 2)
        self.streak_frame.grid(row = 0 , column = 4 , columnspan=1)


        # self.yestarday_text.grid(row = 0 , column = 0)
        # self.yesterday_count.grid(row = 1 ,  column = 0)
        # self.yesterday_time.grid(row = 2  ,column = 0)

        self.yestarday_text.pack(padx = 5 , pady = (50 , 5))
        self.yesterday_count.pack(padx = 5 , pady = 5)
        self.yesterday_time.pack(padx = 5 , pady = 5)


        self.streak_text.pack(padx = 5 , pady = (50 , 5))
        self.streak_count.pack(padx = 5 , pady = 5)
        self.streak_days_text.pack(padx = 5 , pady = 5)







if __name__ == '__main__':
    window  = ctk.CTk()
    Analytics(window)
    window.mainloop()