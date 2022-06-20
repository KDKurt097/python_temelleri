# decorator fonksiyonlar birden fazla fonksiyona özellik vermek için kullanılır

def myDecorator(func):
    def wrapper(name):
        print("önceki işlemler")
        func(name)
        print("sonraki işlemler")
    return wrapper

@myDecorator # bu aşağıdaki fonksiyonları myDecorator fonksiyonuyla ilişkilendirir. bunun yerine sayHella = myDecorator(sayHella) kullanılabilir
def sayHello(name):
    print("Hello", name)

sayHello("Ali") # eğer sayhello ya bir name parametresi vermek istiyorsak func() a ve wrapper() a da name parametresi vermemiz lazım


