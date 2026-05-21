from constants import CELLX, CELLY


class Snake:
    def __init__(self):
        self.lives = 3
        self.reset()

    def reset(self):
        self.body = [[CELLX // 2, CELLY // 2]]
        self.dx = 1
        self.dy = 0
        self.add_segment = False

    def change_direction(self, new_dx, new_dy):
        if self.dx == -new_dx and self.dy == -new_dy and (self.dx != 0 or self.dy != 0):
            return
        self.dx = new_dx
        self.dy = new_dy
        # TODO: Реалізувати захист від розвороту на 180 градусів (самогубства).
        # Якщо новий вектор напрямку (new_dx, new_dy) прямо протилежний поточному (self.dx, self.dy)
        # і ми зараз не стоїмо на місці, команду треба проігнорувати (вийти з методу).
        # В іншому випадку - застосувати нові значення напрямку.

    def move(self):
        head_x = self.body[0][0]
        head_y = self.body[0][1]
        new_head = [head_x + self.dx, head_y + self.dy]
        self.body.insert(0, new_head)
        if self.add_segment:
            self.add_segment = False
        else:
            self.body.pop()
        # TODO: Реалізувати механіку руху змійки та її росту.
        # 1. Розрахувати координати нової "голови" (додати поточний вектор швидкості dx, dy до координат існуючої голови).
        # 2. Вставити нову голову на початок списку тіла змійки (self.body).
        # 3. Керування хвостом:
        #    - Якщо прапорець росту (self.add_segment) активний, просто скинути його (змійка видовжується).
        #    - Якщо ні — видалити останній елемент з кінця тіла, щоб створити ілюзію руху.

    def check_wall_collision(self, walls=None):
        head = self.body[0]
        if head[0] < 0 or head[0] >= CELLX or head[1] < 0 or head[1] >= CELLY:
            return True
        if walls:
            if tuple(head) in walls:
                return True
        return False
