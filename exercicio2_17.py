# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 21:44:46 2014
2.17 Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados formem um
triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
a. Três lados formam um triângulo quando a soma de quaisquer dois
lados for maior que o terceiro;
b. Triângulo Equilátero: três lados iguais;
c. Triângulo Isósceles: quaisquer dois lados iguais;
d. Triângulo Escaleno: três lados diferentes;
@author: Marco Portela
"""
lado1 = float(input("Informe o tamanho do lado1 do triângulo: "))
lado2 = float(input("Informe o tamanho do lado2 do triângulo: "))
lado3 = float(input("Informe o tamanho do lado3 do triângulo: "))
#Verifica se é triângulo
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    #Verifica o tipo do triângulo
    if lado1 == lado2 and lado2 == lado3:
        print ("Triângulo equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
#Caso não seja triângulo
else:
    print("Não é triângulo")