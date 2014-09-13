# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 16:38:27 2014
1.11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e
mostre:
a. o produto do dobro do primeiro com metade do segundo .
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.
@author: Marco Portela
"""
primeiro = int(input("Digite um número inteiro: "))
segundo = int(input("Digite outro número inteiro: "))
terceiro = int(input("Digite um número real: "))
calc_a = (primeiro * 2) * (segundo / 2)
calc_b = (primeiro * 3) + terceiro
calc_c = terceiro ** 3
print ("-- Calculo a = %3.2f \n-- Calculo b = %3.2f \n-- Calculo c = %3.2f" %(calc_a, calc_b, calc_c))