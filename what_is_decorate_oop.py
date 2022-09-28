# class Millas:
# 	def __init__(self, distancia = 0):
# 		self.distancia = distancia
  
#   	# Método getter
# 	def obtener_distancia(self):
# 		return self._distancia

# 	# Método setter
# 	def definir_distancia(self, valor):
# 		if valor < 0:
# 			raise ValueError("No es posible convertir distancias menores a 0.")
# 		self._distancia = valor

# 	def convertir_a_kilometros(self):
# 		return (self.distancia * 1.609344)

# # Creamos un nuevo objeto
# avion = Millas()

# # Indicamos la distancia
# avion.distancia = 200

# # Obtenemos el atributo distancia
# print(avion.distancia)

# # Obtenemos el método convertir_a_kilometros
# print(avion.convertir_a_kilometros())

# ###### Función property() ######
# # Esta función está incluida en Python, 
# # en particular crea y retorna la propiedad de un objeto. 
# # La propiedad de un objeto posee los métodos getter(), setter() y del().

# # En tanto, la función tiene cuatro atributos: property(fget, fset, fdel, fdoc):

# # fget: trae el valor de un atributo.
# # fset: define el valor de un atributo.
# # fdel: elimina el valor de un atributo.
# # fdoc: crea un docstring por atributo.
# # Veamos un ejemplo del mismo caso implementando la función property():

# class Millas:
# 	def __init__(self):
# 		self._distancia = 0

# 	# Función para obtener el valor de _distancia
# 	def obtener_distancia(self):
# 		print("Llamada al método getter")
# 		return self._distancia

# 	# Función para definir el valor de _distancia
# 	def definir_distancia(self, recorrido):
# 		print("Llamada al método setter")
# 		self._distancia = recorrido

# 	# Función para eliminar el atributo _distancia
# 	def eliminar_distancia(self):
# 		del self._distancia

# 	distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)

# # Creamos un nuevo objeto
# avion = Millas()

# # Indicamos la distancia
# avion.distancia = 200

# # Obtenemos su atributo distancia
# print(avion.distancia)

##### Decorador @property ####
# Este decorador es uno de varios con los que ya cuenta Python, el cual 
# nos permite utilizar getters y setters para hacer más fácil la implementación 
# de la programación orientada a objetos en Python cambiando los métodos o 
# atributos de las clases de forma que no modifiquemos el código.

# Pero mejor veamos un ejemplo en acción:

class Millas:
	def __init__(self):
		self._distancia = 0

	# Función para obtener el valor de _distancia
	# Usando el decorador property
	@property
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia

	# Función para definir el valor de _distancia
	@obtener_distancia.setter
	def definir_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		print("Llamada al método setter")
		self._distancia = valor

# Creamos un nuevo objeto
avion = Millas()

# Indicamos la distancia
avion.distancia = 200

# Obtenemos su atributo distancia
print(avion.definir..distancia)