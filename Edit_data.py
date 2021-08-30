import tampilkan_data  
import menu
import time

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
        editTahun()
        time.sleep(5)
        editDataMenu()
    elif keyEdit == 2:
        print("berhasil")
        time.sleep(5)
        editDataMenu()
    elif keyEdit == 3:
        print("berhasil")
        time.sleep(5)
        editDataMenu()
    elif keyEdit == 99:
        menu.menu()


def editTahun():
    print("") # masih bingung menampilkan data nya
    indeks = input("Masukan angka yang ada di samping list: ")
    if(indeks > len(tampilkan_data.tahun)):
        print(tampilkan_data.notFoud)
    else:
        dataThunNew = int(input("Masukan data yang baru: "))
        tampilkan_data.tahun[indeks] = dataThunNew