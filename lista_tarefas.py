# Criar uma lista de tarefas que possa:
"""
-adicionar tarefa
-listar tarefa
-desfazer última ação
-refazer última ação
"""

def listagem_tarefas(tarefas):
    print('\n===== listagem de tarefas =====')
    for c, tarefa in enumerate(tarefas):
        print(f'tarefa {c} - {tarefa}')
    if len(tarefas) == 0:
        print('Nenhuma tarefa!!')
    print('\n\n')


def undo_tarefas():
    try:
        tarefa_removida = tarefas.pop()
        print(f'\nTarefa removida: {tarefa_removida}\n')
        desfeitas.append(tarefa_removida)
    except:
        print('\nNenhuma tarefa para tirar!!\n')


def redo_tarefas():
    try:
        tarefas.append(desfeitas.pop())
        print(f'\nTarefa "{tarefas[-1]}" readicionada\n')
    except:
        print('\nNenhuma tarefa para readicionar!!\n')


opção = ''
tarefas = []
desfeitas = []
while opção != 'sair':
    opção = input('Oque você quer fazer:\n[1]-Adicionar tarefa\n[2]-Listar tarefa\n[3]-Desfazer ação\n[4]-Refazer ação\n')
    if opção == '1':
        tarefa = input('Qual tarefa você deseja adicionar: ')
        tarefas.append(tarefa)
    elif opção == '2':
        listagem_tarefas(tarefas)
    elif opção == '3':
        undo_tarefas()
    elif opção == '4':
        redo_tarefas()
    elif opção != 'sair':
        print('Opção não localizada, favor digitar apenas, por exemplo: 1')
