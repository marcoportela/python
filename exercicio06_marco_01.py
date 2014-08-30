# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 06:54:06 2014
1. Crie uma funcão potencia que receba dois números a e b (base e expoente, respec-
tivamente) e retorne a potência a(base) b(potência).
@author: portela.marco@gmail.com
"""
def potencia(a, b):
    resultado = a**b
    return resultado

base = int(input('Digite a base: '))
poten = int(input('Digite a potencia: '))
print(potencia(base,poten)) 
