import random

result = random.random() # 0 la 1 arasında bir sayı üretir.
result = random.uniform(1,100) # 1 - 100 arasında ondalıklı bir sayı üretir.
result = random.randint(1,100) # 1 - 100 arasında tam bir sayı üretir.

names = ["Ali","Yağmur","Deniz"]
result = names[random.randint(0,len(names)-1)]
result = random.choice(names) # rasgele elemanları seçer.

liste = list(range(10))
random.shuffle(liste) # karıştırır
result = liste

liste = range(100)
result = random.sample(liste,3) # bir liste içinden rasgele sayıları ya da isimleri istediğin sayıda verir

print(result)

