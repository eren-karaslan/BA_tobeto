#1.soru
boy = float(input("Lütfen boyunuzu metre cinsinden girin: "))
kilo = float(input("Lütfen kilonuzu girin: "))


vki = kilo / (boy ** 2)


print("Vücut Kitle İndeksi (VKİ):", vki)

#2.soru
maas=float (input("Maaşı Giriniz : "))
zam=float (input("Zam Oranı(%) : "))
yeniMaas=(maas)+((maas)*(zam)/100)
print("Zamlı Maaş :",yeniMaas)

#3. soru
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
sayi3 = float(input("Üçüncü sayıyı girin: "))
max_sayi = max(sayi1, sayi2, sayi3)
print("En büyük sayı:", max_sayi)

#alternatif
if sayi1>= sayi2 and sayi1>= sayi3:
    buyuk_sayi = sayi1
elif sayi2>= sayi3 and sayi2>= sayi1:
    buyuk_sayi = sayi2
else:
    buyuk_sayi = sayi3
print("En büyük sayı:", buyuk_sayi)

#4. soru
import math
yaricap = float(input("Dairenin yarıçapını girin: "))
alan = math.pi * yaricap**2
cevre = 2 * math.pi * yaricap
print("Dairenin Alanı:", alan)
print("Dairenin Çevresi:", cevre)

#5.soru
sayi=int(input("sayi giriniz "))

sayinin_ilk_hali=sayi
sayinin_son_hali=0

while (sayi!=0):
    son_basamak = sayi % 10
    sayi=sayi//10
    sayinin_son_hali= (sayinin_son_hali*10) + son_basamak

if(sayinin_ilk_hali == sayinin_son_hali):
  print("Bu sayi bir palindrome sayidir ")
else:
  print("Bu sayi bir palindrome sayi değildir")


 #alternatif
  sayi = input("Sayı giriniz: ")
sayinin_tersi = sayi[::-1]
if sayi == sayinin_tersi:
    print("Girdiğiniz sayı palindromdur.")
else:
    print("Girdiğiniz sayı palindrom değildir.")



