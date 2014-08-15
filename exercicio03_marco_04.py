# -*- coding: utf-8 -*-
"""
Created on Fri Aug 15 15:13:47 2014
4. A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
de Fibonacci. F 1 = 1, F 2 = 1, F 3 = 2, etc.
@author: portela.marco@gmail.com 
"""
numero = int(input('Digite um número: '))
x, y, fib = 0, 1, 1
while y <= numero:
    x, y = y, x + y    
    fib = fib + 1
    print (x)