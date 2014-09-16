# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 12:45:34 2014
1.14 João Papo-de-Pescador, homem de bem, comprou um microcomputador para
controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de
peixes maior que o estabelecido pelo regulamento de pesca do estado de São
Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João
precisa que você faça um programa que leia a variável peso (peso de peixes) e
verifique se há excesso. Se houver, gravar na variável excesso e na variável multa
o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com
o conteúdo ZERO.
@author: Marco Portela
"""
excesso = 0
multa = 0
REGULAMENTO = 50
REG_MULTA = 4.00
peso = float(input("Digite o peso do pescado: "))
if peso > REGULAMENTO:
    excesso = peso - REGULAMENTO
    multa = excesso * REG_MULTA
    print("Excesso pescado = %3.2f\nO valor da multa é de R$ %3.2f " %(excesso,multa))
else:
    print("Peso do pescado dentro do Regulamento.\nExcesso = %2.2f\nMulta = R$ %2.2f" %(excesso,multa))
