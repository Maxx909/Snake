import pygame
from constants import *
from snake import Snake
from apple import Apple
from buttons import Button

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змійка")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
font_big = pygame.font.Font(None, 64)

# ─────────────────────────────────────────
#  ЗАВАНТАЖЕННЯ ГРАФІКИ
# ─────────────────────────────────────────
# ─────────────────────────────────────────
#  ЗАВАНТАЖЕННЯ ГРАФІКИ
# ─────────────────────────────────────────
bg_img = pygame.image.load("assets/images/bg.png")
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

apple_img = pygame.image.load("assets/images/apple.png")
apple_img = pygame.transform.scale(apple_img, (CELL, CELL))

heart_img = pygame.image.load("assets/images/live.png")
heart_img = pygame.transform.scale(heart_img, (30, 30))

body_img = pygame.image.load("assets/images/body.png")
body_img = pygame.transform.scale(body_img, (CELL, CELL))

# Завантажуємо базову голову
base_head_img = pygame.image.load("assets/images/head.png")
base_head_img = pygame.transform.scale(base_head_img, (CELL, CELL))

# Створюємо словник з 4 версіями голови (ключі — це вектори dx, dy)
# У Pygame поворот відбувається проти годинникової стрілки
heads_dict = {
    (1, 0): pygame.transform.rotate(base_head_img, 90),  # Вправо (0 градусів)
    (0, -1): pygame.transform.rotate(base_head_img, 180),  # Вгору (90 градусів вліво)
    (-1, 0): pygame.transform.rotate(base_head_img, -90),  # Вліво (180 градусів)
    (0, 1): base_head_img  # Вниз (-90 або 270 градусів)
}

body_dict = {
    (1, 0): pygame.transform.rotate(body_img, 90),  # Вправо (0 градусів)
    (0, -1): pygame.transform.rotate(body_img, 180),  # Вгору (90 градусів вліво)
    (-1, 0): pygame.transform.rotate(body_img, -90),  # Вліво (180 градусів)
    (0, 1): body_img
}
# Якщо ваша оригінальна картинка дивиться ВГОРУ, кути треба буде змінити:
# Вгору: 0, Вліво: 90, Вниз: 180, Вправо: -90

# ─────────────────────────────────────────
#  КНОПКИ МЕНЮ
# ─────────────────────────────────────────
cx = WIDTH // 2

btn_play = Button("PLAY", cx - 100, 150, 200, 55, color=GREEN, text_color=BLACK)
btn_level = Button("Рівень: Easy", cx - 130, 240, 260, 50, color=DARK_GRAY, text_color=WHITE)
btn_vol_minus = Button("−", cx + 60, 330, 40, 40, color=DARK_GRAY, text_color=WHITE)
btn_vol_plus = Button("+", cx + 170, 330, 40, 40, color=DARK_GRAY, text_color=WHITE)

# ─────────────────────────────────────────
#  СТАНИ ТА НАЛАШТУВАННЯ
# ─────────────────────────────────────────
state = "menu"
selected_level = "Easy"
level_names = list(LEVELS.keys())
volume = 0.5
pygame.mixer.music.set_volume(volume)

snake = Snake()
apple = Apple()
frame_counter = 0


# ─────────────────────────────────────────
#  ФУНКЦІЇ ВІДМАЛЬОВКИ
# ─────────────────────────────────────────
def draw_menu():
    screen.blit(bg_img, (0, 0))
    title = font_big.render("🐍 ЗМІЙКА", True, YELLOW)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))
    btn_play.draw(screen)
    btn_level.draw(screen)
    btn_vol_minus.draw(screen)
    btn_vol_plus.draw(screen)
    vol_label = font.render("Гучність:", True, WHITE)
    screen.blit(vol_label, (btn_vol_minus.rect.x - vol_label.get_width() - 10,
                            btn_vol_minus.rect.y + 5))
    bar_x = btn_vol_minus.rect.right + 8
    bar_y = btn_vol_minus.rect.y + 8
    bar_w = btn_vol_plus.rect.x - bar_x - 8
    bar_h = 24
    pygame.draw.rect(screen, GRAY, (bar_x, bar_y, bar_w, bar_h), border_radius=5)
    pygame.draw.rect(screen, YELLOW, (bar_x, bar_y, int(bar_w * volume), bar_h), border_radius=5)


