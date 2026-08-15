# Variables

my_string_variable = "Hello, Python!"
print(my_string_variable)

my_int_variable = 42
print(my_int_variable)

my_float_variable = 3.14
print(my_float_variable)

my_bool_variable = True
print("Este es el valor booleano:", my_bool_variable)

my_int_to_str_variable = str(my_int_variable)
print(type(my_int_to_str_variable))

print(my_string_variable, my_int_to_str_variable, my_int_variable, my_float_variable, my_bool_variable)

# a few Functions of the sistem
print(len(my_string_variable))  # Length of the string
print(type(my_string_variable))  # Type of the variable
print(my_string_variable.upper())  # Convert to uppercase
print(my_string_variable.lower())  # Convert to lowercase
print(my_string_variable.replace("Python", "World"))  # Replace substring
print(my_string_variable.split())  # Split the string into a list of words

# Variables en una sola línea
name, surname, age = "Dafne", "Zurita", 36
print("Name:", name, "Surname:", surname, "Age:", age)

# Input from the user
"""
user_input = input("Please enter your name: ")
print("Hello,", user_input)
"""

# Forzamos el tipo de una variable? no se puede hacer en Python, pero podemos cambiar el tipo de una variable
# by reassigning it to a new value of a different type.
my_int_variable: int = 42
print("Type of my_int_variable:", type(my_int_variable))
my_string_variable: str = "Hello, Python!"
my_string_variable = 32
print("Type of my_string_variable after assignment:", type(my_string_variable))
my_string_variable = "Hello, Python!"
print("Type of my_string_variable:", type(my_string_variable))