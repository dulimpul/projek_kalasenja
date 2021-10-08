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
    print('[99] ~ kembali ke menu utama')
    print("\n")
    keyhit = int(input("Masukan pilihan :"))

    if keyhit == 1:
        os.system('clear')
        SemuaTabel()
        print('\n')
        input('enter to countinue')
        menuhitung()
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
    elif keyhit == 99:
        os.system('clear')
        menu.menu()
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

def Uipangakat2(lihatHsil2='null'):
    UiTB2 = data.Ui.copy()
    my_new_list = []
    for i in UiTB2:
        my_new_list.append(i ** 2)
    
    hasil2 = sum(my_new_list)

    if lihatHsil2 == 'countUi2':
        return hasil2
    else:
        return my_new_list

def Uipangakat4(lihatHsil='null'):
    UiTB4 = data.Ui.copy()
    my_new_list = []
    for u4 in UiTB4:
        my_new_list.append(u4 ** 4)

    hasil4  = sum(my_new_list)

    if lihatHsil == 'countUi4':
        return hasil4
    else:
        return my_new_list
    
def SemuaTabel():
    #jumlah banyak tabel
    a = TmpilTabeldataTh()
    
    # jumlaha yi keseluruhan
    b = TmpilanTabelYi()

    #Ui non pangkat jumlah
    c = TmpilanTbelUi()

    #Ui pangakat2 penjumlahan dan data tabel
    d = Uipangakat2()
    d2 = Uipangakat2(lihatHsil2='countUi2')

    # Ui pangkat4 penjumlahan dan data tabel
    e = Uipangakat4()
    e2 = Uipangakat4(lihatHsil='countUi4')
    
    # =======================================================
    print('='*30, 'HASIL TABEL', '='*30)
    
    # jumlaha keseluruhan tabel tahun
    print('\n')
    print('HASIL   n / TAHUN     =',a)

    # jumlah yi keseluruhan
    print('='*50)
    print('JUMLAH YI KESELURUHAN =',b)
    
    # Ui biasa
    print('='*50)
    print('JUMLAH Ui KESELURUHAN =',c)

    # untuk hasil dari Ui pangkat 2 (Ui2)
    print('='*50)
    print('HASIL DAN JUMLAH =',d)
    print('JUMLAH KESELURUHAN DARI Ui2 =',d2)

    # untuk hasil dari Ui pangkat 4 (Ui4)
    print('='*50)
    print('HASIL DARI Ui4                =',e)
    print('JUMLHA KESELURUHAN  DARI Ui4  =',e2)
    
    # hasil dari Yi kali Ui
    print('='*50)
    menghitungYIdanUI()

    # hasil dari Yi kali Ui pangkat 2
    print('='*50)
    MenghitungYidanUiPangakat()

def menghitungYIdanUI():
    YIclone = data.Yi.copy()
    Uiclone = data.Ui.copy()

    yi_kali_Ui = []

    for hitung in YIclone:
        hitung2 = hitung
    for hitung3 in Uiclone:
        yi_kali_Ui.append(hitung2 * hitung3)

    HasilAkhirUIYI = sum(yi_kali_Ui)
    print('HASIL PERKALIAN YI DAN UI ADALAH =',yi_kali_Ui)
    print('TOTAL PERKALIAN YI DAN UI ADALAH =', HasilAkhirUIYI)

def MenghitungYidanUiPangakat():
    YIclone2 = data.Yi.copy()
    YiKaliUi2 = Uipangakat2(lihatHsil2='null').copy()

    yi_kali_ui2 = []

    for HitungUI2 in YiKaliUi2:
        UI2pangkat = HitungUI2
    
    for HitungUIYI2 in YIclone2:
        yi_kali_ui2.append(HitungUIYI2 * UI2pangkat)

    HasilAkhirUIYI2 = sum(yi_kali_ui2)

    print('HASIL  PERKALIAN YI DAN UI PANGKAT 2 ADALAH =',yi_kali_ui2)
    print('TOTAL  PERKALIAN YI DAN UI PANGKAT 2 ADALAH =', HasilAkhirUIYI2)