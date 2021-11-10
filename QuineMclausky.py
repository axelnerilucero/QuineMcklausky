#import numpy as np
def bintostr(numeros):
    qtd = len(numeros)
    palabra = []
    for x in range(0, len(numeros)):
        if numeros[x] == '1':
            palabra.append(str(chr(65+x)))
        if numeros[x] == '0':
            palabra.append(str(chr(65 + x))+"'")
    palabra_completa = ''.join([str(item) for item in palabra])
    return palabra_completa

letra = bintostr('--11-11-10')
print(letra)

def tablero(variables):
    variables = int(input("Cuantas variables: ")) #aqui pa que le digas cuantas
    tabla_vdd = [] #aqui va hacer la tablita
    num_casas = ( (2) ** (variables)) # aqui van a ser los renglones que tiene la tabla
    if (variables>=2 and variables<=10):
        for cuadrito in range(0, num_casas): #lo recorremos para ir agregando los numeros
            tabla_vdd.append(str(bin(cuadrito).replace("0b", ""))) #aqui vamos agregando los 0s y 1s, bin te da la representacion binaria de un numero pero con un 0b demas, por eso lo remplazamos por un espacio en blanco
            while len(tabla_vdd[cuadrito]) < variables:
                tabla_vdd[cuadrito] = "0"+tabla_vdd[cuadrito]
        return tabla_vdd
        print(tabla_vdd)
    else:
        print("ingrese entre 2 a 10 variables")
        return tablero(0)

tab = tablero(0)
def miniterminos(miniter):
    limit=0
    miniter = input("introduza los miniterminos en orden ascendente separados por una coma (,): ").split(',')
    numeros = [int(x) for x in miniter]
    if len(tab) == 2**2:
        limit = 3
        if len(miniter) > 4:
            print("ingresaste mas miniterminos de los necesarios")
        for x in miniter:
            x2 = int(x)
            if x2 > limit:
                print("no existe el minitermino " +str(x2)+ " dentro de los miniterminos que se permiten")
                return (miniterminos(0))
    if len(tab) == 2**3:
        limit = 7
        if len(miniter) > 8:
            print("ingresaste mas miniterminos de los necesarios")
        for x in miniter:
            x2 = int(x)
            if x2 > 7:
                print("no existe el minitermino " +str(x2)+ " dentro de los miniterminos que se permiten")
                return (miniterminos(0))
    elif len(tab) == 2**4:
        limit = 15
        if len(miniter) > 16:
            print("ingresaste mas miniterminos de los necesarios")
            return (miniterminos(0))
        for x in miniter:
            x2 = int(x)
            if x2 > 15:
                print("no existe el minitermino " +str(x2)+ " dentro de los miniterminos que se permiten")
                return (miniterminos(0))
    elif len(tab) == 2**5:
        limit = 31
        if len(miniter) > 32:
            print("ingresaste mas miniterminos de los necesarios")
            return (miniterminos(0))
        for x in miniter:
            x2 = int(x)
            if x2 > 31:
                print("no existe el minitermino " +str(x2)+ " dentro de los miniterminos que se permiten")
                return (miniterminos(0))
    elif len(tab) == 2**6:
        limit = 63
        if len(miniter) > 64:
            print("ingresaste mas miniterminos de los necesarios")
            return (miniterminos(0))
        for x in miniter:
            x2 = int(x)
            if x2 > 63:
                print("no existe el minitermino " +str(x2)+ " dentro de los miniterminos que se permiten")
                return (miniterminos(0))
    elif len(tab) == 2**7:
        limit = 127
        if len(miniter) > 128:
            print("ingresaste mas miniterminos de los necesarios")
            return (miniterminos(0))
        for x in miniter:
            x2 = int(x)
            if x2 > 127:
                print("no existe el minitermino " +str(x2)+ " dentro de los miniterminos que se permiten")
                return (miniterminos(0))
    elif len(tab) == 2**8:
        limit = 255
        if len(miniter) > 256:
            print("ingresaste mas miniterminos de los necesarios")
            return (miniterminos(0))
        for x in miniter:
            x2 = int(x)
            if x2 > 255:
                print("no existe el minitermino " +str(x2)+ " dentro de los miniterminos que se permiten")
                return (miniterminos(0))
    elif len(tab) == 2**9:
        limit = 511
        if len(miniter) > 512:
            print("ingresaste mas miniterminos de los necesarios")
            return (miniterminos(0))
        for x in miniter:
            x2 = int(x)
            if x2 > 511:
                print("no existe el minitermino " +str(x2)+ " dentro de los miniterminos que se permiten")
                return (miniterminos(0))
    elif len(tab) == 2**10:
        limit = 1023
        if len(miniter) > 1024:
            print("ingresaste mas miniterminos de los necesarios")
            return (miniterminos(0))
        for x in miniter:
            x2 = int(x)
            if x2 > 1023:
                print("no existe el minitermino " +str(x2)+ " dentro de los miniterminos que se permiten")
                return (miniterminos(0))
    return funcion(numeros)
    #print(tab,miniter)
