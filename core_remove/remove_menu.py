import data
import menu
import os
def menuhapus():
    print("="*20,"MENU HAPUS", "="*20 )
    print("\n")
    print("[1]~ Hapus data Tahun")
    print("[2]~ Hapus data Yi")
    print("[3]~ Hapus data Ui")
    print("[99]~ Kembali menu utama")
    print("\n")

    keyHapus = int(input("Masukan pilihan :"))

    if keyHapus == 1:
        os.system("clear")
        hapusTh()
    if keyHapus == 2:
        os.system("clear")
        hapusYi()
    if keyHapus == 3:
        os.system("clear")
        hapusUi()
    if keyHapus == 99:
        os.system("clear")
        menu.menu()

# fungsi hapus data tahun

def hapusTh():
    for v,g in enumerate (data.tahun):
        print(v,g)
    # for i in range(len(data.tahun)):
    #     TH__tmpil = i , data.tahun[i]
    #     print("%d %s"%TH__tmpil)

    if 0 >= len(data.tahun) :
        menuhapus()
    else:
        hapus_THUN = int(input("Masukan angka yang ada di list atas :"))
        data.tahun.remove(data.tahun[hapus_THUN])
        menuhapus()

# fungsi hapus data Yi 

def hapusYi():
    for v,g in enumerate(data.Yi):
        print(v,g)
    if 0 >= len(data.Yi):
        menuhapus
    else:
        hapus_YI = int(input("Masukan angka yang ada di list atas :"))
        data.Yi.remove(data.Yi[hapus_YI])
        menuhapus()

# fungsi hapus data Ui 

def hapusUi():
    for v,g in enumerate(data.Ui):
        print(v,g)

    if 0 >= len(data.Ui):
        menuhapus()
    else:
        hapus_UI = int(input("Masukan angka yang ada di list atas :"))
        data.Ui.remove(data.Ui[hapus_UI])
        menuhapus()