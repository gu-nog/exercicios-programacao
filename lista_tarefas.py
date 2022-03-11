# Criar uma lista de tarefas que possa:
"""
[x] - adicionar tarefa
[x] - listar tarefa
[x] - desfazer última ação
[x] - refazer última ação
[x] - login para ter múltiplas listas de diferentes tarefas
[x] - passar da área de login para cadastro, vice-versa
[] - trocar de usuário
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


def create_account(name, password):
    if (name+password) not in all_tarefas.keys():
        contas[name] = password
        all_tarefas[name+password] = []
        return True  # usuário criado com sucesso
    else:
        return False  # já existe esse usuário


def login(name, password):
    if name in contas.keys():
        if contas[name] == password:
            return True  # ok
        else:
            return False  # senha errada
    else:
        return False  # usuário errado


def get_credentials():
    user = input("Seu nome de usuário: ")
    password = input("Sua senha: ")
    return user, password


def change_sign_route():
    change = input("Deseja trocar de área?[S/N]")
    while change not in ['S', 'N']:
        change = input("Deseja trocar de área?[S/N]")
    return change


# inicialization
all_tarefas = {}
contas = {}
desfeitas = []

# login or create account
opcao = input("Oque você deseja fazer:\n[1]-login\n[2]-cadastrar\n")
while opcao not in ['1', '2']:
    print('Favor escolher uma opcão válida(1 ou 2)')
    opcao = input("Oque você deseja fazer:\n[1]-login\n[2]-cadastrar\n")

user, password = get_credentials()
change = change_sign_route()
while True:
    if change == 'S':
        opcao = input("Oque você deseja fazer:\n[1]-login\n[2]-cadastrar\n")
        while opcao not in ['1', '2']:
            print('Favor escolher uma opcão válida(1 ou 2)')
            opcao = input("Oque você deseja fazer:\n[1]-login\n[2]-cadastrar\n")
    if opcao == '1':
        returned = login(user, password)
        if returned == True:
            print('Login efetuado com sucesso!!')
            break
        else:
            print('Usuário e/ou senha incorretos.')
            change = change_sign_route()
            if change == 'S':
                continue
            user, password = get_credentials()
    elif opcao == '2':
        returned = create_account(user, password)
        if returned == True:
            print('Seja bem vindo!!! Conta criada com sucesso.')
            break
        else:
            print('Infelizmente já existe um usuário com esse nome e senha:( Troque um ou outro.')
            change = change_sign_route()
            if change == 'S':
                continue
            user, password = get_credentials()

# session
tarefas = all_tarefas[user+password]
while opcao != 'sair':
    opcao = input('Oque você quer fazer:\n[1]-Adicionar tarefa\n[2]-Listar tarefa\n[3]-Desfazer ação\n[4]-Refazer ação\nsair\n')
    if opcao == '1':
        tarefa = input('Qual tarefa você deseja adicionar: ')
        tarefas.append(tarefa)
    elif opcao == '2':
        listagem_tarefas(tarefas)
    elif opcao == '3':
        undo_tarefas()
    elif opcao == '4':
        redo_tarefas()
    elif opcao != 'sair':
        print('Opção não localizada, favor digitar apenas opções válidas, por exemplo: 1')
    else:
        all_tarefas[user + password] = tarefas
        print('Salvando lista final de tarefas, volte sempre!')
