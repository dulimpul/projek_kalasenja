import menu
import os
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
        print("masukan")
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
