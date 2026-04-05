BLM332 Bulut Bilişim Dersi 1.Proje
AWS Üzerinde Çift Katmanlı Hava Durumu İzleme Paneli 

Bu ders kapsamında basic bir RESTful API ve bir kullanıcı arayüzünün cloud mimarisi üzerinde nasıl entegre edildiğini göstermek amacıyla geliştirilmiştir.

Proje Hakkında
Uygulama, Open-Meteo API servisinden Ankara şehri için gerçek zamanlı hava durumu verilerini (sıcaklık, hissedilen sıcaklık, nem) çeker, bu verileri AWS üzerinde bir Python/Flask sunucusunda işler ve Bootstrap tabanlı bir arayüzle kullanıcıya sunar.

Backend ve Frontend tamamen birbirinden ayrık (decoupled) yapıdadır.
Dış kaynaklı bir API'den canlı veri akışı sağlanmaktadır.
Uygulama tamamen AWS Elastic Beanstalk üzerinde barındırılmaktadır.
Fetch API kullanılarak sayfa yenilenmeden veri güncellenmesi sağlanır. 

Kullanılan Teknolojiler
Backend
Dil: Python 3.12.3
Framework: Flask
Kütüphaneler: requests (API istekleri), flask-cors (Güvenli veri paylaşımı), datetime (Zaman dilimi yönetimi) 

Frontend
Dil: HTML5, Modern JavaScript (ES6+)
Tasarım: Bootstrap 5
İletişim: Fetch API (JSON veri transferi)

Cloud Platformu 
Sağlayıcı: AWS
Servis: Elastic Beanstalk (PaaS)
Region: Frankfurt (eu-central-1) 

     