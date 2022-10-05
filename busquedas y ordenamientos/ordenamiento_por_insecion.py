import random 

def ordenamiento_insercion(lista):
    # crea un contador segun el largo de la lista para usar el indice como cursor
    for indice in range(1, len(lista)):
        # guarda el valor actual del cursor en una variable
        valor_actual = lista[indice] # ej: (5)
        # si el cursor es mayor que cero
        # y el numero anterior al cursor es mayor que el valor actual
        while indice > 0 and lista[indice - 1] > valor_actual: # ej: 7 > (5)?
            # el valor actual pasa a ser igual al numero anterior al cursor
            lista[indice] = lista[indice -1] # ej: [...7,(5)...] => [...7,(7)...]
            # se resta 1 al indice para posarnos en el numero anterior al cursor
            indice -= 1 # ej: [...(7),7...]
        # como insertamos el valor del numero anterior al cursor en la posicion actual,
        # ahora insertamos en la posicion del numero anterior, el valor que teniamos guardado
        lista[indice] = valor_actual # ej: [...(7),7...] => [...(5),7...]
        # y seguimos con el siguiente indice.
    return lista
        
    
    

if __name__=='__main__':
    
    tamano_de_lista = int(input('De qué tamaño será la lista? '))
    
    lista = [random.randint(0, 100) for i in range (tamano_de_lista)]
    
    lista_ordenada = ordenamiento_insercion(lista)
    
    print(lista)
    print(lista_ordenada)