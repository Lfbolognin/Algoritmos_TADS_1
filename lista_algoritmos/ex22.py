# 22. (Contagem de Vogais e Consoantes) Peça ao usuário uma frase e conte o número de
# vogais e consoantes. Ignore espaços e caracteres especiais.


def verificacao(frase):
    vogais = ['a', 'e', 'i', 'o', 'u']
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    cont_vogais = 0
    cont_consoantes = 0
    frase = frase.lower()
    for char in frase:
        if char in vogais:
            cont_vogais += 1
        elif char in consoantes:
            cont_consoantes += 1
    return cont_vogais, cont_consoantes


frase_user = input('Digite a sua frase: ')
vogais, consoantes = verificacao(frase_user)



print(f'Sua frase tem {vogais} vogais')
print(f'Sua frase tem {consoantes} consoantes')