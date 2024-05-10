print('bienvenido al sorteo')
ganador=input('ingrese el numero ganador: ')
from random import shuffle 
lista=[1,2,3,4,5,6,7,8,9,10]
shuffle(lista)
print(lista[0])


