kargo = 15
hizmet_bedeli_yuzdesi = 0.8
komisyon_yuzdesi = 15
kar_yuzdesi = float(input("Kar Yüzdesi (%): "))
gelis = float(input("Geliş Fiyatı (TL): "))

k = ((gelis + kargo) / (100 - kar_yuzdesi - komisyon_yuzdesi - hizmet_bedeli_yuzdesi))

print(f"Satış Fiyatı: {round(100*k,2)}")
print(f"Kar: {round(22*k,2)}")
