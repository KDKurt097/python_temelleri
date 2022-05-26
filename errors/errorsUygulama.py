

# Question 1
"""
Liste = ["1","2","5a","10b","abc","10","50"]

for i in Liste:
    try:
        print(int(i))
    except ValueError:
        continue
"""
        
# Question 2
"""
while True:
    number = (input("Sayı: "))
    if number == "q":
        break

    try:
        result = (float(number))
        print("Girdiğiniz sayı", result)
        break

    except ValueError:
        print("Lütfen bir sayı giriniz")
"""  

# Question 3
"""
turkceKarakterler = "şçğüöıİ"
password = (input("Bir şifre giriniz: "))

for i in password:
    if i in turkceKarakterler:
        raise TypeError("Şifre türkçe karakterler içeremez.")
    else:
        pass

print("Geçerli Şifre.")
"""

# Question 4

def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError("Negatif değer")

    result = 1

    for i in range(1, x+1):
            result *= i

    return result

for x in [5, 10, 20, -3, "10a"]:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)    





