
# def cria_conta(numero, titular, saldo, limite):
#     conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
#     return conta

# def deposita(conta, valor):
#     conta["saldo"] += valor

# def saca(conta, valor):
#     conta["saldo"] -= valor

# def extrato(conta):
#     print("Saldo: R${}".format(conta["saldo"]))

# class Pessoa:
#     def __init__(self, nome, sobrenome):
#         self.nome = nome
#         self.sobrenome = sobrenome

#     def exibe_nome_e_sobrenome(self):
#         print("{1} {0}".format(self.nome, self.sobrenome))


# pessoa = Pessoa("Chalita", "Steppat")
# pessoa.exibe_nome_e_sobrenome()

class Jogo:
    def __init__(self, contador):
        self.contador = 0

    def incrementa(self):
        self.contador+=1

