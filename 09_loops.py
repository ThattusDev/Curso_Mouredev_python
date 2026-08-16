# Loops built-in functions


# while loop
print(f"\n while loop")
i = 0  # Inicializar i en 0
while i < 10:  # Mientras i sea menor que 10
    print(f"while {i}")  # Imprimir el valor de i en cada iteración
    i += 2  # Incrementar i en 2\
else:
    print(f"Fin del while 1")


# for loop
print(f"\n for loop")
for i in range(0,10,2):  # Iterar desde 0 hasta 10 con un paso de 2
    print(f"for {i}")  # Imprimir el valor de i en cada iteración
else:
    print(f"Fin del for 1")


# break statement
print(f"\n break statement")
for i in range(10):
    if i == 5:  # Si i es igual a 5
        print(f"For break in:, {i}")
        break  # Salir del bucle
    print(f"For break in 5, {i}")  # Imprimir el valor de i en cada iteración
else:
    print(f"Fin del for break 1")


# Iterar sobre una lista
my_list = [1, 2, 3, 4, 5]  # Lista de números
print(f"\n Iterar sobre una lista")
for i in my_list:  # Iterar sobre cada elemento de la lista
    print(f"For in list: {i}")  # Imprimir el valor de i en cada iteración


# Iterar sobre una tupla
my_tuple = (1, 2, 3, 4, 5)  # Tupla de números
print(f"\n Iterar sobre una tupla")
for i in my_tuple:  # Iterar sobre cada elemento de la tupla
    print(f"For in tuple: {i}")  # Imprimir el valor de i en cada iteración


# Iterar sobre un conjunto
my_set = {1, 2, 3, 4, 5}  # Conjunto de números
print(f"\n Iterar sobre un conjunto")
for i in my_set:  # Iterar sobre cada elemento del conjunto 
    print(f"For in set: {i}")  # Imprimir el valor de i en cada iteración


# Iterar sobre un diccionario
my_dict = {"Nombre": "Dafne", "Apellido": "Zurita", "Edad": 36}  # Diccionario de números
print(f"\n Iterar sobre un diccionario")
for key, value in my_dict.items():  # Iterar sobre cada clave y valor del
    print(f"For in dict: {key}, {value}")  # Imprimir la clave y el valor en cada iteración


# Iterar sobre las claves de un diccionario
print(f"\n Iterar sobre las claves de un diccionario")
for key in my_dict:  # Iterar sobre cada clave del diccionario  
    print(f"For in dict keys: {key}")  # Imprimir la clave en cada iteración
    if key == "Edad":
        print(f"For in dict keys: {my_dict[key]}")
else:
    print(f"Fin del for in dict keys")


# Iterar sobre los valores de un diccionario
print(f"\n Iterar sobre los valores de un diccionario")
for value in my_dict.values():  # Iterar sobre cada valor del diccionario
    print(f"For in dict values: {value}")  # Imprimir el valor en cada iteración
    if value == 36:
        print(f"For in dict values: {value}")
        break
else:
    print(f"Fin del for in dict values")


# Iterar sobre los valores de un diccionario
print(f"\n Iterar sobre los valores de un diccionario")
for value in my_dict.values():  # Iterar sobre cada valor del diccionario
    print(f"For_last in dict values: {value}")  # Imprimir el valor en cada iteración
    if value == "Zurita":  # Si el valor es "Zurita"
        print(f"For in dict values: {value}")
        continue  # Continuar con la siguiente iteración si el valor es 36
    print(f"Continuando con el siguiente valor: {value}")  # Imprimir si se continúa
else:
    print(f"Fin del for in dict values")
