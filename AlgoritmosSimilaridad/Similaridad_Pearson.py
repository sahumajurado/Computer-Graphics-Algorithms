#Similaridad por Pearson
import pandas as pd
data = {
    'Usuario_A': [3, 4, 5, 2, 1],
    'Usuario_B': [4, 3, 5, 1, 2]
}
# Crear un dataframe con los datos
df = pd.DataFrame(data)
# Calcular la correlación de Pearson entre los dos usuarios
correlacion_pearson = df['Usuario_A'].corr(df['Usuario_B'])
print("Coeficiente de Correlación de Pearson: {:.2f}".format(correlacion_pearson))
