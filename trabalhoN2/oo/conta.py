import datetime

class Conta:
    def __init__(self, numero, cliente, saldo, limite=10000):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
        self.abertura = Abertura()
        self.historico.dados_conta = (f"Conta : {self.numero} | Titular: {self.cliente.nome}\n")

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(datetime.datetime.today())
        self.historico.transacoes.append("Depósito de {}".format(valor))

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(datetime.datetime.today())
            self.historico.transacoes.append("Saque de {}".format(valor))
            return True
        
    def extrato(self):
        print("**EXTRATO**".center(36, '-'),"\n")
        print(f"Cliente: {self.cliente}")
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))
        self.historico.transacoes.append(datetime.datetime.today())
        self.historico.transacoes.append(f"Tirou extrato - saldo de {self.saldo}")
        print("\n","-" * 35)

    def transfere_para(self, destino, valor):
        tirou = self.saca(valor)
        if (tirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(datetime.datetime.today())
            self.historico.transacoes.append(f"Transferencia de {valor} para conta {destino.numero}")
            return True
    def __str__(self):
        return (f"Conta: {self.conta} Nome: {cliente}")

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        
    def __str__(self):
	    return (f"{self.nome} {self.sobrenome} \nCPF: {self.cpf}")


class Historico:
    def __init__(self):
        self.abertura = datetime.date.today()
        self.transacoes = []
        self.dados_conta = ""
    
    def imprime(self):
        print("**HISTORICO**".center(36, '-'),"\n")
        print("Data abertura: {}".format(self.abertura))
        print(self.dados_conta)
        print("Transações: ")
        for x in self.transacoes:
            print("*", x)
        print("\n","-" * 35)

class Abertura:
    def __init__(self):
        self.abertura = datetime.datetime.today()

if __name__ == "__main__":
    cliente1 = Cliente("Nara","Fernandes","082.840.003-26")
    cliente2 = Cliente("Antonio","Fernandes","000.000.000-00")
    #cliente3 = Cliente()
    conta1 = Conta("000.000-0",cliente1,1000)
    conta2 = Conta("000.000-1",cliente2,1000)
    #conta3 = Conta()
    conta1.deposita(1500)
    conta2.deposita(500)
    #conta3.deposita()
    conta1.historico.imprime()
    conta2.historico.imprime()
    #conta3.historico.imprime()
    conta1.saca(500)
    conta2.saca(200)
    #conta3.saca()
    conta1.extrato()
    conta2.extrato()
    #conta3.extrato()
    conta1.transfere_para(conta2,300)
    conta1.historico.imprime()
    conta2.transfere_para(conta1,500)
    conta2.historico.imprime()
    #conta3.transfere_para()
    #conta3.historico.imprime()
    