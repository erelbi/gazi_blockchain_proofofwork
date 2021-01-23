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
<script src="https://gist.github.com/erelbi/48a77db777d82e5fda35ce0a6011bb38.js"></script>


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







