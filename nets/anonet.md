### anoNet 
- **Lisans:** Açıklamayı okuyunuz
- **Websitesi:** [anonet.org](http://anonet.org/)
- **Durum**: 2005'den beri aktif

#### Açıklama
anoNet, hazır VPN yazılımları üzerine inşa edilmiş özel bir Friend-to-Friend (F2F) ağıdır. Kullanıcıların ağ
üzerindeki kimliklerinin öğrenilmesini zorlaştırarak, anonim olarak farklı servisleri host etmelerine
olanak tanır. Bir F2F ağı olduğudan ağa dahil olmayan sistemlere (açık internete) ağ üzerinden erişmek mümkün değildir.

</br>

anoNet, kullanıcılara herhangi bir yazılım sunmamaktadır ve varolan OpenVPN, tinc, QuickTun ve de Quagga
gibi yazılımlar ile çalışmaktadır. Bu sebeple ağ üzerindeki sistemlerin lisanslamaları değişiklik gösterebilir.

#### Teknik Detaylar
anoNet kullanıcılara 21.0.0.0/8 subneti altında bir IP adresi sağlar. Kullanıcılar bu subnet altındaki diğer
kullanıcılar ile bağlantı kurabilir. Dolayısı ile ağ üzerinde kullanıcılar, diğer kullanıcılar tarafından
erişilebilir her türlü IPv4 ve de IPv6 servisi host edebilir.

</br>

Bu servislerden bazıları anoNet projesi tarafından host edilir. Bunlardan en önemlisi `.ano` alan isimlerinin
çözümünü sağlayan DNS sunucusudur. Bunun dışında anoNet tarafından host edilen webmail sunucusu, arama motoru, 
bittorrent tracker'ı, blog sayfaları, dosya paylaşım servisleri, oyun sunucuları ve de çok daha fazlası mevcuttur.

</br>

Bu ağ üzerinde bağlantıları anonim tutan şey kullanıcılara dinamik IP'ler atanmasıdır. Kullanıcılara dağıtılan OpenVPN
konfigürasyonu her seferinde kullanıcıya farklı bir IP adresi sağlamaktadır. Bunun yanı sıra bağlantı kurmadığınız
kullanıcıların varlığınızdan haberdar olmasını önlemek adına, BGP yerine OSPF routing protokolünü kullanarak tamami
ile hatalı OSPF route'ları dağıtmanız mümkündür.

#### Güvenlik 
anoNet trafiği sadece VPN trafiğinden ibaret olduğundan, kolayca bulunması ve de engellenmesi mümkün değildir.
Bunun dışında ağ kayıt gerektirdiğinden ve de aktif olarak moderasyon altında olduğundan DDoS ve de DoS saldırıları
yöneticiler tarafından hesabın erişimini kaldırarak ya da kullanıcılar tarafından basit firewall kuralları ile
engellenebilir.

</br>

Ağın anonimliği de tam olarak kesin değildir. TCP timestampleri, tarayıcı ajanları, ping ve traceroute
zamanlamaları gibi birçok farklı etken ağ üzerindeki kullanıcıların anonimliğinin ortadan kalkmasına ve IP
adreslerinin keşfedilmesine sebep olabilir.

</br>

Bunun dışında ağ ya da kullanıcılar tarafından kullanılan yazılımlarda bulunabilecek zafiyetler de doğrudan
ağ ve kullanıcı güvenliğini etkileyecektir.

#### İstatistikler
Ağdaki aktif kullanıcı sayısını bilmek tekniken imkansız olduğundan kesin bir istatistik söz konusu değildir.

#### Kurulum
Ağın parçası olmak için ağa kaydolmanız gerekmekte, bu durumda sürekli olarak kullanabileceğiniz bir OpenVPN
konfigürasyonuna erişebileceksiniz. Fakat geçici bir bağlantı istiyorsanız websitelerindeki rehberi takip
edebilirsiniz.
