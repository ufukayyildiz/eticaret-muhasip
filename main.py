hizmet_bedeli_yuzdesi = 0.8
komisyon_yuzdesi = 15
kar_yuzdesi = 22

kargo = 15
gelis = float(input("Geliş Fiyatı: "))

satis_fiyati = ((gelis + kargo) / (100 - kar_yuzdesi - komisyon_yuzdesi - hizmet_bedeli_yuzdesi)) * 100

print(round(satis_fiyati,2))
