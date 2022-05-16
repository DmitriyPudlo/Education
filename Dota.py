import requests
import random


def create_dict_of_heroes(url_api):
    response_heroes_api = requests.get(url_api)
    return response_heroes_api.json()


def create_dict_of_number_of_legs(dict_heroes):
    return tuple(set([hero_info['legs'] for hero_info in dict_heroes]))


def create_dict_of_roles(dict_heroes):
    roles = set()
    for hero_info in dict_heroes:
        for role in hero_info['roles']:
            roles.add(role)
    return tuple(roles)


def search_id_random_hero():
    while True:
        user_legs = int(input('Укажи количество ног: '))
        while True:
            if user_legs not in number_of_legs:
                print(f'Стольконогих героев нет. Выбери из:', *number_of_legs)
                user_legs = int(input())
            else:
                break
        user_role = input('Укажи одну игровую роль: ')
        while True:
            if user_role not in variant_roles:
                print(f'Такой роли нет. Выбери из:', *variant_roles)
                user_role = input()
            else:
                break
        id_heroes = [hero_info['id'] for hero_info in dicts_with_hero_info if
                     user_legs == hero_info['legs'] and user_role in hero_info['roles']]
        if not id_heroes:
            print('Такого сочетания нет')
        else:
            return random.choice(id_heroes)


def search_bad_pick_vs_random_hero(id_hero):
    url_api_matchups = f'https://api.opendota.com/api/heroes/{id_hero}/matchups'
    dict_mutchups = requests.get(url_api_matchups).json()
    max_wins = max([mutchups_info['wins'] for mutchups_info in dict_mutchups])
    for mutchup_info in dict_mutchups:
        if mutchup_info['wins'] == max_wins:
            id_bad_pick = mutchup_info['hero_id']
            for hero_info in dicts_with_hero_info:
                if id_bad_pick == hero_info['id']:
                    print(hero_info['localized_name'])


url_api_heroes = 'https://api.opendota.com/api/heroes'
dicts_with_hero_info = create_dict_of_heroes(url_api_heroes)
number_of_legs = create_dict_of_number_of_legs(dicts_with_hero_info)
variant_roles = create_dict_of_roles(dicts_with_hero_info)
id_random_hero = search_id_random_hero()
search_bad_pick_vs_random_hero(id_random_hero)
