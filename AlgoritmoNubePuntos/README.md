## DESCRIPCIÓN:
Este algoritmo de nube de puntos genera una cantidad entera
de puntos aleatorios ingresados por el usuario en el espacio tridimensional.

## ENTRADA:
- Cantidad de puntos a generar en la nuben
- Extremos del intervalo [a,b] en el eje x rango_x 
- Extremos del intervalo [c,d]en el eje yrango_y
- Extremos del intervalo [e,f] en el eje z rango_z

## SALIDA:
Gráfica de la nube de puntos en el espacio tridimensional

## ALGORITMO DE NUBE DE PUNTOS
- Paso 01   Leer número de puntos n
- Paso 02   Imprimir (Los extremos de intervalos  para cada eje del espacio tridimensional)
- Paso 03   Leer extremos del intervalo [a,b] del eje x: rango_x
- Paso 04   Leer extremos del intervalo [c,d] del eje y: rango_y
- Paso 05   Leer extremos del intervalo [e,f] del eje z: rango_z
- Paso 06   Lista de puntos_x =[ ]
- Paso 07   Lista de puntos_y =[ ]
- Paso 08   Lista de puntos_z =[ ]
- Paso 09   Para j=0, con incremento=1, hasta n
- Paso 10   x=Generar un número aleatorio en el rango x
- Paso 11   y=Generar un número aleatorio en el rango y
- Paso 12   z=Generar un número aleatorio en el rango z
- Paso 13   Lista de puntos_x =[ Lista de puntos_x, x]
- Paso 14   Lista de puntos_y = [Lista de puntos_y, y]
- Paso 15   Lista de puntos_z=[Lista de puntos_z, z]
- Paso 16   Fin_Para
- Paso 17   Imprimir (Gráfica de nube de puntos)
- Paso 18   Graficar (Lista de puntos_x,puntos_y, puntos_z)
- Paso 19   Nombrar etiqueta del eje x
- Paso 20   Nombrar etiqueta del eje y
- Paso 21   Nombrar etiqueta del eje z
- Paso 22   FinAlgoritmo
