#Cria molduras
def moldura(frase):
	tam = len(frase)
	barra(tam)
	print("\nā %s ā" %frase)
	barra(tam)

def barra (num):
	for i in range(1,num+5,1):
		print("ā", end="")