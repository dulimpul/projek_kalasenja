from data import *
import time
import menu
import os

def menutambah():
    print("\n \n")
    print("="*20, "MENU TAMBAH DATA", "="*20)
    print("\n")
    print("[1]~ Input Thun")
    print("[2]~ Input Yi")
    print("[3]~ Input Ui")
    print("[99]~ Kembali ke menu")
    print("\n")
    key_word = int(input("MASUKAN KEY YANG ADA DI SAMPING LIST : "))

    if key_word == 1 :
        tabahTh()
        os.system("clear")
        #os.system("cls")       # if you use windows os remove hashtag
        menutambah()
    elif key_word == 2:
        tambahYi()
        os.system("clear")
        #os.system("cls")       # if you use windows os hashtag
        menutambah()
    elif key_word == 3:
        tambahUi()
        os.system("clear")
        #os.system("cls")       # if you use windows os hashtag
        menutambah()
    elif key_word == 99:
        os.system("clear")
        #os.system("cls")       # if you use windows os hashtag
        menu.menu()
    else:
        os.system("clear")
        #os.system("cls")       # if you use windows os hashtag
        menutambah()

def tabahTh():
    tmbhTh = int(input("MASUKAN TAHUN DALAM BENTUK ANGKA :"))
    tahun.append(tmbhTh)

def tambahYi():
    yitmbah = int(input("MASUKAN NILAI YI :"))
    Yi.append(yitmbah)

def tambahUi():
    Uitambah = int(input("MASUKAN NILAI UI :"))
    Ui.append(Uitambah)