# Question 1
"""
numbers = [1,3,5,7,9,12,19,21]
i = 0
while (i < len(numbers))  :
    print(numbers[i])
    i += 1
"""
# Question 2
"""
start = int(input("Başlangıç değerini giriniz: "))
finish = int(input("Bitiş değerini giriniz: "))
i = start

while i < finish:
    i += 1
    if (i % 2 == 1):
        print(i)
"""

# Question 3
"""
h = 100

while 0 < h:
    h -= 1
    print(h)
"""

# Question 4
"""
i = 0
numbers = []

while i < 5:
    number = int(input("Bir sayı giriniz: "))
    numbers.append(number)
    i += 1
numbers.sort()

print(numbers)
"""

# Question 5
"""
Products = []

piece = int(input("Kaç ürün eklemek istersiniz: "))
i = 0

while (i < piece):
    name = input("Ürün ismi: ")
    price = input("Ürün fiyatı: ")
    Products.append({
        "name":name,
        "price":price  
    })
    i += 1

for Product in Products:
    print(f"Ürün adı: {Product['name']} ürün fiyatı: {Product['price']}")
"""





