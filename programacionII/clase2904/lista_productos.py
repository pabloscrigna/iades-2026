"""
Programa que actualiza la lista de precios de productos
"""
import csv

path = "/home/pablo/Documents/iades/2026/iades-2026/programacionII/clase2904"

file_name = "productos.csv"
file_bkp = "copia_productos.csv"

file = f"{path}/{file_name}"
filecopia = f"{path}/{file_bkp}"

with open(file, "r", encoding="utf-8") as original:
    with open(file_bkp, "w", encoding="utf-8") as destino:
        lineas = csv.DictReader(original)
        
        # nueva columna precio_c_impuesto
        columnas = lineas.fieldnames + ["precio_c_impuestos"]
        print(columnas)
        csv_salida = csv.DictWriter(destino, fieldnames=columnas)
        csv_salida.writeheader()
        
        for linea in lineas:
            linea["precio_c_impuestos"] = float(linea["precio_s_impuestos"]) * 1.21
            print(f"nombre: {linea["nombre"]}  precio: {linea["precio_c_impuestos"]}")

            csv_salida.writerow(linea)