tablaceros = []
tablaunos = []
tabladoss = []
tablatress = []
tablacuatros = []
tablacincos = []
tablaseises = []
tablasietes = []
tablaochos = []
tablanueves = []
tabladieces = []

def funcion(numeros):
    funcion=[]
    for i in tab:
        for j in numeros:
            if(tab.index(i)==j):
                funcion.append(i)
    for z in funcion:
        numeros2 = [int(k) for k in z]
        suma = sum(numeros2)
        if suma == 0:
            tablaceros.append(z)
        if suma == 1:
            tablaunos.append(z)
        elif suma == 2:
            tabladoss.append(z)
        elif suma == 3:
            tablatress.append(z)
        elif suma == 4:
            tablacuatros.append(z)
        elif suma == 5:
            tablacincos.append(z)
        elif suma == 6:
            tablaseises.append(z)
        elif suma == 7:
            tablasietes.append(z)
        elif suma == 8:
            tablaochos.append(z)
        elif suma == 9:
            tablanueves.append(z)
        elif suma == 10:
            tabladieces.append(z)
        elif suma > 10:
            print("nomas hay 10 variables chabacano")
  # Aqui es para que dependiendo de los miniterminos dados muestre las tablas en las cuales contengan n numero de unos
    if len(tablaceros) <= 0:
        pass
    else:
        print(tablaceros," miniterminos con 0 unos")
    if len(tablaunos) <= 0:
        pass
    else:
        print(tablaunos," miniterminos con 1 unos")
    if len(tabladoss) <= 0:
        pass
    else:
        print(tabladoss," miniterminos con 2 unos")
    if len(tablatress) <= 0:
        pass
    else:
        print(tablatress," miniterminos con 3 unos")
    if len(tablacuatros) <= 0:
        pass
    else:
        print(tablacuatros," miniterminos con 4 unos")
    if len(tablacincos) <= 0:
        pass
    else:
        print(tablacincos," miniterminos con 5 unos")
    if len(tablaseises) <= 0:
        pass
    else:
        print(tablaseises," miniterminos con 6 unos")
    if len(tablasietes) <= 0:
        pass
    else:
        print(tablasietes," miniterminos con 7 unos")
    if len(tablaochos) <= 0:
        pass
    else:
        print(tablaochos," miniterminos con 8 unos")
    if len(tablanueves) <= 0:
        pass
    else:
        print(tablanueves," miniterminos con 9 unos")
    if len(tabladieces) <= 0:
        pass
    else:
        print(tabladieces," miniterminos con 10 unos")

"""
def tabla(tablak,tablay):
    a = np.array(tablak)
    b = np.array(tablay)

    for k in a:
        for y in b:
            if k == y:
                print("Que esta pasando doctor garcia")
            else:
                print(y,k)
"""

#si haces este codiguito de 0s y 1s pasa a letras, por lo que esto servira correctamente al mostrar la ultima funcion
#tab = tablero(0)
#for x in tab:
#    print(bintostr(x))"
miniterminos(0)
#print(tabla(tablaunos,tabladoss))
