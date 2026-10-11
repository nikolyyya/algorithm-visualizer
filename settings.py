# settings.py
WIDTH, HEIGHT, FPS = 1100, 700, 60       

COLORS = {
    "normal":    (120, 144, 156),  # серо-голубой: нейтральный элемент
    "comparing": (255, 213,  79),  # жёлтый: сравниваются
    "swapping":  (239,  83,  80),  # красный: обмен
    "min":       (171,  71, 188),  # фиолетовый: выбранный минимум
    "sorted":    (102, 187, 106),  # зелёный: на своём месте
    "range":     ( 66, 165, 245),  # синий: активный диапазон поиска
    "mid":       (255, 152,   0),  # оранжевый: mid
    "found":     (255,  64, 129),  # розовый: найденный элемент
    "excluded":  ( 55,  65,  81),  # тёмно-серый: исключён
}

LEGEND_LABELS = {
    "normal":    "Серо-голубой: нейтральный элемент",
    "comparing": "Жёлтый: сравниваются",
    "swapping":  "Красный: обмен",
    "min":       "Фиолетовый: выбранный минимум",
    "sorted":    "Зелёный: на своём месте",
    "range":     "Синий: активный диапазон поиска",
    "mid":       "Оранжевый: середина",
    "found":     "Розовый: найденный элемент",
    "excluded":  "Тёмно-серый: исключён",
}

FONT_BIG_SIZE = 34
FONT_SMALL_SIZE = 24
FONT_TINY_SIZE = 12

BG_COLOR = (245, 245, 245)
PANEL_COLOR = (225, 228, 232)
TEXT_COLOR = (40, 40, 40)

ARRAY_SIZE_MIN, ARRAY_SIZE_MAX = 20, 50
VALUE_MIN, VALUE_MAX = 10, 100
STEP_DELAY_MS = 200


MARGIN = 40


POSSIBLE_ALGORITHMS = {
    1: "Bubble Sort",
    2: "Selection Sort",
    3: "Binary Search",
}

STEP_DELAY_MS = 100

CONTROLS_TEXT = "SPACE — Start / Pause | N — Next step | R — Reset / New array | M - Menu | Esc — Exit "
