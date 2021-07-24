# "Kaça satmalı"nın cevabını verir.
# geliş + kar + KDV + kargo + komisyon = satış fiyatı

# AKK: Artı KDV Katsayısı (örn. %18 için 1.18)

# TEAKY: Tavsiye Edilen Asgari Kar Yüzdesi
# Yani, muhtemel bir iade vakasından ne kar ne zarar ile çıkmak için gereken kar yüzdesi.
# teaky=(kar/satis_fiyati)*100 ÖYLE Kİ kar=kargo

# TEASS: Tavsiye Edilen Asgari Satış Fiyatı = (kargo/teaky)*100

kdv_yuzdesi = float(input("KDV (%): "))
komisyon_yuzdesi = float(input("Komisyon (%): "))
gelis = float(input("Geliş Fiyatı (TL): "))
kargo = float(input("Kargo Ücreti (TL): "))
akk = (kdv_yuzdesi/100 + 1)
teaky = (100 - komisyon_yuzdesi)/(akk*gelis + 2*kargo)*kargo
teass = (kargo/teaky)*100
print(f"Tavsiye Edilen Asgari Kar Yüzdesi: {round(teaky,2)}")
kar_yuzdesi = float(input("Kar (%): "))

k = (akk*gelis + kargo) / (100 - kar_yuzdesi - komisyon_yuzdesi)
satis_fiyati = 100*k

print(f"\nSatış Fiyatı:\t\t\t\t{round(satis_fiyati)} TL = {round((satis_fiyati - kargo),2)} TL + {kargo} TL")
print(f"Kar:\t\t\t\t\t{round(kar_yuzdesi*k,2)} TL")
print(f"\nTavsiye Edilen Asgari Satış Fiyatı:\t{round(teass,2)} TL = {round((teass - kargo),2)} TL + {kargo} TL")
print(f"Kar:\t\t\t\t\t{round(teaky*k,2)} TL")
