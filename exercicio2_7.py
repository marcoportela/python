# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 13:38:39 2014
2.7 Faça um Programa que leia três números e mostre o maior e o menor deles.
@author: Marco Portela
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if num1 <= num2 and num3 >= num2:
    print("%d é o maior" %num3)
    print("%d é o menor" %num1)
elif num1 <= num3 and num2 >= num3:
    print("%d é o maior" %num2)
    print("%d é o menor" %num1)
elif num1 <= num3 and num3 >= num1:
    print("%d é o maior" %num3)
    print("%d é o menor" %num2)
elif num1 <= num2 and num2 >= num3:
    print("%d é o maior" %num2)
    print("%d é o menor" %num3)
elif num2 <= num1 and num3 >= num2:
    print("%d é o maior" %num1)
    print("%d é o menor" %num2)
else:
    print("%d é o maior" %num1)
    print("%d é o menor" %num3)