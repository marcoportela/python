# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 20:49:50 2014
1.7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro
desta área para o usuário.
@author: Marco Portela
"""
lado = float(input("Digite o tamanho da parede do quadrado: "))
area = lado ** 2
print ("O dobro da área do quadrado é %2.2f" %(area * 2))