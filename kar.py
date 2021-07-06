# "Bize ne bırakıyor/kalıyor?"un cevabını verir.
# geliş + kar + KDV + kargo + komisyon = satış fiyatı

kargo = 15
satis_fiyati = float(input("Satış Fiyatı (TL): "))
gelis = float(input("Geliş Fiyatı (TL): "))
kdv_yuzdesi = float(input("KDV (%): "))
komisyon_yuzdesi = float(input("Komisyon (%): "))

akk = (1 + kdv_yuzdesi/100)

kar = satis_fiyati - akk*gelis - kargo - satis_fiyati*komisyon_yuzdesi/100

print(f"\nKar (TL): {round(kar,2)}")
print(f"Kar Oranı (%): {round((kar/satis_fiyati)*100,1)}")
