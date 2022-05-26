# question 1
"""
number = float(input("Sayı: "))
result = 0 < number < 100

if result:
    print("Sayı 100 ile 0 arasında bulunmaktadır.")
else:
    print("Sayı 100 ile 0 arasında bulunmamaktadır.")
"""

# question 2
"""
number = float(input("Sayı: "))
(number > 0) and (number % 2 == 0)

if (number > 0):
    if ((number % 2 == 0)):
        print("Sayı hem pozitif hem çift sayıdır.")
    else:
        print("Sayı pozitif sayıdır ama çift sayı değildir.")
else:
    print("Sayı pozitif sayı değildir ama çift sayıdır.")
"""

# question 3
"""
email = "kizeyimkurt@gmail.com"
password = "1234"

enteredEmail = input("email: ")
enteredPassword = input("password: ")

if enteredEmail == email:

    if enteredPassword == password:
        print("Hoş geldiniz")  

    else:
        print("Yanlış şifre")

elif (enteredEmail != email) and (enteredPassword != password): 
    print("Yanlış şifre ve email")

else:
    print("Yanlış Email")
"""

# question 4
"""
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

aBigest = (a > b) and (a > c)
bBigest = (b > a) and (b > c)
cBigest = (c > b) and (c > a)

if(aBigest):
    print("a en büyük sayıdır")

if(bBigest):
    print("b en büyük sayıdır")
    
if(cBigest):
    print("c en büyük sayıdır")
"""

# question 5
"""
firstVize = int(input("vize1: "))
secondVize = int(input("vize2: "))
final = int(input("final: "))

average = (((firstVize + secondVize)/2) * 0.6 + (final) * 0.4)

if (average >= 50):
    if (final >= 50):
        print(f"Notunuz {average} , geçtiniz") 

    else:
        print(f"Notunuz {average} , final notunuzdan dolayı kaldınız")

elif (final >= 70):
    print(f"Notunuz {average} , final notunuzdan dolayı geçtiniz")

else:
    print(f"Notunuz {average} , kaldınız")
"""
# question 6
"""
name = input("isminiz: ")
weight = int(input("kilonuz: "))
height = float(input("boyunuz: "))
index = weight / (height**2 )

zayıf = 0 < index <= 18.4
normal = 18.5 <= index <= 24.9
fazlaKilolu = 25.0 <= index <= 29.9
şisman = 30 <= index <= 34.9
kurtKilosu = 35 <= index

if zayıf:
    print(f"{name},indexiniz {index};index gurubunuz zayıf. ")
if normal:
    print(f"{name},indexiniz {index};index gurubunuz normal. ")
if fazlaKilolu:
    print(f"{name},indexiniz {index};index gurubunuz fazlaKilolu. ")
if şisman:
    print(f"{name},indexiniz {index};index gurubunuz şisman. ")
if kurtKilosu:
    print(f"{name},indexiniz {index};index gurubunuz kurtKilosu. ")
"""












