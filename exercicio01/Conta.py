from random import randint

class Conta:
    def __init__(self, titular: str):
        self.titular = titular
        self.saldo = 0.0
        self.numero = randint(1000, 9999)
        
    # método para depositar um valor na conta
    def depositar(self, valor: float):
        self.saldo = self.saldo + valor
        
    # método para sacar um valor da conta
    def sacar(self, valor: float):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
    
    # método para transferir dinheiro da conta para outra
    def transferir(self, valor: float, destino: "Conta"):
        if self.saldo >= valor:
            self.sacar(valor)
            destino.depositar(valor)
        
        
# programa principal
conta = Conta("selmini")
conta2 = Conta("Carlos Rafael")
conta.depositar(7500)
conta.transferir(7000, conta2)
print(conta.saldo)
print(conta2.saldo)