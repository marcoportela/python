# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 14:24:51 2014
2. Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
números ímpares na lista IMPAR. Imprima as três listas.
@author: portela.marco@gmail.com
"""
import random
lista = []
listaPar = []
listaImpar = []
for i in range(20):
    lista.append(random.randint(1,100))
    if (lista[i] % 2) == 0:
        listaPar.append(lista[i])
    else:
        listaImpar.append(lista[i])
print('Lista')
print(lista)
print('Lista par')
print(listaPar)
print('Lista impar')
print(listaImpar)

