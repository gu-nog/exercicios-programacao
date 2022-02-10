from itertools import permutations
from random import randint


def gera_sobrenomes(complementares, qtd_sobrenomes):
    lista_base = ['Silva', 'Santos', 'Alves', 'Rodrigues', 'Souza', 'Ferreira', 'Perereira', 'Castro', 'Nogueira',
                  'Diniz']
    if len(complementares) > 0:
        lista_final = lista_base + complementares
    lista_final = lista_base
    possiveis = list(permutations(lista_final, qtd_sobrenomes))
    indice_escolhido = randint(0, len(possiveis))
    return possiveis[indice_escolhido]


sobrenomes_adicionados = []
while True:
    opção = input('Oque você quer fazer:\n[1]-Adicionar possível sobrenome\n[2]-Gerar nome\n')
    if opção == '1':
        sobrenomes_adicionados.append(input('\nSobrenome que você deseja adicionar: \n'))
    elif opção == '2':
        nome_inicial = input('\nQual o primeiro nome: \n')
        passou = False
        while passou == False:
            try:
                qtd_sobrenomes = int(input('\nQuantos sobrenomes você deseja adicionar: \n'))
                passou = True
            except:
                print('\nFavor colocar um número\n')
        sobrenomes_escolhidos = gera_sobrenomes(sobrenomes_adicionados, qtd_sobrenomes)
        print(f"\nO nome escolhido foi: {nome_inicial} ", end='')
        for sobrenome in sobrenomes_escolhidos:
            print(f'{sobrenome} ', end='')
        print('\n')
        break
    else:
        print('\nFavor digitar apenas, por exemplo: 1\n')
