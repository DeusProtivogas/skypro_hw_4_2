# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)



class Unit:
    def __init__(self, state, x_pos, y_pos, field, base_speed = 1):
        self.state = state
        self.field = field
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.base_speed = base_speed

    def get_speed(self):
        if self.state == 'fly':
            return self.base_speed * 1.2
        elif self.state == 'crawl':
            return self.base_speed * 0.5
        return self.base_speed

    def move(self, direction):
        speed = self.get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y_pos + speed, x=self.x_pos, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y_pos - speed, x=self.x_pos, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y_pos, x=self.x_pos - speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y_pos, x=self.x_pos + speed, unit=self)


#     ...
