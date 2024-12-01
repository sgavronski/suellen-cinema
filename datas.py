from calendar import month
from datetime import date, datetime, timedelta

data1 = date.today()
data2 = data1 + timedelta(days=5)
print(data1)
print(data2)
diferenca = data1 - data2
print("Diferença de dias:", diferenca.days)


'''hoje = date.today()
data = input(str("Data devolução: "))
datastrtodate = datetime.strptime(data, "%d/%m/%Y")
print(datastrtodate)
atraso = hoje - datastrtodate.date()
print(atraso.days)

datadevolucao = date.today()
datadevolucaoformatada = datadevolucao.strftime("%d/%m/%Y")
print(datadevolucaoformatada)
data_limite = date.today()
datalimiteformatada = data_limite.strftime("%d/%m/%Y")
diferenca = datadevolucaoformatada - datalimiteformatada
print(diferenca)'''
#strptime = pega um texto e transforma em data
#strftime = pega uma data e transforma em texto -> NÃO É POSSÍVEL fazer conta com a data em formato string

datadevolucao = date.today()
data_limite = date(day=30, month=11, year=2024)
print(datadevolucao)
print(data_limite)
print(datadevolucao-data_limite)
'''print(datadevolucao)
data_limite = date.today()
print(data_limite)
diferenca = datadevolucao - data_limite
print(diferenca.days)'''

data = "01/12/2024"
dataformat = datetime.strptime(data,"%d/%m/%Y")
print(dataformat.date())
x = date.today()
print(x)

lista1 = []
lista2 = []
soma = sum(lista1)+sum(lista2)
print(f'soma: {soma}')
print(len(lista1))