QUESTAO 12
import random
def maiuscula(palavra):
	palavra = palavra.upper()
	return palavra
def viralista(palavra):
	global lista
	lista = list(palavra)
def embaralhaLista(lista):
	random.shuffle(lista)
def viraString(lista):
	c = ''
	c = c.join(lista)
	return c
lista=[]
print("* EMBARALHADOR DE LETRAS *")
palavra = input("Digite uma palavra: ")
print("\nA palavra digitada foi: ",maiuscula(palavra))
viralista(palavra)
embaralhaLista(lista)
print("\nA palavra digitada com as letras embaralhadas: ",maiuscula(viraString(lista)))