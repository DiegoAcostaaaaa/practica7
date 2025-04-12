#Librerias
import random

#Variables
n=random.randint(1,20)
lista_n=[]
dicc_n={}

#Cuerpo
for x in range(n):
    num=random.randint(1,12)
    lista_n.append(num)
    dicc_n[x+1]=num**2
print(f'La lista de {n} numeros aleatorios con un rango de 1 a 12 es:\n{lista_n}')
print(f'El diccionario con las claves del 1 al {n} y los valores siendo los cuadrados de los números aleatorios generados, es:\n{dicc_n}')
