#inpengu -> penguin

def decodificador():
    cad = ""
    pal = input("Ingrese palabra a decodificar: ")
    l = len(pal) #longitud de la palabra

    if (l > 2):     #si es mas largo de dos caracteres realizar la decodificacion
        for k in range(2,l):    
            cad = cad + pal[k]          #concatenamos las letras apartir de la posicion 2, porque ahi empieza la palabra real
        cad = cad + pal[0] + pal[1]     #al final concatenamos las 2 primeras letras de la palabra a decodificar
    else:           #si la palabra no es mas larga de dos caracteres no realizamos la decodificacion
        cad = pal

    return cad

cant = int(input("Ingrese cantidad de palabras a decodificar: "))
lis = []
for k in range(cant):
    lis.append(decodificador())

print(lis)