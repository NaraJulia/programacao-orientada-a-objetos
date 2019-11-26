QUESTAO 05
def somaImposto(custo,taxa):
	altera = custo + (custo*taxa/100)
	return altera
custo = float(input())
taxa = int(input())
x = somaImposto(custo,taxa)
print("O produto que custava {:.2f} com a taxa de {}% vai custar {:.2f}".format(custo,taxa,x))