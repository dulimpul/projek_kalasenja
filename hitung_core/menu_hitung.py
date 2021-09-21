import menu
import os
import data

def menuhitung():
    print("="*50, "MENU HITUNG", "="*50)
    print("\n")
    print("[1] ~ Tampilkan hasil penjumlahan tabel")
    print("[2] ~ Perhitungan A,B,C")
    print("[3] ~ Perhitungan Yn")
    print("[4] ~ Perhitungan jumlah penduduk")
    print("[5] ~ Perhitungan ysst")
    print("[6] ~ Perhitungan kabel")
    print("\n")
    keyhit = int(input("Masukan pilihan :"))

    if keyhit == 1:
        SemuaTabel()
    elif keyhit == 2:
        print("lorem ip sum")
    elif keyhit == 3:
        print("lorem ip sum")
    elif keyhit == 4:
        print("lorem ip sum")
    elif keyhit == 5:
        print("lorem ip sum")
    elif keyhit == 6:
        print("lorem ip sum")
    else:
        os.system("clear") # Linux
        menu.menu()


def TmpilTabeldataTh():
    tahunTB = len(data.tahun) 
    print(tahunTB)
  

def TmpilanTabelYi():
    YiTB = data.Yi.copy()
    hasilTByi = sum(YiTB)
    print(hasilTByi)

def TmpilanTbelUi():
    UiTB = data.Ui.copy()
    hasilTbui = sum(UiTB)
    print(hasilTbui)

def Uipangakat2():
    UiTB2 = data.Ui.copy()
    my_new_list = []
    for i in UiTB2:
        my_new_list.append(i ** 2)

    print(my_new_list)

def SemuaTabel():
    print("="*30, "Jumlah tabel tahun(n)", "="*30)
    TmpilTabeldataTh()
    print("="*30, "Jumlah YI", "="*30)
    TmpilanTabelYi()
    print("="*30, "Jumlah UI", "="*30)
    TmpilanTbelUi()
    print("="*30, "Jumlah UI PANGAKAT 2", "="*30)
    Uipangakat2()
