def baca_pemasukan(filename):
    file = open(filename, "r")
    teks = file.readline().replace("\n","")

    pemasukan = {}

    while teks != "STOP":
        list_kata = teks.split()
        list_kata2 = (list_kata[0],list_kata[1])
        if int(list_kata[2]) > 0:
            pemasukan[list_kata2] = int(list_kata[2])
        teks = file.readline().replace("\n","")
    
    file.close()


    return(pemasukan)

def baca_pengeluaran(filename):
    file = open(filename, "r")
    teks = file.readline().replace("\n","")

    pengeluaran = {}

    while teks != "STOP":
        list_kata = teks.split()
        list_kata2 = (list_kata[0],list_kata[1])
        if int(list_kata[2]) < 0:
            pengeluaran[list_kata2] = int(list_kata[2])
        teks = file.readline().replace("\n","")
    
    file.close()


    return(pengeluaran)

def rerata(masuk, keluar):
    list1 = masuk.values()
    list2 = keluar.values()
    panjang1 = len(masuk)
    panjang2 = len(keluar)
    x = sum(list1)
    y = sum(list2)
    rata2 = (x+y)/(panjang1 + panjang2)
    return rata2

def tertinggi(masuk):
    maks = 0
    for k, v in masuk.items():
        if (v > maks):
            maks = v
            x = k
    return x

def main():
    nama_file = "contoh_file.txt"
    masuk = (baca_pemasukan(nama_file))
    keluar = (baca_pengeluaran(nama_file))
    print("Rata-rata: ",rerata(masuk,keluar))
    print("Tertinggi: ",tertinggi(masuk))

if __name__ == "__main__":
    main()




















