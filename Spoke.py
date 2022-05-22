def search_winner(x, y):
    list_win = [win_spok, win_scissors, win_paper, win_stone, win_lizard]
    for win in list_win:
        if (x == win[0] or y == win[0]) and (x in win[1:] or y in win[1:]):
            return win[0]

win_spok = ['Спок', 'ножницы', 'камень']
win_scissors = ['ножницы', 'бумага', 'ящерица']
win_paper = ['бумага', 'камень', 'Спок']
win_stone = ['камень', 'ящерица', 'ножницы']
win_lizard = ['ящерица', 'Спок', 'бумага']

player_1 = input()
player_2 = input()

if player_1 == player_2:
    print('ничья')
else:
    if player_1 == search_winner(player_1, player_2):
        print('Тимур')
    else:
        print('Руслан')