from data import *
import time
import menu
import os


notFoud ="""
#  ./$$.../$$../$$$$$$../$$$$$$$$......./$$$$$$$$./$$$$$$../$$.../$$./$$.../$$./$$$$$$$.
#  |.$$$.|.$$./$$__..$$|__..$$__/......|.$$_____//$$__..$$|.$$..|.$$|.$$$.|.$$|.$$__..$$
#  |.$$$$|.$$|.$$..\.$$...|.$$.........|.$$.....|.$$..\.$$|.$$..|.$$|.$$$$|.$$|.$$..\.$$
#  |.$$.$$.$$|.$$..|.$$...|.$$.........|.$$$$$..|.$$..|.$$|.$$..|.$$|.$$.$$.$$|.$$..|.$$
#  |.$$..$$$$|.$$..|.$$...|.$$.........|.$$__/..|.$$..|.$$|.$$..|.$$|.$$..$$$$|.$$..|.$$
#  |.$$\..$$$|.$$..|.$$...|.$$.........|.$$.....|.$$..|.$$|.$$..|.$$|.$$\..$$$|.$$..|.$$
#  |.$$.\..$$|..$$$$$$/...|.$$.........|.$$.....|..$$$$$$/|..$$$$$$/|.$$.\..$$|.$$$$$$$/
#  |__/..\__/.\______/....|__/.........|__/......\______/..\______/.|__/..\__/|_______/.
        """

def showsDataMenu():
    print("\n \n")
    print("="*20, "MENU TAMPILKAN DATA", "="*20)
    print("\n")
    print("[1]~ Tampilakan Data Tahun")
    print("[2]~ Tampilakan Data YI")
    print("[3]~ Tampilakn Data  UI")
    print("[99]~ Kembali ke menu awal")
    print("\n")
    kunci = int(input("MASUKAN KEY YANG ADA DI SAMPING LIST : "))

    if kunci == 1 :
        time.sleep(2)
        print("====> 45%")
        time.sleep(2)
        print("=======> 65%")
        time.sleep(2)
        print("==========> 100%")
        time.sleep(0.6)
        print("\n")
        ShowDataTh() #------------------------------------------>
        print("\n")
        input("input anything key untuk kembali ~")
        time.sleep(2)
        print("kembali ke menu====> 45%")
        time.sleep(2)
        print("kembali ke menu=======> 65%")
        time.sleep(2)
        print("kembali ke menu==========> 100%")
        time.sleep(0.6)
        # os.system("cls")
        os.system("clear")
        showsDataMenu()
    elif kunci == 2:
        time.sleep(2)
        print("====> 45%")
        time.sleep(2)
        print("=======> 65%")
        time.sleep(2)
        print("==========> 100%")
        time.sleep(0.6)
        print("\n")
        showDataYi() # --------------------------------------->
        print("\n")
        input("input anything key untuk kembali ~")
        time.sleep(2)
        print("kembali ke menu====> 45%")
        time.sleep(2)
        print("kembali ke menu=======> 65%")
        time.sleep(2)
        print("kembali ke menu==========> 100%")
        time.sleep(0.6)
        # os.system("cls")
        os.system("clear")
        showsDataMenu()
    elif kunci == 3:
        time.sleep(2)
        print("====> 45%")
        time.sleep(2)
        print("=======> 65%")
        time.sleep(2)
        print("==========> 100%")
        time.sleep(0.6)
        print("\n")
        showDataUi()
        print("\n")
        input("input anything key untuk kembali ~")
        time.sleep(2)
        print("kembali ke menu====> 45%")
        time.sleep(2)
        print("kembali ke menu=======> 65%")
        time.sleep(2)
        print("kembali ke menu==========> 100%")
        time.sleep(0.6)
        # os.system("cls")
        os.system("clear")
        showsDataMenu()
    elif kunci == 99:
        # os.system("cls")
        os.system("clear")
        menu.menu()
    else:
        showsDataMenu(

        )

def ShowDataTh():
    if len(tahun) <= 0:
        print(notFoud) 
    else:
        for v,g in enumerate (tahun, start=1):
             print(v,g)

        # for indeksth in range(len(tahun)):
        #     dataTHun = indeksth, tahun[indeksth]
        #     print("%d %s" % dataTHun)

   

def showDataYi():
    if len(Yi) <= 0:
        print(notFoud) 
    else:
        for indeks in range(len(Yi)):
            print("%d %s" % (indeks, Yi[indeks]))

def showDataUi():
    if len(Ui) <= 0:
        print(notFoud)
    else:
        for indeks in range(len(Ui)):
            print("%d %s" % (indeks, Ui[indeks]))

