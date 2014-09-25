# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 20:42:25 2014
2.4 Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
@author: Marco Portela
"""
letra = raw_input("Digite uma letra: ")
if letra not in ("aeiouAEIOU"):
    print("Consoante")
else:
    print("vogal")
