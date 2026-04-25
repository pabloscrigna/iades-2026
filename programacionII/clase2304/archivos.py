"""
Ejemplos de archivos
"""

# Como eer un archivo
# Abrir el archivo -- metodo open(path_nombre_archivo, tipo_operacion)
# r: lectura    w: escritura   a: agregar

file = open("origen.txt")

print("metodo read")
datos = file.read()
print("datos archivo:")
print(datos)
file.close()



# metodo readlines

print("metodo readlines")
file = open("origen.txt")

datos = file.readlines()

print("datos: ", datos)

for linea in datos:
    print(linea)

# error --- porque el archivo ya se leyo por completo 
# file.read()

file.close()



# metodo readline

print("metodo readline")
file = open("origen.txt")

linea = file.readline()

print("linea: 1", linea)

print("linea: 2", file.readline())


file.close()


# context manager
print("context manager")
with open("origen.txt") as file:
    datos = file.read()

print("datos:", datos)

with open("destino_final.txt", "w") as file:
    file.write(datos)


