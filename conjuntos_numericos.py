# um código com geradores para alguns conjuntos matemáticos e para alguns subconjuntos também, que sejam infinitos apenas para um dos lados (positivo ou negativo)

def count(start=0, step=1, exclude=None):
    if exclude == None:
        _exclude = []
    else:
        _exclude = exclude
    _step = step
    _c = start
    while True:
        if _c not in _exclude:
            yield _c
        _c += _step


naturais = count(start=0, step=1)
naturais_nao_nulos = count(start=0, step=1, exclude=[0])
inteiros_nao_negativos = count(start=0, step=1)
inteiros_positivos = count(start=0, step=1, exclude=[0])
inteiros_nao_positivos = count(start=0, step=-1)
inteiros_negativos = count(start=0, step=-1, exclude=[0])

if __name__ == '__main__':
    todos_conjuntos = [(naturais, 'dos naturais(N)'), (naturais_nao_nulos, 'dos naturais não nulos(N*)'),
                       (inteiros_nao_negativos, 'dos inteiros não negativos(Z+)'),
                       (inteiros_positivos, 'dos inteiros positivos(Z+*)'),
                       (inteiros_nao_positivos, 'dos inteiros não positivos(Z_)'),
                       (inteiros_negativos, 'dos inteiros negativos(Z_*)')]
    for c in todos_conjuntos:
        print(f'Primeiros números do conjunto {c[1]}:')
        for num in c[0]:
            if num <= 10 and num >= -10:
                print(num)
            else:
                print('\n')
                break
