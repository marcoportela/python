# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 17:00:46 2014
2.8 Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato.
@author: Marco Portela
"""
prod1 = float(input("Informe o preço do produto 1: ")) 
prod2 = float(input("Informe o preço do produto 2: "))
prod3 = float(input("Informe o preço do produto 3: "))
if prod1 < prod2 and prod1 < prod3:
    print("Compre o produto 1 preço = R$ %.2f" %prod1)
elif prod2 < prod1 and prod2 < prod3:
    print("Compre o produto 2 preço = R$ %.2f" %prod2)
else:
    print("Compre o produto 3 preço = R$ %.2f" %prod3)
