# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 16:38:40 2014
2.22 Faça um Programa para leitura de três notas parciais de um aluno. O programa
deve calcular a média alcançada por aluno e presentar:
a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a
respectiva média alcançada;
b. A mensagem "Reprovado", se a média for menor do que 7, com a
respectiva média alcançada;
c. A mensagem "Aprovado com Distinção", se a média for igual a 10.
@author: Marco Portela
"""
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
if media == 10:
    print("Média = %2.2f = Aprovado com Distinção" %media)    
elif media >= 7:
    print("Média = %2.2f = Aprovado" %media)
elif media <= 7:
    print("Média = %2.2f = Reprovado" %media)
