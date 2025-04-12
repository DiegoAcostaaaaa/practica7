#Funciones
def calPrecio(lista):
    precios=[]
    for x in lista:
        if x['zona']=='A':
            precio=((x['metros']*1000)+(x['habitaciones']*5000)+(x['garaje']*15000))*(1-(2025-x['año'])/100)
        else:
            precio=((x['metros']*1000)+(x['habitaciones']*5000)+(x['garaje']*15000))*(1-(2025-x['año'])/100)*1.5
        precios.append(precio)
    return precios

#Variables
inmuebles=[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
cont=0

#Cuerpo
for x in calPrecio(inmuebles):
    cont+=1
    print(f'El inmueble de la zona {inmuebles[cont-1]['zona']} tiene un valor de ${x}')
