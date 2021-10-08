import os
import tampilkan_data  
import menu
import time
import data

def editDataMenu():
    print("="*20,"MENU EDIT DATA", "="*20 )
    print("\n")
    print("[1]~ Edit data Tahun")
    print("[2]~ Edit data Yi")
    print("[3]~ Edit data Ui")
    print("[99]~ Kembali menu utama")
    print("\n")
    keyEdit = int(input("Masukan pilihan :")) 

    if keyEdit == 1:
        #Tahun edit data
        editTahun()
        print("Akan kembali")
        time.sleep(5)
        os.system("clear") # if you use windows os add hashtag in first word
        #os.system("cls") # if you use windows os remove hashtag in first word
        editDataMenu()
    elif keyEdit == 2:
        #Yi data edit
        editYi()
        print("Akan kembali")
        time.sleep(5)
        os.system("clear") # if you use windows os add hashtag in first word
        #os.system("cls") # if you use windows os remove hashtag in first word
        editDataMenu()
    elif keyEdit == 3:
        #Ui data edit
        editUi()
        print("Akan kembali")
        time.sleep(5)
        os.system("clear") # if you use windows os add hashtag in first word
        #os.system("cls") # if you use windows os remove hashtag in first word
        editDataMenu()
    elif keyEdit == 99:
        os.system("clear") # if you use windows os add hashtag in first word
        #os.system("cls") # if you use windows os remove hashtag in first word
        menu.menu()

# function edit data tahun
def editTahun():
    for i in range(len(data.tahun)):
        TH__tmpil = i , data.tahun[i]
        print("%d %s"%TH__tmpil)

    indeksTH = int(input("Masukan angaka indeks yang ingin diubah: "))
    os.system("clear")
    if(indeksTH > len(data.tahun)):
        print(tampilkan_data.notFoud)
    else:
        dataThunNew = int(input("Masukan data yang baru: "))
        data.tahun[indeksTH] = dataThunNew

# function edit data Yi
def editYi():
    for i in range(len(data.Yi)):
        YI_tmpil = i , data.Yi[i]
        print("%d %s"% YI_tmpil)

    indeksYi = float(input("Masukan angaka indeks yang ingin diubah: "))
    os.system("clear")
    if (indeksYi > len(data.Yi)):
        print(tampilkan_data.notFoud)
    else:
        dataYiNew  = float(input("Masukan data yang baru: "))
        data.Yi[indeksYi] = dataYiNew
    
# function edit data Ui
def editUi():
    for i in range(len(data.Ui)):
        UI_tmpil = i, data.Ui[i]
        print("%d %s"% UI_tmpil)

    indeksUi = float(input("Masukan angaka indeks yang ingin diubah:")) 
    os.system("clear")
    if (indeksUi > len(data.Ui)):
        print(tampilkan_data.notFoud)
    else:
        dataUiNew = float(input("Masukan data yang baru: "))
        data.Ui[indeksUi] = dataUiNew



def kalimantan_love():
    print('WELCOME KALIMANTAN')

kalimantan_love()