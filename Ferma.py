class Animals:
    def __init__(self, name, weight):
        self.name = name
        self.weigth = weight
        self.__resurs = 4

    def feed(self):
        if self.__resurs == 5:
            print('Животное уже сытое!')
        else:
            self.__resurs += 1
            print('Животное покормлено!')

    def put(self):
        print('Животное довольно урчит')


class Goose(Animals):
    voice = 'Га-га'

    def collect_eggs(self):
        if self.__resurs == 0:
            print('У гуся нет яиц')
        else:
            self.__resurs -= 1
            print('Яйца собраны')


class Cow(Animals):
    voice = 'Му-му'

    def milk(self):
        if self.__resurs == 0:
            return 'У коровы нет молока'
        else:
            self.__resurs -= 1
            return 'Вы надоили много вкусного молочка'


class Lamb(Animals):
    voice = 'Бе-бе'

    def cut(self):
        if self.__resurs == 0:
            return 'У овечки еще не выросла шерсть'
        else:
            self.__resurs -= 1
            return 'Овечка пострижена'


class Chicken(Animals):
    voice = 'Кут-кудах'

    def collect_eggs(self):
        if self.__resurs == 0:
            return 'У курочки нет яиц'
        else:
            self.__resurs -= 1
            return 'Яйца собраны'


class Goat(Animals):
    voice = 'Ме-ме'

    def milk(self):
        if self.__resurs == 0:
            return 'У коза нет молока'
        else:
            self.__resurs -= 1
            return 'Надоили много вкусного молочка'


class Duck(Animals):
    voice = 'Кря-кря'

    def collect_eggs(self):
        if self.__resurs == 0:
            return 'У утки нет яиц'
        else:
            self.__resurs -= 1
            return 'Яйца собраны'


goose_grey = Goose('Серый', 7)
goose_white = Goose('Белый', 6)
cow_manya = Cow('Манька', 800)
lamb_barashek = Lamb('Барашек', 100)
lamb_kudryavy = Lamb('Кудрявый', 80)
chiken_koko = Chicken('Ко-ко', 4)
chiken_kukareku = Chicken('Кукареку', 5)
goat_roga = Goat('Рога', 50)
goat_kopita = Goat('Копыта', 60)
duck_kryakva = Duck('Кряква', 5)

ferma = [goose_grey, goose_white, cow_manya, lamb_barashek, lamb_kudryavy, chiken_koko, chiken_kukareku, goat_roga, goat_kopita, duck_kryakva]

weigth_animal = [animal.weigth for animal in ferma]


print(f'Масса всех животных равна {sum(weigth_animal)}кг')

for animal in ferma:
    if animal.weigth == max(weigth_animal):
        print(f'Самое тяжелое животное это {animal.name}. Его масса равна {animal.weigth}кг')

print(goose_white.voice)



