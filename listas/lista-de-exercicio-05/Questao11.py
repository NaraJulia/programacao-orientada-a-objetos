QUESTAO 11
def validaData(data):
	global m,d,a
	data = data.split('/')
	m = data[1]
	m = int(m)
	d = data[0]
	d = int(d)
	a = data[2]
	a = int(a)
	if m>0 or m<13:
		if m==2:
			if d==29:
				if(a%4 == 0 and a%100!= 0) or (a%400==0): #ano bissexto
					return "VALIDA"
		else:
			return "NULL"
	elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
		if d>0 and d<=31: #m�s de 31 dias
			return "VALIDA"
		else:
			return "NULL"
	elif m==4 or m==6 or m==9 or m==11:
		if d>0 and d<=30: #m�s de 30 dias
			return "VALIDA"
		else:
			return "NULL"
	else:
		return("NULL")
print(" Data com m�s por extenso. ")
data = input("Digite uma data com o seguinte formato dd/mm/aaaa: ")
mes = ['','Janeiro','Fevereiro','Mar�o','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
valida = validaData(data)
if valida == "VALIDA":
	print("Data com m�s por extenso: ",str(d),"de",str(mes[m]),"de",str(a))
else:
	print("Data inv�lida!")