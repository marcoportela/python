# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 20:05:11 2014
5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
preço a pagar.
@author:Marco - data
"""
preco = float(input('Informe o preço da mercadoria: '))
desconto = float(input('Informe o percentual do desconto: '))
pagar = preco - (preco * (desconto/100))
print('O valor a pagar é R$ %2.2f ' %pagar)
