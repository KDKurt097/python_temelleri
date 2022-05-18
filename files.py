
# Dosya açmak ya da oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosyaAdi, dosyaErişmeModu)
# dosyaErişmeModu => dosyayı hangi amaçla açtığını belirtir.

# "w": (Write) yazma modu. Dosyayı konumda oluşturur. (w son dosyayı eskilerin üstüne yazdırır)
file = open("newfile.txt","w",encoding = "utf-8") # encoding = "utf-8" türkçe karakterleri eklemek için
# file = open("c:/users/kizey/desktop/newfile.txt","w")
file.write("Kurt ğıİçöş") # oluşturlan dosyaya fazmak için write
file.close()

# "a": (Append) ekleme. Dosyayı konumda yoksa oluşturur. (a  dosyayı eskilerin yanına ekler.)
# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
# "r": (Read) okuma. varsayılan. dosya konumda yoksa hata verir.

