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
    for cuadrito in range(0, num_casas): #lo recorremos para ir agregando los numeros
        tabla_vdd.append(str(bin(cuadrito).replace("0b", ""))) #aqui vamos agregando los 0s y 1s, bin te da la representacion binaria de un numero pero con un 0b demas, por eso lo remplazamos por un espacio en blanco
        while len(tabla_vdd[cuadrito]) < variables:
            tabla_vdd[cuadrito] = "0"+tabla_vdd[cuadrito]
    return tabla_vdd
    print(tabla_vdd)

def miniterminos(miniter):
    tab = tablero(0)
    limit=0
    miniter = input("introduza los miniterminos en orden ascendente separados por una coma (,): ").split(',')
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
    print(tab,miniter)
"""
tab = tablero(0)
for x in tab:
    print(bintostr(x))
"""
miniterminos(0)
