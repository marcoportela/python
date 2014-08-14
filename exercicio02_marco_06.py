# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 12:01:30 2014
6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$
@author: portela.marco@gmail.com
"""
salHora = float(input('Informe o salário por hora: '))
numHorasMes = int(input('Informe a quantidade de horas trabalhadas no mês: '))
IR = 0.11
INSS = 0.08
SIND = 0.05
salBruto = salHora * numHorasMes
valorIr = salBruto * IR
valorInss = salBruto * INSS
valorSind = salBruto * SIND
salLiquido = salBruto - valorIr - valorInss - valorSind
print ('O salário bruto é R$ %3.2f' %salBruto)
print ('O valor pago ao INSS é R$ %3.2f' %valorInss)
print ('O valor pago ao Sindicato é R$ %3.2f' %valorSind)
print ('O salário líquido é R$ %3.2f' %salLiquido)
