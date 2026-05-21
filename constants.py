CELL = 50
CELLY = 10
CELLX = 15
WIDTH = CELL * CELLX
HEIGHT = CELL * CELLY

FPS = 30

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
DARK_GRAY = (50, 50, 50)
YELLOW = (255, 215, 0)

# TODO: Разом з викладачемописати словник LEVELS.
# Кожен рівень має два параметри:
#   - frames_per_step: скільки кадрів між кроками змійки (більше = повільніше)
#   - walls: список координат клітинок-перешкод [(x, y), ...]
# Приклад структури:
LEVELS = {
    "Easy":   {"frames_per_step": 6, "walls": []},
    "Medium": {"frames_per_step": 4, "walls": [(5,5),(5,6),(5,7)]},
    "Hard":   {"frames_per_step": 2, "walls": [(5,5),(5,6),(5,7),(10,10),(10,11),(10,12)]},
}
