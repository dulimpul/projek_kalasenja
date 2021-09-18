import os
from upload_data import *
from tampilkan_data import *
from Edit_data import *
from core_remove import remove_menu
from hitung_core import menu_hitung

def menu():
    print("""                                                                        
 /$$$$$$/$$$$  /$$$$$$ /$$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$ /$$$$$$$       
| $$_  $$_  $$|____  $| $$__  $$|____  $$/$$__  $$|____  $| $$__  $$      
| $$ \ $$ \ $$ /$$$$$$| $$  \ $$ /$$$$$$| $$  \ $$ /$$$$$$| $$  \ $$      
| $$ | $$ | $$/$$__  $| $$  | $$/$$__  $| $$  | $$/$$__  $| $$  | $$      
| $$ | $$ | $|  $$$$$$| $$  | $|  $$$$$$|  $$$$$$|  $$$$$$| $$  | $$      
|__/ |__/ |__/\_______|__/  |__/\_______/\____  $$\_______|__/  |__/      
                                         /$$  \ $$                        
                                        |  $$$$$$/                        
                                         \______/                         
""")
    print("="*10,"MENU", "="*10)
    print("[1]~ Show data")
    print("[2]~ Uplod data")
    print("[3]~ Edit data")
    print("[4]~ Clear data ")
    print("[5]~ Hitung data")
    print("[6]~ Exit")

    input_key = int(input("INPUT ID YANG ADA DI SAMPING LIST :"))
    
    if input_key ==  1:
        os.system("clear")
        showsDataMenu()
    elif input_key == 2:
        os.system("clear")
        menutambah()
    elif input_key == 3:
        os.system("clear")
        editDataMenu()
    elif input_key == 4:
        os.system("clear")
        remove_menu.menuhapus()
    elif input_key == 5:
        os.system("clear")
        menu_hitung.menuhitung()
    elif input_key == 6:
        os.system("clear")
        exit()
    else:
        os.system("clear")
        menu() 

