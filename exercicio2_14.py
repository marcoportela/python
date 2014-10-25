# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 07:15:12 2014
2.14 Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
@author: Marco Portela
"""
semana = {1:"Domingo", 2:"Segunda", 3:"Terça", 4:"Quarta", 5:"Quinta", 6:"Sexta", 7:"Sábado"}
dia = int(input("Informe um número correnpondente a um dia da semana: "))
if dia in range(1,7):
    print("Dia = %s" %semana[dia])
else:
    print("Valor inválido")    
    