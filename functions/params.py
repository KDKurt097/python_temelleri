# fonksiyonlara parametre olarak fonkisyon yollayabiliriz

def toplama(a,b):
    return a+b
def cikartma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1, f2, f3, f4, islemAdi):
    if islemAdi == "toplama":
        print(f1(2,3))
    elif islemAdi == "cikartma":
        print(f2(2,3))
    elif islemAdi == "carpma":
        print(f3(2,3))
    elif islemAdi == "bolme":
        print(f4(2,3))
    else:
        print("Geçersiz işlem...")

islem(toplama,cikartma,carpma,bolme,"toplama")
