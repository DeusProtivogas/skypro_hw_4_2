# в задании представлен один класс который нужно разбить на 4
# Воин      - Warrior
# Лекарь    - Healer
# Дерево    - Tree
# Ловушка   - Trap

# Для решения этой задачи не используйте наследование


# Воин в состоянии защищаться от врагов, атаковать и передвигаться по полю
class Warrior():
    def attack(self):
        print("Warrior attacks")


    def defense(self):
        print("Warrior defends!")

    def move(self):
        print("Warrior moves!")

# Лекарь может защищаться, лечить воина и панически спасаться бегством
class Healer():

    def defense(self):
        print("Healer defends!")

    def move(self):
        print("Healer moves")

    def heal(self):
        print("Healer heals!")

# Дерево может защищаться (попробуй разруби сходу) и гореть в огне
class Tree():

    def defense(self):
        print("Tree is unkillable!")

    def on_fire(self):
        print("Tree is being killed by fire!")

# Ловушка не может ничего кроме как атаковать того, кто на нее наступит
class Trap():

    def attack(self):
        print("It's a trap!")

if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()