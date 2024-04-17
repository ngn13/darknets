### Lokinet 
- **Lisans:** GPLv3
- **Websitesi:** [lokinet.org](https://lokinet.org/)
- **Durum**: 2018'den beri aktif olarak geliştiriliyor ve maintain ediliyor

#### Açıklama
Lokinet, merkeziyetsiz özgür ve açık kaynaklı referans LLARP (low latency anonymous routing protocol),
implementasyonudur. Lokinet kullanıcılara, kullanıcı dostu bir deneyim, gizli, devlet ve 3. partilerin 
gözetiminden uzak bir şekilde özel websitelere ve servislere erişim sunar. OXEN blockchain ve kripto para 
projesinin bir parçasıdır.

#### Teknik Detaylar
LLARP, Lokinet'i ayakta tutan servis node'larının farklı peer'lar ile iletişime geçmek için kullandığı protokoldür.
Bu protokol Lokinet projesi için özel olarak geliştirilmiştir. 

</br>

Bu protokolün yanı sıra Lokinet node'ları OXEN blokchain yapısı üzerinde çalışır. Tipik bir blockchainde göreceğiniz
para işlemleri, mining ve cüzdan konseptleri Loki ağında da mevcuttur. Yeni node'lar ağa katılmadan önce bir test
ağında belirli bir miktarda katkıda bulunmaları gerekmektedir. Bundan sonra node'lar asıl ağın bir parçası olarak
kaydolur ve de asıl kullanıcıların internet trafiğini yönlendirmek, diğer node'ların performansı hakkında oylama
yapmak, kullanıcıların enkripte mesajlarını yönlendirmek ve kaydetmek gibi farklı Loki servisleri sunar.

</br>

Node'ların kullanıcılar ve diğer node'lar tarafından keşfi, için blockchain üzerine inşa edilen dağıtık hash tablosu
kullanılır. Kullanıcılar ağa katıldıktan sonra exit node'ları aracılığı ile IP adreslerini gizleyerek dış internete
erişebilir, Loki servislerinden biri olan uçtan uca şifreli mesajları farklı kullanıcılara gönderebilir ve de
Lokinet ağına özel gizli TCP/UDP servisleri olan SNApp'lere erişebilir. Bu SNApp'ler TOR üzerindeki onion servislerine
benzer şekilde işler ve de iki ucunda IP adreslerini servis node'larını proxy olarak kullanarak gizler.

#### Güvenlik
Lokinet, TOR ve I2P gibi ağların maruz kalabileceği *sybil* saldırılarını, yeni node'ların asıl ağa
dahil olmadan önce bir test ağında 30 gün boyunca belirli miktar katkıda bulunmalarını zorunlu kılarak oldukça
pahalı hale getirir. Bunun dışında Lokinet ağı üzerinde bilinen ciddi bir güvenlik zafiyeti ya da deanonimizasyon
girişimi söz konusu değildir.

#### İstatistikler
- Aktif olarak **2 bin** kadar servis node'u bulunur.
- OXEN üzerine kurulu Lokinet üzerinde yaklaşık her 4 dakikada bir yeni transaction'lar gerçekleşir

#### Kurulum
Lokinet Debian tabanlı GNU/Linux sistemlerinde kolay kurulum için kendi APT depolarını yönetir. Debian 
tabanlı olmayan dağıtımlarda Lokinet binary formunda Github'dan indirilebilir ya da kullanıcı depolarında
bulunabilir.

</br>

Kurulumdan sonra lokinet grafiksel arayüzü ile kolayca kullanılabilir (`lokinet-gui`), ancak grafiksel arayüzü
kullanmak istemeyen kullanıcılar lokinet systemd servisini `systemctl start lokinet` komutu ile başlatabilir.
Lokinet konfigürasyonu `/etc/loki/` dizini altında bulunabilir. Daha fazla bilgi için OXEN dökümentasyonunu
inceleyebilirsiniz.