def draw_game():
    screen.blit(bg_img, (0, 0))
    walls = LEVELS[selected_level]["walls"]
    for (wx, wy) in walls:
        pygame.draw.rect(screen, DARK_GRAY, (wx * CELL, wy * CELL, CELL, CELL))
        pygame.draw.rect(screen, GRAY, (wx * CELL, wy * CELL, CELL, CELL), 2)
    screen.blit(apple_img, (apple.x * CELL, apple.y * CELL))

    # ВІДМАЛЬОВКА ЗМІЙКИ
    for i, segment in enumerate(snake.body):
        sx, sy = segment[0] * CELL, segment[1] * CELL
        if i == 0:
            # Отримуємо вектор напрямку голови
            current_dir = (snake.dx, snake.dy)

            # Якщо змійка стоїть на місці (наприклад, при старті dx=0, dy=0),
            # задаємо напрямок за замовчуванням, щоб не було помилки ключа.
            if current_dir == (0, 0):
                current_dir = (1, 0)  # дивимось вправо

            # Дістаємо потрібну повернуту картинку
            current_head_img = heads_dict[current_dir]
            screen.blit(current_head_img, (sx, sy))
        else:
            screen.blit(body_img, (sx, sy))

    lives_text = font.render("Lives: ", True, WHITE)
    screen.blit(lives_text, (10, 10))
    for i in range(snake.lives):
        screen.blit(heart_img, (90 + i * 35, 10))
    lvl_text = font.render(f"Рівень: {selected_level}", True, WHITE)
    screen.blit(lvl_text, (WIDTH - lvl_text.get_width() - 10, 10))


def draw_game_over():
    screen.blit(bg_img, (0, 0))
    go = font_big.render("GAME OVER", True, RED)
    screen.blit(go, (WIDTH // 2 - go.get_width() // 2, HEIGHT // 2 - 60))
    hint = font.render("Натисни ENTER щоб повернутись у меню", True, WHITE)
    screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT // 2 + 20))


#  ГОЛОВНИЙ ЦИКЛ
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == "menu":
            if btn_play.is_clicked(event):
                snake = Snake()
                apple = Apple()
                frame_counter = 0
                state = "game"

            if btn_level.is_clicked(event):
                idx = level_names.index(selected_level)
                selected_level = level_names[(idx + 1) % len(level_names)]
                btn_level.update_text(f"Рівень: {selected_level}")

            if btn_vol_minus.is_clicked(event):
                volume = max(0.0, round(volume - 0.1, 1))
                pygame.mixer.music.set_volume(volume)

            if btn_vol_plus.is_clicked(event):
                volume = min(1.0, round(volume + 0.1, 1))
                pygame.mixer.music.set_volume(volume)

        if state == "game" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(0, -1)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(0, 1)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(1, 0)

        if state == "game_over" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                state = "menu"

    # ── ЛОГІКА ГРИ ──
    if state == "game":
        frame_counter += 1
        frames_per_step = LEVELS[selected_level]["frames_per_step"]

        if frame_counter >= frames_per_step:
            frame_counter = 0

            snake.move()
            walls = set(LEVELS[selected_level]["walls"])
            if snake.body[0][0] == apple.x and snake.body[0][1] == apple.y:
                snake.add_segment = True
                apple.randomize()
            if snake.check_wall_collision(walls):
                snake.lives -= 1
                if snake.lives > 0:
                    snake.reset()
                else:
                    state = "game_over"

    # TODO: Залежно від поточного стану (state) викликати потрібну функцію відмальовки.
    # "menu" → draw_menu()
    # "game" → draw_game()
    # "game_over" → draw_game_over()
    if state == "menu":
        draw_menu()
    elif state == "game":
        draw_game()
    elif state == "game_over":
        draw_game_over()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
