# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 16:43:19 2014
1.13 Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um
algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
a. Para homens: (72.7*h) - 58
b. Para mulheres: (62.1*h) - 44.7 (h = altura)
c. Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
@author: Marco Portela
"""
#Função para calcular o peso
def calcPeso(getPeso,getGenero):
    if getPeso <= getGenero:
        return("Parabéns, está dentro do peso ideal que é %2.2f" %getGenero)
    else:
        return("Infelizmente está acima do peso ideal que é %2.2f" %getGenero)
#Inserção dos dados: sexo, altura e peso    
altura = float(input("Informe a altura: "))
#Python 2.7 por isso foi usado raw_input
sexo = raw_input("Digite 'h' para homem ou 'm' para mulher: ")
peso = float(input("Informe o peso: ")) 
#Verificação do sexo e calculo do peso
if sexo == 'h':
    homem = (72.7 * altura) -58
    print(calcPeso(peso,homem))
elif sexo == 'm':
    mulher = (62.1 * altura) - 44.7
    print(calcPeso(peso,mulher))
else:
    print("Sexo indefinido")

