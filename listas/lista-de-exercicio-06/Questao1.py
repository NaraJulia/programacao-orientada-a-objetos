Questao 1
from random import randint  
n = int(input())
nome = ["Nara","Vitoria","Vitor","Mateus","Eliene","Fernando","Adriana","Adriano","Francisco","Eliane","Andreza","Isaac","Andre","Neto","Pedro","Wanderson","Aldivanha","Socorro","Julia","Fernanda"]
sobrenome = ["Fernandes","Diogenes","Silva","Chagas","Jr","Lopes","Paz","Cunha","Park","Vieira","Pinheiro","Lima","Nunes","Oliveira","Muniz","Assis","Cavalcante","Andrade","Moreira","Amorrim"]
#nome = randint(0,21)
#sobrenome = randint(0,21) 
#idade = randint(0,101)
with open("nome_idade.txt","w") as arq:
	for x in range(0,n):
		aleatorio_nome = randint(0,len(nome)-1)
		aleatorio_sobrenome = randint(0,len(sobrenome)-1) 
		idade = randint(0,101)
		valor_aleatorioN = nome[aleatorio_nome]
		valor_aleatorioS = sobrenome[aleatorio_sobrenome]
		print("{} {} {}".format(valor_aleatorioN,valor_aleatorioS,idade), file = arq)