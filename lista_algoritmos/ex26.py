# 26. (Mesclagem de Dois Dicionários) Dado dois dicionários, mescle-os em um terceiro.
# Caso eles tenham chaves em comum, some os valores das chaves correspondentes.
import copy

dic_01 = {
    '1' : 'banana'
    } 
dic_02 = {
    '1' : 'maça'
    } 
def verificacao(dic_01, dic_02):
    dicio_03 = dic_01.copy()
    for chave, valor in dic_02.items():
        if chave in dicio_03:
            dicio_03[chave] += ' ' + valor
        else:
            dicio_03[chave] = valor
    return dicio_03


teste = verificacao(dic_01, dic_02)

print(teste)