# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 08:48:11 2014
1.17 Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os
respectivos preços em 3 situações:
a. comprar apenas latas de 18 litros;
b. comprar apenas galões de 3,6 litros;
c. misturar latas e galões, de forma que o preço seja o menor.
Acrescente 10% de folga e sempre arredonde os valores para cima,
isto é, considere latas cheias.
@author: Marco Portela
"""
area = float(input("Digite o tamanho da área a ser pintada em metros quadrador: "))
COBERTURA = 6
LATA = 18
GALAO = 3.6
PRECO_LATA = 80.00
PRECO_GALAO = 25.00
area_lata = LATA * COBERTURA
area_galao = GALAO * COBERTURA
#10% de folga no cálculo da área
area_folga = area + (area * 0.10)
num_lata = 0
num_galao = 0
total_pagar = 0
#Cálculo de utilização de latas 
if area_folga <= area_lata:
    num_lata = 1
    total_pagar = PRECO_LATA
    print("A) Será necessária %d lata e o valor a pagar é R$ %.2f" %(num_lata, total_pagar))
else:
    num_lata = int(area_folga / area_lata) + 1
    total_pagar = num_lata * PRECO_LATA
    print("A) Serão necessárias %d latas e o valor a pagar é R$ %.2f" %(num_lata, total_pagar))
#Cálculo de utilização de Galões
if area_folga <= area_galao:
    num_galao = 1
    total_pagar = PRECO_GALAO
    print("B) Será necessário %d galão e o valor a pagar é R$ %.2f" %(num_galao, total_pagar))
else:
    num_galao = int(area_folga / area_galao) + 1
    total_pagar = num_galao * PRECO_GALAO
    print("B) Serão necessários %d galões e o valor a pagar é R$ %.2f" %(num_galao, total_pagar))
#Cálculo de misto Latas e galões
    #Cada 3 galões compensa financeiramente em relação 01 lata
if area_folga <= (area_galao * 3):
    num_lata = 0
    num_galao = int(area_folga / area_galao) + 1
    total_pagar = num_galao * PRECO_GALAO
    print("C) Serão necessários %d latas e %d galões e o valor a pagar é R$ %.2f" %(num_lata, num_galao, total_pagar)) 
elif area_folga > (area_galao * 3) and area_folga < area_galao:
    num_galao = 0    
    num_lata = 1
    total_pagar = PRECO_LATA
    print("C) Serão necessários %d latas e %d galões e o valor a pagar é R$ %.2f" %(num_lata, num_galao, total_pagar)) 
else:
    #Caso a área seja maior que o rendimento de 1 lata
    num_lata = int(area_folga / area_lata)
    #resto da divisão por latas será a área a ser dividida em galões + 1    
    num_galao = int((area_folga % area_lata) / area_galao) + 1
    total_pagar = (num_lata * PRECO_LATA) + (num_galao * PRECO_GALAO)
    print("C) Serão necessários %d latas e %d galões e o valor a pagar é R$ %.2f" %(num_lata, num_galao, total_pagar)) 
