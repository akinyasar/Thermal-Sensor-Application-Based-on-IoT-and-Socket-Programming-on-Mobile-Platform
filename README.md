# Thermal Sensor Application Based on IoT and Socket Programming on Mobile Platform
 Lisans programımda Tasarım projesi kapsamında geliştirilmiştir, AMG8851 termal sensör ve RaspberryPi  3 kullanılmıştır. Python Soket programlama ile gerçek zamanlı veri akışı sağlanmıştır.

## Gereklilikler
-> Python 3.6 ve üzeri sürümleri

## UYGULAMA İŞLEYİŞİ

* RaspberryPi 3;

Gerekli kütüphaneler:

1.```pip install numpy```

2.```pip install socket```

->Adım 1: RaspberryPi isimli klasördeki kaynak kodları temiz kurulum yapılmış RaspberyyPi OS işletim sistemine klonlanmalıdır. AMG8851 termal sensörünün datasheet'inde bulunan bilgiler doğrultusunda sensör RaspberryPi'ye doğru bir şekilde bağlanmalıdır. Bağlantı sensörün ışıkları yardımıyla doğrulanabilir.

->Adım 2: RaspberryPi'yi evinizin veya bağlı olduğunuz network'e bağlamak için Raspberry OS'un kurulu olduğu SD kartı bilgisayarımıza bağlayarak wpa.supplicant.conf isimli konfigürasyon dosyasını Raspberry'nin root dizinine kopyalamalısınız. Kopyalamadan önce kendi network bilgileriniz doğrultusunda dosyayı revize etmelisiniz.

->Adım 3: Daha önce klonladığımız server.py dosyasını ilgili dizinde "python server.py" komutu ile çalıştırarak network üzerinde soket bağlantısını açmalısınız.

* Client için;

Gerekli kütüphaneler:

1.```pip install numpy```

2.```pip install matplotlib```

3.```pip install socket```

4.```pip install scipy```

->Adım 1: Client bilgisayarınızı Raspberry'nin bağlı olduğu networke bağlamalısınız.

->Adım 2: client.py dosyasını klonladıktan sonra ilgili dizindeki terminale "python client.py" komutunu yazarak kodu çalıştırabilirsiniz. Bu sayede raspberry'nin
gönderdiği sensör verilerini soket bağlantısı ile gerçek zamanlı alarak, client tarafında verileri interpole ederek ekrana termal görüntüyü çizdirebilirsiniz.

## Önemli Not
Çalışmanın makale olarak yayınlanmış hali Düzce Bilim Dergisi onaylanan makaleler bölümünde bulunmaktadır.
