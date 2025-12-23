#Встроенные модули python,определение собственных модулей б внешние модули и их устоновки,виртуальная среда
import random
#random - это модуль
# from random import randint, randrange
# print (randint (1,10))

# import datetime - работа с датщй и время
# import time - работа со временем
# import os - работа с оперативной памятью
# import pathlib - работа с путями
# это все встроенные модули

# import lesson2
from lesson2 import Hero
hero = Hero("Kirito",11,100)# через точку млжно достовать его отрибуты или методы
print (hero.name )
