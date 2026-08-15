# Conditionals in Python
# # if, elif, else statements
# Comparison operators: ==, !=, <, >, <=, >=
# Logical operators: and, or, not
# Membership operators: in, not in
# Identity operators: is, is not
# Ternary operator: value_if_true if condition else value_if_false

my_condition = False  # Variable booleana para la condición
if my_condition:  # Verificar si my_condition es True
    print(f"La condición es verdadera")  # Imprimir si la condición es verdadera
else:  # Si la condición es falsa
    print(f"La condición es falsa") # Imprimir si la condición es falsa

print(f"\nFin del if_1")  # Imprimir al final del programa

my_condition = 5 * 2 == 10  # Evaluar una condición booleana
if my_condition:  # Verificar si my_condition es True
    print(f"La condición es verdadera")  # Imprimir si la condición es verdadera
else:  # Si la condición es falsa
    print(f"La condición es falsa")  # Imprimir si la condición es falsa

print(f"\nFin del if_2")  # Imprimir al final del programa

my_condition = 5 * 2 - 4
if my_condition >= 10 and my_condition < 20:  # Verificar si my_condition
    print(f"La condición es >= 10 and my_condition < 20")  # Imprimir si la condición es verdadera
elif my_condition < 10:  # Verificar si my_condition es menor que 10
    print(f"La condición es menor que 10")
else:  # Si la condición es falsa
    print(f"La condición es >= 20")  # Imprimir si la condición es falsa

print(f"\nFin del if_3")  # Imprimir al final del programa

my_string = "Dafne"
if my_string:  # Verificar si my_string no está vacío
    print(f"my_string no está vacío")  # Imprimir si my_string no está vacío
else:  # Si my_string está vacío
    print(f"my_string está vacío es")

print(f"\nFin del if_4")  # Imprimir al final del programa