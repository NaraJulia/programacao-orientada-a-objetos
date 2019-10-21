Questao 8
p1 = float(input("Qual o valor do primeiro produto? "))
p2 = float(input("Qual o valor do segundo produto? "))
p3 = float(input("Qual o valor do terceiro produto? "))
menor_valor = p1
if p2 < menor_valor:
	menor_valor = p2
if p3 < menor_valor:
	menor_valor = p3
print("O produto mais baroto é {:.2f}".format(menor_valor))