# Altın İmleç #

* Yazarlar: salah atair, Joseph Lee
* İndir [kararlı sürüm][1]
* NVDA uyumluluğu: 2019.3 ve üstü

Bu eklenti, klavyeyi kullanarak fareyi hareket ettirmenize ve uygulamalar
için fare konumlarını kaydetmenizi sağlar.

## Kısayol Tuşları

* Control+NVDA+L: Varsa, bir uygulama için kaydedilmiş fare konumlarını
  görüntül.
* Shift+NVDA+l: o anda odaklanılan uygulamada geçerli fare konumu için bir
  etiket veya etiket kayded.
* Windows+NVDA+C: fare hareket birimini değiştir.
* Windows+NVDA+R: fare kısıtlamasını aç/kapat.
* Windows+NVDA+S: fare konumunun piksel cinsinden raporlanmasını aç/kapat.
* Windows+NVDA+J: fareyi belirli bir x ve y konumuna götür.
* Windows+NVDA+P: fare konumunu bildir.
* Windows+NVDA+M: fare oklarını açar veya kapatır.
* Windows+NVDA+ok tuşları (veya fare okları açıksa sadece ok tuşları):
  fareyi hareket ettirin.

not, bu hareketler NVDA Girdi Hareketleri iletişim  kutuşunda bulunan Altın
İmleç kategorisinden yeniden atanabilir.

## Notlar

* Konumları (etiketleri) paylaşırken, her bir taraf aynı ekran çözünürlüğünü
  kullanmalıdır. 
* Maksimum uyumluluk için Windows yukarı ok tuşuna basarak pencereleri
  büyütmelisiniz. 
* Konumları paylaşırken, mevcut konum etiketleri yeniden adlandırılmalıdır. 
* Sürüm 1.x ve 2.x fare konumu biçimleri uyumsuzdur. 
* Ok tuşlarının kullanılmasının gerektiği işlemlerde önce fare oklarını
  kapatmanız gerekir.
* Kaydedilen pozisyonlar silinirken, kayıtlı pozisyon kalmamışsa, uygulama
  için pozisyonlar silinecektir.

## Sürüm 5.0

* NVDA 2021.1 ile uyumlu hale getirmek için eklenti kaynak kodu modernize
  edildi.
* Flake8 ile birçok kodlama stili sorunu ve olası hatalar çözüldü.

## Sürüm 4.0

* NVDA 2019.3 veya sonraki bir sürümü gerektirir.
* Altın İmleç ayarları iletişim kutusu, Altın İmleç ayarları paneli ile
  değiştirildi.NVDA 2019.3 veya sonraki bir sürümü gerektirir.

## Sürüm 3.3

* Gelecekteki NVDA sürümlerini desteklemek için dahili değişiklikler.

## Sürüm 3.2

* Eklenti, NVDA 2018.3 (wxPython 4) ile uyumludur.

## Sürüm 3.0

* NVDA 2018.2 kullanılıyorsa, "Altın İmleç" kategorisi altındaki yeni çoklu
  kategori ayarları ekranında eklenti ayarları bulunacaktır.

## Sürüm 2.1

* Etiket adını silmeye çalışırken sabit unicode kod çözme hatası düzeltildi.
* eklentiyle ilgili birden fazla iletişim kutusu açılabilme sorunu
  düzeltildi.
* Fare konumları listesi ve konum atlama iletişim kutularıyla ilgili
  iyileştirmeler.

## Sürüm 2.0

* NVDA 2017.3 ve sonraki bir sürümü gerektirir.
* Konum dosyası formatı 1.x sürümleriyle uyumlu değil. 1.x pozisyon formatı
  bulunursa, kurulum sırasında eski pozisyonlar yeni formata taşınacaktır.
* Fare hareket birimini yapılandırmak ve fare hareket ettikçe fare
  konumlarının duyurusunu yapmak için NVDA Tercihler menüsüne yeni bir Altın
  İmleç ayarları iletişim kutusu eklendi.
* Bu eklentiden gelen çeşitli mesajlar değişti.
* Çeşitli ayarlar arasında geçiş yapılırken geçiş tonu artık
  duyulmayacaktır.
* Artık sadece ok tuşlarına basarak fareyi hareket ettirebileceğiniz fare
  okları moduna girebilirsiniz.
* Yeni ad (artık Fare Konumları olarak adlandırılır) ve düzen, bir etiket
  için fare koordinatlarını görüntüleme ve etkin uygulamanın adını başlığın
  bir parçası olarak gösterme dahil olmak üzere konum listesi iletişim
  kutusundaki değişiklikler.
* Fare Konumları iletişim kutusundan, kaydedilmiş bir etiket üzerinde
  Enter'a basmak, fareyi kaydedilen konuma hareket ettirecektir.
* Bir fare konumunu yeniden adlandırırken, yeni adla aynı ada sahip bir
  etiket varsa bir hata iletişim kutusu gösterilecektir.
* Fare konumlarını silerken veya temizlerken, konumlar silinmeden ve/veya
  temizlenmeden önce şimdi Evet yanıtını vermelisiniz.
* Yeni bir ad (artık Yeni fare konumu olarak adlandırılıyor) ve X ve Y
  koordinatlarını ayrı ayrı veya yukarı veya aşağı ok tuşlarını kullanarak
  girme yeteneği dahil olmak üzere fare atlama özelliğinde yapılan
  değişiklikler.
* Geçerli fare konumu kaydedilirken gösterilen iletişim kutusu artık geçerli
  fare konumu için koordinatları gösteriyor.
* Konumları kaydederken, konumlar klasörü yoksa NVDA'nın hata sesi çalması
  sorunu çözüldü.

## Sürüm 1.4

* Eklentiyi NVDA'nın geçmiş ve gelecekteki sürümleriyle uyumlu hale getirmek
  için win32api bağımlılığı kaldırıldı.

## Version 1.0

* İlk sürüm

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
