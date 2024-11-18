# 27. (Contador de Palavras Frequentes) Peça ao usuário um texto longo e exiba as 5 palavras mais frequentes no texto, ignorando maiúsculas e minúsculas.
import re

texto_1 = ('Em 2016 coloquei como uma das metas do ano "Aprender a fazer um bom nhoque", mas foi só no final de 2018 que finalmente fiz um nhoque com cara e sabor de nhoque. Um prato que eu pensei "Eu pagaria por isso em um restaurante. Não pagaria muito caro, mas pagaria". E considerando meus talentos gastronômicos, pra mim isso foi uma baita conquista, que só foi possível porque eu me empenhei muito mais do que nos anos anteriores. Em um mês eu fiz mais nhoques (e tentativas de nhoques) do que a soma de todas as tentativas dos dois anos anteriores. Eu aprendi empiricamente que a repetição constante é um importante hábito para aprendermos a fazer algo que exige técnica, tal como escrever... Que é uma das minhas metas de 2019 :)')


def limpa_texto(texto_1):
    texto_limpo = re.sub(r'[^\w\s]', '', texto_1.lower())
    palavras = texto_limpo.split()
    return palavras

def contador_frequencia(palavras):
    frequencias = {}
    for palavra in palavras:
        if palavra in frequencias:
            frequencias[palavra] += 1
        else:
            frequencias[palavra] = 1
    mais_frequentes = sorted(frequencias.items(), key=lambda item: item[1], reverse=True)[:5]
    return mais_frequentes
palavras = limpa_texto(texto_1)
mais_frequentes = contador_frequencia(palavras)


for palavra, frequencia in mais_frequentes:
    print(f'{palavra} : {frequencia}')