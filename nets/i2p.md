### Invisible Internet Project (I2P)
- **Lisans:** BSD, GPL, MIT
- **Websitesi:** [geti2p.net](https://geti2p.net/)
- **Durum**: 2003'den beri aktif olarak geliştiriliyor ve maintain ediliyor

#### Açıklama
Peer-to-peer (P2P) iletişime izin veren, özgür ve açık kaynaklı anonim bir ağ katmanıdır. Orjinal olarak Freenet'in 
bir fork'u olarak 2003'de ortaya çıkmıştır. Bir P2P ağı olduğudan ağa dahil olmayan sistemlere (açık internete) ağ
üzerinden erişmek mümkün değildir.

#### Teknik Detaylar 
I2P relay gibi proxy sunucularına bağımlı değildir. I2P üzerindeki her kullanıcı bir peer'dır ve ağ üzerinde trafik 
iletimine garlic routing protokolü ile katkıda bulunur. Her peer'ın kendi kriptokgrafik ID'si, özünde bir public keyi
bulunur. Peer'ların public keyleri ile kimliklenmeleri sayesinde iki peer arası şifreli trafik iletimi için herhangi
bir ek kriptokgrafik anahtar değişimi gerekmez. Ağa yeni katılan peer'lar hard-code'lanmış "bootstrap" peer'larına
bağlanarak farklı peer'ları keşfeder.

</br>

Asıl bağlantıların oluşturulmasına gelince, burda I2P *NetDb* devreye girer. NetDb router iletişim bilgilerini ve de 
hedef bağlantı bilgilerini tutar. Bu sayede ağ üzerinde bulunan peer'lar birbirleri ile farklı rotalar üzerinden
iletişim sağlayabilir.

</br>

I2P farklı TCP/UDP tabanlı internet protokolleri ile veri aktarımı yapmak için (HTTP, IRC, SMTP vs) bu protokolleri 
kullanan applikasyonlara *tünnel*ler sağlar. HTTP sunucularına erişim sağlayan tünneler *eepsite* olarak isimlendirilir.
Bu siteler, I2P'nin eepsite DNS isteklerini, HTTP istekleri ile beraber yöneten *EepProxy* programı aracılığı ile
*.i2p* alan adı uzantılı sitelerden, tünnel bağlantısı oluşturmak için gerekli bilgiyi sağlayan peer kriptokgrafik
anahtarlarına dönüştürülür.

</br>

P2P tasarımı nedeni ile CGI-NAT yapısı kullanan bir ağda, dış ağa giden tünnelere bağlanmak mümkün olsa da iç ağa 
gelen tünneler oluşturmak mümkün değildir. Bundan kaynaklı olarak CGI-NAT akrasında çalışan I2P peer'ları ağa yeteri 
kadar katkıda bulunumadığından yavaş bir deneyim yaşar.

#### Güvenlik
DDoS ve DoS saldırıları ağ üzerinde birçok farklı servise karşı düzenlenebilir. Bunun dışında 2014'te zero-day 
broker servisi sunan Exodus, I2P yazılımında birden fazla kritik XSS ve RCE zafiyetinin yanı sıra, en az 30 bin
peer'ı denanomize etmede kullanılmış bir exploiti geliştiricilere raporlamıştır. Bu olay dışında I2P geçmişinde
ciddi deanonmizasyon girişimleri bulunmamaktadır.

</br>

2017'de yapılan bir çalışma adli çalışanların I2P yazılımını çeşitli kanıt ve bilgiler elde etmek için exploit
edebileceğini ortaya sunmuştur. Yine de bu çalışmanın pratik kullanımda nasıl sonuçlar ortaya koyacağı bilinmemektedir.

#### İstatistikler
- I2P P2P ağına her gün **55 bin**den fazla peer akitf olarak katılmaktadır. 
- Erişilebilir olan I2P servisleri ya da eepsite'leri hakkında kesin bir bilgi söz konusu değildir.

#### Kurulum
I2P, ağa her türlü erişimi sağlamak, I2P tünneleri oluşturmak ve kullanmak için web arayüzü ile yönetilen
bir JAR programı dağıtmaktadır. Aynı zamanda bazı GNU/Linux dağıtımları I2P yazımılını paketlemiş olabilir.

</br>

JAR dosyasını eğer I2P'den indiricek olursanız Java'nın güncel bir versiyonu ile beraber GUI kurulum aracını
çalıştırabilirsiniz. Kurulumdan sonra kurulum sırasında size verilen bilgiler ile `i2prouter` programını
başlatıp tüm konfigürasyonu web arayüzünden yapabilirsiniz.

</br>

Resmi I2P yazılımı size Java ortamında en iyi performansı vermiyorsa, `i2pd` gibi başka bir diller ile yazılmış
alternatifleri de tercih edebilirsiniz.
