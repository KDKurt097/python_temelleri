
# class
# class oluşturmak için class komudu kullanılır


class Person:
    # class attributes # her zaman çalıştırılmayacak olanlar burada bulunur
    addres = "no information"

    # constructor (yapıcı method) # class çalıştırıldığı anda çalıştırılır
    def __init__(self, name, year):
        
        # object attributes
        self.name = name
        self.year = year
        print("init çalıştı")

    # instance methods 
    def intro(self):
        print("Hello There")

# instance

p1= Person("Ali", 1999)
print(type(p1))

p1.intro()
print(p1.addres)
