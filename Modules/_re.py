
#   !!! reguler expression bize arama konusunda yardım eder !!!

import re

#print(dir(re))

str = "Halay Kursu: Halay çekme rehberimiz (40 saat)"

# re.findall()
strArama = re.findall("Halay",str) # verilen bilgi içerisinde aranan bilgiyi her bulduğu zaman için yazdırır
print(strArama)
# ***************************************************

# re.split()
strBölme = re.split(" ",str) # verilen bilgiyi verilen karakterden böler
print(strBölme)
# ***************************************************

# re.sub()
strDeğiştir = re.sub(" ","-",str) # verilen bilgide seçilen karakterleri değiştirir (boşluk yerine \s yazılabilir)
print(strDeğiştir)
# ***************************************************

# re.search()
strAralıkArama = re.search("Halay",str) # bize bulduğu ilk halay bilgisinin bulunduğu aralığı verir
#strAralıkArama = strAralıkArama.span() # sadece aralığı yazar
#strAralıkArama = strAralıkArama.start() # sadece başlangıç sayısını yazar
#strAralıkArama = strAralıkArama.end() # sadece bitiş sayısını yazar
#strAralıkArama = strAralıkArama.group() # bulunan bilgiyi yazar
#strAralıkArama = strAralıkArama.string # aranan bilgiyi yazar
print(strAralıkArama)
# ***************************************************

"""

    [] - köşeli parantezler arasına yazılan bütün karakterler 
        aranır.

        [abc] => a      : 1 match
                 ac     : 2 match
                 Python : No match

        [a-e]  => [abcde]
        [1-5]  => [12345]
        [0-39] => [01239] # 0-3 tekrarlar 9 sabit kalır.

        [^abc] => abc dışındaki karakterler.
        [^0-9] => rakam olmayan karakterler.
"""
#    ÖRNEK

#Örnek1 = re.findall("[1-5]",str)
Örnek1 = re.findall("[^abc]",str)
print(Örnek1)

"""

    . - Her hangi bir tek karakteri belirtir. (.. 2 karakteri ... 3 karakteri belirtir.)
        
        .. => a      : No match
              ab     : 1 match
              abc    : 1 match
              abcd   : 2 matches
"""
#    ÖRNEK

Örnek2 = re.findall("H...y",str)
print(Örnek2)

"""
    	
    ^ - Belirtilen karakterle başlıyor mu ?

    ^a => a   :  1 match
          abc :  1 match
          bac :  No match

"""
#    ÖRNEK

Örnek3 = re.findall("^H",str) # sadece en baştaki harfe bakar.
print(Örnek3)

"""

    $ - Belirtilen karakterle bitiyor mu ?

    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match

"""
#    ÖRNEK

Örnek4 = re.findall(")$",str) # sadece en sondaki harfe bakar. 
print(Örnek4)

"""

    * - Bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder.

        ma*n => mn      : 1 match
                man     : 1 match
                maaan   : 1 match
                main    : No match (a'nın arkasından n gelmesi gerkiyor)

"""
#    ÖRNEK

Örnek5 = re.findall("sa*t",str) 
print(Örnek5)

"""

    + - Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder.

        ma+n => mn      : No match
                man     : 1 match
                maaan   : 1 match
                main    : No match (a'nın arkasından n gelmesi gerkiyor)

"""
#    ÖRNEK

Örnek6 = re.findall("sa+t",str) 
print(Örnek6)

"""

    ? - Bir karakterin sıfır ya da bir kez olmasını kontrol eder.

        ma?n => mn      : No match
                man     : 1 match
                maaan   : NO match
                main    : No match (a'nın arkasından n gelmesi gerkiyor)

"""
#    ÖRNEK

Örnek7 = re.findall("sa?t",str) 
print(Örnek7)

"""

    {} - Karakter sayısını kontrol eder.

        al{2}       => a karakterinin arkasından l karakteri 2 kez tekrarlanmalı
        al{2,3}     => a karakterinin arkasından l karakteri en az 2 kez en fazla 3 kez tekrarlanmalı
        [0-9]{2,4}  => en az 2 en çok 4 basamaklı sayılar

"""
#    ÖRNEK

Örnek8 = re.findall("a{2}",str) 
print(Örnek8)

"""
 
    | - Alternatif seçeneklerden birinin gerçekleşmesi gerkir.

        a|b => a ya da b

            cde    => No match
            ade    => 1 match
            acdbea => 3 match

"""
#    ÖRNEK

Örnek9 = re.findall("Halay|40",str) 
print(Örnek9)

"""
    () - Gruplamak için kullanılır.

        (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.

"""

"""

    \ - Özel karakterileri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterini arar. Yani $ re tarafından yorumlanmaz.

    \A - Belirtilen karakter string in başında mı ?
        \Athe => the string in başında mı

    \Z - Belirtilen karakter string in sonunda mı ?
        the\Z => the string in sonunda mı

    \b - Belirtilen karkter kelimenin başında mı sonunda mı ?
        \bthe => the kelimenin başında mı
        the\b => the kelimenin sonunda mı

    \B - Belirtilen karakter kelimenin başında ya da sonunda değil mi?
        \Bthe => the kelimenin başında değil mı
        the\B => the kelimenin sonunda değil mı

    \d - [0-9] ile aynı anllama gelir yani rakamlar aranır.
    \D - [^0-9] ile aynı anlama gelir yani rakam olmaayanlar aranır
    \s - Boşluk karakterlerini arar.
    \S - Boşluk karakterlerini dışındakileri arar.
    \w - Alfabatik karakterler, rakamlar ve alt çizgi karakterleri
    \W - \w nin tam tersi
"""
