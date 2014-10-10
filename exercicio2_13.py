# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 12:48:59 2014
2.13 Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto (conforme
tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido
corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao
usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
* Salário Bruto até 900 (inclusive) - isento
* Salário Bruto até 1500 (inclusive) - desconto de 5%
* Salário Bruto até 2500 (inclusive) - desconto de 10%
* Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

Salário Bruto: (5 * 220) : R$ 1100,00 
(-) IR (5%) : R$ 55,00
(-) INSS ( 10%) : R$ 110,00
FGTS (11%) : R$ 121,00
Total de descontos : R$ 165,00
Salário Liquido : R$ 935,00

@author: Marco Portela
"""
valor_h = float(input("Informe o valor da hora de trabalho: ")) 
quant_h = float(input("Informe a quantidade de horas trabalhadas no mês: "))
salB = valor_h * quant_h
if salB <= 900:
    ir = 0
elif salB > 900 and salB <= 1500:
    ir = salB * 0.05
elif salB >1500 and salB <= 2500:
    ir = salB * 0.10
elif salB > 2500:
    ir = salB * 0.20
inss = salB * 0.10
fgts = salB * 0.11
total_Desc = ir + inss + fgts
salLiq = salB - total_Desc
print("Salário bruto: R$ %.2f" %salB)
print("IR: R$ %.2f" %ir)
print("INSS: R$ %.2f" %inss)
print("FGTS: R$ %.2f" %fgts)
print("Total de descontos: R$ %.2f" %total_Desc)
print("Salário Líquido: R$ %.2f" %salLiq)