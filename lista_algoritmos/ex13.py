# # 13 - (Média com Notas Maiores que a Média) Peça uma lista de notas de alunos e calcule
# # a média. Em seguida, retorne uma lista com as notas que são maiores do que a média.

def input_Numbers ():
    number_1 = int(input('Digite a 1ª nota: '))
    number_2 = int(input('Digite a 2ª nota: '))
    number_3 = int(input('Digite a 3ª nota: '))
    number_4 = int(input('Digite a 4ª nota: '))
    number_5 = int(input('Digite a 5ª nota: '))
    list_Numbers = [number_1, number_2, number_3, number_4, number_5]
    return list_Numbers

def calc_Grade(list_Numbers):
    total = sum(list_Numbers)
    media = total / len(list_Numbers)
    return media

notas = input_Numbers()
result = calc_Grade(notas)

print(result)

# grade_1 = float(input('Digite sua 1 nota: '))
# grade_2 = float(input('Digite sua 1 nota: '))
# grade_3 = float(input('Digite sua 1 nota: '))

# media = (grade_1 + grade_2 + grade_3) / 3

# if media >= 7:
#     print(f'Parabens vc tirou mais que a media nescessaria, sua media foi {media}')
# else:
#     print(f'Que pena vc tirou menos que a media, vc tirou {media}')

# print(media)
