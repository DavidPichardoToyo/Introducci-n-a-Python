import math

import math as m

print('Programa para calcular la velocidad de escape del planeta tierra')
print('Tomar en cuenta que el valor de radio del planeta tierra es = 6371 km.') 
print('Valor de la constante de gravedad es = 9.8 m/s2') 

r1 = float(input("Ingrese el radio del planeta en kilometros:"))
g = float(input("Ingrese la constante gravedad(g):"))

r = r1 * 1000
v = m.sqrt(2* r * g)

print(f'La velocidad de escape del planeta tierra es: {v:.2f}m/s')


