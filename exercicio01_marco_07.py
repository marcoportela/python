# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 08:46:59 2014
7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
@author: Marco - data
"""
celsius = float(input('Informe a temperatura em Celsius: '))
fahrenheit = 9 * celsius / 5 + 32
print('A temperatura convertida para Fahrenheit é %3.2f f' %fahrenheit)
