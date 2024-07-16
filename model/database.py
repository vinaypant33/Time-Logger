import sqlite3
import datetime



import calculation

connection = sqlite3.connect('task_manager.db')
connect_cursor = connection.cursor()


def saving_data():
    connection.commit()
    
    

def saving_text_data(current_text):
    print(current_text)

