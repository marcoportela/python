# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 16:29:33 2014
3. Crie uma função numero par que permita verificar um dado número, x, passado
como parâmetro ́e número par.
@author: portela.marco@gmail.com
"""
def numeroPar(x):
    if x % 2 == 0:
        return('%d é par' %x)
    else:
        return('%d é impar' %x)

nr= int(input('Digite um número inteiro: '))
print(numeroPar(nr))