# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 16:28:52 2014
1.10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre
em graus Farenheit.
°F = °C × 1,8 + 32
@author: Marco Portela
"""
celsius = float(input("Didite a temperatura em Celsius: "))
faren = celsius * 1.8 + 32
print("A temperatura em Farenheit é %3.2f f" %faren )
