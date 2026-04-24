"""
Dado el archivo mini-access-log, calcular cual es la direccion IP que mas veces aparece
"""
from collections import Counter

file_name = "mini-access-log.txt"


def main():
    with open(file_name, "r") as file:
        data = file.readlines()
    
    # data: es una lista, de las filas de mi archivo !!!!
    data = [
        linea.split()[0]
        for linea in data
    ]

    contador_ips = Counter(data)            # Retorna un tipo de dato Counter
    ip_list = contador_ips.most_common(1)   # retorna una lista de tuplas, con n tuplas, n = 1 [(x, a)]
    print("direccion ip: ", ip_list[0][0])
    print("cantidad de veces: ", ip_list[0][1])

    ip, contador = ip_list[0]
    print("direccion ip: ", ip)
    print("cantidad de veces: ", contador)


if __name__ == "__main__":
    main()