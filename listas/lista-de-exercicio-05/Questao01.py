QUESTÃO 01
def imprimir(num):
	for x in range(1,num+1):
		print("{} {}".format(x,"")*x)
num = int(input())
y = imprimir(num)