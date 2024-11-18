# 14. (Verificador de Palíndromos) Receba uma palavra e determine se ela é um palíndromo
# (ou seja, se lê igual de trás para frente).


word_Input = input('Digite sua palavra: ')
word_List = word_Input[::-1]
print(word_List)

if word_Input == word_List:
    print(f'Sua palavra foi {word_Input}, o palindromo dela é {word_List}, portanto ela é um palindromo')
else:
    print(f'Sua palavra foi {word_Input}, o palindromo dela é {word_List}, portanto ela não é um palindromo')


