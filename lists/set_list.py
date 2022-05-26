meyvalar = {"portakal","elma","muz"}
#print(meyvalar[0]) (indexlenemz)

for x in meyvalar:
    print(x)

meyvalar.add("kivi")
meyvalar.update(["mango","ceviz"]) #birden fazla eleman eklemek için
meyvalar.remove("mango")
#silmek için remove dışında discard ve pop metodu kullanılabilir (pop rasgele bir elemanı siler)
#liste içerisinde bir elemandan sadece bir tane bulunabilir
print(meyvalar)

