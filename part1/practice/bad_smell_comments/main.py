

class Unit:
    def move(self, field, x_param, y_param, direction, can_fly, can_crawl, speed = 1):

        if can_fly and can_crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if can_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = y_param + speed
                new_x = x_param
            elif direction == 'DOWN':
                new_y = y_param - speed
                new_x = x_param
            elif direction == 'LEFT':
                new_y = y_param
                new_x = x_param - speed
            elif direction == 'RIGHT':
                new_y = y_param
                new_x = x_param + speed
        if can_crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = y_param + speed
                new_x = x_param
            elif direction == 'DOWN':
                new_y = y_param - speed
                new_x = x_param
            elif direction == 'LEFT':
                new_y = y_param
                new_x = x_param - speed
            elif direction == 'RIGHT':
                new_y = y_param
                new_x = x_param + speed

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
