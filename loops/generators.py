# generators bellekte yer tutmayan bir iterators oluşturur

def cube():
    for i in range(5):
        yield i ** 3 # generators kullanmak için yield komutunu kullabiliriz ve bu değer tek seferliktir yani bu değere tekrar ulaşmak için işlemi tekrarlamak gerekir

generator = cube()

print(next(generator))

liste = (i**3 for i in range(5)) # yield yerine normal parantez kullanarak bu şekilde de yapılabilir

print(next(liste))
