htmlDoc = """
<!DOCTYPE html> 
<html lang="en"> 
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Halay Kursları</title>
</head>
<body>
<h1>
        Halay Kursları
        </h1>
    <h3>
    Lorem ipsum dolor sit amet.
    </h3>
    <ul>
        <li> Bir mendil alın</li>
    </ul>
    
</body>
</html> 
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(htmlDoc,"html.parser") # html.parser denetleme mekanızmamızdır (html üzerinde denetleme yapılacağı için html.parser)

result = soup.prettify() # karışık olarak verilen dökümanı düzeltir

#result = soup.title # title bilgisini verir. Bu sadece title için değil bütün bölümler için kullanılabilir
#result = soup.title.string # bize title içindeki yazılı bilgiyi verir

#result = 


print(result)