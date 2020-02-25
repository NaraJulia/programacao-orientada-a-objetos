Questão 2
class Computador:
	def __init__(self,marca,modelo,componentes,anos_uso, cor):
		self.marca = marca
		self.modelo = modelo
		self.componentes = componentes
		self.anos_uso = anos_uso
		self.cor = cor
		#mostrarMarca, adicionarComponentes, mostrarComponentes, mostrar_anos_uso, envelhecer
	def mostraMarca(self):
		print(f"{self.marca}")

	def adicionarComponentes(self,novoComponentes):
		self.componentes.append(novoComponentes)
		
	def mostraComponentes(self):
		print(f"{self.componentes}")

	def mostra_anos_uso(self):
		if self.anos_uso >= 6:
			print("Seu computador está tão velho que tem problemas de junta… junta tudo e joga fora...")
		else:
			print(f"{self.anos_uso}")

	def envelhecer(self):
		self.anos_uso += 1
	


c1 = Computador("Itautec","intel",["monitor","teclado"],2,"preto")
c1.mostraMarca()
c1.mostraComponentes()
c1.adicionarComponentes("mouse")
c1.mostra_anos_uso()
c1.envelhecer()
#c1.mostra_anos_uso()