sifre = "123456"
isim= "Mahmut Tuncer"

sifre = "123456"
isim= "Mahmut Tuncer"

username= input("Adınız nedir?")
password= input("Şifreniz nedir?")

if username==isim:
   if password==sifre:
        print(isim, "  Hoşgeldiniz")
   else :
    print(username, "Yanlış Şifre. Tekrar deneyiniz!!!")
else:
 print("Yanlış isim")