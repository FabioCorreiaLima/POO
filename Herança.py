#A herança é um tipo de relacionamento entre classes que significa que uma classe é outra. 
#É uma propriedade dos objetos que permite a criação de uma hierarquia entre eles, onde os descendentes herdem dos seus ancestrais suas estruturas de dados e seu código.

class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

class ContaCorrente(ContaBancaria):
    def __init__(self, saldo):
        super().__init__(saldo)
        self.limite_cheque_especial = 1000

    def sacar(self, valor):
        if valor <= self.saldo + self.limite_cheque_especial:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo):
        super().__init__(saldo)
        self.taxa_rendimento = 0.05

    def calcular_rendimento(self):
        rendimento = self.saldo * self.taxa_rendimento
        self.depositar(rendimento)

# Criando instâncias das classes
conta_corrente = ContaCorrente(1000)
conta_poupanca = ContaPoupanca(2000)

# Realizando operações nas contas
conta_corrente.sacar(500)  # Saque na conta corrente
conta_poupanca.depositar(1000)  # Depósito na conta poupança
conta_poupanca.calcular_rendimento()  # Cálculo de rendimento na conta poupança

print(conta_corrente.saldo)  # Saída: 500
print(conta_poupanca.saldo)  # Saída: 3100
