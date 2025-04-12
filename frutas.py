#Funciones
def calcularPrecio(precios, ordenes):
    total=0
    for x in ordenes:
        total+=x[1]*precios[x[0]]
    return print(f'Precio Total ---------- ${total}')

def listaCompra(lista):
    print('///////////////// RECIBO /////////////////\n')
    print('FRUTA ---------- CANTIDAD')
    for x in lista:
        print(f'{x[0]} ---------- {x[1]}')

#Variables
frutas={
    'manzana' : 8,
    'sandia' : 70,
    'mango' : 15,
    'limon' : 3,
    'naranja' : 6,
}
pedidos=[]

#Cuerpo
while True:
    print('//////////////// FRUTERIA ////////////////')
    un_pedido=[]
    print('Escriba la fruta que desee ordenar:')
    print('-Manzana $8\n-Sandia $70\n-Mango 15$\n-Limon 3$\n-Naranja 6$')
    op_f=input('>>>')
    op_f=op_f.lower()
    if op_f not in frutas:
        print('<NO TENEMOS ESA FRUTA>')
    else:
        print('//////////////////////////////////////////')
        try:
            op_n=int(input('Escriba la cantidad de unidades que desee:\n>>>'))
            if op_n<0:
                int('')
        except:
            print('<CANTIDAD NO VALIDA>')
            continue
        un_pedido.append(op_f)
        un_pedido.append(op_n)
        pedidos.append(un_pedido)
        listaCompra(pedidos)
        print('__________________________________________')
        calcularPrecio(frutas, pedidos)
        print('//////////////////////////////////////////')
        fin=input('Escriba "s" para seguir agregando productos:\n>>>')
        if fin!='s':
            break
    