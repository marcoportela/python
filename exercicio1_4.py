# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 10:09:26 2014
1.4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.
@author: Marco Portela
"""
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print ("A média é %2.2f" %media)