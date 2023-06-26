from math import *

hitrost = float(input("vpiši hitrost krogle: "))

kot = float(input("vpiši kot: "))
kot2 = kot * (pi/180)
g= 10


dolzina_strela = input((((hitrost)**2 * (sin((2* kot2)))) /g))
