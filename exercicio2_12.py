# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 16:40:55 2014
2.12 Faça um programa que recebe o salário de um colaborador e o reajuste segundo
o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5%

Após o aumento ser realizado, informe na tela:
a.o salário antes do reajuste;
b.o percentual de aumento aplicado;
c.o valor do aumento;
d.o novo salário, após o aumento.
@author: Marco Portela
"""
#Função que calcula o aumento
def calc_Sal(sal,taxa):
    print("Salário inicial = R$ %.2f" %salario)    
    print("O percentual aplicado é de %.2f por cento " %taxa )    
    aumento = salario * taxa
    print ("O valor do aumento é de R$ %.2f" %aumento)
    novoSal = salario + aumento
    print ("O novo salário após o aumento é de R$ %.2f" %novoSal)
#Inicio do programa
salario = float(input("Informe o salário do colaborador: R$ "))
if salario <= 280:
    calc_Sal(salario,0.20)
elif salario >= 280 and salario <= 700:
    calc_Sal(salario,0.15)
elif salario >= 700 and salario <= 1500:
    calc_Sal(salario,0.10)
else:
    calc_Sal(salario,0.05)