#Librerias
import random

#Funciones
def crearLista(largo_lista):
    lista_n=[]
    for x in range(largo_lista):
        num=random.randint(1,12)
        lista_n.append(num)
    return lista_n

def crearDicc(lista,lim_claves):
    dicc_n={}
    for x in range(lim_claves):
        dicc_n[x+1]=(lista[x])**2
    return dicc_n

#Variables
n=random.randint(1,20)

#Cuerpo
lista_rand=crearLista(n)
dicc_rand=crearDicc(lista_rand,n)
print(f'La lista de {n} numeros aleatorios con un rango de 1 a 12 es:\n{lista_rand}')
print(f'El diccionario con las claves del 1 al {n} y los valores siendo los cuadrados de los números aleatorios generados, es:\n{dicc_rand}')
