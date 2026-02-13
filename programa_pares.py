"""Programa que cuenta cuántos números pares ingresa el usuario.

Pide números de forma repetida hasta que el usuario escriba 0.
Al final, muestra cuántos de los números ingresados fueron pares.
"""

cantidad_pares = 0

while True:
    numero = int(input("Ingresa un número (0 para terminar): "))

    if numero == 0:
        break

    if numero % 2 == 0:
        cantidad_pares += 1

print(f"Ingresaste {cantidad_pares} número(s) par(es).")
