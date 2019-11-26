QUESTAO 02
num = int(input())
def imprimir(num):
	lista = []
	while num not in lista:		
		for num in range(1,num+1):
			lista.append(num)
			x = str(lista).strip("[]").replace(",","")
			print(x)
imprimir(num)