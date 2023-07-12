import sys
sys.path.append('Views') # To add the Views path to the main Application.

# Importing the files from the views folder
from Views import main_page




def calling_main_app():
    app_dashboard = main_page.main_page("Master" , 900 , 900)



if __name__ == '__main__':
    calling_main_app()