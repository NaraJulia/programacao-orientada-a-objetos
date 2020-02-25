Questão 6
class Retangulo:
	def __init__(self,comprimento,largura):
		self.comprimento = comprimento
		self.largura = largura
	def mudar_valor_lado(self,novo_comprimento,nova_largura):
		self.novo_comprimento = novo_comprimento
		self.nova_largura = nova_largura
	def retornar_valor_lado(self):
		return self.comprimento,self.largura
	def calcular_area(self):
		area = self.comprimento*self.largura
		return area
	def calcular_perimetro(self):
		perimetro = (self.comprimento*2) + (self.largura*2)
		return perimetro

comprimento = int(input())
largura = int(input())

r1= Retangulo(comprimento,largura)      
piso = r1.calcular_area()
print(r1.calcular_area())
print(r1.calcular_perimetro())
rodape = r1.calcular_perimetro()
print(f"Piso:{piso}m²") 
print(f"Rodape:{rodape/2}m²")
