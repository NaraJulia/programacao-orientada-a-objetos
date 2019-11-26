QUESTAO 10
import random
x = "Você ganhou, parabéns\n"
y = "\n\n\t***** Craps! *****\n\nVocê perdeu!!!\tTente de novo\n"
z = "Ponto\n"
def craps():
	dado1 = random.randrange(1,7)
	dado2 = random.randrange(1,7)
	soma = dado1+dado2
	print("Dado 1: ",dado1)
	print("Dado 2: ",dado2)
	print("A soma dos dados é: ",soma,"\n")
	return soma
print("GAME-CRAPS")
while True:
	jogar = input("Rolar dados (s ou n)? ")
	if jogar =='n' or jogar =='N':
		break
	else:
		resultado = craps()
	if resultado == 7 or resultado == 11:
		print(x)
	elif resultado == 2 or resultado == 3 or resultado == 12:
		print(y)
	else:
		print(z)
		while True:
			resultado2 = craps()
			if resultado == resultado2:
				print(x)
				break
			elif resultado2 == 7:
				print(y)
				break
			else:
				print("Ainda não foi dessa vez!\nSEGUE O JOGO!!!!\n")