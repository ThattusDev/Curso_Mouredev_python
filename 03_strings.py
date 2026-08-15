# Los strings son secuencias de caracteres en Python, y se pueden crear utilizando comillas simples o dobles.
# Los strings son inmutables, lo que significa que no se pueden cambiar después de su creación.
# Los strings pueden contener letras, números, espacios y otros caracteres especiales.

my_string = "Mi string"
my_otro_string = "Mi otro string"

print(len(my_string))  # Longitud del string
print(len(my_otro_string))  # Longitud del otro string

print(my_string + " " + my_otro_string)  # Concatenación de strings

my_new_line_string = "Este es un string\ncon salto de línea"
print(my_new_line_string)  # String con salto de línea
print(my_new_line_string.split())  # Dividir el string en una lista de palabras
print(my_new_line_string.split(" "))  # Dividir el string por espacios
print(my_new_line_string.splitlines())  # Dividir el string por líneas
print(my_new_line_string.splitlines(keepends=True))  # Dividir el string por líneas y mantener los saltos de línea

my_tab_string = "Este es un string\tcon tabulación"
print(my_tab_string)  # String con tabulación

# Formateo de strings
my_name = "Juan"
my_last_name = "Pérez"
my_age = 36
print(f"Mi nombre es {my_name} {my_last_name} y mi edad es {my_age}")  # Formateo con f-strings
print("Mi nombre es %s %s y mi edad es %d" %(my_name, my_last_name, my_age))# Formateo con el operador %
print("Mi nombre es {} {} y mi edad es {}".format(my_name, my_last_name, my_age))  # Formateo con format()
print("Mi nombre es " + my_name + " " + my_last_name + " y mi edad es " + my_age)

# Desempaquetado de strings
my_string = "Hola"
a, b, c, d = my_string  # Desempaquetado de caracteres
print("Imprimir los caracteres desempaquetados: ", a, b, c, d)  # Imprimir los caracteres desempaquetados

# División de strings
my_string_slice = my_string[1:3]  # Obtener una porción del string
print(my_string_slice)  # Imprimir la porción del string de 1 a 3, que es "ol"
my_string_slice = my_string[1:]  # Obtener una porción del string desde el índice 1
print(my_string_slice)  # Imprimir la porción del string desde el índice 1
my_string_slice = my_string[:3]  # Obtener una porción del string hasta el índice 3
print(my_string_slice)  # Imprimir la porción del string hasta el índice 3
my_string_slice = my_string[-2]  # Obtener el segundo carácter desde el final del string
print(my_string_slice)  # Imprimir el segundo carácter desde el final, que es "l"
my_string_slice = my_string[-2:]  # Obtener los dos últimos caracteres del string
print(my_string_slice)  # Imprimir los dos últimos caracteres del string, que son "la"
my_string_slice = my_string[:-2]  # Obtener el string sin los dos últimos caracteres
print(my_string_slice)  # Imprimir el string sin los dos últimos caracteres, que es "Ho"
my_string_slice = my_string[0:5:2]  # Obtener una porción del string con un paso de 2
print(my_string_slice)  # Imprimir la porción del string con un paso de 2, que es "Hl"

 # Reverso de un string
my_reversed_string = my_string[::-1]  # Revertir el string
print(my_reversed_string)  # Imprimir el string revertido, que es "aloH"

# Funciones de strings
print(my_string.upper())  # Convertir el string a mayúsculas
print(my_string.capitalize())  # Capitalizar el primer carácter del string
print(my_string.title())  # Capitalizar el primer carácter de cada palabra del string
print(my_string.lower())  # Convertir el string a minúsculas
print(my_string.count("o"))  # Contar cuántas veces aparece "o" en el string
print(my_string.find("o"))  # Encontrar la posición de la primera aparición de "o" en el string
print(my_string.index("o"))  # Encontrar la posición de la primera aparición de "o" en el string (lanza error si no se encuentra)
print(my_string.replace("a", "a Python"))  # Reemplazar "Mi" por "Tu" en el string
print(my_string.isnumeric())  # Verificar si el string es numérico (retorna False)
print(my_string.isalpha())  # Verificar si el string es alfabético (retorna False)
print(my_string.isalnum())  # Verificar si el string es alfanumérico (retorna False)
print(my_string.islower())  # Verificar si el string está en minúsculas (retorna False)
print(my_string.isupper())  # Verificar si el string está en mayúsculas (retorna False)
print(my_string.startswith("Hi"))  # Verificar si el string comienza con "Hi"


# División de strings en una lista
my_string = "Hola, mundo, Python"
my_list = my_string.split(", ")  # Dividir el string por comas y espacios
print(my_list)  # Imprimir la lista resultante

