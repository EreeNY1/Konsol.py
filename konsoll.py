def k_kucuk(int,list):  # 1.Soru

    list.sort()

    sayi_siralama = list[int - 1]

    print("-----------------------------------------------------------------------------------")

    print("Listedeki Sayılar: ",list)
    print("K'ıncı Eleman:",int)
    print("K'ıncı En Küçük Elemanı",sayi_siralama)

    print("-----------------------------------------------------------------------------------")

def en_yakin_cift(int, liste): #2.Soru

    liste.sort() # listedeki elemanları küçükten büyüğe sıralar

    yakintoplam = float('inf')  #Bulduğumuz en yakın toplamı saklamamıza yardımcı olucak
    en_yakin_cift = None #Bulduğumuz en yakın çifti saklamamıza yardımcı olucak

    i, j = 0, len(liste) - 1  # "i" listenin başını "j" ise sonunu göstericek

    while i < j:    # while ile çift toplamları kontrol edicez
        toplam = liste[i] + liste[j]


        if toplam == int:
            en_yakin_cift = (liste[i], liste[j]) #istedğimiz sayıya eşitse biter
            break


        if abs(toplam - int) < abs(yakintoplam - int):  #Şu ana kadar bulunandan daha yakınsa devreye girer
            yakintoplam = toplam
            en_yakin_cift = (liste[i], liste[j])

        if toplam < int:        # "i" bir artırdık "j" bir azalttık işaretçileri birbirne yaklaştırdık
            i += 1              #yoksa döngü sonsuzluğa dönerdi
        else:
            j -= 1

    return en_yakin_cift



def tekrar_eden_eleman(list): #3.Soru

    liste_tasi = []

    for i in list:
        if list.count(i) > 1 and i not in liste_tasi:
            liste_tasi.append(i)

    print("-----------------------------------------------------------------------------------")
    print("Tekrar Eden Elemanlar : ",liste_tasi)
    print("-----------------------------------------------------------------------------------")
    print()


from functools import reduce


def matris_carpimi(matris1, matris2): #4.Soru

    satir1 = matris1
    sutun1 = matris1[0]


    satir2 = matris2
    sutun2 = matris2[0]


    matris2 = list(map(list, zip(*matris2))) # İkinci matrisin satır sütün değiş


    sonuc = [[sum(x * y for x, y in zip(satir1, sutun2)) for sutun2 in matris2] for satir1 in matris1] #Sonucu Hesaplar

    return sonuc

X = [[1, 2, 3], [4, 5, 6]]
Y = [[7, 8], [9, 10], [11, 12]]

from functools import reduce
def kelime_frekansi(dosya_adi): #5.Soru
    try:

        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            metin = dosya.read()

        kelimeler = metin.lower().split()
        frekanslar = reduce(lambda x, y: {**x, y: x.get(y, 0) + 1}, kelimeler, {})

        return frekanslar

    except FileNotFoundError:
        return "Dosya bulunamadı"
    except Exception as e:
        return f"Hata: {str(e)}"



def en_kucuk_deger(liste): #6.Soru

    if len(liste) == 0:
        return 0

    if len(liste) == 1:
        return liste[0]

    listenin_ilk_elemani = liste[0]

    geri_kalanlar = en_kucuk_deger(liste[1:])

    if listenin_ilk_elemani < geri_kalanlar:
        return listenin_ilk_elemani
    else:
        return geri_kalanlar


liste = [2,14,7,-3]


def ebob(sayi1, sayi2): #8.Soru
    while sayi2 != 0:
        sayi1, sayi2 = sayi2, sayi1 % sayi2

    print("-----------------------------------------------------------------------------------")
    print("En Büyük Ortak Bölen: ",sayi1)
    print("-----------------------------------------------------------------------------------")
    print()
    print()

def asal_veya_degil(sayi,bolen = 2): #9.Soru
    if sayi <= 1:
        return "1'den Büyük Bir Sayi Giriniz !"


    if bolen * bolen > sayi:
        return True

    if sayi % bolen == 0:
        return False

    return asal_veya_degil(sayi,bolen + 1)


while True:
    print("********* Console Menu *********")
    print()
    print("1) K'nıncı En Küçük Elemanı Bulma")
    print("2) En Yakın Çifti Bulma")
    print("3) Bir Listenin Tekrar Eden Elemanlarını Bulma")
    print("4) Matris Çarpımı")
    print("5) Bir Text Dosyasındaki Kelimelerin Frekansını Bulma")
    print("6) Liste İçinde En Küçük Değeri Bulma")
    print("8) En Büyük Ortak Bölen")
    print("9) Asallık Testi")
    print("11) Çıkış")



    secim = int(input("Hangi Soruyu Açmak İsiyorsunuz? (1/2/3/4/5/6/8/9) (Çıkış İçin = 11) : "))
    print()

    if secim == 1:
        k_kucuk(3,[7,10,4,3,20,15])
    print()
    print()

    if secim == 2:
        sayi2 = 54
        liste = [10, 22, 28, 29, 30, 40]
        yakin = en_yakin_cift(sayi2, liste)
        hepsi = (sayi2, liste)
        print(yakin)
        print("-----------------------------")
        print(hepsi)

    if secim == 3:
        tekrar_eden_eleman([1,2,3,2,1,5,6,5,5,5,5])
    print()
    print()

    if secim == 4:
        sonuc = matris_carpimi(X, Y)

        print("-----------------------------------------------------------------------------------")
        for satir in sonuc:
            print(satir)

        print("-----------------------------------------------------------------------------------")
        print()

    if secim == 5:
        dosya_adi = 'odev.txt'
        frekanslar = kelime_frekansi(dosya_adi)

        for kelime, frekans in frekanslar.items():
            print(f"{kelime}={frekans}")



    if secim == 6:
        print("-----------------------------------------------------------------------------------")
        print("En Küçük Değer:", en_kucuk_deger(liste))
        print("-----------------------------------------------------------------------------------")
        print()
        print()

    if secim == 8:
        ebob(48, 18)


    if secim == 9:
        print(asal_veya_degil(7))

    if secim == 11:
        print("Program Sonlanıyor...")
        exit()





