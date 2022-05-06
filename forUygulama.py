# Question 1
"""
numbers = [1,3,5,7,9,12,19,21]

for n in numbers:
    print(n % 3 == 0 )
"""

# Question 2
"""
numbers = [1,3,5,7,9,12,19,21]

total = 0
for n in numbers:
    total += n
print("toplam:",total)
"""   

# Question 3
"""
numbers = [1,3,5,7,9,12,19,21]

for n in numbers:
    if n % 2 == 1:
        print(n**2)
"""

# Question 4
"""
cities = ["kocaeli","istanbul","ankara","izmir","rize"]

for c in cities:
    if len(c) <= 5:
        print(c)
"""      
# Question 5
"""
Products =[
    {"name":"samsung S6", "price": "3000"},
    {"name":"samsung S7", "price": "4000"},
    {"name":"samsung S8", "price": "5000"},
    {"name":"samsung S9", "price": "6000"},
    {"name":"samsung S10", "price": "7000"}
] 

total = 0
for p in Products:
    price = int(p["price"])
    total += price
print("toplam ürün fiyatı",total)
"""

# Question 6
"""
Products =[
    {"name":"samsung S6", "price": "3000"},
    {"name":"samsung S7", "price": "4000"},
    {"name":"samsung S8", "price": "5000"},
    {"name":"samsung S9", "price": "6000"},
    {"name":"samsung S10", "price": "7000"}
] 

for p in Products:
    if int(p["price"]) <= 5000:
        print(p["name"])
"""
