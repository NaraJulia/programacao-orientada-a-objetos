from datetime import datetime
class Compras:
    def __init__(self,vendedor,data,valor):
        self.vendedor = Vendedor()
        self.data = datetime.now()
        self.valor = valor

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def is_adulto(self):
        if self.idade >= 18:
            return True
        else:
            return False

class Cliente:
    def __init__(self,nome,idade):
        super().__init__(nome, idade)
        self.compras = []
    def __str__(self):
        return f"Cliente:{self.nome} Idade:{self.idade}"

    def registrar_compra(self,compra):
        self.compras.append(compra)
    def total_compra(self):
        total = 0
        for item in self.compras:   
            total += item.valor
        print(f"Total:R${total}")

    def get_data_ultima_compra(self):
        pass
        
class Vendedor:
    def __init__(self,nome,idade,salario):
        super().__init__(nome, idade)
        self.salario = salario
    def __str__(self):
        return f"Vendedor:{self.nome} Idade:{self.idade}"



if __name__ == "__main__":
    p1 = Pessoa("Nara","18")
    
    
    
