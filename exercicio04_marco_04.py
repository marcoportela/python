# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 13:54:18 2014
4. Seja o statement sobre diversidade: “The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com
split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras
“python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais
e cuidado com maiúsculas e minúsculas.
@author: portela.marco@gmail.com
"""
texto = "The Python Software Foundation and the global Python \
community welcome and encourage participation by everyone. Our community is based on \
mutual respect, tolerance, and encouragement, and we are working to help each other live up \
to these principles. We want our community to be more diverse: whoever you are, and \
whatever your background, we welcome you."
import string
for caracter in string.punctuation:
    texto = texto.replace(caracter, ' ')
texto = texto.lower()
texto = texto.split()
print('Lista de palavras deste texto')
print(texto)
lista = []
#lista com as letras da palavra python
letra = tuple('python')
for palavra in texto:
    if palavra.startswith(letra) or palavra.endswith(letra):
        lista.append(palavra)
print('Lista com as palavras que começam ou terminam com uma das letras python')
print(lista)    
