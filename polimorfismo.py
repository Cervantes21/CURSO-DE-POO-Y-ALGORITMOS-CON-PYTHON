
class Person:
    
    def __init__ (self, name):
        self.name = name
        
    def avanza(self):
        print('Ando caminando')
        

class Ciclista(Person):
    
    def __init__ (self, name):
        super().__init__(name)
    
    def avanza(self):
        print('Ando moviendome en mi bicicleta')

def main():
    persona = Person('Andy')
    persona.avanza()
    
    ciclista = Ciclista('David')
    ciclista.avanza()
        
if __name__ == '__main__':
    main()