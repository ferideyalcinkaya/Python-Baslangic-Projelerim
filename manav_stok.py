#python projemize hoşgeldiniz

stok_durumu=[["elma",50,5],
             ["muz",35,10],
             ["nar",40,6],
             ["erik",20,30],
             ["kiraz",35,15],
             ["karpuz",40,11]]

sepet=[]
toplam_tutar=0

print("Hoşgeldin!! İyi alışverişler..")
print("Mevcut ürünlerimiz: ")

for satir in stok_durumu:                                             #stok_durumunu liste halinde yazdırır
    print(f"{satir[0]} | Stok: {satir[1]} kg | Fiyat: {satir[2]} TL")


while True:
    print("\nHangi meyvemizden almak istersin? :) (Çıkmak için 'q' yazın)")
    meyve_adi = input("Hangi meyve? ")
    if meyve_adi=='q': break


    bulundu=False

    for satir in stok_durumu:
        if satir[0]==meyve_adi:
            bulundu=True
            print("istediğiniz meyve stokta bulunmaktadır ..")

            print("Kaç kg almak istersin?")
            kg=int(input("kg?"))
        
            if satir[1]>=kg:
                print("Stok yeterli, sepete ekleniyor...")
                satir[1] -= kg # O çekmecedeki stok miktarını güncelliyoruz
                if satir[1]<5:
                    print(f"Stok uyarısı {satir[0]}  eşik değerin (5kg) altına düştü..")
                fiyat= kg * satir[2]
                toplam_tutar += fiyat
                sepet.append([meyve_adi, kg])

                print("sepete eklendi,tutar: " + str(toplam_tutar))
                
            else:
                print(f"Maalesef stok yetersiz! Elimizde sadece {satir[1]} kg var.")
            break 

    if bulundu==False :
        print("maalesef aradığınız meyve bizde yok :( ")


     # FİŞ YAZDIRMA: Alışveriş bittiğinde sepeti gösteriyoruz.
print("\n--- ALIŞVERİŞİNİZ TAMAMLANDI ---")
print(f"Toplam Ödemeniz Gereken Tutar: {toplam_tutar} TL")
print("Bizi tercih ettiğiniz için teşekkürler!")
   
 



