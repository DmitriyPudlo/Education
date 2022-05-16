import requests
import os


def search_breed_with_max_sub_breed(link):
    response_from_dog_api = requests.get(link)
    all_breeds = response_from_dog_api.json()['message']
    list_length = 0
    breed_with_max_sub_breed = {}
    for breed, sub_breeds in all_breeds.items():
        list_length_breed = len(sub_breeds)
        if list_length_breed > list_length:
            list_length = list_length_breed
            breed_with_max_sub_breed = {breed: sub_breeds}
    return breed_with_max_sub_breed


def search_random_image_sub_breeds(dict_sub_breeds):
    for breed, sub_breeds in dict_sub_breeds.items():
        if not os.access(f'{breed}', os.F_OK):
            os.mkdir(f'{breed}')
        for sub_breed in sub_breeds:
            response_from_random_image = requests.get(f'https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random')
            link_random_image = requests.get(response_from_random_image.json()['message'])
            with open(f'{breed}/{sub_breed}_{breed}.jpeg', 'wb') as image:
                image.write(link_random_image.content)


link_api = 'https://dog.ceo/api/breeds/list/all'
dict_breed_with_max_sub_breeds = search_breed_with_max_sub_breed(link_api)
search_random_image_sub_breeds(dict_breed_with_max_sub_breeds)
