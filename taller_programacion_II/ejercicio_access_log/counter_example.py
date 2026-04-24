from collections import Counter

numeros = [4, 6, 7, 8, 3, 6, 2, 8, 9, 34, 56, 23, 56, 3]

print(Counter(numeros))
print(Counter(numeros).most_common())
print(Counter(numeros).most_common(1))