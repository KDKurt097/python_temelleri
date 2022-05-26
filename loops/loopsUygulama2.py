userNumber = int(input("Lütfen bir sayı giriniz: "))

if userNumber == 1:
    print("Girdiğiniz sayı asal sayı değildir.")


for i in range(2, userNumber):
    if userNumber % i ==0:
        print("Girdiğniz sayı asal bir sayı değildir.")
        
    else:
        print("Girdiğiniz sayı asal bir sayı.")
    break



