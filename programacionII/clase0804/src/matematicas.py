def resta(numero1: int, numero2: int) -> int:
    return numero2 - numero1


def suma(numero1: int, numero2: int) -> int:
    resultado = numero1 + numero2
    return resultado


if __name__ == "__main__":
    num1 = 10
    num2 = 20
    
    print("nombre matematicas: ", __name__)
    print(f"numero1: {num1}   -- numero2: {num2}")
    print("resultado: ", suma(num1, num2))
    print("resultado", resta(num2, num1))
