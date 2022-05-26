# range method
"""
# elimizde liste olmadan kullanmak liste kullanmak için
for item in range(20,100,30):
    print(item)
print(list(range(20,100,30)))
"""

# enumerate method
"""
# hem index numaralarının yazdığı hem elemanların yazdığı bir listeye çevirir
greeting = "Hello There"

for index,letter in enumerate(greeting):
    print(f"index: {index} letter: {letter}")
"""

# zip method
"""
# listeleri eşleştirmeye yarar
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]

print(list(zip(list1,list2)))
"""


