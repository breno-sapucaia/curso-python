PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}

textos = [
    'João gosta de futebol e política',
    'A praia foi divertido'
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('O texto possui palavra proibidas:', intersecao)
    else:
        print('O texto ta limpo: ', texto)
