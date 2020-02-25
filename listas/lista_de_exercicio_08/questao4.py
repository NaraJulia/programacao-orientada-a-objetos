Questão 4
class Caneta:
	def __init__(self,cor, marca, numero_ponta, volume_tinta):
		self.cor = cor
		self.marca = marca
		self.numero_ponta = numero_ponta
		self.volume_tinta = volume_tinta

	def encher_caneta(self):
		self.volume_tinta = 50
		print(f"{self.volume_tinta}")

	def volume_caneta(self):
		self.volume_tinta -=1
		print(f"{self.volume_tinta}")

	def escrever(self,palavra):
		self.palavra = palavra
		print(palavra)
		self.volume_tinta -= 1

	def retornar_marca(self):
		return self.marca

	def imprimir_caracteristicas(self):
		print(f"Caracteristicas:\n{self.cor}\n{self.marca}\n{self.numero_ponta}\n{self.volume_tinta}")


can1 = Caneta("preta","bic",7,50)
can1.escrever("nara")
can1.volume_caneta()
can1.encher_caneta()
can1.imprimir_caracteristicas()		 