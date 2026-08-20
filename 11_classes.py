# Clases
# Las clases son plantillas para crear objetos. Encapsulan datos y comportamiento.
# Una clase se define usando la palabra clave `class` seguida del nombre de la clase y dos puntos.
# Las clases pueden tener atributos (datos) y métodos (funciones) que operan sobre esos datos.
# Las clases también pueden tener un método constructor `__init__` que inicializa los atributos del objeto.
# Las clases pueden estar vacías al agregar 'pass', es decir, no tienen atributos ni métodos definidos.
# Las clases también pueden tener métodos que realizan acciones o cálculos.
# Las clases se pueden instanciar para crear objetos, que son instancias de la clase.
# Las clases se pueden usar para crear objetos con atributos y métodos específicos.
# Las clases son una parte fundamental de la programación orientada a objetos en Python.

class MyEmptyPerson:
    pass #Te permite definir clases o funciones vacías sin que Python se queje.

print(MyEmptyPerson)
print(MyEmptyPerson())
print(type(MyEmptyPerson))

print("\n")


class Person:

    def __init__(self, age, name = "Pepe", surname = "Loco"): #'__init__'= constructor de clases (lo que se ejecuta al crear un objeto de la clase)
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

#########################################

class Person:
                # Parameters: name (str), surname (str), alias (str, optional)
    def __init__(self, name, surname, alias = "(Sin alias)"): #Siempre llamas self, init = constructor
        # Attributes of the class
        self.name = name    # El self es obligatorio para referirse a los atributos y métodos de la clase
        self.surname = surname
        self.alias = alias
        self.full_name = f"{self.name} {self.surname} {self.alias}"  # Atributo que almacena el nombre completo de la persona
        self.__name = "Rodrigo"  # Atributo privado, no se puede acceder directamente desde fuera de la clase

    def get_name(self): #get y set (propiedades)
        # No puedo modificar el atributo privado desde fuera de la clase, pero puedo acceder a él mediante un método público.
        return self.__name # Solo puedo acceder a este atributo desde dentro de la clase, no desde fuera.

    def walk(self): # Tienes que pasarle self para poder acceder a los atributos de la clase.
        print(f"{self.full_name} está caminando.") 

my_person = Person("Dafne", "Zurita")
print(f"Mi nombre es: {my_person.name} {my_person.surname}")  # Imprime el nombre y apellido de la persona
print(f"Mi nombre completo es (atributo full_name): {my_person.full_name}")  # Imprime el nombre completo de la persona
my_person.walk()  # Llama al método walk para que la persona camine

my_other_person = Person("Juan", "Perez", "El Juancho")
print(f"\nMi nombre es: {my_other_person.name} {my_other_person.surname}")  
print(f"Mi nombre completo es (atributo full_name): {my_other_person.full_name}")  
my_other_person.walk()  
# Modifica el atributo full_name de la persona
my_other_person.full_name = "Sergio Perez checo"  
print(f"\nMi nombre completo modificado es (atributo full_name): {my_other_person.full_name}")  # Imprime el nombre completo modificado de la persona

#Llamar metodo get_name() para acceder al atributo privado __name
print(f"\nMi nombre es (método get_name()): {my_other_person.get_name()}")  # Imprime el nombre de la persona usando el método get_name