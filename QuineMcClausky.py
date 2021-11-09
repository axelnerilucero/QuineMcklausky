def tablero(variables):
    variables = int(input("Cuantas variables: ")) #aqui pa que le digas cuantas
    tabla_vdd = [] #aqui va hacer la tablita
    num_casas = ( (2) ** (variables)) # aqui van a ser los renglones que tiene la tabla
    for cuadrito in range(0, num_casas): #lo recorremos para ir agregando los numeros
        tabla_vdd.append(str(bin(cuadrito).replace("0b", ""))) #aqui vamos agregando los 0s y 1s, bin te da la representacion binaria de un numero pero con un 0b demas, por eso lo remplazamos por un espacio en blanco
    return tabla_vdd

tab = tablero(0)

for x in tab:
    print(x)

miniterminos = input("Introduza el número del minitérmino: ").split(",")
numeros = [int(x) for x in miniterminos]


def funcion(numeros):
    funcion=[]
    for i in tab:
        for j in numeros:
            if(tab.index(i)==j):
                funcion.append(i)
    return funcion

fun=funcion(numeros)

for z in fun:
    print(z)
