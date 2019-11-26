QUESTAO 06
def horas(hora,minu):
	calculo = hora-12
	hm = ("{} {}".format(calculo,minu))
	return hm
hora= int(input())
minu = int(input())
x = horas(hora,minu)

def periodos(hora,minu):
	if (x == "00:00" and "11:59"):
		return ("A.M")
	else:
		return ("P.M")
h = periodos(hora,minu)
print(x,h)