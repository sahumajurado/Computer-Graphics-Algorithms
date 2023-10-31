#Similitud por Coseno
#Importar librerías
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
# Definimos dos vectores de ejemplo
vector1 = [3, 2, 0, 1, 4]
vector2 = [1, 0, 3, 4, 2]
# Convertimos los vectores en matrices de una sola fila para que sklearn pueda trabajar con ellos
vector1 = np.array(vector1).reshape(1, -1)
vector2 = np.array(vector2).reshape(1, -1)
# Calculamos la similitud del coseno entre los dos vectores
similitud = cosine_similarity(vector1, vector2)
# Imprimimos la similitud del coseno
print("Similitud del coseno:", similitud[0][0])