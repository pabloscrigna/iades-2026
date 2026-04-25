"""
Hacer un programa que copie el archivo origen al destino

usage: python copiar.py origen.txt destino.txt
"""
import sys


if __name__ == "__main__":
    print("lista argumentos: ", sys.argv)
    print("tipo: ", type(sys.argv))
    # for i, argumento in enumerate(sys.argv):
    #     print(f"posicion {i} de la lista, tiene el valor {argumento}")

    # lista_argumentos = sys.argv

    # archivo_origen = lista_argumentos[1]
    # archivo_destino = lista_argumentos[2]

    origen = sys.argv[1]
    destino = sys.argv[2]
    
    with open(origen) as file:
        datos = file.read()

    with open(destino, "w") as file:
        file.write(datos)

