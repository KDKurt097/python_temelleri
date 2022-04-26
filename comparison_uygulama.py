# soru 1
"""
a =int(input("a: "))
b =int(input("b: "))

hangisi_büyük = (a > b)
print(f"a: {a} b: {b} den büyüktür: {hangisi_büyük}")
"""

# soru 2
"""
ilk_vize = int(input("vize1: "))
ikinci_vize = int(input("vize2: "))
final = int(input("final: "))


ortalama = (((ilk_vize + ikinci_vize)/2) * 0.6 + (final) * 0.4)/3
print(f"Not ortalamanız : {ortalama} sınıavdan geçme durmunuz {ortalama>= 50 }" )
"""

# soru 3
"""
sayi = int(input("sayı: "))

tek_cift = (sayi % 2 == 0)

print(f"girilen sayı çift olma durumu: {tek_cift}")
"""

# soru 4
"""
sayi = int(input("sayı: "))
pozitif_mi = (sayi > 0)

print(f"girilen sayının pozitif olma durumu: {pozitif_mi}")
"""

# soru 5
email = "kizeyimkurt@gmail.com"
password = "cba321"

girilen_email = input("email:")
girilen_password = input("parola:")

is_email = (email == girilen_email.lower().strip())
is_password = (password == girilen_password.lower())

print(f"Email bilgisi doğru mu: {is_email} ve parola doğru mu: {is_password}")









