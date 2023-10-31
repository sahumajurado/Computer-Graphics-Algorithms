#Similaridad por Jaccard
def jaccard(grupo1, grupo2):
	interseccion = len(set(grupo1).intersection(set(grupo2)))
	union = len (set(grupo1).union(set(grupo2)))
	return interseccion / union

grupo_amigos1 = ["Manuel", "Rodrigo", "Miguel", "Jesus", "Irving"]
grupo_amigos2 = ["Manuel", "Alejandro", "Fernando", "Antonio", "Jesus", "Pablo"]

jacard_amigos = jaccard(grupo_amigos1, grupo_amigos2)
print ("Porcentaje de similitud: {:.2f}".format(jacard_amigos))