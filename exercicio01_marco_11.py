# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 19:40:39 2014
11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado
a um milhão.
@author: Marco - portela
"""
numero = 2**1000000
palavra = str(numero)
contagem = len(palavra)
print("2 elevado a um milhão possui %d dígitos." %contagem)
