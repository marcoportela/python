# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 15:23:32 2014
2.20 Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a
mesma é uma data válida.
@author: Marco Portela
"""
data = raw_input("Digite uma data no formato dd/mm/aaaa: ")
#Verifica o formato da string pelo tamanho 
if len(data) < 10:
    print("Data inválida")
    #Verifica a utilização de separadores    
elif data[2] != '/' or data[5] != '/':
    print("Data inválida, digite / para separar o dia/mês/ano" )
else:
    #Separa a string em dia  mês e ano
    dia, mes, ano = data.split('/')
    #Verifica dia      
    if int(dia) >= 1 and int(dia) <= 31:
        print ("Dia válido")
    else:
        print("Dia inválido, redigite no formato dd/mm/aaaa")
    #Verifica mês
    if int(mes) >= 1 and int(mes) <= 12:
        print("Mês válido")
    else:
        print("Mês inválido, redigite no formato dd/mm/aaaa")