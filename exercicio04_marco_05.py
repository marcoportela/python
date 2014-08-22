# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 18:07:11 2014
5. Seja o mesmo texto abaixo “splitado”. Calcule quantas palavras possuem uma das letras
“python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para
minúsculas e de remover antes os caracteres especiais.
@author: portela.marco@gmail.com
"""
texto = "The Python Software Foundation and the global Python \
community welcome and encourage participation by everyone. Our community is based on \
mutual respect, tolerance, and encouragement, and we are working to help each other live up \
to these principles. We want our community to be more diverse: whoever you are, and \
whatever your background, we welcome you."
import string
#substitui pontuação por espaço
for i in string.punctuation:
    texto = texto.replace(i,' ')
texto = texto.lower()
texto = texto.split()
#separa a palavra python
letras = tuple('python')
lista = []
for palavra in texto:
    separa = []
    separa = tuple(palavra)
    for separa in letras:
        #implementar uma verificação de repetição de palavras
        if len(palavra) > 4:
            lista.append(palavra)
            #Sai para evitar repetição da mesma palavra            
            break
print('Lista de palavras que possuem uma das letras “python” e que tenham mais de 4 caracteres')
print(lista)
print('O número de palavras com mais de 4 caracteres e que possuem uma das letra python é %d' %len(lista) )