# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 15:11:28 2014
3. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de
seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do
estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você
faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na
variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais
variáveis com o conteúdo ZERO.
@author: Marco - data - portela.marco@gmail.com
"""
#peso de peixes
peso = float(input('Informe o peso total dos peixes: '))
#regulamento de São Paulo 50 Kilos
REGULAMENTO = 50.0
#multa de R$ 4,00 por quilo excedente
MULTAPORKILO = 4.00
if peso > REGULAMENTO:
    excesso = peso - REGULAMENTO
    multa = MULTAPORKILO * excesso
    print('O exesso foi de %3.2fKg e o valor da multa é de R$%3.2f' %(excesso,multa))
else:
    excesso = 0
    multa = 0
    print('Peso dentro do permitido, não há multa.')