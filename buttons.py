import pygame
from constants import WHITE


class Button:
    def __init__(self, text, x, y, width, height,
                 color=(100, 100, 100),
                 text_color=WHITE,
                 font_size=36):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.Font(None, font_size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)
        pygame.draw.rect(screen, WHITE, self.rect, 2, border_radius=10)
        label = self.font.render(self.text, True, self.text_color)
        lx = self.rect.x + (self.rect.width - label.get_width()) // 2
        ly = self.rect.y + (self.rect.height - label.get_height()) // 2
        screen.blit(label, (lx, ly))

    # TODO: Написати метод is_clicked(self, event).
    # Метод має повернути True, якщо:
    #   1. Тип події — натискання миші (pygame.MOUSEBUTTONDOWN)
    #   2. Координати кліку потрапляють всередину кнопки (self.rect.collidepoint)
    # В усіх інших випадках повернути False.
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

    # TODO: Написати метод update_text(self, new_text).
    # Метод просто замінює поточний текст кнопки на новий.
    # Використовується коли треба змінити напис (наприклад: "Рівень: Easy" → "Рівень: Medium")
    def update_text(self, new_text):
        self.text = new_text
