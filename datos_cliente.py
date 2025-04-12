#Funciones
def separar_csv(csv):
    elemento=''
    datos_separados=[]
    for i in csv:
        if i!=';' and i!='\n':
            elemento+=i
        elif i==';' or i=='\n':
            datos_separados.append(elemento)
            elemento=''
    return datos_separados
        
def crearDicc(datos_separados):
    cont=0
    nif=''
    cliente={}
    titles=['nombre','email','telefono','descuento']
    for i in datos_separados:
        cont+=1
        if cont==1:
            nif=i
            clientes[i]=cliente
        elif cont<6:
            cliente[titles[cont-2]]=i
        if cont==5:
            clientes[nif]=cliente
            cont=0
            cliente={}

#Variables
datos="nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
clientes={}

#Cuerpo
crearDicc(separar_csv(datos))
clientes.pop('nif')
print(clientes)