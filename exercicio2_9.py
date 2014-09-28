# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 18:13:08 2014
2.9 Faça um Programa que leia três números e mostre-os em ordem decrescente.
@author: Marco Portela
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if num1 < num2 and num2 < num3:
    print("Ordem decrescente: %d - %d - %d" %(num3, num2, num1))
elif num2 < num1 and num1 < num3:
    print("Ordem decrescente: %d - %d - %d" %(num3, num1, num2))
elif num3 < num1 and num1 < num2:
    print("Ordem decrescente: %d - %d - %d" %(num2, num1, num3))
elif num1 < num3 and num3 < num2:    
    print("Ordem decrescente: %d - %d - %d" %(num2, num3, num1))
elif num3 < num2 and num2 < num1:    
    print("Ordem decrescente: %d - %d - %d" %(num1, num2, num3))
else:    
    print("Ordem decrescente: %d - %d - %d" %(num1, num3, num2))