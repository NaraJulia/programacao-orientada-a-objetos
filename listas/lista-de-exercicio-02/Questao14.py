Questao 14
peso = int(input("Digite o peso:"))

if peso > 50:
	excesso = peso - 50
	multa   = excesso * 4
else:
	excesso = "ZERO"
	multa = "ZERO"

print ("O excesso de peso foi de {} ,por isso a multa vai ser de {}".format(excesso,multa))