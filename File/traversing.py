# with kullanıldığında close yazıp dosyayı kapatmaya gerek kalmaz
with open("newfile.txt", encoding = "utf-8") as file: 
    content = file.read()
    print(content)
    file.seek(0) # klosörü girilen sayıya gönderir
    print(file.tell()) # klosörün nerede olduğunu sayı olarak yazdırır