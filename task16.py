from random import *
import os


welcome_text = ('Приветствую тебя, дорогой игрок! Давай начнем игру!')
print(welcome_text)

message = ['Ты ходишь!']


def player_vs_player():
    candies_total = 200
    max_take = 28
    count = 0
    player_1 = input('\nПожалуйста, представься: ')
    player_2 = input('\nКто твой соперник?: ')

    print(f'\n {player_1} и  {player_2}, начнем игру!\n')
    print('\nДля начала опеределим, кто первый ходит.\n')

    x = randint(1, 2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
    print(f'Поздравляю {lucky} ты ходишь первым!')

    while candies_total > 0:
        if count == 0:
            step = int(input(f'\n{choice(message)} {lucky} = '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nОго, как много ты берешь! По правилам игры можно взять только {max_take} конфет {lucky}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна кону еще {candies_total}')
            count = 1
        else:
            print('Прости, конфет больше нет')

        if count == 1:
            step = int(input(f'\n{choice(message)}, {loser} '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nОставь немного второму игроку! По правилам можно взять {max_take} конфет {loser}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nОсталось всего{candies_total}')
            count = 0
        else:
            print('Ну вот, конфеты закончились!(')

    if count == 1:
        print(f'{loser} ПОБЕДИЛ! УРА!')
    if count == 0:
        print(f'{lucky} ПОБЕДИЛ! УРА!')


player_vs_player()


def player_vs_bot():
    candies_total = 200
    max_take = 28
    player_1 = input('\nКак тебя зовут?: ')
    player_2 = 'Компьютер'
    players = [player_1, player_2]
    print(f'\n{player_1} и  {player_2}, ДАВАЙТЕ ЖЕ ИГРАТЬ! !\n')
    print('\nСначала решите, кто ходит первым.\n')

    lucky = randint(-1, 0)

    print(f'Поздравляю {players[lucky+1]} ты ходишь первым!')

    while candies_total > 0:
        lucky += 1

        if players[lucky % 2] == 'Компьютер':
            print(
                f'\nХодит {players[lucky%2]} \nОсталось всего-то{candies_total}. \n{choice(message)}: ')

            if candies_total < 29:
                step = candies_total
            else:
                delenie = candies_total//28
                step = candies_total - ((delenie*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\nПора сделать ход,  {players[lucky%2]} \nОсталось {candies_total} {choice(message)}:  '))
            while step > max_take or step > candies_total:
                step = int(input(f'\nНе торопись! За один ход можно взять{max_take} конфет, попробуй еще раз: '))
        candies_total = candies_total - step

    print(f'Всего осталось {candies_total} \nПобедил {players[lucky%2]}')

player_vs_bot()