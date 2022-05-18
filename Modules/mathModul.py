# YÖNTEM 1
# import math
# import math as islem # bunu kullanırsak math yerine islem yazmamız gerekir

"""
# modülün içindeki fonksiyonları öğrenmek için "dir" ne işe yardıklarını görmek için "help" kullanılır. tek bir fonksiyondan bilgi almak için fonksiyonun adını yazmak yeterli.
#value = dir(math)
#value = help(math)
#value = help(math.factorial)

value = math.factorial
"""

# YÖNTEM 2
from math import * # mathın içindeki herşeyi aldığı için "math." kullanmamıza gerek kalmadı.
# from math import factorial,sqrt # böyle yazarsak belirli fonksiyonları içeri aktarırız.

value = factorial(5)


print(value)



