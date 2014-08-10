# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 15:38:05 2014
3) Escreva um programa que leia a quantidade de dias, horas, 
minutos e segundos do usuário. Calcule o total em segundos.
@author: Marco data
"""
from datetime import datetime
hoje = datetime.today()
print ("Hoje é dia:")
print("%s/%s/%s" %(hoje.day , hoje.month , hoje.year))
print("Horário:")
print("%s:%s:%s" %(hoje.hour, hoje.minute, hoje.second))
ano=int(input("Digite o ano do nascimento: "))
mes=int(input("Digite o mês do nascimento: "))
dia=int(input("Digite o dia do nascimento: "))
horanasc=int(input("Digite a hora do nascimento (obs.Só a hora): "))
minunasc=int(input("Digite o minuto do nascimento: "))
totalano = int(hoje.year) - ano
totalmes = int(hoje.month) - mes
#caso resultado do mês seja negativo
if totalmes <= -1:
    totalmes = totalmes * -1
totaldia = int(hoje.day) - dia
totalhora = int(hoje.hour) - horanasc
totalminu = int(hoje.minute) - minunasc
totalsegundos=int(hoje.second) + (totalminu * 60) + (totalhora * 3600) + (totaldia * 86400) + (totalmes * 2592000) + (totalano * 31104000) 
print ("Anos = %d , Meses = %d , Dias = %d" %(totalano, totalmes, totaldia))
print ("Foi calculado %d segundos vividos" %totalsegundos)