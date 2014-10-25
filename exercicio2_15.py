# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 14:38:41 2014
2.15 Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média. A atribuição de
conceitos obedece à tabela abaixo:
Média de Aproveitamento Conceito
Entre 9.0 e 10.0        A
Entre 7.5 e 9.0         B
Entre 6.0 e 7.5         C
Entre 4.0 e 6.0         D
Entre 4.0 e zero        E
@author: Marco Portela
"""
conceito = ''
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 9 and media <= 10:
    conceito = 'A'
    print("Média= %.2f ==> Conceito = %s" %(media, conceito))
elif media >= 7.5 and media <= 9:
    conceito = 'B'
    print("Média= %.2f ==> Conceito = %s" %(media, conceito))
elif media >= 6 and media <=7.5:
    conceito = 'C'
    print("Média= %.2f ==> Conceito = %s" %(media, conceito))
elif media >=4 and media <= 6:
    conceito = 'D'
    print("Média= %.2f ==> Conceito = %s" %(media, conceito))
else:
    conceito = 'E'
    print("Média= %.2f ==> Conceito = %s" %(media, conceito))