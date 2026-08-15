# Dictionaries are mutable, unordered collections of key-value pairs.

my_dict = dict()  # Crear un diccionario vacío
my_other_dict = {}  # Crear un diccionario vacío

print(type(my_dict))  # Imprimir el tipo de my_dict, que es un diccionario
print(type(my_other_dict))  # Imprimir el tipo de my_other_dict, que es

my_other_dict = {
    "name": "Dafne", 
    "last_name": "Zurita",
    "age": 36, 
    "height": 1.7, "is_student": True
}  # Crear un diccionario con diferentes tipos de datos

my_dict = {
    "name": "Dafne",
    "last_name": "Zurita",
    "age": 36,
    "languages": {"Python", "JavaScript", "C++"},
    1: "one",  # Clave numérica
}  # Crear un diccionario con un set como valor


print(f"\n {my_other_dict}")  # Imprimir el diccionario con diferentes tipos de datos
print(f" {my_dict}")  # Imprimir el diccionario con un set como valor

print(f"\n {my_dict['name']}")  # Acceder al valor asociado a la clave "name" en my_dict
print(f" {my_dict[1]}")  # Acceder al valor asociado a la clave numérica 1 en my_dict

my_dict["name"] = "Dafne Zurita"  # Modificar el valor asociado a la clave "name" en my_dict
print(f"\n {my_dict['name']}")  # Imprimir el valor modificado de la clave "name"
my_dict["calle"] = "Calle Falsa 123"  # Agregar una nueva clave "calle" con su valor en my_dict
print(f" {my_dict}")  # Imprimir el diccionario después de agregar la nueva clave

my_dict["languages"].add("Java")  # Agregar un nuevo lenguaje al set asociado a la clave "languages"
print(f"\n {my_dict['languages']}")  # Imprimir el set de lenguajes después de agregar
del my_dict["languages"]  # Eliminar la clave "languages" del diccionario
print(f" {my_dict}")  # Imprimir el diccionario después de eliminar la clave "languages"

print(f"\n Zurita" in my_other_dict)  # Verificar si "Zurita" es un valor en el diccionario
print(f"last_name" in my_other_dict)  # Verificar si "apellido" es una clave en el diccionario

print(f"\n keys: {list(my_other_dict.keys())}")  # Imprimir las claves del diccionario
print(f"values: {list(my_other_dict.values())}")  # Imprimir los valores del diccionario
print(f"items: {list(my_other_dict.items())}")  # Imprimir los pares clave-valor del diccionario

print(f"\n {my_dict.fromkeys(['name', 'age'], 'unknown')}")  # Crear un nuevo diccionario con claves y un valor por defecto
print(f"{dict.fromkeys(['name', 'age'], 'unknown')}")  # Crear un nuevo diccionario con claves y un valor por defecto usando dict
print(f"{my_other_dict.fromkeys(['name', 'age', 'Piso'], '7')}")  # Crear un nuevo diccionario con claves y un valor por defecto

my_new_dict = my_other_dict.copy()  # Hacer una copia (clon) del diccionario my_other_dict
print(f"\n {my_new_dict}")  # Muestra en pantalla la copia del diccionario
my_new_dict = dict.fromkeys(my_other_dict, ['Dafne', 'Zurita'])  # Genera un nuevo diccionario usando las claves de my_other_dict
# y asigna la misma lista ['Dafne', 'Zurita'] como valor para cada clave
print(f"{my_new_dict}")  # Imprime el nuevo diccionario creado con dict.fromkeys

print(f"\n {list(my_other_dict)}")  # Convertir las claves del diccionario en una lista e imprimirla
print(f"{list(my_other_dict.keys())}")  # Convertir las claves del diccionario en una lista
print(f"{list(my_other_dict.values())}")  # Convertir los valores del diccionario en una lista e imprimirla
print(f"{list(my_other_dict.items())}")  # Convertir los pares clave-valor del diccionario en una lista e imprimirla

print(f"\n {tuple(my_other_dict)}")  # Convertir las claves del diccionario en una tupla e imprimirla
print(f"{tuple(my_other_dict.keys())}")  # Convertir las claves del diccionario en una tupla
print(f"{tuple(my_other_dict.values())}")  # Convertir los valores del diccionario en una tupla e imprimirla
print(f"{tuple(my_other_dict.items())}")  # Convertir los pares clave-valor del diccionario en una tupla e imprimirla

print(f"\n {set(my_other_dict)}")  # Convertir las claves del diccionario en un set e imprimirlo
print(f"{set(my_other_dict.keys())}")  # Convertir las claves del diccionario en un set
print(f"{set(my_other_dict.values())}")  # Convertir los valores del diccionario en un set e imprimirlo
print(f"{set(my_other_dict.items())}")  # Convertir los pares clave-valor del diccionario en un set e imprimirlo