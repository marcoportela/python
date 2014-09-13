# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 21:01:06 2014
1.9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e
mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
@author: Marco Portela
"""
faren = float(input("Digite a temperatura em Fahrenheit: "))
celsius = 5 * (faren - 32) /9
print ("A temperatura em Celsius é de %2.2f c" %celsius)
