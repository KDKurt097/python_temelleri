

# !!! os bize işletim sistemi ile ilgili konularda yardım eder !!!


import os

#print(dir(os))

istimSistemi = os.name
print(istimSistemi) # sistemin ismini verir

dosyaBilgisi = os.stat("Modules") # belirtilen dostayla ilgili bilgi verir.
print(dosyaBilgisi)

#             Klasör değiştirme 
# os.chdir("C:\\") bu bizi c dizinine götürür. 
# os.chdir("..") dersek bizi bir üst dizine atar.
# os.chdir("../..") iki üst dizeye atar.
# ***************************************************

#             Klasör oluşturma 
# os.mkdir("newdirectory") bulunduğumuz klasörün altına newdirectory dosyasını ekler.
# os.makedirs("newdirectory/yeniKlasör") newdirectory dosyasının içine yeniKlasörü  oluşturur
# os.rename("newdirectory","tazeKlasör") Klasörün adını değiştirir
# os.rmdir("newdirectory") klasörü siler
# os.removdir("newdirectory/yeniKlasör") klasörün içindeki seçilen klasörü siler
# ***************************************************

#              Listeleme
# os.listedir() içerdeki klasörleri listeler
# os.listedir("C:\\") C klasörü içindeki klasörleri listeler
"""
for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)
"""
# ***************************************************

#              Etkin  dizin öğrenme
hangiKlasor = os.getcwd()
print(hangiKlasor) 
# ***************************************************  

#              Path
dosyaKonum = os.path.abspath("_os.py") # girilen dosyanın tam konumunu verir
dosyaYol = os.path.dirname(dosyaKonum) # dosyanın tam yolunu(dizin ismini) verir
print(dosyaYol)

dosyaVarMi = os.path.exists("_os .py") # girilen dosya ilgili konumda var mı
print(dosyaVarMi)

klasorMu = os.path.isdir("Modules") # klasör olup olmadığına bakar
dosyaMi = os.path.isfile("_os.py")  # dosya olup olmadığına bakar
print(klasorMu,dosyaMi)

bilestir = os.path.join("C:\\","deneme","deneme1") # verilen bilgileri birleştirir
ayir = os.path.split("C:\\deneme") # verilen bilgileri ayırır
uzantiAyir = os.path.splitext("_os.py") # verilen bilgiyi uzantısından ayırır

print(bilestir,ayir,uzantiAyir)


