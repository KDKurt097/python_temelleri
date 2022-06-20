# Bu modül gibi python ile birlikte gelmeyen modülleri terminale "pip install modül adı" yazarak yükleyebiliriz
# İndirebileceğimiz modüllere bakmak için "https://pypi.org/" sitesi kullanılabilir

# !!! requests websitelerin kaynak kodlarına ulaşmamızda yardım eder !!!

import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text) # verdiğimiz sitedeki bilgiyi terminale yazdırır (json bilgiyi düzgün bir şekilde yazdırmak için kullanılamıştır. kullanmaya gerek yoktur)


for i in result:
    print(i)