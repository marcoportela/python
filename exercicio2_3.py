# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 19:17:03 2014
2.3 Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a
letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
@author: Marco Portela
"""
letra = raw_input("Digite M para Masculino ou F para Feminino: ")
if letra == 'F' or letra == 'f':
    print("Feminino")
elif letra == 'M' or letra == 'm':
    print("Masculino")
else:
    print("Sexo inválido")
