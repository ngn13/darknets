### GNUnet 
- **Lisans:** AGPLv3
- **Websitesi:** [gnunet.org](https://gnunet.org/)
- **Durum**: 2001'den beri aktif olarak geliştiriliyor ve maintain ediliyor

#### Açıklama
GNUnet, merkeziyetsiz ve Peer-to-Peer (P2P) ağ sistemleri için bir yazılım paketidir. Aynı zamanda
resmi bir GNU paketidir.

#### Teknik Detaylar
GNUnet birçok farklı TCP ve UDP gibi protokol üzerinden merkeziyetsiz, P2P ağ yapısı için gerekli
özellikleri destekler. Anonim ve özel bağlantılar için Friend-to-Friend (F2F) bir opsiyonu da
bulunur. Bu sayede bir kullanıcı ve onun "arkadaşları" birbirlerinin IP adreslerine doğrudan erişime
gerek duymadan dosya alışverişinde bulunabilir.

</br>

GNUnet farklı protokol ve servisler için özel bir (resmi olmayan) URI sistemi kullanır. Bu sistem
`gnunet://servis/id` formunda çalışır. Ağdaki peer'lar bir mesh ağ topolojisi üzerinden haberleşir,
bir peer GNUnet URI'ı ile karşılaştığı zaman önce cache'isini kontrol eder. Eğer bu URI zaten
çözülmediyse (URI cachede yoksa), peer URI'ın belirtiği servisi çalıştıran peerları bulmak için,
ağ üzerinde bir broadcast yapar. Bu servisi çalıştıran GNUnet peerları bu broadcaste yanıt verir.

</br>

Yanıt veren peer'lardan biri, broadcasti gönderen peer tarafından rastgele seçilir ve de sonraki
istekler için cache'lenir. Son olarak peer doğrudan servisi sunan peer'a bağlanarak URI'ın son
kısmında belirtilen içeriği ister.

</br>

Doğrudan peer bağlantıları şifreli olarak aktarılır, bunun dışında peerların anonim kalmasını
sağlamak adına peer'lar "aracı" peer'lar da kullanabilir.

</br>

GNUnet aynı zamanda kendi standartlaştırılmış alan adı sistemine sahiptir. *GNS* olarak adlandırılan
bu sistem, *GANA* registry sistemi tarafından dağıtık olarak yönteilir. Bunun dışında, dosya paylaşım sistemi
ve P2P sohbet sisteminin yanı sıra topluluk tarafından GNUnet üzerinde inşa edilen elektronik ödeme sistemi,
ve de sosyal ağ applikasyonu da bulunmaktadır.

#### Güvenlik 
GNUnet'in asıl anonimliği git proxy olarak davranan peer'lar aracılığı ile sağlanır. Bu proxy'lerin
anonimliği bozmak adına kötüye kullanımı mümkündür. Bunun dışında GNUnet diğer çoğu alternatifi
gibi DoS ve de DDoS saldırılarına maruz kalabilir.

#### İstatistikler 
GNUnet üzerindeki aktif peer sayısı konusunda herhangi kesin bir bilgi söz konusu değildir.

#### Kurulum
Resmi GNUnet araçları genel olarak komut satırı üzerinden çalışmaktadır ve de `gnunet` paket
adı altında birçok GNU/Linux dağıtımının depolarında ve de kullanıcı depolarında bulunabilir.

</br>

Bunun dışında GTK arayüzüne sahip applikasyonu da `gnunet-gtk` paket adı altında bulunabilir.
Kurulumdan sonra GNUnet araçlarını kullanmaya başlamak için GNUnet'i başlatmanız gerekmektedir.
Bunun için `gnunet-arm -s` komutunu kullanabilirsiniz. Daha fazla bilgilendirme için 
[dökümentasyonu](https://www.gnunet.org/en/use.html) inceleyebilirsiniz.
