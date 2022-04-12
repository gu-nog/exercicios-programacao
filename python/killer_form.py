# https://wiki.python.org.br/ExerciciosListas > exércicio número 14

# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#   1 - "Telefonou para a vítima?"
#   2 - "Esteve no local do crime?"
#   3 - "Mora perto da vítima?"
#   4 - "Devia para a vítima?"
#   5 - "Já trabalhou com a vítima?"

def get_yes_or_no_response(question):
    response = input(f'{question} - ')
    while response not in ['Sim', 'Não']:
        print('Favor responder apenas com Sim ou Não.')
        response = input(f'{question} - ')
    print()
    if response == 'Sim':
        return 1
    else:
        return 0


# Basic informations
suspect_name = input("Olá, qual é o seu nome? ")
victim_name = input("Qual é o nome da vítima que você é acusado de matar? ")

# Complete forms
positive_answers = 0
print(f"Senhor(a) {suspect_name}, favor responder as próximas perguntas sobre o dia do assassinato de {victim_name} "
      "apenas com Sim ou Não.")
questions = [f'Você telefonou para {victim_name} no dia?', 'Você esteve no local do crime?',
             f"Você mora perto do/a {victim_name}?", f"Você devia para o/a {victim_name} ou ele/a te devia?",
             f"Você já trabalhou com o/a {victim_name}?"]
for question in questions:
    positive_answers += get_yes_or_no_response(question)


# Resultado: O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Sendo,
# de acordo com Num de questões positivas:
# 2 - "Suspeita"
# 3 e 4 - "Cúmplice"
# 5 - "Assassino"
# 0 e 1 - "Inocente".


# Say the results
sentences_dict = {0: 'inocente', 1: 'inocente', 2: 'suspeito/a', 3: 'cúmplice', 4: 'cúmplice', 5: 'assassino/a'}
sentence = sentences_dict[positive_answers]
if sentence == 'assassino/a':
    print(f'O veredito é que o senhor(a) {suspect_name} é o/a {sentence} do/a senhor(a) {victim_name}')
else:
    print(f'O veredito é que o senhor(a) {suspect_name} é {sentence} na morte do/a senhor(a) {victim_name}')
