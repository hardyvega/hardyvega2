import random
import numpy as np

numero_random=np.random.randint(0,100)

x=range(0,10)
arreglo=np.array(x)
for n in x:
    arreglo[n]=np.random.randint(0,100)
print(arreglo) 
print("El numero mas grande: ",arreglo.max())
print("el numero mas pequeño: ",arreglo.min())
print("La suma de todos los numeros: ",arreglo.sum())
print("El promedio de los elementos: ",arreglo.mean())



