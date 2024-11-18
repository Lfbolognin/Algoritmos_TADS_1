#7. (Inversor de String) Receba uma palavra e exiba-a invertida (exemplo: "Python-> "nohtyP").

teste = input('fale uma palavra:' )


controle = teste
while controle >= teste:
    print(teste[-1::])
else:
    print('fim')

    #7

# word_Input = input('Digite sua palavra: ')


# word_List = [word_Input]

# print(f' Vc digitou {word_List}, o inverso da sua palavra é word_Input[::-1]')