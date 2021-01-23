# Basit Proof Of Work Mantığı






> Bileşenler

* Rest-Api için Django kullanılmıştır.
* Websocket teknolojisi için broker redis kullanılmıştır.
* Hızlı bir kurulum için veritabanı SqLite Kullanılmıştır.
* Arayüz için Angular kullanılmıştır.

> Proof Of Work

Bitcoin ve diğer pek çok kriptopara birimi, merkezsiz düğümlerin (node) bir araya gelerek oluşturduğu ağlar vasıtasıyla,
ağda madenci ismi verilen ve blokzincirine yeni bloklar eklemekle görevli operatörler bulunmaktadır.
Bu blokların eklenebilmesi ise bazı karmaşık matematik problemlerinin çözülmesiyle mümkün olabilmektedir.
Söz konusu problemleri çözmek hayli zor olduğu için güçlü işlemcilere ihtiyaç duyulmaktadır.

> Projenin Amacı

Blok zincir mantığını kavramak için öncelikle zincir mantığını nasıl çalıştığını anlamamız gerekir.
Her bir blok kendinden önce gelen bloğun hash değerini değerini previous hash değeri olarak atar.
Tabiki ilk bloğun öncesi olmadığı için varsayılan "0" olarak atadık.
Hash değeri ise: Previous Hash + Data olarak belirlenmektedir.
Biz miner işlemine atıfda bulunmak ve miner işleminin baside indirgerek anlatmak istediğimiz için miner butonuna tıklandığında
Hash değerini ve P.Hash değerini bilen madencimiz datayı tahmin etmeye çalışıyor ve tahmin doğru ise blok zincire bağlanmış bulunuyor.
İşlemlerin kısa süremesi için datayı 2 karakterle sınırlandırdık.

### Projenin  Model Kısmı
``` def _pcreateHash():
    """Bu fonksiyon  hash üretir"""
    value = BlockChain.objects.values('id').distinct().last()
    if value is None:

        return 0
    else:
        value = BlockChain.objects.values('hash').distinct().last()
        return  value['hash']


class BlockChain(models.Model):
    data = models.CharField(max_length=2)
    p_hash = models.CharField(max_length=64, default=_pcreateHash, unique=True)
    hash = models.CharField(max_length=64, unique=True,  default=None, null=True)
    status = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)


    class Meta:
        app_label = 'node1'

    def save(self,*args,**kwargs):
        """Bu fonksiyon toplam hash üretir"""
        if self.hash is None:
            value = BlockChain.objects.values('id').distinct().last()
            if value is None:
                md5_key = hashlib.md5(str("12").encode())
                self.hash = md5_key.hexdigest()
                super().save(*args, **kwargs)
            else:
                try:
                    total_value = str(self.p_hash + self.data)
                    print(type(total_value), type(self.p_hash), total_value)
                    self.hash = hashlib.md5(total_value.encode()).hexdigest()
                    super().save(*args,**kwargs)
                except Exception as err:
                    print(err)


```

### Projenin Veri Tabanı Yapısı
| id | Data          | P_Hash        |   Hash        | Status | Time        |
| -- |:-------------:| -------------:| -------------:| ---:|  -------------:|

|88  |  12	|    0      |	c20ad4d76fe97759aa27a0c99bff6710	|1|	|2021-01-06 14:41:35.666229|
|89|23 |	c20ad4d76fe97759aa27a0c99bff6710|6147e50964cf135542be89751ee2196a|1|2021-01-06 14:58:02.822682|
|90|12 |6147e50964cf135542be89751ee2196a|0d2a349e804923112cb62653a1f97413|1|2021-01-06 15:03:28.333841|





## Ön Hazırlık
- İşletim Sistemi: debian10, mint19, ubuntu yada debian tabanlı başka işletim sistemleri
- python pip kurulumu :``` sudo apt install python3-pip -y ```
- redis kurulumu: ``` sudo apt install redis -y ```
- virtualenv kurulumu: ``` pip3 install virtualenv ```
- Node.js Kurulum:
  ``` sudo apt-get install software-properties-common
      curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
      sudo apt-get install nodejs
  ```
- Angular Kurulum: ``` npm install -g @angular/cli ```
## Kurulum Django

- git clone https://github.com/erelbi/gazi_blockchain_proofofwork
- cd gazi_blockchain_proofofwork/blockchain_backend/
- Klasördeki mevcut venv klasörünü ve dbsqlite3  siliniz ( Temiz bir kurulum için)
- ``` rm -rf venv/ && rm -rf db.sqlite3 ```
- Yeni bir venv oluşturalım: ``` virtualenv venv ```
- Oluşturduğumuz venv ortamına paketleri yükleyeceğimiz için aktif hale getirelim ```source venv/bin/active ```
- Paketlerimizi Yükleyelim: ``` pip3 install -r requirements.txt ```
- Django db migrate işlemleri : ``` python3 manage.py migrate ``` İşlem bitince ``` python3 manage.py makemigrations ```
- Eksi veriler beni rahatsız etmez derseniz veritabanı kalabilir silmeye bilirsiniz!
- django başlatmak için # python3 manage.py runserver 127.0.0.1:8000

## Kurulum Angular
-  cd  gazi_blockchain_proofofwork/blockchain_frontend/
-  ng serve --prod
-  http://localhost:4200/ adresine browser üzerinden gidilir.




## Lisans

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2021 © <a href="https://erelbi.github.io/web/" target="_blank">Ergün Elvan Bilsel</a>.


## Gazi Üniversitesi
#### Blok Zincir 2021
##### Saygı Değer Hocamız Doç. Dr. Utku KÖSE  Teşekkürler
- <a href="http://www.utkukose.com/tr/" target="_blank">Doç. Dr. Utku KÖSE  Kişisel Web Sitesi</a>.







