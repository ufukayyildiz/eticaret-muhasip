# "Bize ne bırakıyor/kalıyor?"un cevabını verir.
# geliş + kar + KDV + kargo + komisyon = satış fiyatı

kdv_yuzdesi = float(input("KDV (%): "))
komisyon_yuzdesi = float(input("Komisyon (%): "))
gelis = float(input("Geliş Fiyatı (TL): "))
kargo = float(input("Kargo Ücreti (TL): "))
satis_fiyati = float(input("Kargo DAHİL Satış Fiyatı (TL): "))

akk = 1 + kdv_yuzdesi/100

kar = satis_fiyati - akk*gelis - kargo - satis_fiyati*komisyon_yuzdesi/100

print(f"\nKar (TL): {round(kar,2)}")
print(f"Kar Oranı (%): {round((kar/satis_fiyati)*100,1)}")
