# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 20:19:26 2014
6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
esperada para a viagem.
@author: Marco - data
"""
distancia = float(input('Informe a distância a percorrer(Km): '))
velocidade = float(input('Digite a velocidade do veículo(Km/h): '))
tempo = distancia / velocidade
print('O tempo esperado da viagem é de %2.2f horas' %tempo)