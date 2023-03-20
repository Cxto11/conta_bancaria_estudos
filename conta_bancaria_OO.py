class Conta:
    def __init__(self,numero,titular,saldo,limite):
        print("criando conta... {}" .format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def extrato(self):
        print("O titular {},possui {} de saldo disponivel." .format(self.titular , self.saldo))
    
    def saque(self, valor):
        self.saldo -= valor
    
    def deposita(self,valor):
        self.saldo += valor
    