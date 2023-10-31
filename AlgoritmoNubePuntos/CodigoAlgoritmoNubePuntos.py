# Importar librerías
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Solicitar datos al usuario
n = int(input("Ingrese cantidad de puntos en la nube: "))  # Paso 01

# Solicitar extremos de cada intervalo en el espacio tridimensional
print("Los extremos de intervalo para cada eje del espacio tridimensional")  # Paso 02
rango_x = tuple(map(float, input("Ingrese extremos del intervalo [a,b] separados por un espacio: ").split()))  # Paso 03
rango_y = tuple(map(float, input("Ingrese extremos del intervalo [c,d] separados por un espacio: ").split()))  # Paso 04
rango_z = tuple(map(float, input("Ingrese extremos del intervalo [e,f] separados por un espacio: ").split()))  # Paso 05

# Listas vacías
puntos_x = []  # Paso 06
puntos_y = []  # Paso 07
puntos_z = []  # Paso 08

# Añadir cada elemento a las listas
for j in range(n):  # Paso 09
    x = random.uniform(rango_x[0], rango_x[1])  # Paso 10
    y = random.uniform(rango_y[0], rango_y[1])  # Paso 11
    z = random.uniform(rango_z[0], rango_z[1])  # Paso 12
    puntos_x.append(x)  # Paso 13
    puntos_y.append(y)  # Paso 14
    puntos_z.append(z)  # Paso 15

# Crear gráfica de nube de puntos
print("Gráfica de nube de puntos")  # Paso 17

# Paso 18
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(puntos_x, puntos_y, puntos_z, c='b', marker='o')
ax.set_xlabel('Eje X')  # Paso 19
ax.set_ylabel('Eje Y')  # Paso 20
ax.set_zlabel('Eje Z')  # Paso 21

# Mostrar el gráfico
plt.show()