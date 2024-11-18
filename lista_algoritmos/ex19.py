# 19. (Contador de Caracteres de uma Frase) Receba uma frase e retorne um dicionário
# que contém a quantidade de cada caractere (inclusive espaços).

contador_de_letra = {}

def fun_verifica_frase():
    for letra in frase:
        if letra in contador_de_letra:
            contador_de_letra[letra] += 1
        else:
            contador_de_letra[letra] = 1
    return contador_de_letra

frase = input('Digite uma frase: ')

var_Contadora_carac = fun_verifica_frase()

print(f'As seguintes letras se repetem:\n{var_Contadora_carac}')
