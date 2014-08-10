# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 09:05:53 2014
9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
@author: Marco - data
"""
percorrido = float(input('Informe a quantidade de Km percorrido: '))
diasUso = int(input('Informe a quantidade de dias de aluguel: '))
preco = (percorrido * 0.15) + (diasUso * 60)
print ('O preço total do aluguel é R$ %3.2f ' %preco)
