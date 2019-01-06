---
id: 5
title: Nikon D70 ile Pinhole
date: 2006-06-12T01:16:00+00:00
author: admin
layout: post
guid: http://www.subjektif.org/blog/?p=5
permalink: /blog/2006/06/nikon-d70-ile-pinhole/
blogger_blog:
  - merenswall.blogspot.com
blogger_permalink:
  - /2006/06/nikon-d70-ile-pinhole.html
pvc_views:
  - "15656"
categories:
  - Ekipman
  - Öğreten Adam Modu
  - Sanat Filan Üzerine
  - Teknik
---
Bu yazı daha önceki yazılardan birisinde bahsettiğim Pinhole mevzusunun digital bir makine ile nasıl icra edileceğine dair bilgiler içeriyor olacak. Burada anlatılanlar Nikon serisi 16x24mm. CCD sensöre sahip bütün makineler için geçerli olacak hesaplamalardan yola çıkılarak elde edilmiş bilgiler olacaklar. Bu makineler Nikon D70, D70s, D100, D1X modellerini de kapsamaktadır.

Öncelikle pratikte gerçekleşen olayları tam olarak anlamak isteyenler için bir miktar teori.

İlk önce bir pinhole kamera ile çekilen görüntünün net olması için etkili olan -bir önceki yazıda da bahsi geçen- kriterlerin arasında nasıl bir ilişki olduğundan bahsedelim. Üstünkörü bir bakış ile pinhole deliğinin çapı ve bu deliğin sensöre olan uzaklığının netlik ile ilgili bir ilişki içerisinde olacağı optik ya da matematik konularından hoşlanan birisi tarafından kolayca görülebilir. Hatta aynı kişi biraz hayal meyal de olsa deliğin çapının, deliğin ışığa duyarlı yüzeye uzaklığının karekökü ile orantılı olduğunu da hissedebilir sanırım :)

