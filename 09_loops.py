# Loops built-in functions

# while loop
i = 0  # Inicializar i en 0
while i < 10:  # Mientras i sea menor que 10
    print("while", i)  # Imprimir el valor de i en cada iteración
    i += 2  # Incrementar i en 2\
else:
    print("Fin del while 1")

# for loop
for i in range(0,10,2):  # Iterar desde 0 hasta 10 con un paso de 2
    print("for", i)  # Imprimir el valor de i en cada iteración
else:
    print("Fin del for 1")

# break statement
for i in range(10):
    if i == 5:  # Si i es igual a 5
        print("For break in:", i)
        break  # Romper el bucle
    print("For break in 5", i)  # Imprimir el valor de i en cada iteración
else:
    print("Fin del for break 1")

my_list = [1, 2, 3, 4, 5]  # Lista de números
my_tuple = (1, 2, 3, 4, 5)  # Tupla de números
my_set = {1, 2, 3, 4, 5}  # Conjunto de números
my_dict = {"Nombre": "Dafne", "Apellido": "Zurita", "Edad": 36}  # Diccionario de números

# Iterar sobre una lista
for i in my_list:  # Iterar sobre cada elemento de la lista
    print("For in list:", i)  # Imprimir el valor de i en cada iteración

# Iterar sobre una tupla
for i in my_tuple:  # Iterar sobre cada elemento de la tupla
    print("For in tuple:", i)  # Imprimir el valor de i en cada iteración

# Iterar sobre un conjunto
for i in my_set:  # Iterar sobre cada elemento del conjunto 
    print("For in set:", i)  # Imprimir el valor de i en cada iteración

# Iterar sobre un diccionario
for key, value in my_dict.items():  # Iterar sobre cada clave y valor del
    print("For in dict:", key, value)  # Imprimir la clave y el valor en cada iteración

# Iterar sobre las claves de un diccionario
for key in my_dict:  # Iterar sobre cada clave del diccionario  
    print("For in dict keys:", key)  # Imprimir la clave en cada iteración
    if key == "Edad":
        print("For in dict keys:", my_dict[key])
else:
    print("Fin del for in dict keys")

# Iterar sobre los valores de un diccionario
for value in my_dict.values():  # Iterar sobre cada valor del diccionario
    print("For in dict values:", value)  # Imprimir el valor en cada iteración
    if value == 36:
        print("For in dict values:", value)
        break
else:
    print("Fin del for in dict values")


# Iterar sobre los valores de un diccionario
for value in my_dict.values():  # Iterar sobre cada valor del diccionario
    print("For_last in dict values:", value)  # Imprimir el valor en cada iteración
    if value == "Zurita":  # Si el valor es "Zurita"
        print("For in dict values:", value)
        continue  # Continuar con la siguiente iteración si el valor es 36
    print("Continuando con el siguiente valor:", value)  # Imprimir si se continúa
else:
    print("Fin del for in dict values")
