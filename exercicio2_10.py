# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 00:20:17 2014
2.10 Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-
matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!",
"Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
@author: Marco Portela
"""
turno = raw_input("Digite M -matutino ou V - Vespertino ou N - Noturno: ")
if turno == 'm' or turno == 'M':
    print("Bom Dia!")
elif turno == 'v' or turno == 'V':
    print("Boa Tarde!")
elif turno == 'n' or turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")