import os
import sys

sys.path.append('Views')



import tkinter as tk
from tkinter import ttk
import ttkbootstrap as btk

from Views import mainpage




if __name__ == '__main__':
    main_application  = btk.Window()
    mainpage.MainPage(main_application)
    main_application.mainloop()
    





# import os
# import sys




# sys.path.append("Views")
# from Views import main_page
# from Views import tasklist
# from Views import custom_spinbox

# from pubsub import pub # Module for message passing  :




# def tempcalling():
#     print("called inm hjere r")
#     custom_spinbox.SpinMeterBox.static_starting_timer(20)


# pub.subscribe(tempcalling , "starttimer")





# if __name__ =='__main__':
#     main_page.MainPage()