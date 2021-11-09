
print("QuineMcClausky")
print("Indroduza el número de variables")
dato = int(input())

def verificar_variables(dato):
    if not (dato>=2 and dato<=10):
        print("Inserte entre 2 y 10 variables")
        dato = int(input())
        return dato
verificar_variables(dato)

print("Introduzca el minitérmino seguido de una coma")
numeros = input().split(",")

def verificar_miniterminos(numeros):
    numeros2=[int(x) for x in numeros]
    for i in numeros2:
        if not(i<(2**dato)):
            print("Los minitérminos inician desde 0, introduzca nuevamente el minitérmino correcto")
        else:
            repetidos=numeros2.count(i)
            if not (repetidos<2):
                print("Se repite el minitérmino", i)

verificar_miniterminos(numeros)

columnas = int(dato)
filas = 2**columnas
matriz=[["0" for x in range(columnas)] for y in range(filas)]
resultado=filas

for r in matriz:
    print(r)


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
