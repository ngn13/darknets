### Hyphanet (Freenet)
- **Lisans:** GPLv3 
- **Websitesi:** [www.hyphanet.org](https://www.hyphanet.org/)
- **Durum**: 2000'den beri aktif olarak geliştiriliyor ve maintain ediliyor

#### Açıklama
Eski adı ile Freenet, anonim iletişim sağlayan bir Peer-to-Peer (P2P) ağı. Veriyi dağıtmak için
merkeziyetsiz bir veri sistemi kullanıyor. Aynı zamanda kullanıcılara, web üzerinde özgürce, sansür
korkusu olmadan paylaşım ve iletişimde bulunmak adına bir dizi özgür yazılım sunuyor. Bir P2P ağı olduğudan 
ağa dahil olmayan sistemlere (açık internete) ağ üzerinden erişmek mümkün değildir.

</br>

Orjinal Freenet kodu 2023'de Hyphanet olarak yeniden isimlendirilmiştir, ve de aynı geliştiriciler
ile aktif olarak geliştirilmeye devam edilmektedir. Rust ile yazılan yeni Freenet ise hala geliştirme
altındadır ve de kullanıma hazır değildir. Biz orjinal Java ile yazılan Freenet veya yeni ismi
ile Hyphanet'den bahsediyor olacağız.

#### Teknik Detaylar
Hyphanet bir çok farklı *node* aracılığı ile çalışıyor. Her node kullanıcıların ağa yerleştirdikleri
içeriklerin bir kısmını node'un yöneticisi tarafından kontrol edilen bir disk alanına yerleştiriliyor.
Bu alan genel olarak bir kaç GB boyutunda olur.

</br>

Bir kullanıcı ağa bir dosya "yerleştirdiğinde", yani yüklediğinde, bu içeriğin yüklendiği node, diğer
node'lar ile P2P olarak iletişime geçer ve içeriğin birden fazla node arasında dağıtılmasını sağlar.
Dosya tek bir bütün halinde bulunmak zorunda da değil, Hyphanet genelde dosyayı küçük *blok*lara böler,
bu bloklar bağımsız olarak haraket eder. Bu sayede Hyphanet ağ üzerinde paylaşımı kolaylaştırır ve node'lar
üzerindeki disk kullanımını azaltır. Limitli disk alanı nedeni ile, node'lar, disk alanları dolunca az talep edilen 
içerikleri (dosya ve blokları) *unuturlar* yani silerler.

</br>

Veri birçok farklı node arasında bloklar halinde tutulduğundan, orjinal dosyayı paylaşan node'un ağdan
ayrılsa bile dosya ağ üzerinde erişilebilir bir konumda kalır. Yine aynı sebepten Freenet'e yüklenen
içeriklerin silinmesi mümkün değildir. Bir içeriğin tek yolu içeriğin her node tarafından unutulmasıdır.

</br>

Ağdaki node'lar key-based bir yönlendirme protokolü kullanır. Ağa yeni bir node katıldığı zaman *seed
nodeları* olarak bilinen birkaç node ile iletişimde bulunur. Bu node'lar araclığı ile diğer node'lar
hakkında bilgi edinir. Buna *gossiping* denir. Bu işlemden sonra belirli bir sayıda node ile
iletişime girerek onlara "komşu" olur. Ağa bağlanan ve veri kaydı yapmayan node'lar - yani asıl
kullanıcı/istemciler herhangi bir dosyaya erişmek istediğinde, node komşuları ile iletişime 
geçerek dosyayı veya dosyanın bloklarını bulmaya çalışır. Komuşu node'lar sürekli
olarak birbiri ile iletişim sağlayarak dosya ve blokları ağ üzerinde aktarır.

</br>

Hyphanet projesi, ağ kapsamında iletişim için statik HTML sayfalarından ibaret olan *freesite* ve de 
DoS ve spam korumalı post tabanlı iletişim için *freenet messaging system (FMS)*'in yanı sıra birçok
farklı IM ve dosya dağıtım yazılımı sağlar.

#### Opennet ve Darknet
Hyphanet node'ları *opennet* ve *darknet* olmak üzere iki modda çalışabilir. Opennet modunda node'lar
seed node'ları aracılığı ile herkese açık yeni node'lar keşfedebilir ve bunlar ile iletişimde bulunabilir.
Darknet modunda ise node sadece kendisine kullanıcı tarafından belirtilen bir liste node ile iletişimde bulunur.

#### Güvenlik
Hyphanet yazılımlarında, DDoS ve DoS saldırılarını önlemek adına kullanıcıların diğer kullanıcıları kriptografik
anahtarları ile doğrulamalarına ve de güvenmelerine izin veren sistemler bulunmaktar. Bu *güven listesi* sistemi
sayesinde DDoS ve DoS saldırılarının hyphanet ağı üzerindeki etkileri minimaldir. Bu saldırı vektörleri
haricinde Hyphanet/Freenet geçmişinde herhangi bir kritik deanonimizasyon ya da genel güvenlik saldırısı söz
konusu değildir.

#### İstatistikler
Erişilebilir olan hyphanet nodeları hakkında kesin bir bilgi söz konusu değildir, ancak her gün binlerce node
aktif olarak ağ üzerinde iletişimde bulunmaktadır.

#### Kurulum
Hyphanet, tüm yazılım koleksiyonlarını içeren tek bir paket halinde sunulmaktadır. Kurulum için hyphanet projesinin
sitesinden JAR dosyasını indirip güncel bir java versiyonu ile JAR dosyasını çalıştırabilirsiniz. Bu grafiksel
bir kurulum arayüzü sağlayacaktır. Kurulumu konsol üzerinden çalıştırmak içinse `-console` argümanını kullanabilirsiniz.

</br>

Kurulumdan sonra Hyphanet üzerinden erişebileceğiniz farklı yazılımlar localhost port 8888 üzerinde çalışan bir
web arayüzü tarafından size sunulacaktır.
