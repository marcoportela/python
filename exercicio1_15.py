# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 09:45:44 2014
1.15 Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela
abaixo:
+Salário Bruto : R$
-IR (11%) : R$
-INSS (8%) : R$
-Sindicato ( 5%) : R$
=Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
@author: Marco Portela
"""
sal_hora = float(input("Informe o salario por hora: ")) 
horas_mes = float(input("Informe o número de horas trabalhadas no mês: "))
sal_bruto = sal_hora * horas_mes
ir = sal_bruto * 0.11
inss = sal_bruto * 0.08 
sindicato = sal_bruto * 0.05 
total_desc = ir + inss + sindicato 
sal_liquid = sal_bruto - total_desc
print ("Salário bruto: R$ %.2f" %sal_bruto)
print ("Imposto de renda: R$ %.2f" %ir)
print ("INSS: R$ %.2f" %inss)
print ("Sindicato: R$ %.2f" %sindicato)
print ("Salário Líquido: R$ %.2f" %sal_liquid)


