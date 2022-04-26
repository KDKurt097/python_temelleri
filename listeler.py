A = ["BMW","Mercedes","Opel","Mazda"]
print(A)

list_number = len(A)

print(list_number)

print(A[0])
print(A[-1])

A[-1] = "Toyota"
print(A)

A0 = "Mercedes" in A
print(A0)

print(A[-2])
print(A[:3])

#A[-2:] = ["Toyota","Renault"]
A[-1] = "Rwnault"
A[-2] = "Toyota" 
print(A)

A1 = A + ["Audi","Nissan"]
print(A1)

del A[-1]
print(A)

print(A[::-1])

studentA = ["Yiğit","Bilgi",2010,[70,60,70]]
studentB = ["Sena","Turan",1999,[80,80,70]]
studentC = ["Ahmet","Turan",1998,[80,70,90]]
print(studentA)
print(studentB)
print(studentC)






