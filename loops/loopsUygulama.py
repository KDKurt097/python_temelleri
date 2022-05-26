import random

r = random.randint(1,100)

userNumber = int(input("1 ile 100 arasında bir sayı giriniz: "))
health = int(input("Kaç denemede sayıyı bulacağınız düşünüyorsunuz, lütfen giriniz: "))
health1 = health
counter = 0
print("  ")


    
while health1 > 0:
    health1 -= 1
    counter += 1

    if userNumber == r:
        print(f"Tebrikler {counter}. denemede bildiniz.")
        print(f"Puanınız {100 - (100//health)*counter}")
        break

    if 1 <= userNumber <= 100:
        print("Oyunumuza katıldığınız için teşekkürler.")
    else:
        print("Yanlış bir sayı girdiniz, lütfen 1 ile 100 arasında bir sayı giriniz.")
        break

    if userNumber < r:
        print("Seçtiğiniz sayı aşağıda.")
        userNumber = int(input("(son " + str(health1) + " hakkınız) Lütfen yeni bir sayı deniyiniz: "))
    elif userNumber > r:
        print("Seçtiğiniz sayı yukarıda.")
        userNumber = int(input("(son " + str(health1) + " hakkınız) Lütfen yeni bir sayı deniyiniz: "))

if health1 == 0:
    print(f"Hakkınız bitti, sayı {r}.")




