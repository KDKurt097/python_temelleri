file = open("newfile.txt", encoding = "utf-8") # ekstra r yazmaya gerek yok   

# *************************** read() fonksiyonu okur
"""
content1 = file.read()

print("içerik 1")
print(content1)

content2 = file.read()

print("içerik 2")
print(content2) # içerik 2 de yazı yok çünkü içerik bir bittiğinde imleç en sonda kaldı bu yüzden içerik 2 boş kaldı
# eğer içerik 1 ve 2 nin arasına "file.close()" ya da tekrar "file = open("newfile.txt", encoding = "utf-8")"  konulursa 2. içerik de yazılır
"""
# ***************************
"""
content = file.read(2) # ilk 2 karakteri okur ve orda kalır
print(content)
content = file.read(4) # kaldığı yerden devam eder ve sonraki 4 karakteri okur
print(content)
"""
# *************************** readline() fonksiyonu her sefernde 1 satırı okur
"""
print(file.readline())
"""
# *************************** readlines() fonksiyonu liste şeklinde okur

list = file.readlines()
print(list)

file.close()

