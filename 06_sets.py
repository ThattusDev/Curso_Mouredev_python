# Sets son colecciones desordenadas de elementos únicos, no permiten duplicados y no tienen un orden específico.
# Se utilizan para almacenar elementos únicos y realizar operaciones matemáticas como uniones, intersecciones y diferencias.

my_set = set()  # Crear un set vacío
print(f"type(my_set) created with set(): {type(my_set)}")  # Imprimir el tipo de my_set, que es un set

my_set = {1, 2, 3, 4, 5, 1, 2, 3}  # Crear un set con números, los duplicados se eliminan
print(f"my_set = {{1, 2, 3, 4, 5, 1, 2, 3}}: {my_set}")  # Imprimir el set, que no tendrá duplicados

# Acceso a elementos de un set
# Los sets no soportan acceso por índice, ya que son colecciones desordenadas
# my_set[0]  # Esto generará un error, ya que los sets no tienen orden
print(f"len(my_set): {len(my_set)}")  # Imprimir la longitud del set

my_set.add("Rojo")  # Agregar un elemento al set
my_set.add(6)  # Agregar otro elemento al set
my_set.add(0)  # Agregar un elemento al set, en este caso el número 0
my_set.add(3.14)  # Agregar un número decimal al set
my_set.add("Verde")  # Agregar un string al set
my_set.add(1)  # Intentar agregar un elemento que ya existe, no tendrá efecto
print(my_set)  # Imprimir el set con el nuevo elemento agregado
my_set.remove("Rojo")  # Eliminar un elemento del set, sino existe marca error
print(my_set)  # Imprimir el set después de eliminar un elemento

my_set.discard("Azul")  # Intentar eliminar un elemento que no existe, no generará error
print(my_set)  # Imprimir el set después de intentar eliminar un elemento que no existe


my_other_set = {}  # Esto no es un set, es un diccionario vacío
print(f"type(my_other_set) created with {{}}: {type(my_other_set)}")  # Imprimir el tipo de my_other_set, que es un diccionario
my_other_set = {"Dafne", "Zurita", "Morado"}  # Crear un set con diferentes tipos de datos
print(f"After add data type(my_other_set): {type(my_other_set)}")  # Imprimir el tipo de my_other_set, que es un set
print(f"my_other_set: {my_other_set}")  # Imprimir el set con diferentes tipos de datos
print(f"Dafne in {{my_other_set}}: { 'Dafne' in my_other_set}")  # Verificar si "Dafne"

print(f"my_other_set: {my_other_set}")  # Imprimir el set original
my_other_set.clear()  # Limpiar el set, eliminando todos sus elementos  
print(f"After my_other_set.clear() show len(my_other_set): {len(my_other_set)}")  # Imprimir el set después de limpiarlo, debería estar vacío
del my_other_set  # Eliminar el set
# print(my_other_set)  # Esto generará un error, ya que el set ha sido eliminado

# Operaciones con sets
set_a = {1, 2, 3, 4, 5} # Crear un set A
set_b = {4, 5, 6, 7, 8} # Crear un set B

print(f"set_a: {set_a}")  # Imprimir el set A
print(f"set_b: {set_b}")  # Imprimir el set B
print(f"Union: {set_a.union(set_b)}")  # Otra forma de hacer la unión de set A y set B
print(f"Union |: {set_a | set_b}")  # Unión de set A y set B, imprime todos los elementos únicos de ambos sets
print(f"Union A, B, 9, 10: {set_a.union(set_b).union({9, 10})}")  # Unión de set A y set B con otros elementos, imprime todos los elementos únicos de ambos sets y los nuevos
print(f"A Difference B: {set_a.difference(set_b)}")  # Otra forma de hacer la diferencia de set A y set B
print(f"A - B(Diferencia): {set_a - set_b}")  # Diferencia de set A y set B, imprime los elementos que están en set A pero no en set B
print(f"A intersection B: {set_a.intersection(set_b)}")  # Otra forma de hacer la intersección de set A y set B
print(f"Intersection A & B: {set_a & set_b}")  # Intersección de set A y set B, imprime los elementos que están en ambos sets
print(f"A ^ B(Diferencia simétrica): {set_a ^ set_b}")  # Diferencia simétrica entre set A y set B # Imprime los elementos que están en uno de los sets pero no en ambos
print(f"A symetric_difference B: {set_a.symmetric_difference(set_b)}")  # Otra forma de hacer la diferencia simétrica entre set A y set B
print(f"Set A isdisjoint B: {set_a.isdisjoint(set_b)}")  # Verifica si set A y set B no tienen elementos en común, devuelve True si no hay intersección
print(f"Set A issubset B: {set_a.issubset(set_b)}")  # Verifica si set A es un subconjunto de set B, devuelve True si todos los elementos de set A están en set B
print(f"Set A issuperset B: {set_a.issuperset(set_b)}")  # Verifica si set A es un superconjunto de set B, devuelve True si todos los elementos de set B están en set A
print(f"Set A == set B?: {set_a == set_b}")  # Compara si set A y set B son iguales   # Devuelve True si ambos sets tienen los mismos elementos
print(f"Set A != set B?: {set_a != set_b}")  # Compara si set A y set B son diferentes # Devuelve True si ambos sets tienen diferentes elementos
print(f"Set A <= set B?: {set_a <= set_b}")  # Verifica si set A es un subconjunto de set B, devuelve True si todos los elementos de set A están en set B
print(f"Set A >= set B?: {set_a >= set_b}")  # Verifica si set A es un superconjunto de set B, devuelve True si todos los elementos de set B están en set A