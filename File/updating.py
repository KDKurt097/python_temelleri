# "r+" klosörün olduğu konuma göre güncelleme işlemi yapar
"""
with open("newfile.txt","r+", encoding = "utf-8") as file: 
    file.seek(0)
    file.write("deneme ")

with open("newfile.txt","r+", encoding = "utf-8") as file: 
    print(file.read())
"""
# "r+" dosyada belirtilen yeri , "a" dosyanın en sonuna günceller
# *************** dosyanın en başını güncelleme ***************
"""
with open("newfile.txt","r", encoding = "utf-8") as file: 
    content = file.read()
    content = "Mahmut Tuncer\n" + content
    file.seek(0)
    file.write(content)

with open("newfile.txt","r", encoding = "utf-8") as file: 
    print(file.read())
"""
# *************** dosyanın ortasını güncelleme ***************
with open("newfile.txt","r+", encoding = "utf-8") as file:
    list = file.readlines()
    list.insert(1,"Muharrem\n")
    file.seek(0)
    file.writelines(list) # writelines okumak için liste kullanır

with open("newfile.txt","r", encoding = "utf-8") as file: 
    print(file.read())


