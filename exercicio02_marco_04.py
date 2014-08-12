# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 16:06:14 2014
4. Faça um Programa que leia três números e mostre o maior deles.
@author: Marco - portela.marco@gmail.com
"""
num1 = int(input('Digite um número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
if num1 > num2 and num1 > num3:
    print('O %d é o maior' %num1)
elif num2 > num1 and num2 > num3:
    print ('O %d é o maior' %num2)
else:
    print ('O %d é o maior' %num3)

