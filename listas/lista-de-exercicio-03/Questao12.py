Questão 12
hora = float(input("Informa o valor recebido por hora trabalhada:"))
qhora = float(input("Informe a quantidade de horas trabalhadas no mes:"))

salariobruto = hora * qhora
fgts = (salariobruto * 11) / 100
sindicato = (salariobruto * 3) / 100

if salariobruto <= 900:
    salariol = salariobruto - sindicato

elif salariobruto > 900 and salariobruto <=  1500:
    ir = (salariobruto * 5) / 100
    salariol = salariobruto - ir - sindicato
 
elif salariobruto > 1500 and salariobruto <= 2500:
    ir = (salariobruto * 10) / 100
    salariol = salariobruto - ir - sindicato

else:
    ir = (salariobruto * 20) / 100
    salariol = salariobruto - ir -sindicato
    
print("Seu salario bruto e :{:.2f}".format(salariobruto))
print("O valor de seu FGTS e de:{:.2f}".format(fgts))
print("O sindicato vai te levar:{:.2f}".format(sindicato))
print("Seu salario liquido e de:{:.2f}".format(salariol))
