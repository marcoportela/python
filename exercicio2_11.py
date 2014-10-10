# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 08:09:55 2014
2.11 As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contrata para desenvolver o programa que calculará os
reajustes.
@author: Marco Portela
"""
salario_atual = float(input("Informe o salário atual: "))
tx_reajuste = float(input("Informe a porcentagem de aumento: "))
salario_novo = salario_atual + (salario_atual * (tx_reajuste / 100))
print("O salário reajustado é de R$ %.2f" %salario_novo)