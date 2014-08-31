# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 15:54:17 2014
2. Crie uma função que permita a conversao de graus Celsius para Fahrenheit.
°F = °C × 1,8 + 32
@author: portela.marco@gmail.com
"""
def celsius2Fahr(c):
    fah = c * 1.8 + 32
    return (fah)

temp = float(input('Digite a temperatura em Celsius:'))
novaTemp = celsius2Fahr(temp) 
print('A Temperatura em Fahrenheit é %3.2f' %novaTemp)