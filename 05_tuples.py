# Tuples are immutable sequences in Python, meaning they cannot be changed after creation.
# They are defined using parentheses () and can contain elements of different data types.

my_tuple = tuple()  # Crear una tupla vacía
print(type(my_tuple))  # tipo
my_tuple = (36, 1.7, "Dafne", "Zurita", "Azul", True, [7, 8.5, 10])  # Crear una tupla con diferentes tipos de datos
print(my_tuple)  # Imprimir la tupla

print(my_tuple[0])  # Acceder al primer elemento de la tupla
print(my_tuple[1:3])  # Acceder a una porción de la tupla
print(my_tuple[-1])  # Acceder al último elemento de la tupla

print(my_tuple.count("Azul"))  # Contar cuántas veces aparece "Azul" en la tupla
print(my_tuple.index("Azul"))  # Encontrar la posición de "Azul" en la tupla
print(my_tuple.index("Azul", 0, 5))  # Encontrar la posición de "Azul" en la tupla desde el índice 0 hasta el 5
print(my_tuple.index("Azul", 0))  # Encontrar la posición de "Azul" en la tupla desde el índice 0
print(my_tuple.index("Azul", 0, len(my_tuple)))  # Encontrar la posición de "Azul" en la tupla desde el índice 0 hasta el final de la tupla
print(my_tuple.index("Azul", 0, len(my_tuple) - 1))  # Encontrar la posición de "Azul" en la tupla desde el índice 0 hasta el penúltimo elemento

# my_tuple[1] = 1.75  # Modificar el segundo elemento de la tupla (esto no es posible, ya que las tuplas son inmutables)
# Esto generará un error, ya que las tuplas son inmutables

my_other_tuple = (10, 200, 3000)  # Crear otra tupla
my_sum = my_tuple + my_other_tuple  # Concatenar dos tuplas
print(my_sum)  # Imprimir la tupla resultante de la concatenación
print(my_tuple * 2)  # Repetir la tupla dos veces

my_list = list(my_tuple)  # Convertir una tupla en una lista
print(my_list)  # Imprimir la lista convertida a partir de la tupla
print(type(my_list))  # Imprimir el tipo de la lista
my_list.insert(5, "Verde")  # Insertar un elemento en la lista
print(my_list)  # Imprimir la lista con el nuevo elemento insertado
my_tuple = tuple(my_list)  # Convertir la lista de nuevo a una tupla
print(my_tuple)  # Imprimir la tupla resultante de la conversión
print(type(my_tuple))  # Imprimir el tipo de la tupla

del my_tuple  # Eliminar la tupla
# print(my_tuple)  # Esto generará un error, ya que la tupla ha sido eliminada
