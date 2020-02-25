Qurstão 3
class Quadrado:
	def __init__(self,tamanho_do_lado):
		self.tamanho_do_lado = tamanho_do_lado

	def mudar_valor_lado(self,novo_valor_lado):

		self.tamanho_do_lado = novo_valor_lado

	def retornar_valor_lado(self):
		return self.tamanho_do_lado 

	def calcular_area(self):
		return  (self.tamanho_do_lado*self.tamanho_do_lado)

q1 = Quadrado(4)
q1.mudar_valor_lado(6)
resultado = q1.retornar_valor_lado()
area = q1.calcular_area()
print(resultado)
print(area)