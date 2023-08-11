class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_sound(self):
        return self.sound

    def who_am_i(self):
        return self._SPECIES

    def say_my_name(self):
        return self.name


class Tyrannosaur(Animal):
    sound = 'gao'
    _SPECIES = 'тиранозавр'

    def __init__(self, size, *args, **kwargs):
        self.length = size
        super().__init__(*args, **kwargs)


class Dog(Animal):
    sound = 'wan'
    _SPECIES = 'пёсель'

    def __init__(self, size, *args, **kwargs):
        self.length = size
        super().__init__(*args, **kwargs)


class Cat(Animal):
    sound = 'nya'
    _SPECIES = 'киса'

    def __init__(self, size, *args, **kwargs):
        self.length = size
        super().__init__(*args, **kwargs)


class AnimalFactory:
    @staticmethod
    def create_animal(animal_species, *args):
        return animal_species(*args)


tyr = AnimalFactory.create_animal(Tyrannosaur, 100, 'Петя', 150)
print(f'{(tyr.who_am_i()).title()} {tyr.say_my_name()} говорит {tyr.get_sound()}')
cat = AnimalFactory.create_animal(Cat, 10, 'Мурка', 15)
print(f'{(cat.who_am_i()).title()} {cat.say_my_name()} говорит {cat.get_sound()}')
dog = AnimalFactory.create_animal(Dog, 25, 'Полкан', 30)
print(f'{(dog.who_am_i()).title()} {dog.say_my_name()} говорит {dog.get_sound()}')
