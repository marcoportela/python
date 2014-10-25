# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 18:02:47 2014
2.18 Faça um programa que calcule as raízes de uma equação do segundo grau, na
forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as
consistências, informando ao usuário nas seguintes situações:
a. Se o usuário informar o valor de A igual a zero, a equação não é
do segundo grau e o programa não deve fazer pedir os demais valores,
sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raizes
reais. Informe ao usuário e encerre o programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma
raiz real; informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raiz reais;
informe-as ao usuário;
@author: Marco Portela
"""
import math
a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
c = int(input("Informe o valos de c: "))
delta = (b**2) - 4*a*c
raiz = math.sqrt(delta) 
if delta > 0:
    x1 = (-b+raiz)/(2*a)
    x2 = (-b-raiz)/(2*a)
    print("As raizes calculadas são: x1= %f e x2= %f" %(x1,x2))
elif delta == 0:
    x1,x2 = (-b+math.sqrt(delta))/2*a
    print("Delta = 0 a raiz encontrada é %f" %x1)
# delta menor que 0
else:
    print("Delta < 0, portanto não há raiz")