isimler = ["Ali","Yağmur","Hakan","Deniz"]
yıl = [1998, 2000, 1998, 1987]

isimler.append("Cenk")
isimler.insert(0,"Sena")
index = isimler.index("Deniz")
isimler.remove("Deniz")
isimler_ali = "Ali" in isimler
isimler.sort()
isimler.reverse()
yıl.sort()
yıl_1998 = yıl.count(1998)
str = "chevrolet,Dacia"
araba = str.split(",")
markalar = []
marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)

print(isimler)
print(isimler_ali)
print(yıl)
print(yıl_1998)
print(min(yıl))
print(max(yıl))
yıl.clear()
print(yıl)
print(index)
print(araba)
print(markalar)
