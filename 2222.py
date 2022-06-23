#CODIGO 2 GRAFICO DE FUNCION Y SU RESTRICCION PREGUNTA 2.4
from cProfile import label
from matplotlib import projections
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import sympy
import os
#-------------Funciones-----------
def funcion(m,c): #Rerornamos nuestra funcion 
    raiz = pow(m**2*c, 1/3)#pidiendo parametros de x e y
    return 50*raiz

def restriccion(m,c): #Hacemos lo mismo con la restriccion
    raiz = pow(m**2*c, 1/3)
    restricc = (100 * m + 300 * c - 45000)
    return  50*raiz + restricc
#---------------------------------   

#--------------Grafica-------------
fig = plt.figure()    

x = np.linspace(0,300,100) #Generamos un array con 
y = np.linspace(0,50,100) #los puntos dados (en el eje x y en el eje y)

X, Y = np.meshgrid(x,y)
z = funcion(X,Y) #iniciamos nuestra funcion para guardarla en z
r = restriccion(X,Y) #Hacemos lo mismo con la restriccion

ax = fig.gca(projection='3d') 
ax1 = fig.gca(projection='3d')

surface = ax.plot_surface(X, Y, z,cmap="summer") #le damos los valores
surface1 = ax1.plot_surface(X, Y, r, cmap="hot") #al grafico y le damos 
                                                # color con cmap

os.system("cls") #borramos la consola para un codigo mas legible
plt.plot(300,50, funcion(300,50) ,marker= "*", markersize = 10 ,color = "red") #creamos un punto 
plt.title("GRAFICO 2")                                                         #donde se encuentran 
plt.show() #mostramos la grafica en pantalla                                  y le damos forma