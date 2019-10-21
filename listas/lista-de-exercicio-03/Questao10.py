Questao 10
t = str(input("Digite em que turno você estuda: M=maturnino, V=vespertino ou N=noturno: ").upper())
if t == "M":
    print("Bom dia!")
elif t == "V":
    print("Boa tarde!")
elif t == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")