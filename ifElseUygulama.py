# question 1
"""
name = input("İsminiz: ")
age = int(input("Yaşınız: "))
education_status = input("Eğitim durumunuz: ")
driver_license = age >= 18 and (education_status == "Lise" or "Üniversite")

if driver_license:
    print("Sürücü lisansınız onaylanmıştır.")
else:
    print("Sürücü lisansınız onaylanmamıştır.")
""" 
# question 2
"""
exam1 = int(input("1. sınav: "))
exam2 = int(input("2. sınav: "))
opinion_note = int(input("sözlü: "))
avarage = (exam1 + exam2 + opinion_note)/3

if 0 <= avarage <= 24:
    print(f"Ortalamanız: {avarage} notunuz: 0")
elif 25 <= avarage <= 44:
    print(f"Ortalamanız: {avarage} notunuz: 1")
elif 45 <= avarage <= 54:
    print(f"Ortalamanız: {avarage} notunuz: 2")
elif 55 <= avarage <= 69:
    print(f"Ortalamanız: {avarage} notunuz: 3")
elif 70 <= avarage <= 84:
    print(f"Ortalamanız: {avarage} notunuz: 4")
elif 85 <= avarage <= 100:
    print(f"Ortalamanız: {avarage} notunuz: 5")
"""


# question 3
"""
import datetime

tarih = input("ne zaman trafihe çıktı? (2019/8/9): ")
tarih = tarih.split("/")
trafige_cikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafige_cikis

days = fark.days


if days <= 365:
    print("1.servis aralığı.")
elif 365 < days <= 365*2:
    print("2.servis aralığı.")
elif 365*2 < days <= 365*3:
    print("3.servis aralığı.")
else:
    print("hatalı süre.")
"""




