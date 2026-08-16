# Clases
# Las clases son plantillas para crear objetos. Encapsulan datos y comportamiento.

# Una clase se define usando la palabra clave `class` seguida del nombre de la clase y dos puntos.

# Las clases pueden tener atributos (datos) y métodos (funciones) que operan sobre esos datos.

# Las clases también pueden tener un método constructor `__init__` que inicializa los atributos del objeto.

# Las clases pueden estar vacías, es decir, no tienen atributos ni métodos definidos.

# Las clases también pueden tener métodos que realizan acciones o cálculos.

# Las clases se pueden instanciar para crear objetos, que son instancias de la clase.

# Las clases se pueden usar para crear objetos con atributos y métodos específicos.

# Las clases son una parte fundamental de la programación orientada a objetos en Python.


class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())
print(type(MyEmptyPerson))

print("\n")

class Person:
    def __init__(self, age, name = "Pepe", surname = "Loco"):
        self.name = name
        self.surname = surname
        self.age = age
        self.__name = name  # Atributo privado, no se puede acceder directamente desde fuera de la clase
        self.__surname = surname  # Atributo privado, no se puede acceder directamente desde fuera de la clase
        self.__age = age  # Atributo privado, no se puede acceder directamente desde fuera de la c
       # Eliminamos el atributo full_name para evitar conflicto con el método

    def get_name(self):
        return self.__name
    
    def greating(self):
        return f"Hola, soy {self.full_name()} y tengo {self.age} años"
    
    def walk(self):
        print(f"{self.full_name()} está caminando. {self.full_name()}")
    
    def full_name(self):
        return f"{self.name} {self.surname}"

pepe = Person(30)
print(f"{pepe.name} {pepe.surname} tiene {pepe.age} años") 

pepe.name = "Pedro"
pepe.surname = "Fernandez"
pepe.age = 36
print(pepe.greating())  # Imprime el saludo personalizado


# print(f"{pepe.name} {pepe.surname} tiene {pepe.age} años")

carlos = Person(25, "Carlos", "Lara")
carlos.greating = carlos.greating()
print(carlos.greating)  # Imprime el saludo personalizado
#print(f"{carlos.name} {carlos.surname} tiene {carlos.age} años")
carlos.walk()  # Llama al método walk de la clase Person

print(carlos.get_name())  # Imprime el nombre de Carlos usando el método get_name
print(pepe.get_name())  # Imprime el nombre de Pepe usando el método get_name   
