# Exceptions Handling in Python
# Exceptions are used to handle errors and other exceptional events in Python.
# They allow you to manage errors gracefully without crashing the program.

x = int(input())
y = int(input())
z = int(input())

n = int(input())

'''
resultado = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                resultado.append([i, j, k])
print(resultado)
'''
res = [
    [i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if i + j + k != n
]

print(res)

#EJERCICIO

'''
n = int(input("Hasta que numero quieres hacer tu lista?: "))
concatenar = ""
for i in range(n):
    concatenar += str(i + 1)
print(concatenar)

#lista
n2 = int(input("Hasta que numero quieres hacer tu lista?: "))
my_list= list(range(1,n2+1))
print(my_list)
'''

#MAS OPTIMO
###############################################################

n = int(input("Hasta qué número quieres hacer tu lista?: "))
    # Generar lista de strings con comprensión de listas
numeros = [str(i + 1) for i in range(n)]
    # Unir todos los elementos en una sola cadena
concatenar = "".join(numeros)
print(concatenar)

###############################################################

n = int(input("Hasta qué número quieres hacer tu lista?: "))
    # map convierte cada número en string directamente
concatenar = "".join(map(str, range(1, n + 1)))
print(concatenar)

###############################################################




def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))

'''
the year is bisiesto si:
ES divisible por 400, o
ES divisible por 4 Pero no por 100
# return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

the year is bisiesto si:
ES divisible por 4, y
No es divisible por 100 o es divisible por 400
# return year % 4 == 0 and (year %  100 != 0 or year % 400 == 0)
'''
def is_leap(year):
    # Write your logic here
    return year % 4 == 0 and (year %  100 != 0 or year % 400 == 0)

year = int(input())
print(is_leap(year))





