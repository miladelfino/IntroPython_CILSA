#agrego todos los datos del archivo a un diccionario
diccionario={
    'DNI':[],
    'Nombre': [],
    'Apellido': [],
    'Email':[],
    'Fecha':[],
    'Lugar':[]
}
try:
    archivo= open('RecursosPython.csv', 'r')
    for linea in archivo:
        personas = linea.split(',')
        diccionario['DNI'].append(personas[0])
        diccionario['Nombre'].append(personas[1])
        diccionario['Apellido'].append(personas[2])
        diccionario['Email'].append(personas[3])
        diccionario['Fecha'].append(personas[4])
        diccionario['Lugar'].append(personas[5])
    archivo.close()
except:
    print('Algo salió mal. Inténtelo nuevamente.')

diccionario['DNI'].pop(0)
diccionario['Nombre'].pop(0)
diccionario['Apellido'].pop(0)
diccionario['Email'].pop(0)
diccionario['Fecha'].pop(0)
diccionario['Lugar'].pop(0)

#filtro personas de apellido Gomez
try:
    for i in range(len(diccionario['Apellido'])):

        if diccionario['Apellido'][i] == 'Gomez':
            print('Nombre:', diccionario['DNI'][i])
            print('Apellido:', diccionario['Nombre'][i])
            print('DNI:', diccionario['Apellido'][i])
            print('Email:', diccionario['Email'][i])
            print('Fecha:', diccionario['Fecha'][i])
            print('Lugar:', diccionario['Lugar'][i])
except: 
    print("No se encontraron personas con ese apellido.")

#agrego personas de cordoba o santa fe a un archivo nuevo
localidades={}
contador=1
for i in range(len(diccionario['Lugar'])):
    if (diccionario['Lugar'][i]== 'Santa_Fe') | (diccionario['Lugar'][i]== 'Cordoba'):
        localidad=[]
        localidad.append(diccionario['DNI'][i])
        localidad.append(diccionario['Nombre'][i])
        localidad.append(diccionario['Apellido'][i])
        localidad.append(diccionario['Email'][i])
        localidad.append(diccionario['Fecha'][i])
        localidad.append(diccionario['Lugar'][i])
        localidades['persona '+str(contador)]=localidad
        contador=+1

resultado= open('Resultado.csv', 'w')
for local in localidades:
    resultado.write(','.join(localidades[local]) + '\n')
resultado.close() 