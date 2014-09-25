# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 12:35:52 2014
2.1 Faça um Programa que peça dois números e imprima o maior deles.
@author: Marco Portela
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    print("O %d é o maior" %num1)
elif num2 > num1:
    print("O %d é o maior" %num2)
else:
    print("Os número são iguais")
