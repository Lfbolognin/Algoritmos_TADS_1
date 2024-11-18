# 17. (Ordenação de Lista com Números Negativos e Positivos) Dada uma lista de números inteiros que incluem positivos e negativos,
# ordene-os de forma que os negativos fiquem
# antes dos positivos, mantendo a ordem original relativa entre eles.


lista = [12, -45, 67, -89, 23, -5, 45, -12, 78, -34, 56, -9, 10, -3, 90, -77, 33, -22, 50, -60, 7, -14, 27, -19, 83, -92, 15, -8, 61, -30]
lista_positiva = []
lista_negativa = []

def distribuicao():
    for numero in lista:
        if numero > 0:
            lista_positiva.append(numero)
        else:
            lista_negativa.append(numero)

distribuicao()

print(f'Lista positiva:', lista_positiva)
print(f'Lista negativa:', lista_negativa)


