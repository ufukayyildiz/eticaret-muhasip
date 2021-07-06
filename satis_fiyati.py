# "Kaça satmalı"nın cevabını verir.
# geliş + kar + KDV + kargo + komisyon = satış fiyatı

# AKK: Artı KDV Katsayısı (örn. %18 için 1.18)

# TEAKY: Tavsiye Edilen Asgari Kar Yüzdesi
# Yani, muhtemel bir iade vakasından ne kar ne zarar ile çıkmak için gereken kar yüzdesi.
# teaky=(kar/satis_fiyati)*100 ÖYLE Kİ kar=kargo

# TEASS: Tavsiye Edilen Asgari Satış Fiyatı = (kargo/teaky)*100

kargo = 15
komisyon_yuzdesi = float(input("Komisyon (%): "))
gelis = float(input("Geliş Fiyatı (TL): "))
kdv_yuzdesi = float(input("KDV (%): "))
akk = (kdv_yuzdesi/100 + 1)
teaky = (100 - komisyon_yuzdesi)/(akk*gelis + 2*kargo)*kargo
teass = (kargo/teaky)*100
print(f"Tavsiye Edilen Asgari Kar Yüzdesi: {round(teaky,2)}")
kar_yuzdesi = float(input("Kar (%): "))

k = (akk*gelis + kargo) / (100 - kar_yuzdesi - komisyon_yuzdesi)

print(f"\nSatış Fiyatı (TL): \t\t {round(100*k,2)}")
print(f"Kar (TL): \t\t\t {round(kar_yuzdesi*k,2)}")
print(f"Tavsiye Edilen Asgari Satış Fiyatı: {round(teass,2)}")
