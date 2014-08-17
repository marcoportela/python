# -*- coding: utf-8 -*-
"""
Created on Fri Aug 15 20:58:13 2014
5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
o algoritmo de Euclides.
@author: portela.marco@gmail.com
"""
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
while num1 % num2 != 0:
    resto = num1 % num2
    num1 = num2    
    num2 = resto
#ou num1, num2 = num2, num1 % num2
print ('O MDC é %d' %num2)
    
