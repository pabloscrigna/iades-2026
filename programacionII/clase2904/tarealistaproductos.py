"""
Programa que actualiza la lista de precios de productos
"""

path = "/home/pablo/Documents/iades/2026/iades-2026/programacionII/clase2904"

file_name = "productos.csv"
file_bkp = "copia_productos.csv"

file = f"{path}/{file_name}"
filecopia = f"{path}/{file_bkp}"


def archivo(file):
    with open(file, "r", encoding="utf-8") as original:
        contenido = original.read()

    with open(filecopia, "w", encoding="utf-8") as copia:
        copia.write(contenido)

    print("Se creó un backup")

    lineas = contenido.strip().split("\n")

    encabezados = lineas[0].split(",")
    encabezados.append("precios_con_impuestos")
    nuevas_lineas= [",".join(encabezados)]

    for fila in lineas[1:]:
        campos = fila.split(",")
        precio_sin_impuestos= float(campos[3])
        precio_con_imp=round(precio_sin_impuestos * 1.21,2)
        campos.append(str(precio_con_imp))
        nuevas_lineas.append(",".join(campos))

    with open(file,'w',encoding='utf-8') as archivo:
        archivo.write('\n'.join(nuevas_lineas))


if __name__== "__main__":
    archivo(file)
