QUESTAO 14
import random
                #j(coluna)
matriz = [[1, 2, 3],#i(linha)
          [4, 5, 6],
          [7, 8, 9]]
res = False
#DEFINIR UMA FUN��O PARA CALCULAR AS SOMAS DE TODOS OS LADOS
def magicsquare():
    global res
    if matriz[0][0] + matriz[1][0] + matriz[2][0] == matriz[0][1] + matriz[1][1] + matriz[2][1] == matriz[0][2] + matriz[1][2] + matriz[2][2] == matriz[0][0] + matriz[0][1] + matriz[0][2] == matriz[1][0] + matriz[1][1] + matriz[1][2] == matriz[2][0] + matriz[2][1] + matriz[2][2] == matriz[0][0] + matriz[1][1] + matriz[2][2] == matriz[0][2] + matriz[1][1] + matriz[2][0]:
        res = True  # Primeiro atribui...
    else:
        res = False # Primeiro atribui...
    return res # ...depois usa

#DEFINIR UM LOOP PARA GERAR N� ALEAT. AT� ENCONTRAR OS QUE SATIZFAZEM
#AS CONDI��ES DE UM QUADRADO M�GICO
while res == False:
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Dentro do while, n�o fora
    for i in range(3): # 3, n�o 2 (0,1,2)
        for j in range(3):
            z = random.choice(seq)
            matriz[i][j] = z
            x = seq.index(z)
            seq = seq[:x] + seq[x+1:] # Remove o elemento x do conjunto
    magicsquare()
print (matriz)

def magicsquare():
    global res
    if matriz[0][0] + matriz[1][0] + matriz[2][0] == matriz[0][1] + matriz[1][1] + matriz[2][1] == matriz[0][2] + matriz[1][2] + matriz[2][2] == matriz[0][0] + matriz[0][1] + matriz[0][2] == matriz[1][0] + matriz[1][1] + matriz[1][2] == matriz[2][0] + matriz[2][1] + matriz[2][2] == matriz[0][0] + matriz[1][1] + matriz[2][2] == matriz[0][2] + matriz[1][1] + matriz[2][0]:
        res = True  # Primeiro atribui...
    else:
        res = False # Primeiro atribui...
    return res # ...depois usa
#        0  1  2  3  4  5  6  7  8
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if res == False:
    for i in range(8):
        w = random.choice(seq)
        #Repor o valor w(1 a 9) no index i(0 a 8). Sem usar valores e indexes repetidos
        vetor.insert(i, w)
        #Eliminar os valores j� utilizados
        x = seq.index(w)
        seq[x] =[]
    magicsquare()
print (vetor)