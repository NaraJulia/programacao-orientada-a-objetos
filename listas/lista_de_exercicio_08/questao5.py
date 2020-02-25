Questão 5
class Pokemon:
	def __init__(self,nome, tipo, descricao, ataques, nivel, poder_luta ,brilhante):
		self. nome = nome
		self.tipo = tipo
		self.descricao = descricao
		self.ataques = []
		self.nivel = nivel
		self.poder_luta = poder_luta
		self.brilhante = brilhante
	def mostrar_ataques(self):
		print(self.ataques)
	def subir_nivel(self,nivel_acima):
		self.nivel_acima = nivel_acima
		self.nivel += nivel_acima
	def mostrar_poder_luta(self):
		print(self.poder_luta)
	def e_brilhante(self):
		if self.nivel > 100 or self.poder_luta > 1000:
			return True
		else:
			return False
	def adicionar_ataque(self, ataques_novos):
		self.ataques.append(ataques_novos)

pok1 = Pokemon("charmander","Fogo","Charmander é uma criatura reptiliana laranja.",[], 1,  139, True)
pok1.adicionar_ataque("Fogo")
pok1.mostrar_ataques()
pok1.subir_nivel(15)
pok1.mostrar_poder_luta()
print(pok1.e_brilhante())