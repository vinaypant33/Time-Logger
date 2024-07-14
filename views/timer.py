import ttkbootstrap as btk
from pubsub import pub 
from ttkbootstrap.dialogs import Messagebox


from PIL import Image
Image.CUBIC = Image.BICUBIC



class Spinbox():


    def control_leave(self , e , control):
        self.main_frame.focus()


    def add_clicked(self):
        if self.timer_var >= self.max_time:
            Messagebox.show_error("Error - Unable to Increase Time" , "Time Logger" ,self.main_frame)
        elif self.timer_var < self.max_time and 0 <=self.timer_var <= 8:
            self.timer_var+=1
            self.current_label.configure(text = str(f"0{self.timer_var}"))
        elif self.timer_var < self.max_time and 9 <= self.timer_var <= self.max_time:
            self.timer_var+=1
            self.current_label.configure(text = str(f"{self.timer_var}"))

    def subtract_clicked(self):
        if self.timer_var <= 0:
            Messagebox.show_error( "Error - Unable to decrease timer - Please check max time settings" ,"Log Timer" , self.main_frame )
        elif self.timer_var <= self.max_time and 11 <= self.timer_var :
            self.timer_var-=1
            pub.sendMessage('hour' , hourly_time = self.timer_var)
            self.current_label.configure(text = str(self.timer_var))
        elif self.timer_var <= self.max_time and self.timer_var <= 11:
            self.timer_var-=1
            pub.sendMessage('hour' , hourly_time = self.timer_var)
            self.current_label.configure(text =str(f"0{self.timer_var}"))


    def __init__(self , master) -> None:


        # Constatns for the main app  : 
        self.timer_var  = 0
        self.max_time  = 30
    
        self.label_style  = btk.Style()
        self.label_style.configure("Label.TLabel" , font = ('Helvetica' , 15 , 'bold'))
        self.master = master
    
        self.main_frame  = btk.Frame(self.master , height=54 , width=100 , bootstyle = 'info')

        self.main_frame.pack_propagate(0)

        self.add_button  = btk.Button(self.main_frame , text="+" , command=self.add_clicked)
        self.subtract_button = btk.Button(self.main_frame ,text=" -" ,command=self.subtract_clicked)
        # self.text_frame  = btk.Frame(self.main_frame , bootstyle = 'danger' , height=100 , width=60)
        self.current_label = btk.Label(self.main_frame , text="00" , style = 'Label.TLabel')

        # Configuring Controls  :

        # Binding Controls  : 
        self.add_button.bind("<Leave>" , lambda e : self.control_leave(e = None , control=self.add_button) )
        self.subtract_button.bind("<Leave>" , lambda e : self.control_leave(e  = None ,  control=self.subtract_button))
        



        self.main_frame.pack()
        self.add_button.pack(side='top' , anchor='ne')
        self.subtract_button.pack(side='bottom' , anchor='se')
        # self.text_frame.pack(side='left')
        self.current_label.place(x = 30, y  =15)

    def delete(self):
        self.main_frame.pack_forget()




