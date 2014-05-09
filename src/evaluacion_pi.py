#! encoding: UTF-8
import time
import timeit
import modulo
import sys
import matplotlib.pylab as pl
import numpy as np
def error(nro_intervalos,nro_test,umbral):
    fallos=0
    for i in range (nro_test):
      s=modulo.aproxpi(nro_intervalos)
      error=abs(s-modulo.pi)
      if error>=umbral:
        fallos=fallos+1
      return ((fallos/nro_test)*100)
x=[]
y=[]
t_upla_p1=(10,50,100,150,500,550,1000)
t_upla_p3=(0.0001,0.00001,0.000001,0.0000001,0.00000001)
for i in range(7):
   start=time.time() 
   p1=t_upla_p1[i]
   p2= 7
   p3=0.001
   s=error(p1,p2,p3)
   print "El porcentaje de error es de: %5.3f" %s
   finish=time.time()-start
   print "El tiempo que tarda en realizarse es: %14.13f" %finish
   x=x+[finish]
   y=y+[p1]
print x
print y
v=[]
t=[]
for i in range(5):
   start=time.time() 
   p1=10
   p2=5
   p3=t_upla_p3[i]
   s=error(p1,p2,p3)
   print "El porcentaje de error es de: %5.3f" %s
   finish=time.time()-start
   print "El tiempo que tarda en realizarse es: %14.13f" %finish
   v=v+[s]
   t=t+[p3]
S=[]
for i in range(5):
   start=time.time() 
   p1=50
   p2=5
   p3=t_upla_p3[i]
   s=error(p1,p2,p3)
   print "El porcentaje de error es de: %5.3f" %s
   finish=time.time()-start
   print "El tiempo que tarda en realizarse es: %14.13f" %finish
   S=S+[s]
D=[]
for i in range(5):
   start=time.time() 
   p1=100
   p2=5
   p3=t_upla_p3[i]
   s=error(p1,p2,p3)
   print "El porcentaje de error es de: %5.3f" %s
   finish=time.time()-start
   print "El tiempo que tarda en realizarse es: %14.13f" %finish
   D=D+[s]
A=[]
for i in range(5):
   start=time.time() 
   p1=150
   p2=5
   p3=t_upla_p3[i]
   s=error(p1,p2,p3)
   print "El porcentaje de error es de: %5.3f" %s
   finish=time.time()-start
   print "El tiempo que tarda en realizarse es: %14.13f" %finish
   A=A+[s]
B=[]
for i in range(5):
   start=time.time() 
   p1=500
   p2=5
   p3=t_upla_p3[i]
   s=error(p1,p2,p3)
   print "El porcentaje de error es de: %5.3f" %s
   finish=time.time()-start
   print "El tiempo que tarda en realizarse es: %14.13f" %finish
   B=B+[s]    
F=[]
for i in range(5):
   start=time.time() 
   p1=550
   p2=5
   p3=t_upla_p3[i]
   s=error(p1,p2,p3)
   print "El porcentaje de error es de: %5.3f" %s
   finish=time.time()-start
   print "El tiempo que tarda en realizarse es: %14.13f" %finish
   F=F+[s] 
E=[]
for i in range(5):
   start=time.time() 
   p1=1000
   p2=5
   p3=t_upla_p3[i]
   s=error(p1,p2,p3)
   print "El porcentaje de error es de: %5.3f" %s
   finish=time.time()-start
   print "El tiempo que tarda en realizarse es: %14.13f" %finish
   E=E+[s]   
   

grafic1=pl.subplot(212)
pl.plot(y,x,'ro-')

pl.xlabel('Intervalos')
pl.ylabel('Tiempo en segundos')

grafic2=pl.subplot(211)

pl.plot(t,v, color="blue",  linestyle="o-", label="10")
pl.plot(t,S, color="red", linestyle="*-", label="50")
pl.plot(t,D, color="green", linestyle="+-", label="100")
pl.plot(t,A, color="cyan", linestyle="h-", label="150")
pl.plot(t,B, color="magenta", linestyle="d-", label="500")
pl.plot(t,F, color="yellow", linestyle="s-", label="550")
pl.plot(t,E, color="black", linestyle="p-", label="1000")

pl.xticks([10,50,100,150,500,550,1000])
pl.yticks([0,20,40,60,80,100])

pl.title('Porcentaje de fallos')

pl.legend(loc=0, numpoints=2)

pl.savefig('grafica.eps',dpi=72)
pl.show()