## Modulos ##

import my_module 
my_module.sumValue(5, 3, 1)
my_module.printValue("Hola daf")


from my_module import sumValue, printValue
sumValue(5, 4, 1)
printValue("Holaaaaaaaa")


import math 
print(math.pi)
print(math.pow(2, 8))


from math import pi as pi_value
print(pi_value)