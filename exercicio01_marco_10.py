# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 17:22:31 2014
10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
total de dias.
@author: Marco - portela
"""
porDia = int(input('Informe a quantidade de cigarros fumados por dia: '))
porAno = int(input('Informe quantos anos usa cigarro: '))
# cada cigarro equivale a perda de 0.00694444 dia, pois um dia tem 1440 minutos 
diasPerdidos = (0.006944444 * porDia) * porAno
print('Este fumante perdeu %2.2f dias de vida' %diasPerdidos )
