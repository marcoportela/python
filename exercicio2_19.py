# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 17:31:54 2014
2.19 Faça um Programa que peça um número correspondente a um determinado ano e
em seguida informe se este ano é ou não bissexto.
Feitas as correções de calendário definiu-se a nova regra para o cálculo dos anos bissextos:

De 4 em 4 anos é ano bissexto.
De 100 em 100 anos não é ano bissexto.
De 400 em 400 anos é ano bissexto.
Prevalecem as últimas regras sobre as primeiras
fonte:Wikipedia
@author: Marco Portela
"""
ano = int(input("Informe um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print ("O ano é bissexto")
else:
    print ("O ano não é bissexto")