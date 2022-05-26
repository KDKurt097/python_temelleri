# encapsulation #
# fonksiyon içindeki fonksiyonların çalışması için içerdeki fonksiyonların dışardaki fonksiyonların içinde kullanılaması lazım
# eğer inner_increment'i direk kullanmak istersek hata verir. vermemesi için örnekteki gibi kullanılması gerekir
def outer(num1):
    print("outer")
    def inner_increment(num1):
        print("inner")
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1, num2)

outer(10) 
    