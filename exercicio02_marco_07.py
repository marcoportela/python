# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 19:26:36 2014
7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
@author: portela.marco@gmail.com
"""
area = float(input('Informe o tamanho da área em metros quadrados a ser pintada: '))
LATA = 18
PRECO_UNIT = 80.00
#Cada litro rende 3 metros quadrados de pintura
rendimento = LATA * 3
if area <= rendimento:
    nrLatas = 1
else:
    #somente são vendidos um número inteiro de latas    
    nrLatas = int(area / rendimento) + 1 
precoTotal = PRECO_UNIT * nrLatas
print('O número de latas necessárias é %d' %nrLatas)
print('O preço total é R$ %3.2f' %precoTotal)