QUESTAO 07
def valorPagamento(p,dias):
	if dias > 0:
		multa = p*0.03
		juro = p*(0.001*dias)
		valorApagar = p+multa+juro
	else:
		valorApagar = p
	return valorApagar
total = 0
while True:
	p = float(input("Digite o valor da prestação (PARA SAIR DIGITE 0 (zero)): "))
	if p == 0:
	 	break
	dias = int(input("Digite o número de dias em atraso: "))
	presta = valorPagamento(p,dias)
	total += presta
	print("O valor a ser pago é: %.2f"%presta)
print("O total de prestações pagas no dia é: %.2f"%total,"\n\n Valores de pagamentos encerrados \n Fim do programa")