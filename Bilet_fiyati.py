# Python_Al-t-rmalar
# if-elif-else ile uzun bir çözümdür ..

print("Uçak-Ekonomi-200",
      "Uçak-Business-300",
      "Tren-1-80",
      "Tren-2-120",
      "Otobüs-*-90")
vasıta=input("Vasıta giriniz : ").lower().strip()
sınıf=input("Sınıf giriniz : ").lower().strip()

if vasıta=="uçak":
    if sınıf=="ekonomi":
        print("Bilet fiyatı : 200 ")
    elif sınıf=="business":
        print(" Bilet fiyatı : 300 ")
    else:
        print("Geçersiz sınıf ")
elif vasıta=="tren":
    if sınıf=="1":
        print("Bilet fiyatı :80 ")
    elif sınıf=="2":
        print("Bilet fiyatı : 120 ")
    else:
        print("Geçersiz sınıf ")
elif vasıta=="otobüs":
    if sınıf=="*":
        print("Bilet fiyatı : 90 ")
    else:
        print("Geçersiz sınıf ")
        
else:
    print("Geçersiz Taşıt ")
