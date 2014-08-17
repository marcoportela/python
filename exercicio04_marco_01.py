# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 22:10:10 2014
1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
as funções max e min.
@author: portela.marco@gmail.com
"""
import random
lista = []
maior = 0
menor = 101 
for i in range(10):
    lista.append(random.randint(1, 100))
    if menor > lista[i]:
        menor = lista[i]
    if maior < lista[i]:
        maior = lista[i]
print(lista)
print('O maior é %d e o menor é o %d' %(maior, menor))
