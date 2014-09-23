# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 20:41:35 2014
1.16 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a
serem compradas e o preço total.
@author: Marco Portela
"""
tamanho = float(input("Informe o tamanho em metros quadrados: "))
COBERTURA = 3
LATA = 18
#Cobertura por lata de 18 litros
cobert_lata = LATA * COBERTURA
custo = 80.00
if tamanho < cobert_lata:
    quant_lata = 1
else:
    quant_lata = int(tamanho / cobert_lata) + 1
total = custo * quant_lata
print ("Quantidade de latas: %d" %quant_lata)
print ("Preço total: R$ %.2f" %total)
    