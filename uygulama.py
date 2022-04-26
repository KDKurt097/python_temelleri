


website = "http://www.mahmuttuncer.com"
kurs = "Halay kursu: Baştan sona halay çekme rehberimiz (40 saat)"

m = " Hello World "
m0 = m.strip()
print(m0)

#print(website[11:-4])
website4 = "www.MahmuttunÇer.com".strip("moc.w")
print(website4)


kurs0 = kurs.lower()
print(kurs)

website1 = website.count("a")
print(website1)


website1 = website.startswith("www")
website2 = website.endswith("com")
print(website1)
print(website2)


website3 = website.find(".com")
print(website3)

kurs1 = kurs.isalpha()
kurs2 = kurs.isdigit()
print(kurs1)
print(kurs2)

C = "contents"
C = C.center(50,"*")
print(C)

kurs3 = kurs.replace(" ","-")
print(kurs3)

m1 = m0.replace("World","There")
print(m1)

kurs4 = kurs.split(" ")
print(kurs4)































