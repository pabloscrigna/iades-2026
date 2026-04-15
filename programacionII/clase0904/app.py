import time

from functools import lru_cache


@lru_cache
def cuadrado(n):
    time.sleep(n)
    return n**2


print("cuadrado 10: ", cuadrado(10))
print("cuadrado 10: ", cuadrado(10))
