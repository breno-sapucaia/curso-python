#!python


def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')
        
    return ' '.join(f'<{tag} {k}={v}> {"".join(args)} </{tag}>' for k, v in kwargs.items() )



if __name__ == "__main__":
    print(
        tag('p',
            tag('span', 'Curso de Python 3, por '),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('span', 'e'),
            tag('strong', 'Leonardo Leitão', id='ll'),
            tag('span', '.'),
            html_class='alert')
            
    )