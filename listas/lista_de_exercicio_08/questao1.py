Questão 1
class Bola:
	def __init__(self,cor,circunferencia,material):
		self.cor = cor
		self.circunferencia = circunferencia
		self.material = material

	def trocarCor(self , novaCor):
		self.cor = novaCor

	def mostraCor(self):
		print(f"{self.cor}")

	def imprimir(self):
		print(f"{self.circunferencia}\n{self.material}")

b1 = Bola("Preto",70,"couro")
b1.trocarCor("Pink")
b1.mostraCor()
b1.imprimir()