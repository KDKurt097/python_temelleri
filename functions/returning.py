# içteki fonksiyonları return ile geri gönderirsek direk olarak ana fonksiyonlar bir çalışırlar
def islemler(islemAdi):
    def toplama(*args):
        toplama = 0
        for i in args:
            toplama += i
        return toplama

    def carpma(*args):
        carpma = 1
        for i in args:
            carpma *= i
        return carpma

    if islemAdi == "toplama":
        return toplama
    elif islemAdi == "carpma":
        return carpma

toplama = islemler("toplama")
print(toplama(1,4,7,9))

carpma = islemler("carpma")
print(carpma(1,4,7,9))


