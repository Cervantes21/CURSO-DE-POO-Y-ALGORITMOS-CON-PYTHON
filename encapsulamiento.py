# Usando OOP, podemos restringir el acceso a métodos y variables.
# Esto evita que los datos se modifiquen directamente,
# lo que se denomina "Encapsulación", ó "Encapsulamiento".
# Existen dos maneras de crear atributos privados en Python:
# guión bajo al principio del nombre, o con dos guiones bajos (__)
# la primera forma establece que los atributos son privados pero
# Sólo por convención(Internamente, no son realmente privadas.)
# La segunda forma hace que los atributos adquieran las propiedades
# que realmente los hacen privados
 
class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
            # Aquí utilizamos programacion defensiva para cuidar nuestro codigo.
        else:
            raise ValueError(f'La region {region} no esta en la lista')


casilla = CasillaDeVotacion(123,['Mexico','Morelos'])
print(casilla.region)
casilla.region = 'Mexico'
print(casilla.region)