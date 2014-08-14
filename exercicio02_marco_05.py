# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 20:30:07 2014
5. Faça um Programa que leia três números e mostre o maior e o menor deles.
@author: portela.marco@gmail.com
"""
print('DIGITE NÚMEROS INTEIROS DIFERENTES')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
# 1 - 2 - 3
if num1 < num2 and num2 < num3:
    print ('Número %d é o menor e o %d é o maior' %(num1, num3))
#2 - 1 - 3
elif num2 < num1 and num1 < num3:
    print ('Número %d é o menor e o %d é o maior' %(num2, num3))
#3 - 2 - 1
elif num2 < num1 and num3 < num2:
    print ('Número %d é o menor e o %d é o maior' %(num3, num1))
#1 - 3 - 2
elif num1 < num3 and num3 < num2:
    print ('Número %d é o menor e o %d é o maior' %(num1, num2))
#2 - 3 - 1
elif num1 < num2 and num3 < num1:
    print ('Número %d é o menor e o %d é o maior' %(num3, num2))
#3 - 1 - 2
else:
    print ('Número %d é o menor e o %d é o maior' %(num2, num1))
