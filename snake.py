import pygame
import constants


class Snake:
    def __init__(self):
        # Початкове тіло змійки (список координат [x, y])
        # Починаємо з одного сегмента в центрі екрана
        self.body = [[constants.WIDTH // 2, constants.HEIGHT // 2]]

        # Початковий напрямок (x, y). (0, 0) - змійка стоїть на місці
        self.direction = [0, 0]

        # Прапорець для запобігання росту без їжі
        self.add_segment = False

    def draw(self):
        """Малює кожен сегмент змійки на екрані."""
        for segment in self.body:
            rect = pygame.Rect(segment[0], segment[1], constants.CELL, constants.CELL)
            pygame.draw.rect(constants.SCREEN, (0, 255, 0), rect)  # Зелений колір

    def move(self):
        """Оновлює позицію тіла змійки."""
        if self.direction == [0, 0]:
            return

        # Створюємо нову голову на основі поточного напрямку
        new_head = [
            self.body[0][0] + self.direction[0] * constants.CELL,
            self.body[0][1] + self.direction[1] * constants.CELL
        ]

        # Додаємо нову голову в початок списку
        self.body.insert(0, new_head)

        # Якщо ми не з'їли яблуко, видаляємо останній сегмент (хвіст)
        if not self.add_segment:
            self.body.pop()
        else:
            self.add_segment = False

    def change_direction(self, new_dir):
    #TODO:зробити else
        """Змінює напрямок, забороняючи розворот на 180 градусів."""
        # Заборона руху в протилежний бік
        if (new_dir[0] * -1 != self.direction[0]) or (new_dir[1] * -1 != self.direction[1]):
            self.direction = new_dir

    def check_collision(self):
        head = self.body[0]

        # 1. Перевірка зіткнення з власним тілом
        # Перевіряємо, чи є голова в решті тіла (починаючи з 1-го елемента)
        if head in self.body[1:]:
            return True

        # 2. Перевірка зіткнення з межами екрана (стінами)
        if head[0] < 0 or head[0] >= constants.WIDTH or head[1] < 0 or head[1] >= constants.HEIGHT:
            return True


def change_direction():
    return None