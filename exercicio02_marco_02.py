# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 07:03:48 2014
2. Determine se um ano é bissexto. Verifique no Google como fazer isso...
Google:um ano é bissexto, isto é tem 366 dias se for divisivel por 4. existem no entanto exceções:
se for divisivel por 100 então não é bissexto,
mas se tambem esta exceção tem uma exceção: se forem tambem divisiveis por 400 são bissextos.
@author: Marco - data - portela.marco@gmail.com
"""
ano = int(input('Digite algum ano com 4 dígitos:'))
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('Ano %d é bissexto' %ano)
else:
    print('Ano %d não é bissexto' %ano)
    
    
