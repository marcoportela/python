# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 07:45:15 2014
1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Propriedade: o comprimento de cada lado de um triângulo é menor do que a soma dos comprimentos dos outros
dois lados.

Triângulo Equilátero: aquele que tem os comprimentos dos três lados iguais;

Triângulo Isóscele: aquele que tem os comprimentos de dois lados iguais. Portanto, todo triângulo equilátero é
também isóscele.

Triângulo Escaleno: aquele que tem os comprimentos de seus três lados diferentes.

@author:Marco - data - portela.marco@gmail.com
"""
lado1 = int(input('Digite o tamanho do lado 1: '))
lado2 = int(input('Digite o tamanho do lado 2: '))
lado3 = int(input('Digite o tamanho do lado 3: '))
if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
    print ('É um triangulo')
    if lado1 == lado2 and lado2 == lado3:
        print('Equilátero')
    elif lado1==lado2 or lado2 == lado3 or lado3 == lado1:
        print('Isóscele')
    else:
        print ('Escaleno')
else:
    print('Não é um triângulo')