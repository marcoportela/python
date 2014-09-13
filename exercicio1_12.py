# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 13:08:39 2014
1.12 Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
@author: Marco Portela
"""
altura = float(input("Digite a altura: "))
peso = (72.7 * altura) - 58
print ("O peso ideal é %2.2f" %peso)
