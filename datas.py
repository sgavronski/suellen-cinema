from datetime import date, datetime, timedelta

data1 = date.today()
data2 = data1 + timedelta(days=5)
print(data1)
print(data2)
diferenca = data1 - data2
print("Diferença de dias:", diferenca.days)
