# 24. (Verificação de Anagrama) Receba duas palavras e determine se elas são anagramas
# (ou seja, possuem as mesmas letras em qualquer ordem).


palavra = "teste"
dicionario = {}
palavra_02 = "teste"
dicionario_02 = {}

for letra_01 in palavra:
    if letra_01 in dicionario:
        dicionario[letra_01] += 1
    else:
        dicionario[letra_01] = 1

for letra_02 in palavra_02:
    if letra_02 in dicionario_02:
        dicionario_02[letra_02] += 1
    else:
        dicionario_02[letra_02] = 1

if dicionario == dicionario_02:
    print(f'A palavra "{palavra}" é um anagrama de "{palavra_02}"')
else:
    print('Deu ruim, não são anagramas.')