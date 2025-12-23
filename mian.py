from django.contrib.auth.models import AbstractUser

from my_paceje.module_1 import add
from my_paceje.module_2 import *
# *- озночает все
# from my_paceje import Hero,Eliza, add
# eliza = Eliza()
# print (add (12,20))
# *- его минус в том что если импортируюмая файл содержит в себе еще какие то импорто
# то оно и его тоде будет импортироват что бы его избежать надо писать (__all__=( и здесь указать классы
# или функции которые мы хотим импортировать )
# __all__ означает у нас все (* - работает с ним )
#
# from colorama import Fore, Back, Style
# print (Fore.RED + "some red text ")  # перекрасит на красны
# print (Back.GREEN + " and with a green blackround") # изменит его под зелений рамку
# print (Style. DIM +"and in dim text ") #это изменит его стиль
# print (Style.RESET_ALL) #збрасывет все стили
# print (" back to normal now ")
#

# from django.utils.translation import gettext_lazy as _
# from django.db import models
#
# class User:
#     name = models.CharField(verbose_name=_("test"))


import pandas as pd
# as- это ключивое сло Python и его нельза изменить ( в нашем случи мы написали pd потому что это pandas)
# pd - это просто кароткое название и его как угодна изменить
data = {
    "Brand": ["Ford", "Ford", "Ford"],
    "Model": ["Sierra" , "F-150" , "Mustang"],
    "Typ": ["2.0 GL" , "Raptor",["Mach-E", "Mach-1"]]
}
df = pd.DataFrame(data) # DateFrame - создоет таблицу
newdf = df.explode("Typ") # разбирает их на несколько строк
