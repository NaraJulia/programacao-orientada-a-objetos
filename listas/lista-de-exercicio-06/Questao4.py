Questao 4
def  media(nome,notas):
	notas = []
	nome = []
	nomeI = 0
	notasI = 0
	with open("notas.txt") as arq_notas:
		for linhas_nota in arq_notas:
			nota = linhas_nota.split() 
			n1 = float(nota[0])
			n2 = float(nota[1])
			notas.append((n1+n2)/2)
	with open("nome.txt") as arq_nome:
		with open("media.txt","w") as arq_media:
			for linhas_nome in nome:
				nome.append(linhas_nome.split("\n"))
				print("{},{:.2f}".format(nome[nomeI],nota[notasI]),file = arq_media)
				nomeI = nomeI + 1
				notasI = notasI + 1
media("nome.txt", "notas.txt")