# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 08:24:09 2014
4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
porcentagem do aumento. Exiba o valor do aumento e do novo salário.
@author: Marco - data
"""
salarioAtual = 1000.00
aumentoPorCem = float(input("Digite a porcentagem de aumento: "))
aumento = salarioAtual * (aumentoPorCem/100) 
novoSal= salarioAtual + aumento
print("O salário inicial era de R$ %2.2f " %salarioAtual)
print("O aumento foi de R$ %2.2f " %aumento)
print("O novo salário é agora R$ %2.2f" %novoSal)