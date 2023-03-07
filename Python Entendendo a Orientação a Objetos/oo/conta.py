

class Conta:
    
    def __init__(self, numero, titular, saldo, limite): #Função construtora
        print("Construindo objeto ... {}".format(self))
        self.numero = int(numero)
        self.titular = str(titular)
        self.saldo = float(saldo)
        self.limite = float(limite)

    def extrato(self):
        print("Saldo de R${} do titular {}".format(self.saldo, self.titular))
  
    def saca(self, valor=0):
        #valor = input("Qual valor do saque? R$ ")
        self.saldo -= valor
        #print("Saldo de R${} do titular.".format(self.saldo))

    def deposita(self, valor):
        self.saldo += valor

    #def saldo(self):
    #    print("O saldo é de R$ {} ".format(self.saldo))