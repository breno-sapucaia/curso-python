#!python

def tag_bloco(conteudo, *args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}"> \n{html}</{tag}>'

def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li> \n' for item in itens)
    return f'<ul>\n{lista}</ul>'

if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('item 1','item 2', 'item 3'), classe='info'))