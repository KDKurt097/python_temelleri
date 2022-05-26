# error => hata

# print(a) => NameError
# int("1a2") => ValueError
# print(10/0) => ZeroDivisionError
# print("denme"e) => SyntaxError

# error handling => hata yönetimi

while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)


    except Exception as ex:#(ZeroDivisionError,ValueError) as ex:
        print("Hatalı bilgi girdiniz. Lütfen tekrar deneyin.", ex)
        #print(ex)
    else:
        break
    finally:
        print("try except sonlandı.")



