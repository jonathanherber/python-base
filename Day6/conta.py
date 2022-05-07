class Conta:
    def __init__(self,nome):
        self.nome = nome
        self.__saldo = 0
    @property
    def saldo(self):
        return self.__saldo
    
    
conta = Conta("jonathan")
conta.saldo = 12
print(conta.saldo)