# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 15:55:52 2014
1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido.
@author: portela.marco@gmail.com
"""
while True:
    nota = int(input('Digite uma nota entre zero e dez: '))
    if nota in range(0,11):
        print('Valor válido')
        break
    else:
        print('Valor inválido')
