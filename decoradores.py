# Funciones que a su vez añaden funcionalidades a otras funciones.
# Por eso se les denomina "Decoradores", porque "decoran" a otras funciones. añadiendoles funcionalidad.
# Estructura de un decorador:
# hecha por 2 funciones (A,B y C) donde A recibe como parámetro a B para devolver C.
# Un decorador devuelve una función
# def funcion_decorador(funcion):
#     def funcion_interna():
#         #Código de la función interna
#         return función_interna

def funcion_decoradora(funcion_parametro):
    
    def funcion_interior():
        #Acciones adicionales que decoran, o agregan.
        
        print('Vamos a Realizar un cálculo: ')
        
        funcion_parametro()
        #Acciones Adicionales que decoran
        
        print('Hemos terminado el cálculo.')
        
    return funcion_interior

@funcion_decoradora
def suma():
    
    print(15+20)
    
@funcion_decoradora
def resta():
    
    print(30-10)

suma()
resta()