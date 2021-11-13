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

variables = int(input("Cuantas variables: ")) #aqui pa que le digas cuantas
def tablero():
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

tab = tablero()
def miniterminos(miniter):
    limit=0
    miniter = input("introduza los miniterminos en orden ascendente separados por una coma (,): ").split(',')
    numeros = [int(x) for x in miniter]
    if len(tab) == 2**variables:
        limit = (2**variables)-1
        if len(miniter) > 2**variables:
            print("ingresaste mas miniterminos de los necesarios")
        for x in miniter:
            x2 = int(x)
            if x2 > limit:
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
    print("\n\n")
palabra2 = []

tablaceros1 = []
tablaunos1 = []
tabladoss1 = []
tablatress1 = []
tablacuatros1 = []
tablacincos1 = []
tablaseises1 = []
tablasietes1 = []
tablaochos1 = []
tablanueves1 = []
tabladieces1 = []

def comparaciones(A,P,out):
  if len(A) > 0:
    for i in range(len(A)-len(P)+1):
      for j in range(len(P)):
        if P[j] == A[i+j]:
          cad1 = P[j]
          palabra2.append(cad1)
        elif P[j] != A[i+j]:
          cad2 = P[j].replace('1','-')
          palabra2.append(cad2)
    else:
      pass

  lista = lambda palabra2, variables: [palabra2[i:i+variables] for i in range(0, len(palabra2), variables)]
  output = lista(palabra2, variables)
  for min in output:
      min2 = ''.join(min)
  out.append(min2)

def _comparar(arr,prr,out):
  for elem in arr:
    for ele in prr:
      comparaciones(elem,ele,out)

def conteo(t,num):
  veces = 0
  for i in range(len(t) - len(num) + 1):
    for j in range(len(num)):
      if num[j] == t[i+j]:
        pass
      else:
        break
    if j+1 == len(num) and t[i+j] == num[j]:
        veces = veces + 1
  #print(f"Se encontro en la posicion: {i}")
  return veces

tablaceros2 = []
tablaunos2 = []
tabladoss2 = []
tablatress2 = []
tablacuatros2 = []
tablacincos2 = []
tablaseises2 = []
tablasietes2 = []
tablaochos2 = []
tablanueves2 = []
tabladieces2 = []

def compararTodas():
    _comparar(tablaceros,tablaunos,tablaceros1)
    if len(tablaceros) > 0:
        print(tablaceros1)
    _comparar(tablaunos,tabladoss,tablaunos1)
    if len(tablaunos) > 0:
        for elem in reversed(tablaunos1):
            res = conteo(elem,"1")
            if res < 1:
                tablaunos1.remove(elem)
        print(tablaunos1)
    _comparar(tabladoss,tablatress,tabladoss1)
    if len(tabladoss) > 0:
        for elem in reversed(tabladoss1):
            res = conteo(elem,"1")
            if res < 2:
                tabladoss1.remove(elem)
        print(tabladoss1)
    _comparar(tablatress,tablacuatros,tablatress1)
    if len(tablatress) > 0:
        for elem in reversed(tablatress1):
            res = conteo(elem,"1")
            if res < 3:
                tablatress1.remove(elem)
        print(tablatress1)
    _comparar(tablacuatros,tablacincos,tablacuatros1)
    if len(tablacuatros) > 0:
        for elem in reversed(tablacuatros1):
            res = conteo(elem,"1")
            if res < 4:
                tablacuatros1.remove(elem)
        print(tablacuatros1)
    _comparar(tablacincos,tablaseises,tablacincos1)
    if len(tablacincos) > 0:
        for elem in reversed(tablacincos1):
            res = conteo(elem,"1")
            if res < 5:
                tablacincos1.remove(elem)
        print(tablacincos1)
    _comparar(tablaseises,tablasietes,tablaseises1)
    if len(tablaseises) > 0:
        for elem in reversed(tablaseises1):
            res = conteo(elem,"1")
            if res < 6:
                tablaseises1.remove(elem)
        print(tablaseises1)
    _comparar(tablasietes,tablaochos,tablasietes1)
    if len(tablasietes) > 0:
        for elem in reversed(tablasietes1):
            res = conteo(elem,"1")
            if res < 7:
                tablasietes1.remove(elem)
        print(tablasietes1)
    _comparar(tablaochos,tablanueves,tablaochos1)
    if len(tablaochos) > 0:
        for elem in reversed(tablaochos1):
            res = conteo(elem,"1")
            if res < 8:
                tablaochos1.remove(elem)
        print(tablaochos1)
    _comparar(tablanueves,tabladieces,tablanueves1)
    if len(tablanueves) > 0:
        for elem in reversed(tablanueves1):
            res = conteo(elem,"1")
            if res < 9:
                tablanueves1.remove(elem)
        print(tablanueves1)
    if len(tabladieces) > 0:
        print(tabladieces)
    else:
        pass
