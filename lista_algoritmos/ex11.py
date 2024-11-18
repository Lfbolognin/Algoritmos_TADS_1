# 11. (Contador de Palavras Únicas) Peça ao usuário uma frase e, em seguida, conte quantas
# palavras únicas ela possui (sem considerar maiúsculas e minúsculas).


def contador_palavras_unicas():
    frase = input("Digite uma frase: ") #INPUT
    
    palavras = frase.lower().split() #LOWER = JOGA PRO MINUSCULO E SPLIT DIVIDE A FRASE EM LISTAS
    
    palavras_unicas = set(palavras) # 
    
    # Conta a quantidade de palavras únicas
    quantidade = len(palavras_unicas)
    
    # Exibe o resultado
    print(f"A frase contém {quantidade} palavras únicas.")

# Chamada da função
contador_palavras_unicas()