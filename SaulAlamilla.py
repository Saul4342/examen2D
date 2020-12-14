"""
Nombre: Saul Humberto Alamilla Calixto
No. control: 18390023
Fecha: 14/12/2020
"""
import matplotlib.pyplot as plt 
import numpy as np 

plt.axis([0,140,0,80])
plt.axis('on')
plt.grid(True)
color=(0/10,2/10,3/10)#Se guarda en una variable los colores dependiendo de los ultimos 3 digitos de nuestro no. de control

#Se saca el centro del circulo para dibujarlo en esa parte
xc=60
yc=50
r=3*5 #El radio del circulo se hace con lo que dice la instruccion

p1=0*np.pi/180 #Se inicia el dibujo del circulo en el angulo 0 convirtiendolo a radianes
p2=360*np.pi/180
dp=(p2-p1)/100

xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)

for p in np.arange(p1,p2+dp,dp):
    xp=xc+r*np.cos(p)
    yp=yc+r*np.sin(p)
    plt.plot([xlast,xp],[ylast,yp],color=color)
    xlast=xp
    ylast=yp

#Se dibujan los rectangulos, tomando como base el centro del circulo
x=np.array([xc,xc,xc+4*r,xc+4*r,xc])
y=np.array([yc,yc-2*r,yc-2*r,yc,yc])
plt.plot(x,y, color=color) #Se ocupa el color indicado.

x=[90,90,30,30,90]
y=[35,65,65,35,35]
plt.plot(x,y, color=color)

plt.axes().set_aspect('equal')
plt.show()