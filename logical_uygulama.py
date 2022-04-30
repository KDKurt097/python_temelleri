# 1.soru
"""
x = int(input("sayı giriniz:"))

aralik = 0 < x <100

print(aralik)
"""

# 2.soru
"""
kontrol = x > 0 and x % 2 == 0

print(kontrol)
"""

# 3.soru
"""
email = "kizeyimkurt@gmail.com"
parola = "123"
girilen_email = input("emailinizi girin: ")
girilen_parola = input("parolanızı girin: ")
giris = (girilen_email == email) and (girilen_parola == parola)
print(giris)
"""

# 4.soru
"""
x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
x_büyüklük = (x > y) and (x > z)
y_büyüklük = (y > x) and (y > z)
z_büyüklük = (z > y) and (z > x)

print(f"x en byük sayıdır: {x_büyüklük}")
print(f"y en byük sayıdır: {y_büyüklük}")
print(f"z en byük sayıdır: {z_büyüklük}")
"""

# 5.soru
"""
ilk_vize = int(input("vize1: "))
ikinci_vize = int(input("vize2: "))
final = int(input("final: "))
ortalama = (((ilk_vize + ikinci_vize)/2) * 0.6 + (final) * 0.4)

print(f"Not ortalamanız : {ortalama} sınıavdan geçme durmunuz {ortalama >= 50 and final >= 50 or final >= 70 }" )
"""

# 6.soru
"""
ad = input("isminiz: ")
kilo = int(input("kilonuz: "))
boy = float(input("boyunuz: "))
index = kilo / ( boy**2 )
zayıf = 0 < index <= 18.4
normal = 18.5 <= index <= 24.9
fazlaKilolu = 25.0 <= index <= 29.9
şisman = 30 <= index <= 34.9
kurtKilosu = 35 <= index 

print(f"Kilo-boy indexiniz {index} zayıflık durumunuz {zayıf}")
print(f"Kilo-boy indexiniz {index} normal durumunuz {normal}")
print(f"Kilo-boy indexiniz {index} fazla kilolu durumunuz {fazla_kilolu}")
print(f"Kilo-boy indexiniz {index} şisman durumunuz {şisman}")
print(f"Kilo-boy indexiniz {index} kurt kilosu durumunuz {kurt_kilosu}")
"""














