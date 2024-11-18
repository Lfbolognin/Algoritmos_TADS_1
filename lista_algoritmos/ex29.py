# 29. (Remoção de Elementos Duplicados de uma Lista Aninhada) Receba uma lista de
# listas (uma lista aninhada) com valores duplicados e crie uma nova lista de listas onde cada
# sublista contenha apenas valores únicos.


def remover_duplicados(lista_aninhada):
    lista_vazia = []
    for lista_secundaria in lista_aninhada:
        lista_vazia.append(set(lista_secundaria))
    return lista_vazia

lista_aninhada = [
    [9, 2, 2],          # Sublista 1
    [9, 5, 1],          # Sublista 2
    [9, 5, 1]           # Sublista 3
]



lista_secundaria = remover_duplicados(lista_aninhada)

print(lista_secundaria)