QUESTAO 13
def moldura(lin,col):
	print("+","-"*col,"+")
	for x in range(lin):
		print("|"," "*col,"|")
		print("+","-"*col,"+")

col = input("Número de Colunas: ")
lin = input("Número de Linhas: ")
if col == "":
	col = '1'
if lin =="":
	lin = '1'
col = int(col)
lin = int(lin)
if col == 0:
 col = 1
elif col > 20:
	col = 20
if lin == 0:
	lin = 1
elif lin > 20:
	lin = 20
moldura(lin,col)