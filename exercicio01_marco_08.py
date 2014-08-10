# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 08:56:56 2014
8) Faça agora o contrário, de Fahrenheit para Celsius.
°C = (°F − 32) / 1,8
@author: Marco - data
"""
fahrenheit = float(input('Informe a temperatura em fahrenheit: '))
celsius =  (fahrenheit - 32) / 1.8
print('A temperatura convertida para Celsius é %3.2f C' %celsius)
