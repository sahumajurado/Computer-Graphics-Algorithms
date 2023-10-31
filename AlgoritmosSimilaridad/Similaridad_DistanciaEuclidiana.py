#Similitud por Distancia Euclidiana
import math
def calcular_distancia_euclidiana(punto1, punto2):
    return math.sqrt((punto1[0] - punto2[0])**2 + (punto1[1] - punto2[1])**2)
# Definimos dos puntos en un espacio bidimensional
punto1 = (2, 3)
punto2 = (4, 7)
# Calculamos la distancia euclidiana utilizando la función
distancia = calcular_distancia_euclidiana(punto1, punto2)
# Imprimimos la distancia euclidiana entre los puntos
print("La distancia euclidiana entre los puntos es:", distancia)