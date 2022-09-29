# Ejemplo para almacen de playeras:

class Playera:
    def __init__ (self, color, talla, genero, tipo,choose):
        self.color = color
        self.talla = talla
        self.genero = genero
        self.tipo = tipo
        self.choose = choose
    choose = ()
        
    def color(self, choose_color):
        list_colors = ('rojo', 'azul', 'negro', 'blanca')
        self._choose = choose_color
        choose_color = input(print(f"{list_colors} Escoge un color: "))
        return choose_color
    
    def talla(self, choose_size):
        size_list = ('chica', 'mediana', 'grande', 'extragrande')
        self._choose = choose_size
        choose_size = input(print(f"{size_list} Escoge una talla: "))
        return choose_size
    
    def genero(self, choose_gender):
        gender_list = ('unisex', 'mujer', 'hombre')
        self._choose = choose_gender
        choose_gender = input(print(f"{gender_list} Escoge un genero para tu playera: "))
        return choose_gender
    
    def tipo(self, choose_type):
        list_type = ('cuello V', 'cuello R', 'Polo')
        self._choose = choose_type
        choose_type = input(print(f'{list_type} Escoge un tipo de playera: '))
        return choose_type
    
class your_shirt(Playera):
    def __init__ (self, choose):
        super().__init__(choose)
        
if __name__ == '__main__':
    
    tu_playera = your_shirt(choose)
    
    print(tu_playera.choose)