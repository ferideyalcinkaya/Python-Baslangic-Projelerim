# Python-Baslangic-Projelerim
İlk başlangıç projesi olarak "Manav & Kasa Yönetim Sistemi" yapacağız.

🍎 Manav & Kasa Yönetim Sistemi 

Bu proje, Python'da "matrisler (2D Lists), iç içe döngüler ve fonksiyonel programlama" mantığını kullanarak geliştirilmiş bir stok ve satış simülasyonudur. Basit bir hesap makinesinden öte, gerçek dünya senaryolarına uygun mantıksal kontrol mekanizmaları içerir.


🚀 Yeni Eklenen Özellikler

- Gelişmiş Sepet Mantığı: Tekli satış yerine, bir liste (sepet) dolusu ürünün aynı anda işlenmesi.
- Kritik Stok Uyarı Sistemi: Stok miktarı belirlenen eşik değerin (5 kg) altına düştüğünde sistemi otomatik olarak uyarması.
- Dinamik Fiş Oluşturma: Satış sonunda satılan ürünleri, birim fiyatları ve genel toplamı içeren detaylı bir makbuz çıktısı.
- Hata Yönetimi: Listede olmayan ürün veya yetersiz stok durumlarında kullanıcıya bilgilendirme yapılması.


🛠️ Teknik Detaylar

- Veri Yapısı: Ürün adı, stok ve fiyat bilgileri `[[Meyve, Stok, Fiyat], ...]` şeklinde bir matris yapısında tutulur.
- Algoritma: Sepetteki her ürün için ana matris üzerinde arama yapan iç içe döngü (nested loop) yapısı kullanılmıştır.

 📝 Örnek Çıktı (Planlanan)


--- SATIŞ FİŞİ ---
- 2 kg Elma: 40 TL
- 1 kg Muz: 50 TL (UYARI: Stok 5kg altına düştü!)
------------------
GENEL TOPLAM: 90 TL
