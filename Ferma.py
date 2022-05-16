class Goose:
    def __init__(self, name, weight):
        self.name = name
        self.weigth = weight
        self.voice = 'Га-га'
        self.__resurs = 4

    def feed(self):
        if self.__resurs == 5:
            return 'Гусь сыт'
        else:
            self.__resurs += 1
            return 'Гуся покормили'


    def collect_eggs(self):
        if self.__resurs == 0:
            return 'У гуся нет яиц'
        else:
            self.__resurs -= 1
            return 'Яйца собраны'


class Cow:
    def __init__(self, name, weight):
        self.name = name
        self.weigth = weight
        self.voice = 'Му-му'
        self.__resurs = 4

    def feed(self):
        if self.__resurs == 5:
            return 'Корова наелась'
        else:
            self.__resurs += 1
            return 'Корову накормили'


    def collect_eggs(self):
        if self.__resurs == 0:
            return 'У коровы нет молока'
        else:
            self.__resurs -= 1
            return 'Вы надоили много вкусного молочка'


class Lamb:
    def __init__(self, name, weight):
        self.name = name
        self.weigth = weight
        self.voice = 'Бе-бе'

        self.__resurs = 4

    def feed(self):
        if self.__resurs == 5:
            return 'Овечка наелась'
        else:
            self.__resurs += 1
            return 'Овечка поела'


    def collect_eggs(self):
        if self.__resurs == 0:
            return 'У овечки еще не выросла шерсть'
        else:
            self.__resurs -= 1
            return 'Овечка пострижена'


class Chicken:
    def __init__(self, name, weight):
        self.name = name
        self.weigth = weight
        self.voice = 'Кут-кудах'
        self.__resurs = 4

    def feed(self):
        if self.__resurs == 5:
            return 'Курочка сытая'
        else:
            self.__resurs += 1
            return 'Курочку покормили'


    def collect_eggs(self):
        if self.__resurs == 0:
            return 'У курочки нет яиц'
        else:
            self.__resurs -= 1
            return 'Яйца собраны'


class Goat:
    def __init__(self, name, weight):
        self.name = name
        self.weigth = weight
        self.voice = 'Ме-ме'
        self.__resurs = 4

    def feed(self):
        if self.__resurs == 5:
            return 'Коза сытая'
        else:
            self.__resurs += 1
            return 'Коза поела'


    def collect_eggs(self):
        if self.__resurs == 0:
            return 'У коза нет молока'
        else:
            self.__resurs -= 1
            return 'Надоили много вкусного молочка'


class Duck:
    def __init__(self, name, weight):
        self.name = name
        self.weigth = weight
        self.voice = 'Кря-кря'
        self.__resurs = 4

    def feed(self):
        if self.__resurs == 5:
            return 'Утка сытая'
        else:
            self.__resurs += 1
            return 'Утку покормили'


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
print(sum(weigth_animal))
print(max(weigth_animal))
print('Hello World')



