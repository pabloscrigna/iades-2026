# hacer una funcion que tome como argumento un str y retorne el caracter que mas veces aparec
# y la cantidad de veces
# "hola!!!"   --> !, 3
# 


def max_caracter(frase: str)-> tuple:
    conteo = {}

    for c in frase:
        if c in conteo:
            conteo[c] += 1
        else:
            conteo[c] = 1

    repite = ""
    cantidad = 0

    for c in conteo:
        if conteo[c] > cantidad:
            repite = c
            cantidad = conteo[c]

    return repite, cantidad

print(max_caracter("hola!!!"))
