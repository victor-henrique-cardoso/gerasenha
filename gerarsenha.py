# -- coding: utf-8 --

#4. Gerador de Senhas
#Crie um programa que gere senhas aleatórias com um número

import random
import string

def gerar_senha(tamanho=12):
    numeros = string.digits        
    todos_os_caracteres = numeros
    senha = random.choices(todos_os_caracteres, k=tamanho)
    return ''.join(senha)

senha_gerada = gerar_senha(12)

print("Senha gerada:",senha_gerada)
