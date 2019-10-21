Questao 11
salario = float(input("Quanto você ganha? "))
if salario <= 280:
	reajuste = (salario * 0.20) 
	novo = reajuste + salario
	print("O salário antes do reajuste era {:.2f}".format(salario))
	print("O percentual de aumento aplicado foi de 20%")
	print("O valor do aumento foi de {:.2f}".format(reajuste))
	print("o novo salário, após o aumento vai ficar {:.2f}".format(novo))
elif salario > 280 and salario <= 700:
	reajuste = (salario * 0.15) 
	novo = reajuste + salario
	print("O salário antes do reajuste era {:.2f}".format(salario))
	print("O percentual de aumento aplicado foi de 15%")
	print("O valor do aumento foi de {:.2f}".format(reajuste))
	print("o novo salário, após o aumento vai ficar {:.2f}".format(novo))
elif salario > 700 and salario <= 1500:
	reajuste = (salario * 0.10) 
	novo = reajuste + salario
	print("O salário antes do reajuste era {:.2f}".format(salario))
	print("O percentual de aumento aplicado foi de 10%")
	print("O valor do aumento foi de {:.2f}".format(reajuste))
	print("o novo salário, após o aumento vai ficar {:.2f}".format(novo))
else:
	reajuste = (salario * 0.05) 
	novo = reajuste + salario
	print("O salário antes do reajuste era {:.2f}".format(salario))
	print("O percentual de aumento aplicado foi de 5%")
	print("O valor do aumento foi de {:.2f}".format(reajuste))
	print("o novo salário, após o aumento vai ficar {:.2f}".format(novo))