Basamak Sayısına Göre Sıralama Algoritması
Bu proje, verilen sayıları basamak sayılarına göre gruplandıran ve her grup içinde sıralama yapan bir sıralama algoritması sunmaktadır. Algoritma, her gruptaki sayıları sıralamak için Quicksort algoritmasını kullanır ve gruplar arasındaki sıralamayı basamak sayısına göre yapar.

Özellikler
Sayılar, basamak sayılarına göre gruplandırılır (1 basamaklı, 2 basamaklı, 3 basamaklı vb.).
Her grup içindeki sayılar Quicksort algoritması ile sıralanır.
Gruplar, basamak sayılarına göre sıralandıktan sonra birleştirilir.
Performans ölçümü yaparak, algoritmanın hızını ve doğruluğunu karşılaştırabilirsiniz.
Kullanım
Projenin Çalıştırılması:

Python 3.x sürümüne sahip bir ortamda çalıştırılabilir.
random modülü ile 1.000.000 elemandan oluşan bir liste rastgele oluşturulup sıralanır.
Algoritma Adımları:

Adım 1: Sayılar, basamak sayılarına göre gruplandırılır.
Adım 2: Gruplar basamak sayılarına göre sıralanır.
Adım 3: Her grup içinde Quicksort algoritması ile sıralama yapılır.
Adım 4: Sıralı gruplar birleştirilir ve sonuç elde edilir.
Performans Ölçümü:

Quicksort ve kendi algoritmanızın süreleri karşılaştırılır ve sonuçlar bir dosyaya kaydedilir.
Örnek Çıktı

❯ python vs2.py
Quicksort Süre: 2.239316 saniye
Kendi Algoritmanız Süre: 1.567475 saniye
Kendi algoritmanız daha hızlı!


Quicksort Sonuç:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]

Kendi Algoritmanız Sonuç:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
Kullanıcı Geri Bildirimi
Bu algoritmanın hızını ve doğruluğunu test etmek için performans karşılaştırmaları yapabilirsiniz. Sonuçları performance_results.txt dosyasına kaydederek her iki algoritmanın performansını inceleyebilirsiniz.

Katkıda Bulunma
Bu projeye katkıda bulunmak isterseniz, lütfen bir pull request göndermeden önce aşağıdaki adımları takip edin:

Projeyi fork edin.
Yeni bir branch oluşturun.
Değişikliklerinizi yapın ve commit edin.
Pull request gönderin.
