# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 20:03:29 2014
3. Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um
terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados dos dois outros vetores. Imprima os três vetores.
@author: portela.marco@gmail.com
"""
import random
vetor1 = []
vetor2 = []
vetor3 = []
for i in range(10):
    vetor1.append(random.randint(1,100))
    vetor2.append(random.randint(1,100))
for j in range(10):
    vetor3.append(vetor1[j])
    vetor3.append(vetor2[j])
print('Vetor1')
print(vetor1)
print('Vetor2')
print(vetor2)
print('Vetor3')
print(vetor3)