
class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def valida(self, dia, mes, ano):
        if (self.dia>0 and self.dia<=31):
            return self.dia
        elif (self.mes>0 and self.mes<=12):
            return self.mes
        elif (self.ano>=1):
            return self.ano

    def formatada(self):
        if (self.dia and self.mes and self.ano != 0):
            print("{:02}/{:02}/{:04}".format(self.dia, self.mes, self.ano))
        else:
            print("Data inválida!")

# python   
# from datas import Data
# d = Data(21,11,2007)
# d.formatada()