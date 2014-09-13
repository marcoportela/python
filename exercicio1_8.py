# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 20:41:18 2014
1.8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
@author: Marco Portela
"""
salHora = float(input("Digite o valor ganho por hora: "))
trabMes = int(input("Digite o número de horas trabalhadas no mês: "))
salTotal = salHora * trabMes
print("O salário ganho neste mês foi de R$ %3.2f" %salTotal)

