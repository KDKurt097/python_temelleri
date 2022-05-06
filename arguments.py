
# sum toplama işlemi görevi gören bir fonksiyondur

"""
def add(a, b, c =0): # c sıfır olduğu için istersek c ye değer vermiyebiliriz
    return sum((a,b,c))


print(add(30,40,50))
"""
"""
def add(*params): # buraya sayılar yerine direk bi tuple( * dediğimiz için tuple) verdiğimiz için istediğim kadar sayı ekliyebilirim
    return sum((params))


print(add(10,40,50,-10))
"""
"""
def user(**args): # ** dictionary(dict) demek
    for key, value in args.items():
        print(f"{key} is {value}")

user(name= "Kuzey", age= 22, city= "Aydın")
"""





