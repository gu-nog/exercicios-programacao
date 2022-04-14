from itertools import permutations
from random import randint


def generate_middle_names(new_possibilities_list, middle_names_quantity):
    default_middle_names_list = ['Webb', 'Owen', 'Smith', 'Jones', 'Taylor', 'Brown', 'Williams', 'Wilson', 'Johnson',
                  'Davies', 'Robbinson', 'King', 'Green', 'Harris', 'Martin', 'Thomas', 'Ward', 'Lee']
    if len(new_possibilities_list) > 10:
        all_middle_names = new_possibilities_list
    else:
        all_middle_names = default_middle_names_list + new_possibilities_list
    possible_full_names = list(permutations(all_middle_names, middle_names_quantity))
    chosen_name_index = randint(0, len(possible_full_names))
    return possible_full_names[chosen_name_index]


added_middle_names = []
while True:
    menu_option = input('What do you need to do:\n[1]-Add a possible middle name\n[2]-Generate name\n')
    if menu_option == '1':
        added_middle_names.append(input('\nMiddle name to add: \n'))
    elif menu_option == '2':
        first_name = input('\nWhat is the first name: \n')
        correct_input = False
        while correct_input == False:
            try:
                middle_names_quantity = int(input('\nHow many middle names to add: \n'))
                correct_input = True
            except:
                print('\nPlease put a number\n')
        chosen_middle_names = generate_middle_names(added_middle_names, middle_names_quantity)
        print(f"\nThe chosen name was: {first_name} ", end='')
        for middle_name in chosen_middle_names:
            print(f'{middle_name} ', end='')
        print('\n')
        break
    else:
        print('\nPlease type only 1, for example\n')
