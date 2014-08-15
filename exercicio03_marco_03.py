# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 19:08:50 2014
3. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento
@author: portela.marco@gmail.com
"""
povo_A = 80000
povo_B = 200000
ano = 0
while povo_A < povo_B:
    povo_A = povo_A + povo_A * 0.03
    povo_B = povo_B + povo_B * 0.015
    ano += 1
print ('Em %d anos\nA população A será de %d habitantes\nA população B será de %d habitantes' %(ano, povo_A, povo_B))
    
    
