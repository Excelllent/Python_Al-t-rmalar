# Python_Al-t-rmalar
#Yazdığımız kelimeleri tersten yazar


kelime=input("Kelime giriniz : ")
ters=""

uzunluk=len(kelime)
i= - 1

while i>= -uzunluk:
    ters=ters+kelime[i]
    i= i-1
print(ters)
