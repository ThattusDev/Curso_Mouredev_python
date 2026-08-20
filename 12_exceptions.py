# Manejo de excepciones en Python
# Las excepciones se utilizan para manejar errores y otros eventos excepcionales en Python.
# Permiten gestionar errores de manera elegante sin hacer que el programa se bloquee.

numero_1, numero_2 = 10, 2
numero_2 = "0" 
#print(numero_1 + numero_2)

# try except
try:
    print(numero_1 + numero_2)
    print("No se ha producido un error")
except: 
    # se ejecuta si se produce un error en el bloque try
    print("Se a producido un error")

print("\n")

# try except else
try:
    print(numero_1 + numero_2)
    print("No se ha producido un error")
except:
    print("Se a producido un error")
else:       
    # else es opcional y se ejecuta si no se produce ninguna excepción en el bloque try
    print("La ejecucion continua correctamente")

print("\n")

# try except else finally
try:
    print(numero_1 + numero_2)
    print("No se ha producido un error")
except:
    print("Se a producido un error")
else:       
    # else es opcional y se ejecuta si no se produce ninguna excepción en el bloque try
    print("La ejecucion continua correctamente")
finally:    
    # finally es opcional y se ejecuta siempre, independientemente de si se produce una excepción o no
    print("La ejecucion ha finalizado")

print("\n")

# Excepción por tipo
try:
    print(numero_1 + numero_2)
    print("No se ha producido un error")
except TypeError: # 'Tipo incorrecto' - tipo de excepción que se produce cuando se intenta realizar una operación con tipos de datos incompatibles
    # se ejecuta si se produce un error de tipo en el bloque try
    print("Se ha producido un TypeError")
except ValueError: # 'Valor incorrecto' - tipo de excepción que se produce cuando se intenta convertir un valor a un tipo de dato incompatible
    # se ejecuta si se produce un error de valor en el bloque try
    print("Se ha producido un ValueError")

print("\n")

# Captura de la información de la excepción
try:
    print(numero_1 + numero_2)
    print("No se ha producido un error")
except TypeError as error: 
    print(f"TypeError {error}")
except Exception as error: # exception es la clase base para todas las excepciones en Python, y permite capturar cualquier tipo de excepción que se produzca en el bloque try
    # as error permite capturar la información de la excepción y almacenarla en una variable
    print(f"Se ha producido un error: {error}")

print("\n")
