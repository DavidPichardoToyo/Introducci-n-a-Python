import math
import math as m

print('Programa para calcular las utilidades de un proyecto')
print('No se permiten valores negativos')

P = float(input("Ingrese precio de suscripción:"))
U = int(input("Ingrese el número de usuarios:"))
GT = float(input("Ingrese los gastos:"))

Utilidades = P * U - GT

print(f'Las utilidades calculadas son:{Utilidades:.2f}')