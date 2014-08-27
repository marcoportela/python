# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 16:06:34 2014
Questão D. Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo
se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, quantos números
sortudos existem entre 18644 e 33087, incluindo os extremos?
Resposta: 7995
@author: portela.marco@gmail.com
"""
cont = 0
for i in range(18644,33087):
    digito = str(i)
    if digito.find('2') != -1 and digito.find('7') == -1:
        cont += 1
print(cont)
