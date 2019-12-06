Questao 6
def ler(arquivo):
	validos = open(arquivo.split('.')[0] + '_validos.txt', 'w')
	invalidos = open(arquivo.split('.')[0] + '_invalidos.txt', 'w')

	with open(arquivo, "r") as handler:
		ips = handler.read().split('\n')

		for ip in ips:
			if ip[0] == "1":
				validos.write(ip + '\n')
			else:
				invalidos.write(ip + '\n')

	validos.close()
	invalidos.close()

ler("IPs.txt")