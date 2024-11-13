#Classe para clientes na Netflix

class Clientes:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception ("Plano inválido")

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print ("Plano inválido")

    def ver_filme(self,filme,plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme {filme}')
        elif self.plano == "premium":
            print (f'Ver filme {filme}')
        elif self.plano == "basic" and plano_filme == "premium":
            print('Faça upgrade para premium para ver esse filme')
        else:
            print ('Plano inválido')

cliente1 = Clientes('Suellen', 'ga.suellen@gmail.com','basic')
print(cliente1.plano)
cliente1.ver_filme('Harry Potter','premium')

#no botao de upgrade:
cliente1.mudar_plano('premium')
print(cliente1.plano)
cliente1.ver_filme('Harry Potter','premium')