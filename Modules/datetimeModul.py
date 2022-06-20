

# !!!datetime bize zamanla ilgili işlerde yardım eder!!!


#import datetime
from datetime import date, datetime

#print(dir(datetime))

simdi = datetime.now()
print(simdi)

saniye = simdi.second # saniye dışındaki diğer zaman birimleriyle de çalışabilir
print(saniye)

simdiV1 = datetime.ctime(simdi)
print(simdiV1)

simdiV2 = datetime.strftime(simdi,"%Y %B %A") # bu şekilde de istediğin bilgileri alabilirsin ama burdaki komutların çoğunu araştırman gerek
print(simdiV2)

t = "21 April 2019"
dt = datetime.strptime(t, "%d %B %Y")
dt = dt.year
print(dt)



