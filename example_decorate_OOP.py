# Decoradores = Son funciones que tiene como parámetro 
# otras funciones con el objetivo de añadirle funcionalidades 
# sin la necesidad de modificarla. 
# Ejemplo: Tengo una función que hace un helado y quiero añadirle 
# chispas de chocolate o chispas de colores, sin tener que modificar 
# la función original helado.

def helado():       #función que no deseo modificar
    print("Helado de vainilla")

def chispas_de_chocolate(fun):  #decorador 
    def run():
        fun()           #llamo a función que recibí como parametro      
        print('Añadiendo chispas de chocolate') #añado una nueva funcionalidad
    return run()        #ejecuto la función run()

def chispas_de_colores(fun):  #decorador 
    def run():
        fun()           #llamo a función que recibí como parametro       
        print('Añadiendo chispas de colores') #añado una nueva funcionalidad
    return run()        #ejecuto la función run()

chispas_de_chocolate(helado)