# "Bize ne bırakıyor/kalıyor?"un cevabını verir.

hizmet_bedeli_yuzdesi = 0.8
kargo_ucreti = 15
satis_fiyati = float(input("Satış Fiyatı (TL): "))
gelis = float(input("Geliş Fiyatı (TL): "))
komisyon_yuzdesi = float(input("Komisyon (%): "))

kar = satis_fiyati - gelis - satis_fiyati*(hizmet_bedeli_yuzdesi + komisyon_yuzdesi)/100 - kargo_ucreti

print(f"\nKar (TL): {round(kar,2)}")
print(f"Kar Oranı (%): {round((kar/satis_fiyati)*100,1)}")
