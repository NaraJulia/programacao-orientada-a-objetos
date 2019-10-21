Questao 13
sexo = input("Qual seu sexo?")
altura = float(input("Digite sua altura:"))
if sexo == "masculino":
	pesoIm = (72.7*altura)-58
	print("Seu peso ideal é {:.2f}".format(pesoIm))
else:
	pesoIf = (61.1*altura)-44.7
	print("Seu peso ideal é {:.2f}".format(pesoIf))