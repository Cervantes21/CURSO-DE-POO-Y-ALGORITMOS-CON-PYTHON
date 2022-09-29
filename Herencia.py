# # Herencia:
# la herencia nos permite modelar una jerarquía de clases.
# Permite compartir comportamiento común en la jerarquía
# Al padre se le conoce como superclase y al hijo como una subclase.
# Hay que recordar que primero abstraemos y analizamos nuestro problema.
# decomponiendo la clase maestra se les da atributos que conforman una superclase
# y estos parametros se les puede heredar a nuestras subclases. 
# para ir haciendo definiciones de que hacen.

class Rectangulo: 
# Comenzamos con nuestra primera clase padre.#
    
    def __init__(self, base, altura): 
    # Aquí hacemos nuestras definiciones.
        self.base = base
        self.altura = altura
    
    def area(self): 
    # Expresiones dentro de funciones para que podamos definir nuestra variable Padre.
        return self.base * self.altura

# La Clase cuadrado (hereda de Rectangulo):    
class Cuadrado(Rectangulo): 
# Aquí en esta clase le damos de parametro una superclase.
    
    def __init__(self, lado):
        super().__init__(lado, lado) 
        # Aquí estamos llamando a su constructor. 
        # Cuando inicializamos una subclase, debemos inicializar las SUPERCLASES

if __name__ == '__manin__':
    rectangulo = Rectangulo(base=3, altura=4) 
    # Aquí estamos llamando al contructor con parametros reales
    # para que nos pueda "Crear un rectangulo"
    print(rectangulo.area()) 
    # Aquí le decimos que nos imprima nuestra variable que contiene nuestro nuevo objeto.
    
    cuadrado = Cuadrado(lado=5) 
    # Aquí estamos creando nuestro objeto hijo, con las caracteristicas ya señaladas.
    print(cuadrado.area()) 
    # Aquí lo interante es que .area() esta heredando este metodo de Rectangulo.area()