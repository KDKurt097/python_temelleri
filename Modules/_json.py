
#  !!! json bize veri taşımada yardım eder !!!

import json

personString = '{"name":"Ali", "languages":["python","C#"]}'

personDict = { "name": "Ali","languages": ["Python","C#"]} 

# JSON string to Dict
"""
jsonDonusturme = json.loads(personString)
#jsonDonusturme = jsonDonusturme["name"]

print(jsonDonusturme)
"""
# Bunun yerine bu kullanılabilir
with open("person.json") as f:
    data = json.load(f)
    print(data)
# ***************************************************


# Dict to JSON string
"""
print(type(personDict))

jsonCevirme = json.dumps(personDict) # json un bilgiye ulaşabilmesi için bilgiyi str yapar
print(type(jsonCevirme))
"""
personDict = json.loads(personString)
result = json.dumps(personDict, indent= 4) # okunaklığı arttırmak için belirtilen sayıda boşluk bıraktırır

print(personDict)
print(result)