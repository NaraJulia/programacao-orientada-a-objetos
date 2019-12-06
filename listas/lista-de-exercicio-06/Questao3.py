Questao 3
def copiar(nome_idade):
	with open("nome_idade.txt") as arq:
		with open("Arquivo_2","w") as arq2:
			for x in arq:
				if "//" in x:
					pass
				else:
					print(x, file = arq2)
copiar("nome_idade")