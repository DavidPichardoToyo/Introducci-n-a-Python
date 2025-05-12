import math
import math as m

print('Programa para calcular las utilidades de un proyecto')

P = float(input("Ingrese precio de suscripción:"))
U = int(input("Ingrese el número de usuarios normales:"))
UP = int(input("Ingrese el número de usuarios premium:"))
GT = float(input("Ingrese los gastos:"))

Utilidades = P * (U + UP*1.5) - GT

print(f'Las utilidades calculadas son:{Utilidades}')