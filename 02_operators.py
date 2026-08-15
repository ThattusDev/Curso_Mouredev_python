# Operadores
print("Operador suma (3 + 5):", 3 + 5)  # Suma
print("Operador resta (10 - 4):", 10 - 4)  # Resta
print("Operador multiplicación (2 * 6):", 2 * 6)  # Multiplicación
print("Operador división (8 / 2):", 8 / 2)  # División
print("Operador división entera (7 // 3):", 7 // 3)  # División entera
print("Operador módulo (10 % 3):", 10 % 3)  # Módulo
print("Operador potencia (2 ** 3):", 2 ** 3)  # Potencia

print("Operador negación (-5):", -5)  # Negación
print("Operador absoluto abs(-10):", abs(-10))  # Valor absoluto

print("Hola " + "Python! " + "Que tal?")  # Concatenación de cadenas
print("Hola " + str(5) + " Python!")  # Concatenación de cadena y entero convertido a cadena
print("Hola * 3" * 3)  # Repetición de cadena solo con enteros
print("Hola * 3" * 3 + "Python!")  # Repetición de cadena y concatenación con cadena
print("Hola * 3" * 3 + str(5))  # Repetición de cadena y concatenación con entero convertido a cadena

# Operadores de comparación
print("Operador igualdad (5 == 5):", 5 == 5)  # Igualdad
print("Operador desigualdad .,,,,,(5 != 3):", 5 != 3)  # Desigualdad
print("Operador mayor que (7 > 3):", 7 > 3)  # Mayor que
print("Operador menor que (2 < 4):", 2 < 4)  # Menor que
print("Operador mayor o igual que (5 >= 5):", 5 >= 5)  # Mayor o igual que
print("Operador menor o igual que (3 <= 4):", 3 <= 4)  # Menor

print("Hola > Python:", "Hola" > "Python")  # Comparación de cadenas (lexicográfica ASCII)
print("Hola < Python","Hola" < "Python")  # Comparación de cadenas (lexicográfica)
print("Hola == Hola", "Hola" == "Hola")  # Comparación de cadenas (igualdad)
print("Hola != Python", "Hola" != "Python")  # Comparación de cadenas (desigualdad)

# Operadores lógicos
print("Operador AND (3 > 2 and 2 > 3):", 3 > 2 and 2 > 3)  # AND lógico
print("Operador OR (3 > 2 or 2 > 3):", 3 > 2 or 2 > 3)  # OR lógico
print("Operador NOT (not 3 > 2):", not 3 > 2)  # NOT lógico
print("Operador AND con cadenas (\"Hola\" and \"Python\"):", "Hola" and "Python")  # AND lógico
print("Operador OR con cadenas (Hola or Python):", "Hola" or "Python")  # OR lógico
print("Operador NOT con cadenas:", not "Hola")  # NOT lógico (cadena no vacía es True)

# Operadores de identidad
a = [1, 2, 3]
b = a
c = a.copy()
print("Operador identidad (is):", a is b)  # Identidad (mismo objeto)
print("Operador identidad (is not):", a is not c)  # No identidad
print("Operador identidad (is):", a is c)  # Identidad (no es el mismo objeto)
print("Operador identidad (is not):", a is not b)  # No identidad