# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 18:41:09 2014
6. Crie uma função em que, dados 3 números como parâmetros, permita verificar se a
soma de quaisquer par de números gera a soma do terceiro número.
@author: portela.marco@gmail.com
"""
def somaTer(a,b,c):
    if a + b == c:
        print ('%d + %d = %d' %(a,b,c))
    elif b + c == a:
        print ('%d + %d = %d' %(b,c,a))
    elif c + a == b:
        print ('%d + %d = %d' %(c,a,b))
    else:
        print('Não há combinação possível')
        
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
somaTer(n1,n2,n3)
