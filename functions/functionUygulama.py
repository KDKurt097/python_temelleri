
# Question 1
"""
def q1():
    word = input("Hangi kelimenin yazılmasını istersiniz, giriniz: ")
    number = int(input("Kelimeyi kaç kez göstermek istersiniz, giriniz: "))

    while number > 0:
        number -= 1

        print(word)

q1()
"""

# Question 2
"""
def q2(*params):
    return(params)

print(q2(10, 40, "Mahmut"))
"""

# Question 3
"""
def q3(number1, number2):
    for number in range(number1, number2+1):
        if number > 1:
            for i in range(2,number):
                if(number % i == 0):
                    break
            else:
                print(number)
                
number1 = int(input("sayı 1: "))
number2 = int(input("sayı 2: "))

q3(number1, number2)
"""

# Question 4
"""
def q4(number4):
    numbers = []
    for i in range(1,number4):
        if number4%i == 0:
            numbers.append(i)
            print(numbers)
q4(int(input("Sayıyı giriniz: ")))
"""




