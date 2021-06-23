satis_fiyati = float(input("Satış Fiyatı (TL): "))
kar_yuzdesi = float(input("Kar (%): "))

kar = satis_fiyati * (kar_yuzdesi/100)
print(f"Kar (TL): {round(kar,2)}")
