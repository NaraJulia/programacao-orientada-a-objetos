Questao 15
salarioH = float(input('Quanto ganha por hora? '))
horasM = int(input('Horas trabalhadas por m�s: '))
salarioB = salarioH * horasM
ir = salarioB * 0.11
inss = salarioB * 0.08
sindicato = salarioB * 0.05
salarioL = salarioB - ir - inss - sindicato 
print("+ Sal�rio Bruto : R$ {:.2f}".format(salarioB))
print("- IR (11%) : R$ {:.2f}".format(ir))
print("- INSS (8%) : R$ {:.2f}".format(inss))
print("- Sindicato (5%) : R$ {:.2f}".format(sindicato))
print("= Sal�rio Liquido : R$ {:.2f}".format(salarioL))
