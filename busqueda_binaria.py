import random

def busqueda_lineal(lista, objetivo,iter_lin=0):
    match = False

    for elemento in lista:
        iter_lin+=1
        if elemento == objetivo:
            match = True
            break

    return (match,iter_lin)



def busqueda_binaria(lista, comienzo, final, objetivo,iter_bin=0):
    iter_bin+=1
    if comienzo > final:
        return (False,iter_bin)

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return (True,iter_bin)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo,iter_bin=iter_bin)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo,iter_bin=iter_bin)


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño es la lista? '))
    objetivo = int(input('¿Qué número quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    (encontrado,iter_bin) = busqueda_binaria(lista, 0, len(lista), objetivo)
    (encontrado,iter_lin) = busqueda_lineal(lista, objetivo)

    #print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Iteraciones busqueda lineal: {iter_lin}')
    print(f'Iteraciones busqueda binaria: {iter_bin}')