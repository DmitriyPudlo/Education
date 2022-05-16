import requests


def return_int_hero(name_hero):
    response_hero_data = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{name_hero}')
    hero_info = response_hero_data.json()['results']
    for info in hero_info:
        if info['name'] == f'{name_hero}':
            return int(info['powerstats']['intelligence']), name_hero


def search_the_smartest(name_hero_1, name_hero_2, name_hero_3):
    int_hero_1 = return_int_hero(name_hero_1)
    int_hero_2 = return_int_hero(name_hero_2)
    int_hero_3 = return_int_hero(name_hero_3)
    return max(int_hero_1, int_hero_2, int_hero_3)


Hero_1 = 'Hulk'
Hero_2 = 'Captain America'
Hero_3 = 'Thanos'

the_smartest = search_the_smartest(Hero_1, Hero_2, Hero_3)
print(the_smartest[1])
