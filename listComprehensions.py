# Döngülerin daha basit ve temiz versiyonu
"""
numbers = [x*x for x in range(10) if x % 3 == 0]

print(numbers)
"""
"""
myString = "Hello"
myList = [letter for letter in myString]
print(myList)
"""
"""
years = [1987,2003,1961,2000]
ages = [2022 - year for year in years]
print(ages)
"""
"""
results = [x if x%2==0 else "Tek" for x in range(1,10)]
print(results)
"""
"""
numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)
"""










