# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 16:28:05 2014
2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
@author: portela.marco@gmail.com
"""
while True:
    usuario = raw_input('Digite o nome do usuário: ')
    senha = raw_input('Digite uma senha: ')
    if usuario == senha:
        print('A senha não pode ser igual ao nome do usuário. \nTente novamente')
    else:
        print('Senha cadastrada com sucesso')
        break
