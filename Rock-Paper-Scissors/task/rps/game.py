import random

name_user = input('Enter your name: ').title()
print(f'Hello, {name_user}')

fisier_rating = open('rating.txt', 'r')
lista_players = [line.split() for line in fisier_rating]
dic_players = dict((i[0], i[1]) for i in lista_players)
fisier_rating.close()

score = int(dic_players[name_user])
choices = input().split(',')
lista_choice = [i for i in choices]
if choices == ['']:
    lista_choice = ['paper', 'scissors', 'rock']
print("Okay, let's start")

while True:
    input_users = input()
    if input_users == '!rating':
        print(score)
    elif input_users == '!exit':
        print('Bye!')
        break
    elif input_users in lista_choice:
        input_computer = random.choice(lista_choice)
        index_user = lista_choice.index(input_users)
        new_list = lista_choice[lista_choice.index(input_users)+1:]
        new_list.extend(lista_choice[:lista_choice.index(input_users)])
        win_list = new_list[:int(len(new_list) / 2)]
        if input_users == input_computer:
            print(f'There is a draw ({input_users})')
            score += 50
        elif input_computer in win_list:
            print(f'Sorry, but the computer chose {input_computer}')
        elif input_computer not in win_list:
            print(f'Well done. The computer chose {input_computer} and failed')
            score += 100
    else:
        print('Invalid input')
