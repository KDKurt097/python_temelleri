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
email = input("emailinizi girin: ")
parola = input("parolanızı girin: ")
giris = (email == "kizeyimkurt@gmail.com") and (parola == "123")
print(giris)
"""

# 4.soru
"""
x = int(input("ilk sayıyı giriniz:"))
y = int(input("ikinci sayıyı giriniz:"))
z = int(input("üçüncü sayıyı giriniz:"))
büyüklük = x > y > z

print(büyüklük)
"""

# 5.soru
"""
ilk_vize = int(input("vize1: "))
ikinci_vize = int(input("vize2: "))
final = int(input("final: "))
ortalama = (((ilk_vize + ikinci_vize)/2) * 0.6 + (final) * 0.4)/3

print(f"Not ortalamanız : {ortalama} sınıavdan geçme durmunuz {ortalama >= 50 and final >= 50 or final >= 70 }" )
"""

# 6.soru

ad = input("isminiz: ")
kilo = int(input("kilonuz: "))
boy = float(input("boyunuz: "))
index = kilo / ( boy**2 )
zayıf = 0 < index <= 18.4
normal = 18.5 <= index <= 24.9
fazla_kilolu = 25.0 <= index <= 29.9
şisman = 30 <= index <= 34.9
kurt_kilosu = 35 <= index 



print(f"Kilo-boy indexiniz {index} zayıflık durumunuz {zayıf}")
print(f"Kilo-boy indexiniz {index} normal durumunuz {normal}")
print(f"Kilo-boy indexiniz {index} fazla kilolu durumunuz {fazla_kilolu}")
print(f"Kilo-boy indexiniz {index} şisman durumunuz {şisman}")
print(f"Kilo-boy indexiniz {index} kurt kilosu durumunuz {kurt_kilosu}")















