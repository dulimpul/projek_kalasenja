import menu
import os
import data
import numpy as np

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
        os.system('clear')
        menuhitung()
    elif keyhit == 2:
        os.system('clear')
        A_B_C_nilia()
        print('\n')
        input('enter to countinue')
        os.system('clear')
        menuhitung()
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

# fungsi tahun
def TmpilTabeldataTh():
    tahun_akhir = len(data.tahun) 
    return tahun_akhir
  
# fungsi yi
def TmpilanTabelYi():
    YiTB = data.Yi.copy()
    hasilTByi = sum(YiTB)
    return hasilTByi

# fungsi ui
def TmpilanTbelUi():
    UiTB = data.Ui.copy()
    hasilTbui = sum(UiTB)
    return hasilTbui

# fungsi ui pangkat 2
def Uipangakat2(lihatHsil2='null'):
    global hasil2
    UiTB2 = data.Ui.copy()
    my_new_list = []
    for i in UiTB2:
        my_new_list.append(i ** 2)
    
    hasil2 = sum(my_new_list)

    if lihatHsil2 == 'countUi2':
        return hasil2
    else:
        return my_new_list

# fungsi Ui pangkat 4
def Uipangakat4(lihatHsil='null'):
    global hasil4
    UiTB4 = data.Ui.copy()
    my_new_list = []
    for u4 in UiTB4:
        my_new_list.append(u4 ** 4)

    hasil4  = sum(my_new_list)

    if lihatHsil == 'countUi4':
        return hasil4
    else:
        return my_new_list

# fungsi menghitung ui dan yi 
def menghitungYIdanUI():
    global HasilAkhirUIYI
    YIclone = data.Yi.copy()
    Uiclone = data.Ui.copy()

    a = np.array(YIclone)
    b = np.array(Uiclone)
    
    yi_kali_Ui = a * b
    HasilAkhirUIYI = sum(yi_kali_Ui)
    print('HASIL PERKALIAN YI DAN UI ADALAH =',yi_kali_Ui)
    print('TOTAL PERKALIAN YI DAN UI ADALAH =', HasilAkhirUIYI)

# fungsi menghitung yi dan ui pangakat 2
def MenghitungYidanUiPangakat():
    global HasilAkhirUIYI2
    YIclone2 = data.Yi.copy()
    YiKaliUi2 = Uipangakat2(lihatHsil2='null').copy()

    a = np.array(YIclone2)
    b = np.array(YiKaliUi2)
    yi_kali_ui2 = a * b
    HasilAkhirUIYI2 = sum(yi_kali_ui2)

    print('HASIL  PERKALIAN YI DAN UI PANGKAT 2 ADALAH =',yi_kali_ui2)
    print('TOTAL  PERKALIAN YI DAN UI PANGKAT 2 ADALAH =', HasilAkhirUIYI2)


# fungsi menapilkana hasil jumlah tabel
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

# =============================================new fungsi============================================================


def mencarinilai_B():
    vaktorA = HasilAkhirUIYI / hasil2
    return vaktorA
def mencarinilai_C():

    # varibake satu 
    tahun_y = TmpilTabeldataTh()
    ui2_x = hasil2
    yijumlah = TmpilanTabelYi()

    # varibek ke dua 
    ui4_x = hasil4
    yiUIpangkat4 = HasilAkhirUIYI2

#     solnya = 9x + 60y = 4.7
#           60x + 708y =32.62

    m_list = [[tahun_y,ui2_x], [ui2_x, ui4_x]]
    
    A = np.array(m_list)
    B = np.array([yijumlah,yiUIpangkat4])

    inv_A = np.linalg.inv(A)
    C_hasil_akhir = inv_A.dot(B)
    X = np.linalg.inv(A).dot(B)
    return C_hasil_akhir[1]

def mencari_nilai_A():
    # varibel
    tahun_A = TmpilTabeldataTh() # masih ada bug yakni di tahunya apabila hanya 1 data harus 2 data
    ui2_A = hasil2
    nilaiC_A = mencarinilai_C()
    YIjumlah_A = TmpilanTabelYi()

    # perhitungan
    perkalina_Th_dan_nilaic = nilaiC_A * ui2_A
    pengurangan_tahun = YIjumlah_A - perkalina_Th_dan_nilaic
    NiliaAkhir_A = pengurangan_tahun / tahun_A
    return NiliaAkhir_A

def A_B_C_nilia(): 
    print('A =', mencari_nilai_A())
    print('B =', mencarinilai_B())
    print('C =', mencarinilai_C())
