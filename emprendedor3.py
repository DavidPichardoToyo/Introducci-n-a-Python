import math
import math as m

print('Programa para calcular las utilidades de un proyecto y comparación de utilidades')
print("Error: No se permiten valores negativos para un buen funcionamiento de la calculadora")

P = float(input("Ingrese precio de suscripción:"))
U = int(input("Ingrese el número de usuarios:"))
GT = float(input("Ingrese los gastos:"))
UA = float(input("Ingrese las utilidades del año anterior:"))

Utilidades = P * U - GT
razon = Utilidades / UA

print(f'Las utilidades calculadas son:{Utilidades:.2f}')
print(f'La razon entre las utilidades actuales y anteriores es:{razon:.2f}')