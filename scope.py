
# bu global bir veri
x = "global x"

def function():
    # bu local bir veri ve local veriler global veriyi etkilemez eğer x i local in içinde değiştirmek istersek global metodunu kullanabiliriz
    #global x
    x = "local x"
    print(x)

function()
print(x)



