Questao 6 
x = int(input("Digite um numero:"))
y = int(input("Digite outro numero:"))
z = int(input("Digite mais um numero:"))
if x > y and x > z  :
	print("O numero {} � maior que {} � maior que {}".format(x,y,z))
if y > x and y > z :
	print("O numero {} � maior que {} � maior que {}".format(y,x,z))
if z > y and z > x:
	print("O numero {} � maior que {} � maaior que {}".format(z,y,x))