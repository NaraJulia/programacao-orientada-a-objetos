Questão 7
class Pessoa:
	def __init__ (self, nome, idade, peso, altura):
		self.nome = nome
		self.idade = idade
		self.peso = peso
		self.altura = altura
	def envelhecer(self,ano):
		self.idade += ano
		if self.idade < 21:
			self.altura+=0.5
	def engordar(self,peso_mais):
		self.peso += peso_mais
	def emagrecer(self,peso_menos):
		self.peso -= peso_menos
	def crescer(self,altura_mais):
		self.altura += altura_mais

p1 = Pessoa('nara julia', 18, 70, 168)
p1.envelhecer(1)
print(p1.idade)
print(p1.altura)
p1.engordar(1)
print(p1.peso)
p1.emagrecer(3)
print(p1.peso)
p1.crescer(2) #(2 + 0.5) 
print(p1.altura)