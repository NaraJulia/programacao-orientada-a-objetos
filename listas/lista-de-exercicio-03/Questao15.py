Quest�o 15
l1 = float(input())
l2 = float(input())
l3 = float(input())
if l1 == l2 == l3:
	print("Equil�tero")
elif l1 == l2 or l2 == l3 or l3 == l1:
	print("Is�sceles")
elif l1 != l2 != l3 :
	print("Escaleno")