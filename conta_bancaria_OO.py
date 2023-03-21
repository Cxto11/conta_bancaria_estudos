
class conta:
##################OBJETO####################    
    def __init__(self):#PARAMETROS#
        self.__titular = input("Titular: ")
        self.__saldo = (0.0)
        self.__credito = (100.00)
        print("Conta criada com sucesso! ID({})" .format(self))
        print("saldo {}".format(self.__saldo))

##################METODOS###################           
    def saque(self,valor):
        self.__saldo -=valor
    
    def deposito(self,valor):
        self.__saldo += valor   
    
    def extrato(self):
        print("O titular {},possui {} de saldo disponivel." .format(self.__titular , self.__saldo)) 

    def transfere(self,valor,destino):
        self.saque(valor)
        destino.deposito(valor)

    @property   
    def credito(self):
        return self.__credito

    def get_titular(self):
        return self.__titular.title
    def get_saldo(self):
        return self.__saldo
    
    @credito.setter
    def credito(self, credito):
        self.__credito =credito
    