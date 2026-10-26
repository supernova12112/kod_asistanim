"""
ad= "supernova121"
yaş=83
print("ad:",ad, "yaş:",83 )

karsilama = "Merhaba " + "supernova121"
print(karsilama)

kullanici = "supernova121"
islem_adedi = 5
print(f"Hoş geldiniz {kullanici}. Bugün yapay zekâ ile {islem_adedi} kod denetlediniz.")

print("Siber", "Güvenlik", "Mühendisliği", sep="-")

print("Kod denetimi başladı...", end=" [BAŞARILI] ")
print("Sistem kararlı.")
"""

"""mevcut_yil = 2026
dogum_yili = int(input("Lütfen doğum yılınızı giriniz: "))
kullanici_yasi = mevcut_yil - dogum_yili
print(f"Doğum Yılınız: {dogum_yili} | Hesaplanan Yaşınız: {kullanici_yasi}")
"""

tl_miktari_input = input("Kumbaraya eklenen TL miktarını giriniz: ")
doviz_kuru_input = input("Bugünkü güncel döviz kurunu giriniz (Örn: 34.55): ")

tl_miktari = float(tl_miktari_input)
doviz_kuru = float(doviz_kuru_input)

doviz_karsiligi = tl_miktari / doviz_kuru

print(f"\n--- Kumbara Asistanı Raporu ---")
print(f"Kumbaraya Eklenen Tutar: {tl_miktari:.2f} TL")
print(f"Kullanılan Döviz Kuru: {doviz_kuru:.2f}")
print(f"Kumbaranızdaki Paranın Döviz Karşılığı: {doviz_karsiligi:.2f} Birim")