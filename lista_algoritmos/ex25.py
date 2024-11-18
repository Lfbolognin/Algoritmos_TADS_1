# 25. (Filtro de Números Pares em uma Lista) Receba uma lista de inteiros e filtre apenas
# os números pares.


def verificacao(lista_base):
    lista_limpa = []
    for num in lista_base:
        if num % 2 == 0:
            lista_limpa.append(num)
    return lista_limpa

lista_base = [1, 2, 3, 4, 5, 6, 7, 8]

listra_pronta = verificacao(lista_base)

print(lista_base)
print(listra_pronta)