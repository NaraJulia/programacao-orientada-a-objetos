QUESTAO 04
def valor(x):
	if x != 0 and x % 2 == 0:
		return "P"
	else:
		return "N"
x = int(input())
y = valor(x)
print(y)