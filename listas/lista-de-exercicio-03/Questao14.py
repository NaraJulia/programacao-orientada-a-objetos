Questão 14
n1 = float(input())
n2 = float(input())
media = (n1 + n2)/2
if media >= 9 and media <= 10:
	print("Sua nota foi {}".format(media))
	print("A")
	print("Aprovado")
if media >= 7.5 and media <= 9:
	print("Sua nota foi {}".format(media))
	print("B")
	print("Aprovado")
if media >= 6 and media <= 7.5:
	print("Sua nota foi {}".format(media))
	print("C")
	print("Aprovado")
if media >= 4 and media <= 6:
	print("Sua nota foi {}".format(media))
	print("D")
	print("Reprovado")
if media >= 4 and media <= 0:
	print("Sua nota foi {}".format(media))
	print("E")
	print("Reprovado")