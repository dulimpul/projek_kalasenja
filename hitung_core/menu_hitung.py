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
    return tahunTB
  

def TmpilanTabelYi():
    YiTB = data.Yi.copy()
    hasilTByi = sum(YiTB)
    return hasilTByi

def TmpilanTbelUi():
    UiTB = data.Ui.copy()
    hasilTbui = sum(UiTB)
    return hasilTbui

def Uipangakat2():
    UiTB2 = data.Ui.copy()
    my_new_list = []
    for i in UiTB2:
        my_new_list.append(i ** 2)
    
    hasil2 = sum(my_new_list)
    
    return my_new_list,hasil2

def Uipangakat4():
    UiTB4 = data.Ui.copy()
    my_new_list = []
    for u4 in UiTB4:
        my_new_list.append(u4 ** 4)

    hasil4  = sum(my_new_list)
    return my_new_list,hasil4


def SemuaTabel():
    a = TmpilTabeldataTh()
    b = TmpilanTabelYi()
    c = TmpilanTbelUi()
    d = Uipangakat2()
    e = Uipangakat4()

    print('='*30, 'HASIL TABEL', '='*30)
    print('HASIL n          =',a)
    print('JUMLAH YI        =',b)
    print('JUMLAH UI        =',c)
    print('HASIL DAN JUMLAH =',d)
    print('HASIL DAN JUMLAH =',e)
    