Optik konularında yaptığı alışmalar ile ün salmış olan Slovak bilim insanı Jozef Maximilián Petzval (1807 &#8211; 1891), yaptığı çalışmalar sonucunda bir Pinhe düzeneğinin net fotoğraflar üretbilmesi için delik çapı ve deliğin ışığa duyarlı yüzeye uzaklığı arasındaki bağıntıyı formulize etmiş (elleri dert görmesin):

<p style="text-align: center;">
  <img class="aligncenter" style="margin: 0px auto 10px; display: block; text-align: center;" src="{{ site.baseurl }}/images/nikon-d70-ile-pinhole-37c667efddbefe1e9eec48477aefbcd1.png" border="0" alt="" />
</p>

Bu formülün bileşenleri şöyle,

> <pre>d     : Deliğin çapı.
f     : Deliğin sensöre (ya da film kağıdına) uzaklığı.
lambda: Sensörün (ya da filmin) duyarlı olduğu ışık dalgaboyu.</pre>

Gördüğünüz gibi, deliğin açıldığı yüzeyin Z eksenindeki boyu, yani kullanılan malzemenin kalınlığının netlik üzerinde hiç bir etkisi yok. Fakat başka bir şey üzerinde etkisi var, ve onu daha sonra tartışacağız. Önce Nikon bir makine için net görüntü elde etmemizi sağlayacak bir deliğin kaç milimetre olması gerektiğini hesaplayalım.

Deliğin kaç milimetre olduğunu hesaplayabilmemiz için bilmemiz gereken değerlerden birisi olan _lambda_, yani sensörün duyarlı olduğu ışık dalgaboyunun değerini biliyoruz (CCD sensör üzerindeki IR-cut yüzey çıkartılmadığı durumda): **650nm**.

Diğer bilinmeyen ise _f_, yani deliğin sensöre olan uzaklığı. Bu noktada aslında deliği nasıl bir şeye açacağımızı bilmemiz gerekiyor. Ben şimdilik Nikon&#8217;un body-cap&#8217;i yani hiç bir lens takılı değilken kameranın içine toz girmemesi için kullandığımız kapaktan faydalanarak bir pinhole yapacağımızı öngördüğüm için uzaklığı body-cap&#8217;ten sensöre kadarki mesafe olarak alıyorum. O da tüm digital Nikon&#8217;larda yaklaşık olarak **5.5cm**.

Evet, bu veriler ışığında elde edilen verileri formüldek yerlerine yerleştirdiğimizde şöyle bir sonuç elde ediyoruz:

> <pre>d = 1.9 x (5.5cm x 650nm)<sup>1/2</sup>
  = 1.9 x (5.5cm x 0.000065cm)<sup>1/2</sup>
  = 1.9 x (5.5cm x 0.000065cm)<sup>1/2</sup>
  = 1.9 x (0.0003575cm<sup>2</sup>)<sup>1/2</sup>
  = 1.9 x 0.0189cm
  = 0.035cm<strong>
d = 0.35mm</strong></pre>

Yani, eğer Nikon bir body&#8217;nin body-cap&#8217;i dolaylarında bir deliğe sahip olacaksak, çekeceğimiz fotoğrafların net olması için bu deliğin çapının 0.35mm, yani milimetrenin üçte biri büyüklüğünde olması gerekiyormuş.

Evet. Geldiğimiz nokta itibarı ile kullanacağımız yüzey üzerine, çok küçük uzunluklardan bahsediyor olsak da yaklaşık olarak ne kadarlık bir delik açtığımızda çekeceğimiz fotoğrafların net çıkacağını biliyoruz.

Peki ya lensin görüş açısı?

Bu tamamen pinhole lensin sensöre olan uzaklığı ile ilgili. Nikon için yapılabilecek pinhole lensler cihazın fiziksel sınırları nedeni ile 5 santimetreden daha yakın olamıyor sensöre (body-cap&#8217;e takılan içbükey malzemeler ile son fiziksel sınır zorlanıyor, fakat daha fazla yaklaşmasının önünde hiç bir şeye çarpmadan inip kalkmak zorunda olan bir &#8220;ayna&#8221; engeli var; makinenizin içine bakıp çekim esnasında nasıl çalıştığını hayal ederseniz kolayca neden 5 santimetreden daha fazla yaklaşamadığımızı anlarsınız, elbette bunun da hacky yolları var, fakat bu noktada zaten risk altında olan makinemizi daha fazla riske atmak istemiyoruz).

Deliğin sensöre olan uzaklığını değiştiremiyor olduğumuza ve sensör alanı da sabit olduğuna göre (16mmx24mm) yapabileceğimiz bir şey yok. Elimizdeki pinhole lens bu koşullarda, yaklaşık 70-75mm&#8217;lik bir objektifin görüş açısına sahip oluyor (bu bilgi benim kendi gözlemlerim sonucu elde ettiğim bir veri, bunu sonraki haftalarda fırsat bulduğumda basit şekilde formulize etmeyi düşünüyorum, daha önceden etmiş olan birisi varsa öğrenmek isterim).

Fakat bir başka sorun daha var, sensör yüzeyimiz çok küçük ve lens sensöre çok uzak. Bu yüzden pinhole etkisi olan, fotoğrafın köşelerinde bir karaltı ve ortasından uzaklaştıkça artan optik bozulma ile bizim fotoğraflarımızda karşılaşmıyoruz. Bunun nedeni üzerinde delik açılan malzemenin kalınlığı ile ilgili. Bunun nedeninin daha kolay anlaşılabilmesi ve kıyaslanabilmesi için üşenmedim ve buraya kadar okumuş olan siz meraklılar için iki adet çizim hazırladım:

<div>
  <p style="text-align: center;">
    <img class="aligncenter" src="{{ site.baseurl }}/images/nikon-d70-ile-pinhole-pinholelens2-787060.jpg" border="0" alt="" />
  </p>
</div>

<p style="text-align: center;">
  <img class="aligncenter" src="{{ site.baseurl }}/images/nikon-d70-ile-pinhole-pinholelens1-784581.jpg" border="0" alt="" />
</p>

Yukardaki kesitlerde en soldaki gri dikdörtgenler sensörü, eğriler pinhole deliğinin açıldığı yüzeyleri, birbirini kesen iki düz çizgi ise maksimum görüş açısını temsil ediyor. Ayrıca deliğin çapı, deliğin sensöre uzaklığı ve sensör alanları iki çizimde de eşit. Tek değişen materyalin kalınlığı.

1 numaralı çizimde ince olan materyal üzerine açılmış delikten geçen ışık sayesinde lens geniş bir açıyı izleyebiliyor. Fakat sensör boyutu çok küçük olduğu için görüntünün çok büyük bir kısmı sensörün dışında kalan alanlara denk geliyor. Dolayısıyla çok ince materyaller ile hazırlanan pinhole lensler (Nikon için 0.7 milimetreden daha ince materyallerle hazırlananlarda) pinhole etkisi, yani köşelerdeki kararma ve bozulmalar fotoğraflarda gözlemlenmiyor.

2 numarali çizimde ise her şey sabitken materyalin kalınlığı arttırılıyor ve görüntünün oluştuğu alan daralıp sensörün alanına yaklaşıyor. Bu çizimlerdeki sensör kesitlerinin kısa kenar uzunluğunda olduğunu ve 3 boyutlu düşünüldüğünde görüntüyü temsil eden çizgilerin bir koni oluşturduğunu hayal ederseniz sensörün kenarlarında bozulmanın etkilerinin hissedileceğini kolayca anlayabilirsiniz.

Benim yaptığım denemeler sonucunda ortaya çıkan sonuçlara göre fotoğraflarda pinhole etkisini yakalamak için Nikon makinelerde kullanılan ve pinhole deliğinin açıldığı materyalin kalınlığı, yaklaşık olarak **0.8mm ile 1.1mm arasında olmalı**.

Bütün bu bilgilerin ardından artık Nikon D70 için iyi performans veren bir pinhole lensi nasıl yaptığımı anlatmaya başlayabilirim.

_(Devam edecek..)_
