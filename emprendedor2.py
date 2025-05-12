import math
import math as m

print('Programa para calcular las utilidades de un proyecto con usuarios premium')
print('No se permiten valores negativos')


P = float(input("Ingrese precio de suscripción:"))
UN = int(input("Ingrese el número de usuarios normales:"))
UP = int(input("Ingrese el número de usuarios premium:"))
GT = float(input("Ingrese los gastos:"))

ingresos_normales = P * UN
ingresos_premium = (P * 1.5) * UP

Utilidades = ingresos_normales + ingresos_premium - GT

print(f'Las utilidades calculadas son:{Utilidades:.2f}')