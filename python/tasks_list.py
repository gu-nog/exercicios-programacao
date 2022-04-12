# Criar uma lista de tarefas que possa:
"""
[x] - adicionar tarefa
[x] - listar tarefa
[x] - desfazer última ação
[x] - refazer última ação
[x] - login para ter múltiplas listas de diferentes tarefas
[x] - passar da área de login para cadastro, vice-versa
[x] - trocar de usuário
[x] - trocar a senha
[] - não permitir usuário com mesmo nome
"""

def listagem_tarefas(tarefas):
    print('\n===== listagem de tarefas =====')
    for c, tarefa in enumerate(tarefas):
        print(f'tarefa {c + 1} - {tarefa}')
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


def signin_or_signup():
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
    return user, password


# inicialization
all_tarefas = {}
contas = {}
desfeitas = []
opcao = str()

user, password = signin_or_signup()

# session
tarefas = all_tarefas[user+password]
while opcao != 'sair':
    opcao = input('Oque você quer fazer:'
                  '\n[1]-Adicionar tarefa'
                  '\n[2]-Listar tarefa'
                  '\n[3]-Desfazer ação'
                  '\n[4]-Refazer ação'
                  '\n[5]-Opções de conta'
                  '\nsair'
                  '\n')
    if opcao == '1':
        tarefa = input('Qual tarefa você deseja adicionar: ')
        tarefas.append(tarefa)
    elif opcao == '2':
        listagem_tarefas(tarefas)
    elif opcao == '3':
        undo_tarefas()
    elif opcao == '4':
        redo_tarefas()
    elif opcao == '5':
        opcao = input('Oque você quer fazer:'
                      '\n[1]-change account'
                      '\n[2]-change password'
                      '\n')
        while opcao not in ['1', '2']:
            print('Favor digitar um opção válida')
            opcao = input('Oque você quer fazer:'
                          '\n[1]-change account'
                          '\n[2]-change password'
                          '\n')
        if opcao == '1':
            all_tarefas[user + password] = tarefas
            user, password = signin_or_signup()
            tarefas = all_tarefas[user + password]
            desfeitas = []
        else:
            del contas[user]
            valid = False
            while valid == False:
                new_password = input("Qual sua nova senha: ")
                valid = create_account(user, new_password)  # cria usuário em contas e adiciona chave no all_tarefas
                if valid == False:
                    print('Favor escolher outra senha, essa já está em uso para um usuário de mesmo nome')
            all_tarefas[user+new_password] = tarefas
            del all_tarefas[user+password]
            password = new_password
            print('Senha alterada com sucesso!!!')


    elif opcao != 'sair':
        print('Opção não localizada, favor digitar apenas opções válidas, por exemplo: 1')
    else:
        print('Salvando lista final de tarefas, volte sempre!')
