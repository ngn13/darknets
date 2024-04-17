### The Onion Router (TOR)
- **Lisans:** BSD 3-clause
- **Websitesi:** [www.torproject.org](https://www.torproject.org)
- **Durum**: 2002'den beri aktif olarak geliştiriliyor ve maintain ediliyor

#### Açıklama
Anonim iletişim için özgür ve açık kaynaklı bir yazılımdır. *De facto*, en popüler darknet sistemidir. Çalışma yapısı nedeniyle,
birçok katmadan oluşan soğana benzetildiğinden bu şekilde isimlendirilmiştir.

#### Teknik Detaylar
TOR relay olarak isimlendirilen **8 bin**den fazla merkeziyetsiz node aracılığı ile çalışır.Bir kullanıcı TOR'a bağlandığında trafiği 
sırasıyla guard, middle ve exit olarak adlandırılan 3 farklı relay'e katmanlı şifreleme ile iletilir. Soğan benzetmesi buradan gelmektedir.
Kullanıcıdan gelen trafiğin hedefe ulaşmadan önce farklı relay'ler ile çizdiği rotaya *circuit* (devre) denir. Bu rota 
*onion routing protocol* (onion yönlendirme protokolü) ile çizilir. Bu yönlendirme protokolünün yapısı nedeni ile TOR sadece
TCP tabanlı iletimi destekler.

</br>

Ağa yeni katılan relay'ler kendilerini *directory authority*lerine tanıtır. Bu authority'ler aynı zamanda ağa bağlanmak
isteyen istemcilere bir relay listesi sağlar. Bir bakıma authority'ler ağa bağlı tüm relay'lerin tutulduğu devasa bir
listedir.

</br>

Anlık bir trafik aktarımında, relay'lerin hepsi ele geçirilmediği sürece trafiği takip etmek mümkün değildir. Ayrıca TOR
düzenli olarak kullanılan relay'leri değiştirir. Bu relay'ler aynı zamanda sadece TOR üzerinden erişilebilen *onion servis*lerine 
bağlantı ve iletim sağlar.

#### Güvenlik
Popüleritesinden dolayı geçmişte TOR üzerinde birçok farklı deanonmizasyon saldırısı denenmiştir. Bazıları başarılı olmak ile beraber
modern TOR genel olarak bu tarz saldırılara karşı dayanıklıdır. Birden fazla relay ile trafiği yönlendirmesine rağmen, 
TOR diğer alternatiflere kıyasla hızlıdır. Bundan dolayı zaman tabanlı deanonimize saldırılarına karşı korunaklıdır.
Deanonmizasyon saldırılarının yanı sıra TOR relayleri ve servisleri düzenli olarak DDoS saldırılarına hedef olur. 

</br>

TOR'un güvenlik konusundaki ana problemlerinden biri *sybil* saldırısıdır. Kötü amaçlı biri yüzlerce TOR node'u çalıştırarak 
ve de ağdaki diğer node'ları DoS ve DDoS saldırıları ile kapatarak, tüm kullanıcıları kendi node'larını kullanmaya zorlayabilir.
Bu noktadan sonra TOR ağındaki trafiği izleyip kullanıcıları deanonmize edebilir. Bu saldırı TOR daha az popülerken birçok kez
farklı şekilde denenmiştir ve bazı durumlarda başarılı da olmuştur. Ancak günümüzde TOR ağının inanılmaz kapasitesi nedeni ile
pratik bir yöntem değildir.

#### Türkiye ve TOR
2014'de Türkiye TOR tarayıcısının indirmelerini, 2016'da ise TOR ve birçok VPN servisine erişimi tamamen bloklamıştır. Günümüzde 
TOR türkiye tarafından herhangi bir bilinen bloğa maruz değildir. Aynı zamanda TOR kullanmak ülkemizde tamamen yasaldır, bu bloklamar
sadece *sıradan* kullanıcının TOR'a erişmini güçleştirmeyi amaçlamaktadır, arkalarında ise tamamen siyasi nedenler yatmaktadır.

#### Drama ve TOR
TOR projesi, TOR ağındaki yasadışı içeriklerin çokluğu nedeni ile birçok kez farklı devlet kurumları tarafından kapatılmaya çalışılmış
ve de toplum tarafından eleştirilmiştir. Eva Galperin, Businessweek magazininde yaptığı bir yorumla durumu oldukça basitçe
özetlemiştir: "TOR'un en büyük sorunu basın. Kimse birilerinin istismarcılar tarafından istismara uğramadığı haberlerini yazmıyor. Birilerinin
çocuk pornosu indirdiği haberlerini yazıyor."

#### İstatistikler
- Her gün **2 milyondan fazla** kullanıcı, internet sansüründen kurtulmak, devlet ve de diğer 3. partilerin gizlilik haklarını ihlal
etmesini engellemek veya basitçe anonim internet deneyiminin tadını çıkarmak için TOR ağına bağlanır. 
- Sadece TOR ağı üzerinden erişilebilir **800 binden fazla** onion servisi mevcuttur.
- Bu onion servislerinden **%75**'i dünya çapında yasadışı olan içeriklere yer verir.

#### Kurulum
TOR projesi "TOR Daemon" isimli tek bir yazılım paketi dağıtmaktadır. Bu daemon yani arkaplan programı sayesinde 
TOR ağını kullanmak için bir SOCKS proxy servisi başlatılabilir, TOR ağına destek olmak adına TOR relay'leri ve bridge'leri çalıştırılabilir.
TOR daemon'un kullanımı hakkında daha fazla bilgi edinmek için TOR projesinin websitesini ziyaret edebilirsiniz.

</br>

TOR daemon birçok GNU/Linux dağıtımının depolarında mevcuttur. Genelde `tor` ya da `tord` olarak isimlendirilir.
Bu paketi kurduktan sonra, konfigürasyon dosyası `/etc/tor/torrc` yolunda bulunabilir. `systemd` tabanlı sistemlerde
TOR daemon'ı başlatmak için `systemctl start tor` komutunu kullanabilirsiniz. TOR daemon varsayılan konfigürasyonu
ile çalıştırıldığı zaman, localhost port 9050'de gelen trafiği TOR ağı üzerinden yönlendirecek bir SOCKS proxy servisi 
başlatacaktır.