final = []

def compararTodas2():
    _comparar(tablaceros1,tablaunos1,tablaceros2)
    if len(tablaceros1) > 0:
        pass

    _comparar(tablaunos1,tabladoss1,tablaunos2)
    if len(tablaunos1) > 0:
        for elem in reversed(tablaunos2):
            res = conteo(elem,"1")
            if res < 1:
                tablaunos2.remove(elem)
            elif res < 1 and elem== elem:
                final.append(elem)
                tablaunos2.remove(elem)

    _comparar(tabladoss1,tablatress1,tabladoss2)
    if len(tabladoss1) > 0:
        for elem in reversed(tabladoss2):
            res = conteo(elem,"1")
            if res < 2:
                tabladoss2.remove(elem)
"""
        print(tabladoss2)
    _comparar(tablatress1,tablacuatros1,tablatress2)
    if len(tablatress1) > 0:
        for elem in reversed(tablatress2):
            res = conteo(elem,"1")
            if res < 3:
                tablatress2.remove(elem)
        print(tablatress2)
    _comparar(tablacuatros1,tablacincos1,tablacuatros2)
    if len(tablacuatros1) > 0:
        for elem in reversed(tablacuatros2):
            res = conteo(elem,"1")
            if res < 4:
                tablacuatros2.remove(elem)
        print(tablacuatros2)
    _comparar(tablacincos1,tablaseises1,tablacincos2)
    if len(tablacincos1) > 0:
        for elem in reversed(tablacincos2):
            res = conteo(elem,"1")
            if res < 5:
                tablacincos2.remove(elem)
        print(tablacincos2)
    _comparar(tablaseises1,tablasietes1,tablaseises2)
    if len(tablaseises1) > 0:
        for elem in reversed(tablaseises2):
            res = conteo(elem,"1")
            if res < 6:
                tablaseises2.remove(elem)
        print(tablaseises2)
    _comparar(tablasietes1,tablaochos1,tablasietes2)
    if len(tablasietes1) > 0:
        for elem in reversed(tablasietes2):
            res = conteo(elem,"1")
            if res < 7:
                tablasietes2.remove(elem)
        print(tablasietes2)
    _comparar(tablaochos1,tablanueves1,tablaochos2)
    if len(tablaochos1) > 0:
        for elem in reversed(tablaochos2):
            res = conteo(elem,"1")
            if res < 8:
                tablaochos2.remove(elem)
        print(tablaochos2)
    _comparar(tablanueves1,tabladieces1,tablanueves2)
    if len(tablanueves1) > 0:
        for elem in reversed(tablanueves2):
            res = conteo(elem,"1")
            if res < 9:
                tablanueves2.remove(elem)
        print(tablanueves2)
    if len(tabladieces) > 0:
        print(tabladieces)
    else:
        pass

"""


miniterminos(0)
compararTodas()
compararTodas2()
tablaceros2 = list(set(tablaceros2))
tablaunos2 = list(set(tablaunos2))
tabladoss2 = list(set(tabladoss2))
print(tablaceros2)
print(tablaunos2)
print(tabladoss2)
