# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 19:45:02 2014
2.23 Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
usuário a valor do saque e depois informar quantas notas de cada valor serão
fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor
mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar
com a quantidade de notas existentes na máquina.
a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece
duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas 
de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
@author: Marco Portela
"""
saque = int(input("Informe o valor do saque: R$ "))
stringSaque = str(saque)
tamanhoSaque = len(stringSaque)
quantidade = ['nenhuma nota','uma nota','duas notas','três notas','quatro notas','cinco notas','seis notas', 'sete notas', 'oito notas', 'nove notas']

if saque < 10 or saque > 600:
    print("O valor do saque deve ser maior que R$10,00 e menor que R$600,00")
elif tamanhoSaque == 3:
    unidade = quantidade[int(stringSaque[2])]
    dezena = quantidade[int(stringSaque[1])]
    centena = quantidade[int(stringSaque[0])]
    
    #Verifica notas de 50
    
    if int(stringSaque[1])/5 >= 1:
        nota50 = quantidade[int(stringSaque[1])/5]
        dezena = quantidade[int(stringSaque[1])%5]    
    #Verifica notas de 5
    
    if int(stringSaque[2])/5 >= 1:
        nota5 = quantidade[int(stringSaque[2])/5]
        unidade = quantidade[int(stringSaque[2])%5]

    print("Para sacar a quantia de R$ %d,00 reais, o programa fornece %s de 100, %s de R$50,00, %s de R$10,00, %s de R$5,00 e %s de R$1,00 " %(saque,centena,nota50,dezena,nota5,unidade))
elif tamanhoSaque == 2:
    unidade = quantidade[int(stringSaque[1])]
    dezena = quantidade[int(stringSaque[0])]
    
    #Verifica notas de 50
    
    if int(stringSaque[0])/5 >= 1:
        nota50 = quantidade[int(stringSaque[0])/5]
        dezena = quantidade[int(stringSaque[0])%5]    

    #Verifica notas de 5

    if int(stringSaque[1])/5 >= 1:
        nota5 = quantidade[int(stringSaque[1])/5]
        unidade = quantidade[int(stringSaque[1])%5]
 
    print("Para sacar a quantia de R$ %d,00 reais, o programa fornece %s de R$50,00, %s de R$10,00, %s de R$5,00 e %s de R$1,00 " %(saque,nota50,dezena,nota5,unidade))
