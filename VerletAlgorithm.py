#Proyecto de Curso de verano en el departamento de computacion de Exactas 2019
#Idea: Implementar el "algoritmo de verlet" en Python con el fin de ubicar la posicion del Planeta Tierra con respecto al Sol durante un ano

import matplotlib.pyplot as plt

dt = 0.001 #para el paso temporal (en segundos)
numero_pasos = 2050 #el numero de pasos a simular
g = 9.8 #la aceleracion de la gravedad en m/s2
y0 = 0 #la posicion desde la que es lanzado el objeto en m
vy = 10 #la velocidad con la que es lanzado el objeto en m/s
y1 = 0.01 #la posicion en el instante t=0 + dt en mx

tiempos = [0, dt]
alturas = [y0, y1]

for i in range (1 , numero_pasos - 1) :
    # actualizo la posicion
    y_actual = alturas [i]
    y_prev = alturas [i-1]
    nueva_posicion = 2 * y_actual - y_prev - g * dt **2
    alturas.append (nueva_posicion)

    # actualizo el tiempo
    nuevo_tiempo = tiempos [i] + dt
    tiempos.append (nuevo_tiempo)

#Creo usando la libreria MatplotLib una grafica que nos muestra la orbita planetaria.
plt.title("Posicion del objeto ")
plt.plot(tiempos, alturas, "r")
plt.xlabel("tiempo (s)")
plt.ylabel("altura (m)")
plt.show()
