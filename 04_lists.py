# Las listas son colecciones ordenadas y mutables de elementos en Python.

# Crear una lista vacía
my_other_list = list()  # Crear una lista vacía
print(f"type(my_other_list) created with list(): {type(my_other_list)}")

my_other_list = []  # Otra forma de crear una lista vacía
print(type(my_other_list))

print(len(my_other_list))  # Longitud de la lista vacía
print(my_other_list)  # Imprimir la lista vacía

my_list = list("1234567890")  # Crear una lista a partir de un string
print(my_list) # Imprimir la lista creada a partir del string
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Crear una lista con números del 1 al 10
print(my_list) # Imprimir la lista completa
my_list = list(range(1, 11))  # Otra forma de crear una lista de números del 1 al 10
print(my_list) # Imprimir la lista completa
print(len(my_list))  # Longitud de la lista


my_other_list = [35, 1.77, "Rodrigo", True, [7, 9, 10]]  # Lista con diferentes tipos de datos
my_other_list[2] = "Dafne"  # Modificar el tercer elemento de la lista
print("Lista modificada", my_other_list)  # Imprimir la lista con el tercer elemento modificado

print(my_other_list)  # Imprimir la lista con diferentes tipos de datos
print(type(my_other_list))  # Imprimir el tipo de la lista

my_other_list.insert(1, "Rojo")  # Insertar un elemento como segundo elemento de la lista
print(my_other_list)  # Imprimir la lista con el nuevo elemento insertado al principio
my_other_list[1] = "Azul"  # Modificar el segundo elemento de la lista
print(my_other_list)  # Imprimir la lista con el segundo elemento modificado

# Desempaquetado de listas
age, color, height, name, is_student, scores = my_other_list  # Desempaquetar la lista en variables
print(age, height, name, is_student, scores)  # Imprimir las variables desempaquetadas
age, height = my_other_list[:2]  # Desempaquetar solo los dos primeros elementos de la lista
print(age, height)  # Imprimir las dos primeras variables desempaquetadas

# Acceso a elementos de la lista
print(my_list[0], my_list[1])  # Primer y segundo elemento de la lista
print(my_list[-1], my_list[-2])  # Último y penúltimo elemento de la lista
print(my_list[1:3])  # Porción de la lista del segundo al tercer elemento
print(my_list[1:])  # Porción de la lista desde el segundo elemento
print(my_list[:3])  # Porción de la lista hasta el tercer elemento
print(my_list[-2:])  # Porción de la lista desde el penúltimo elemento
print(my_list[:-2])  # Porción de la lista sin los dos últimos elementos 

print(my_list[::2])  # Porción de la lista con un paso de 2
print(my_list[::-1])  # Lista revertida

print(my_list.count(5))  # Contar cuántos elementos hay en la lista
print(my_list.index(5))  # Encontrar la posición del primer elemento 5 en la lista
print(my_list.index(5, 0, 5))  # Encontrar la posición del primer elemento 5 en la lista desde el índice 0 hasta el 5
print(my_list.index(5, 0))  # Encontrar la posición del primer elemento 5 en la lista desde el índice 0
print(my_list.index(5, 0, 10))  # Encontrar la posición del primer elemento 5 en la lista desde el índice 0 hasta el 10
print(my_list.index(5, 0, len(my_list)))  # Encontrar la posición del primer elemento 5 en la lista desde el índice 0 hasta el final de la lista
print(my_list.index(5, 0, len(my_list) - 1))  # Encontrar la posición del primer elemento 5 en la lista desde el índice 0 hasta el penúltimo elemento

# Modificación de listas
my_list[0] = 100  # Modificar el primer elemento de la lista
print(my_list)  # Imprimir la lista modificada
my_list[1:3] = [200, 300]  # Modificar una porción de la lista
print(my_list)  # Imprimir la lista modificada

print(my_list + my_other_list)  # Concatenar dos listas
print(my_list * 2)  # Repetir la lista dos veces

# Añadir elementos a la lista
my_list.append(11)  # Añadir un elemento al final de la lista
print(my_list)  # Imprimir la lista con el nuevo elemento añadido
my_list.insert(0, 0)  # Insertar un elemento al principio de la lista
print(my_list)  # Imprimir la lista con el nuevo elemento insertado al principio
my_list.extend([12, 13, 14])  # Añadir varios elementos al final de la lista
print(my_list)  # Imprimir la lista con los nuevos elementos añadidos al final
my_list += [15, 16, 17]  # Otra forma de añadir varios elementos al final de la lista
print(my_list)  # Imprimir la lista con los nuevos elementos añadidos al final
# Eliminar elementos de la lista
my_list.remove(100)  # Eliminar el primer elemento 100 de la lista
print(my_list)  # Imprimir la lista con el elemento 100 eliminado
my_list.pop()  # Eliminar el último elemento de la lista
print(my_list)  # Imprimir la lista con el último elemento eliminado
print(my_list.pop(0))  # Eliminar el primer elemento de la lista  
print(my_list)  # Imprimir la lista con el primer elemento eliminado
print(my_list.pop(1))  # Eliminar el segundo elemento de la lista
print(my_list)  # Imprimir la lista con el segundo elemento eliminado
del my_list[10]  # Eliminar el primer elemento de la lista usando del
print(my_list)  # Imprimir la lista con el primer elemento eliminado
# Ordenar la lista
my_list.sort()  # Ordenar la lista en orden ascendente
print(my_list)  # Imprimir la lista ordenada

my_new_list = my_list.copy()  # Hacer una copia de la lista
print(my_new_list)  # Imprimir la copia de la lista

# Limpiar la lista
my_list.clear()  # Limpiar la lista
print(my_list)  # Imprimir la lista vacía después de limpiarla
print(my_new_list)  # Imprimir la lista con diferentes tipos de datos

my_new_list.reverse()  # Revertir el orden de los elementos en la lista
print(my_new_list)  # Imprimir la lista revertida
my_new_list.sort()  # Ordenar la lista en orden ascendente
print(my_new_list)  # Imprimir la lista ordenada

# Comprobar si un elemento está en la lista
print(5 in my_new_list)  # Comprobar si el elemento 5 está en la lista
print(100 in my_new_list)  # Comprobar si el elemento 100 está en la lista
print(100 not in my_new_list)  # Comprobar si el elemento 100 no está en la lista
print(5 not in my_new_list)  # Comprobar si el elemento 5 no está en la lista