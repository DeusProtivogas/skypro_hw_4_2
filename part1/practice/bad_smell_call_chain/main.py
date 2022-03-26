# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


class Person:
    def __init__(self, room_num, city_population):
        self.planet = Planet()
        self.room_num = room_num
        self.city_population = city_population

    def get_person_room(self):
        # return self.planet.get_contry().get_city().get_street().get_room().get_name()
        return self.room_num

    def get_city_population(self):
        # return self.planet.get_contry().get_city().population()
        return self.city_population

# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

pers1 = Person(1, 100)
# pers2 = Person(2, 200)

print(pers1.get_person_room())
print(pers1.get_city_population())