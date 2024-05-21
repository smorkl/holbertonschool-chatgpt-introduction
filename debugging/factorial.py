#!/usr/bin/python3
import sys

def factorial(n):
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1  # Decrementar n para terminar eventualmente el bucle
    return resultado

f = factorial(int(sys.argv[1]))
print(f)