class Timer():


    def start_stop(self):

        if self.working == True :
        #    print(self.checkvar.get())
           self.time_selector  = self.time_type_selector.get()

        #    print(self.main_spin.current_label.cget('text'))
           self.count_value  = int(self.main_spin.current_label.cget('text'))

           if self.count_value == 0:
               Messagebox.show_error("Value cannot be zero" , "Time Logger")
           else:
               
                try:
                   self.main_spin.delete()
                except Exception as error:
                    print("Error For Exception")
                    print(error)

           
        # if self.count_value == 0:
        #        Messagebox.show_error("Value cannot be Zero")
        # else:
        #        print('done')
            
        #    if self.count_value == 0:
        #        Messagebox.show_error("Value cannot be 0")
        #     else:

                
        #    print(type(self.count_value))
        #    print(self.count_value)
        #    self.getfocus_label.destroy()

               

        #    self.spinbox_frame.destroy()
                self.time_type_selector.destroy()
                self.skip_breaks_checkbox.destroy()
                global timer_meter_data 
                timer_meter_data = Running_Timer(self.spinbox_frame)
                timer_meter_data.timer_run(current_text=self.time_selector , count=self.count_value)
                self.start_stop_button.configure(text=f"{self.stop_icon} Stop Focus Session")
                self.working = False


        elif self.working == False:
           self.working = True 
           timer_meter_data.delete()
           self.spinbox_frame.destroy()
           # Controls for the main applicatoin redefine :
           self.start_stop_button.destroy()

           self.getfocus_label  = btk.Label(self.main_frame , text="Get ready to focus" , bootstyle  = 'danger' , style='custom.TLabel')
           self.spinbox_frame  = btk.Frame(self.main_frame , height=120 , width=120 , bootstyle  = 'danger')
           self.main_spin = Spinbox(self.spinbox_frame) # Loading the main spinbox class to this class : 
           self.time_type_selector  = btk.Combobox(self.main_frame , values=self.options , width=12)
           self.skip_breaks_checkbox = btk.Checkbutton(self.main_frame , text="Skip Breaks" , style='custom.TCheckbutton' , variable=self.checkvar)
           self.start_stop_button  = btk.Button(self.main_frame , text=f'{self.play_icon} Start Focus Session' , command=self.start_stop)
           self.main_frame.pack_propagate(0)
           self.time_type_selector.set('Hours')
           self.checkvar.set(0)
           self.skip_breaks_checkbox.bind("<Leave>" , lambda e : self.main_frame.focus())
           self.start_stop_button.bind("<Leave>" , lambda e : self.main_frame.focus())
           self.main_frame.pack()
           self.getfocus_label.pack(pady=(10 ,0))
           self.spinbox_frame.pack(pady = (10 , 0))
           self.time_type_selector.pack(pady=(10, 0))
           self.skip_breaks_checkbox.pack(pady=(10 , 0))
           self.start_stop_button.pack(pady=(10 , 0))




    def __init__(self , master , width  = 480 , height  = 350) -> None:
        self.master  = master
        self.height  = height
        self.width  = width 

        


        # Custom Constatns :  
        label_style  = btk.Style()
        label_style.configure("custom.TLabel" , font = ('Helvetica', 12 , 'bold'))

        self.options  = ['Hours' , 'Minutes' , 'Seconds']

        self.checkbox_style  = btk.Style()
        self.checkbox_style.configure('custom.TCheckbutton' , font= ('Helvetica' , 9 , 'bold'))

        self.play_icon   = '\u25B6'
        self.stop_icon  = '\u23F9'
        self.checkvar = btk.IntVar()
        self.working   = True

        # Defining Controls  : 
        self.main_frame  = btk.Frame(self.master , width=self.width , height=self.height)
        self.getfocus_label  = btk.Label(self.main_frame , text="Get ready to focus" , bootstyle  = 'danger' , style='custom.TLabel')

        self.spinbox_frame  = btk.Frame(self.main_frame , height=120 , width=120 , bootstyle  = 'danger')

          
        self.main_spin = Spinbox(self.spinbox_frame) # Loading the main spinbox class to this class : 
        
        self.time_type_selector  = btk.Combobox(self.main_frame , values=self.options , width=12)
        self.skip_breaks_checkbox = btk.Checkbutton(self.main_frame , text="Skip Breaks" , style='custom.TCheckbutton' , variable=self.checkvar)
        self.start_stop_button  = btk.Button(self.main_frame , text=f'{self.play_icon} Start Focus Session' , command=self.start_stop)

        # Configuring Controls  : 
        self.main_frame.pack_propagate(0)
        self.time_type_selector.set('Hours')
        self.checkvar.set(0)


        # Binding Controls : 
        self.skip_breaks_checkbox.bind("<Leave>" , lambda e : self.main_frame.focus())
        self.start_stop_button.bind("<Leave>" , lambda e : self.main_frame.focus())


        # Packing Contorls  : 
        self.main_frame.pack()
        self.getfocus_label.pack(pady=(10 ,0))
        self.spinbox_frame.pack(pady = (10 , 0))
        self.time_type_selector.pack(pady=(10, 0))
        self.skip_breaks_checkbox.pack(pady=(10 , 0))
        self.start_stop_button.pack(pady=(10 , 0))




class Running_Timer(Timer):

    def __init__(self, master, width=480, height=350) -> None:
        
        self.master  = master
        self.height = height
        self.width = width
        '''
        3 meter for the second minutes and hours frame :  and stop meter button 
        
        '''

        self.seconds_count  = 0
        self.minutes_count  = 0 
        self.hours_count  = 0

        self.initial_seconds  = 0
        self.initial_minutes = 0
        self.initial_hours = 0
        self.master  = master 

        self.main_frame  = btk.Frame(self.master , height=self.height , width=self.width)
        self.seconds_timer  = btk.Meter(self.main_frame , metersize=162 ,bootstyle="primary", subtextstyle="primary" , subtext="Seconds" , 
                                        amountused=0,metertype="full" ,interactive=True, meterthickness=15 ,amounttotal=60,
                                        )
        
        self.minutes_timer  = btk.Meter(self.main_frame , metersize=162 , bootstyle='primary' , subtextstyle='primary' , subtext='Minutes',
                                        amountused=0 , metertype='full' , interactive=True , meterthickness=15 , amounttotal=60)
        
        self.hours_timer  = btk.Meter(self.main_frame , metersize=162 , bootstyle='primary' , subtextstyle='primary' , subtext='Hours',
                                        amountused=0 , metertype='full' , interactive=True , meterthickness=15 , amounttotal=100)


        # Configuring Controls : 

        # Binding Controls : 


        # Packing Controls : 
        self.main_frame.pack()
        self.seconds_timer.pack(side='right')
        self.minutes_timer.pack(side='right')
        self.hours_timer.pack(side='right')

    def delete(self):
        # self.main_frame.pack_forget()
        self.main_frame.destroy()

    def seconds_timer_run(self):
        if self.seconds_count > int(self.initial_seconds):
            return None
        else:
            self.seconds_count+=1
            self.seconds_timer.configure(str(self.seconds_count))
            self.main_frame.after(1000 , self.seconds_timer_run)

    def minutes_timer_run(self):
        pass

    def hours_timer_run(self):
        pass

    def timer_run(self , current_text  , count):
        if current_text == 'Seconds':
            self.initial_seconds = count
            print(self.initial_seconds)
            self.seconds_timer_run()
        elif current_text == 'Minutes':
            print("Passed is minutes")
        elif current_text == 'Hours':
            print("Passed in Hours")



if __name__ == '__main__':
    main_window  = btk.Window()
    Timer(main_window )

    # Spinbox(main_window)

    # Running_Timer(main_window)
    main_window.mainloop()


