# 21. (Remoção de Elementos Duplicados) Receba uma lista de inteiros e retorne uma nova
# lista sem elementos duplicados, mantendo a ordem original.

def remocao(list_Int):
    lista_vazia = []
    for numero in list_Int:
        if numero not in lista_vazia:
            lista_vazia.append(numero)
    return lista_vazia

list_Int = [80, 80, 80, 77, 57, 80, 31, 37, 80, 19, 95, 80, 80, 97, 80]
lista_final = remocao(list_Int)


print("Lista original:", list_Int)
print("Lista sem duplicados:", lista_final)

# sem_dupl = set(list_Int)
# print(sem_dupl)