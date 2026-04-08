# Hacer una funcion que tome como argumento una lista de numeros y retorne el menor valor de la lista.


def menor(numeros: list)-> int:
	valor = numeros[0]

	for num in numeros:
		if num < valor:
			valor = num
	return valor

	


lista = [5, 7, 8, 9, 4]

resultado = menor(lista)

print("menor: ", resultado)

