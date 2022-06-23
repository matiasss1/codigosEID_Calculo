#CODIGO 1 DESARROLLO GRAFICO Y MATEMATICO 
from matplotlib import projections
import matplotlib.pyplot as plt
import sympy
import numpy as np

x, y = sympy.symbols("x,y")

def fun(x,y): #funcion de la funcion a trabajar
    return -5*y**2+6*y*x+590*y-3*x**2-90*x-28800

def gradi(funcion):#sacamos las deivadas parciales
    parcial_x=sympy.diff(funcion,x)#y las retornamos 
    parcial_y=sympy.diff(funcion,y) # como par ordenado
    return(str(parcial_x),str(parcial_y))

def s_ecuaciones(): #resolveos sistema de ecuacinoes con .solve
    A=np.array([[6,-10],[-6,6]])
    B=np.array([-590,90])
    X=np.linalg.solve(A,B) 
    return X

def m_hess(myfc,det): #sacamos la matriz hessiana, 
    x,y = sympy.symbols("x,y") # que son derivadas 
    p_xx = sympy.diff(myfc,x,2)#en matrices de segundo orden
    p_xy = sympy.diff(myfc,x,y)
    p_yx = sympy.diff(myfc,y,x)
    p_yy = sympy.diff(myfc,y,2)
    det=[[p_xx,p_xy],
        [p_yx,p_yy]]
    return (det)

PARCIAL_X, PARCIAL_Y = str(gradi(fun(x,y))[0]), str(gradi(fun(x,y))[1])
det=[]
a=0

dxx = m_hess(fun(x,y),det)[0][0]
dyy = m_hess(fun(x,y),det)[1][1]
dxy = m_hess(fun(x,y),det)[0][1]
dxy = m_hess(fun(x,y),det)[0][1]

det = (dxx * dyy) - (dxy * dxy) 

print("----------------------")
print("----------------------")
print("Derivada parcial en x: ",PARCIAL_X,',', "Derivada parcial en y: ",PARCIAL_Y, "Punto Critico: ", s_ecuaciones(),"Determinante: ", det)
print("----------------------")
print("----------------------")

#usamos linspace de numpy en las variables x e y 
#con un total de 100 datos de muestreo para el grafico 3d
x, y=np.linspace(100,200,100), np.linspace(100,200,100)
X,Y=np.meshgrid(x, y)

fig=plt.figure(figsize=(10,10))
axis=fig.gca(projection="3d")
s=axis.plot_surface(X,Y,fun(X,Y),cmap="hot")
plt.plot(110,125,fun(110,125),marker='*',color='blue',markersize=20)
plt.title("GRÁFICO 3D")
plt.show()
##### OUTPUT #####
#----------------------
#----------------------
#Derivada parcial en x:  -6*x + 6*y - 90 , Derivada parcial en y: 
# 6*x - 10*y + 590 Punto Critico:  [110. 125.] Determinante:  24
#----------------------
#----------------------