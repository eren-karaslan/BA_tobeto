#1. SORU
#İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.
uzunluk = int(input("Fibonacci serisinin uzunluğunu girin: "))

fibonacci = [1, 1]

while len(fibonacci) < uzunluk:
    next_number = fibonacci[-1] + fibonacci[-2]  # Son iki sayının toplamı
    fibonacci.append(next_number)

print("Fibonacci Serisi:", fibonacci)

#2.SORU
#Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.
sayi=int(input("sayi giriniz: "))
total = 0
for i in range(1,sayi):
    if sayi%i ==0:
        total += i
if sayi == total:
    print("mükemmel sayı")
else: print("mükkemmel sayı değil")

#3.SORU
#Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.
birinciSayi = int(input("Birinci Sayıyı Giriniz : "))
ikinciSayi = int(input("İkinci Sayıyı Giriniz : "))
 
if (birinciSayi > ikinciSayi):
    kucuksayi = ikinciSayi
else:
    kucuksayi = birinciSayi
for i in range(1,kucuksayi+1):
    if (birinciSayi % i==0) and (ikinciSayi%i ==0):
        ebob = i
        ekok = (birinciSayi*ikinciSayi)//ebob

print ("EBOB:", ebob)
print ("EKOK:", ekok)

#4.SORU
#Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.
sayi = int(input("Sayiyi Girin : "))
if sayi > 1:
    for i in range(2, sayi):
        if (sayi % i) == 0:
            print("{} Asal Sayi Degildir.".format(sayi))
            break
    else:
        print("{} Asal Sayidir.".format(sayi))
else:
    print("{} Asal Sayi Degildir.".format(sayi))
#5.SORU
#Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız.
def asal_carpanlar(sayi):
    carpanlar = []
    i = 2
    while sayi > 1:
        if sayi % i == 0:
            carpanlar.append(i)
            sayi = sayi // i
        else:
            i = i + 1
    return carpanlar

def tekrarsiz_asal_carpan(liste):
    son_liste=[]
    for i in range(len(liste)):
        tekrar=False
        for j in range(i+1,len(liste)):
            if(liste[i]==liste[j]):
                tekrar=True
                break
        if(tekrar == False):
            son_liste.append(liste[i])
    
    return son_liste

sayi = int(input("Bir sayi girin: "))
print(f"{sayi} 'nin asal çarpanları {tekrarsiz_asal_carpan(asal_carpanlar(sayi))} sayılarıdır")
